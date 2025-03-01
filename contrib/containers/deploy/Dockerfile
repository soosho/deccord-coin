FROM phusion/baseimage:focal-1.0.0
LABEL maintainer="Deccord Developers <dev@deccord.org>"
LABEL description="Dockerised Deccord, built from Travis"

ARG USER_ID
ARG GROUP_ID

ENV HOME /home/deccord

# add user with specified (or default) user/group ids
ENV USER_ID ${USER_ID:-1000}
ENV GROUP_ID ${GROUP_ID:-1000}
RUN groupadd -g ${GROUP_ID} deccord && \
    useradd -u ${USER_ID} -g deccord -s /bin/bash -m -d /home/deccord deccord && \
    mkdir /home/deccord/.deccord && \
    chown ${USER_ID}:${GROUP_ID} -R /home/deccord

COPY bin/* /usr/local/bin/

RUN chmod a+x /usr/local/bin/*

USER deccord

VOLUME ["/home/deccord"]

EXPOSE 22945 9999 32945 32946

WORKDIR /home/deccord
