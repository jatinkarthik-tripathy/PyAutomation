@echo off

set fn1=%1
set fn2=%2

If "%1"=="" (
    echo "error"
) else (
    python D:\Projects\PyAutomation\main_auto.py %fn1% %fn2%
)
timeout 5 >nul
exit