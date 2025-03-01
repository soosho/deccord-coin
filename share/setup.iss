[Setup]
AppName=Deccord
AppVersion=20.0.1
DefaultDirName={pf}\Deccord Core
DefaultGroupName=Deccord
OutputDir=.
OutputBaseFilename=deccord_setup
Compression=lzma
SolidCompression=yes
LicenseFile=D:\work\DECCORD\release\deccord-20.0.1-win64\license.txt
WizardImageFile=D:\work\DECCORD\release\deccord-20.0.1-win64\nsis-wizard.bmp
SetupIconFile=D:\work\DECCORD\release\deccord-20.0.1-win64\icon.ico

AppPublisher=Deccord Team (support@deccord.com)

[Files]
Source: "D:\work\DECCORD\release\deccord-20.0.1-win64\deccord-cli.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\work\DECCORD\release\deccord-20.0.1-win64\deccordd.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\work\DECCORD\release\deccord-20.0.1-win64\deccord-qt.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\work\DECCORD\release\deccord-20.0.1-win64\deccord-tx.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Deccord Core"; Filename: "{app}\deccord-qt.exe"
Name: "{group}\Deccord CLI"; Filename: "{app}\deccord-cli.exe"
Name: "{group}\Deccord Daemon"; Filename: "{app}\deccordd.exe"
Name: "{group}\Deccord Transaction"; Filename: "{app}\deccord-tx.exe"
Name: "{commondesktop}\Deccord Core"; Filename: "{app}\deccord-qt.exe"

[UninstallDelete]
Type: files; Name: "{app}\deccord-cli.exe"
Type: files; Name: "{app}\deccordd.exe"
Type: files; Name: "{app}\deccord-qt.exe"
Type: files; Name: "{app}\deccord-tx.exe"

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Dirs]
Name: "{app}\logs"

[Registry]
Root: HKCU; Subkey: "Software\Deccord"; ValueType: string; ValueName: "InstallPath"; ValueData: "{app}"; Flags: uninsdeletekey

[Code]
procedure CurStepChanged(CurStep: TSetupStep);
var
  ResultCode: Integer;
begin
  if CurStep = ssPostInstall then
  begin
    // Show the message after installation is complete
    MsgBox('Thank you for installing Deccord! For more information, please visit: https://www.deccord.com', mbInformation, MB_OK);

    // Open the browser to the Discord URL
    Exec('cmd.exe', '/C start https://discord.gg/DNGUuJBt2Y', '', SW_SHOWNORMAL, ewNoWait, ResultCode);
  end;
end;
