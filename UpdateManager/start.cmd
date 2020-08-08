@echo off
title Update OrangeOS
set version_of_orangeos=%*
python3 updater_main.py --version %version_of_orangeos%
echo UpdateManager exited. Press any key to exit.
pause>nul
exit