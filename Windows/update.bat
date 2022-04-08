@echo off
set CWD=%~dp0
set PROJ_ROOT=%CWD%..
set PYTHON=%PROJ_ROOT%\env\Scripts\python.exe
cd %PROJ_ROOT%

setlocal
:: RUS? Maybe Backup first?
echo "It is recommended you export a backup of your data prior to running updates."
echo "Common approaches include using the built-in 'export' tool in the admin console or taking a snapshot of the server state (ideally both)."
:PROMPT
SET /P AREYOUSURE=Have you backed up your data and prepared to go through with this update (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END
git pull
%PYTHON% -m pip install -r %PROJ_ROOT%\TEKDB\requirements.txt
%PYTHON% %PROJ_ROOT%\TEKDB\manage.py migrate
%PYTHON% %PROJ_ROOT%\TEKDB\manage.py collectstatic --no-input
%PYTHON% %PROJ_ROOT%\TEKDB\manage.py compress
C:\Windows\System32\iisreset.exe

:END
endlocal