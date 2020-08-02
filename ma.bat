@echo off

set fn1=%1
set fn2=%2
set fn3=%3

If "%1"=="" (
    echo "error"
) else (
    python F:\Projects\PyAutomation\main_auto.py %fn1% %fn2% %fn3%
)
exit