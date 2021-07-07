set python_home=c:\app\python24
rem set python_home=d:\app\python24
set main=pyconsole_nevow.py
set pythonpath=%~dp0
start %python_home%\python.exe %python_home%\Scripts\twistd.py -noy %~dp0\%main%
