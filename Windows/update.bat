@echo off
set CWD=%~dp0
set PROJ_ROOT=%CWD%..
set PYTHON=%PROJ_ROOT%\env\Scripts\python.exe
cd %PROJ_ROOT%
git pull
%PYTHON% -m pip install -r %PROJ_ROOT%\TEKDB\requirements.txt
%PYTHON% %PROJ_ROOT%\TEKDB\manage.py migrate
%PYTHON% %PROJ_ROOT%\TEKDB\manage.py collectstatic --no-input
%PYTHON% %PROJ_ROOT%\TEKDB\manage.py compress
C:\Windows\System32\iisreset.exe