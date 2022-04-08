set PROJ_ROOT=C:\Apps\TEKDB
set PYTHON=%PROJ_ROOT%\env\Scripts\python.exe
cd %PROJ_ROOT%
git pull
%PYTHON% -m pip install -r %PROJ_ROOT%\TEKDB\requirements.txt
%PYTHON% %PROJ_ROOT%\TEKDB\manage.py migrate
%PYTHON% %PROJ_ROOT%\TEKDB\manage.py collectstatic
%PYTHON% %PROJ_ROOT%\TEKDB\manage.py compress
C:\Windows\System32\iisreset.exe
PAUSE