#!/usr/bin/env python3
# Copyright (c) 2021-2022 The Dash Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from test_framework.test_framework import DeccordTestFramework
from test_framework.util import assert_equal, assert_raises_rpc_error

'''
rpc_verifychainlock.py

Test the following RPC:
 - gettxchainlocks
 - verifychainlock

'''


class RPCVerifyChainLockTest(DeccordTestFramework):
    def set_test_params(self):
        # -whitelist is needed to avoid the trickling logic on node0
        self.set_deccord_test_params(5, 3, [["-whitelist=127.0.0.1"], [], [], [], []], fast_dip3_enforcement=True)
        self.set_deccord_llmq_test_params(3, 2)

    def run_test(self):
        node0 = self.nodes[0]
        node1 = self.nodes[1]
        self.activate_dip8()
        self.nodes[0].sporkupdate("SPORK_17_QUORUM_DKG_ENABLED", 0)
        self.wait_for_sporks_same()
        self.mine_quorum()
        self.wait_for_chainlocked_block(node0, node0.generate(1)[0])
        chainlock = node0.getbestchainlock()
        block_hash = chainlock["blockhash"]
        height = chainlock["height"]
        chainlock_signature = chainlock["signature"]
        # No "blockHeight"
        assert node0.verifychainlock(block_hash, chainlock_signature)
        # Invalid "blockHeight"
        assert not node0.verifychainlock(block_hash, chainlock_signature, 0)
        # Valid "blockHeight"
        assert node0.verifychainlock(block_hash, chainlock_signature, height)
        # Invalid "blockHash"
        assert not node0.verifychainlock(node0.getblockhash(0), chainlock_signature, height)
        self.wait_for_chainlocked_block_all_nodes(block_hash)
        # Isolate node1, mine a block on node0 and wait for its ChainLock
        node1.setnetworkactive(False)
        node0.generate(1)
        self.wait_for_chainlocked_block(node0, node0.generate(1)[0])
        chainlock = node0.getbestchainlock()
        assert chainlock != node1.getbestchainlock()
        block_hash = chainlock["blockhash"]
        height = chainlock["height"]
        chainlock_signature = chainlock["signature"]
        # Now it should verify on node0 without "blockHeight" but fail on node1
        assert node0.verifychainlock(block_hash, chainlock_signature)
        assert_raises_rpc_error(-32603, "blockHash not found", node1.verifychainlock, block_hash, chainlock_signature)
        # But they should still both verify with the height provided
        assert node0.verifychainlock(block_hash, chainlock_signature, height)
        assert node1.verifychainlock(block_hash, chainlock_signature, height)

        node1.generate(1)
        height1 = node1.getblockcount()
        tx0 = node0.getblock(node0.getbestblockhash())['tx'][0]
        tx1 = node1.getblock(node1.getbestblockhash())['tx'][0]
        locks0 = node0.gettxchainlocks([tx0, tx1])
        locks1 = node1.gettxchainlocks([tx0, tx1])
        unknown_cl_helper = {'height': -1, 'chainlock': False}
        assert_equal(locks0, [{'height': height, 'chainlock': True}, unknown_cl_helper])
        assert_equal(locks1, [unknown_cl_helper, {'height': height1, 'chainlock': False}])


if __name__ == '__main__':
    RPCVerifyChainLockTest().main()
