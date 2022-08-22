@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~0"" h",0)(window.close)&&exit
:begin

timeout 1

set path=D:\Program Files\Python38

python D:\±ÚÖ½\set_today_background.py

pause


