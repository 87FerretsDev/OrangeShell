#    Copyright (C) 2020 OrangeShell Developers
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    See https://www.gnu.org/licenses/ for a copy of the GNU GPL License
#
# 	 The ORANGEShell Repo can be found here: https://87ferrets.ml/FTP/OrangeShell/

# I am caching the results of readConfig() because python is pestering me saying "variable 'needed' is not used" and also it looks cool, you can delete cache, i cant stop the 
# caching via shellconfig because this IS the function that reads shellconfig, if you hate caching, just remove the cache code and recompile using
# "python -OO -m py_compile shell.py" and rename the file in _pycache_ to shell.py and replace the source version with the binary version.
# I know its inconvient, I will look for a way to not use the 'needed' variable, currently using it because I cant have a blank "if" statement
# The command "exit" will auto-delete the cache as it doesnt matter because it will respawn on every new instance.
# Cache code has a "# CACHE CODE" comment next to it if you want to remove...
# Thanks!

import os
if not os.path.exists(os.getcwd() + '\\OrangeSH_Cache'): # WE NEED THE OrangeSH_Cache FOLDER FOR IMPORTANT THINGS SUCH AS GETFILE PLACING YOUR REQUIRED FILES HERE IF YOU DONT HAVE A HOME DIRECTORY
	os.system('mkdir OrangeSH_Cache')
from random import randint
def readConfig(key):
	read_cache_number = str(key) + '.' + str(randint(1,100)) # CACHE CODE
	read_cache = open(os.getcwd() + '\\OrangeSH_Cache\\' + read_cache_number + '.read_data.log', "a+") # CACHE CODE
	read_cache.write('LookingForKey:"' + str(key) +'", SearchFile:shellconfig.txt, Handler:readConfig(), CacheMethod:ReadCache' + "\n\n") # CACHE CODE
	read_cache.close() # CACHE CODE
	configFile = open('shellconfig.txt', "r")
	for line in configFile:
		if line.strip() == "":
			needed = 'NO'
			read_cache = open(os.getcwd() + '\\OrangeSH_Cache\\' + read_cache_number + '.read_data.log', "a+") # CACHE CODE
			read_cache.write('Read:"' + str(line.strip()) + '", Needed:' + needed +", Reason:Line_has_no_data, ActionTaken:N/A \n") # CACHE CODE
			read_cache.close() # CACHE CODE
		else:
			line_stripped = line.strip()
			ln_split = line_stripped.split()
			if ln_split[0] == "#":
				needed = 'NO'
				read_cache = open(os.getcwd() + '\\OrangeSH_Cache\\' + read_cache_number + '.read_data.log', "a+") # CACHE CODE
				read_cache.write('Read:"' + str(line.strip()) + '", Needed:' + needed +", Reason:Comment_Line, ActionTaken:N/A \n") # CACHE CODE
				read_cache.close() # CACHE CODE
			elif ln_split[0] == key:
				needed = 'YES'
				read_cache = open(os.getcwd() + '\\OrangeSH_Cache\\' + read_cache_number + '.read_data.log', "a+") # CACHE CODE
				read_cache.write('Read:"' + str(line.strip()) + '", Needed:' + needed +", Reason:Correct_Key, ActionTaken:Variable_Returned \n") # CACHE CODE
				read_cache.write('Action: HALT_CACHE, Start:NOW, End:NOW') # CACHE CODE
				read_cache.close() # CACHE CODE
				return ln_split[2]
			else:
				needed = 'NO'
				read_cache = open(os.getcwd() + '\\OrangeSH_Cache\\' + read_cache_number + '.read_data.log', "a+") # CACHE CODE
				read_cache.write('Read:"' + str(line.strip()) + '", Needed:' + needed +", Reason:Wrong_Key, ActionTaken:N/A \n") # CACHE CODE
				read_cache.close() # CACHE CODE
	configFile.close()

# ---- this section imports dependencies ----
import importlib
import sys
if os.path.isfile('user_setup.pyc'):
	os.system('cls')
	print('Entering user setup ...')
	print('')
	user_setup = importlib.import_module('user_setup')
	status = user_setup.setup()
	sys.exit(0)
try:
	UpdateStatus = readConfig('CheckForUpdates') 
	EncryptHomeStatus = readConfig('EncryptHome')
	RemoveCacheStatus = readConfig('RemoveCache')
	os.system('cls')
	os.system('title OrangeShell')
	print('Welcome to OrangeShell v2.0.0')
	print('[Starting] Verifying OS ...') # verifies that he OS is windows if not give error and exit.
	if os.name != "nt":
		print('E: This shell only works in Windows.')
		sys.exit(0)
	ROOT_DIR = str(os.getcwd())
	print('Log in to shell.\n')
	try:
		sys.path.insert(1, str(ROOT_DIR) + '\\UMS')
		login_system = importlib.import_module('login')
		MASH = login_system.login()
		UserAcc = MASH[0]
		PassW = MASH[1]
	except Exception as e:
		print('E: An error occurred with login.')
		print('EXCEPTION DETAILS: '+ str(e))
		sys.exit(0)
	try:
		from colorama import init, Fore, Back, Style
		init(convert=True)
	except:
		print('E: MISSING DEPENDENCY "colorama". PLEASE DOWNLOAD THIS PACKAGE THEN RESTART THE SHELL')
		sys.exit(0)
	sys.path.insert(1, str(ROOT_DIR) + '\\Commands') # inserts C:\Orange_OS\System\Commands as path to use later

	# ---- this section is the main body of the commandline ----
	def Prompt():
		try:
			print(Style.BRIGHT + Fore.MAGENTA + str(UserAcc) + ' ' + Fore.WHITE + '[' + os.getcwd() + ']:' + Style.RESET_ALL, end = '')
			command_Original = input(' ') # prompt where user types commands
			command_Original_Strip = command_Original.strip() # removes leading and trailing whitespace
			command_Split = list(command_Original_Strip.split(" ")) # turns input into array
			if command_Split[0] == "": # if no words entered, return
				Prompt()
			command_Directory = str(ROOT_DIR) + "\\Commands\\" # where commands are located
			command_Loc = command_Directory + command_Split[0] # adds the command itself into the directory var
			if os.path.exists(command_Loc + '.py'): # adds .py extension and checks if that file exists
				cmd_Args = " ".join(command_Split[1:]) # IF COMMAND EXISTS: Takes out command name and turns rest of array back to string for arguments
				shellprg = importlib.import_module(command_Split[0]) # imports commandfile for execution as shellprg
				# all commands must have a function called shellexec that the shell calls to execute commands.
				try:
					shellprg.shellexec(cmd_Args) # executes commands and passes any args to it
					Prompt()
				except Exception as e:
					print("Something went wrong with command execution. \nERROR DETAILS: While executing '" + str(command_Split[0]) + "', the following error occured: "+ str(e))
					Prompt()
			else:
				print(Style.BRIGHT + Fore.RED + 'E: Command "'+ command_Split[0] +'" not found' + Style.RESET_ALL) # IF COMMAND DOESNT EXIST: Give error and go back to prompt
			Prompt()
		except KeyboardInterrupt:
			print('^C') # if ctrl+c pressed, do nothing.
			Prompt()
	print("")
	if os.path.isdir(ROOT_DIR + '\\..\\' + UserAcc):
		os.chdir(ROOT_DIR + '\\..\\' + UserAcc)
	else:
		print(Style.BRIGHT + Fore.YELLOW + 'Warning: Your home directory which should be located at '+ ROOT_DIR + '\\..\\' + UserAcc + ' is non-existent. Some programs may not work with this issue.' + Style.RESET_ALL)
	if UpdateStatus == "YES":
		try:
			import requests
		except:
			print('MISSING COMPONENT: requests')
			sys.exit(0)
		try:
			print('Checking for updates ...', end="\r")
			orangeosver = requests.get('https://87ferrets.ml/SystemFetchArchive/OrangeOS/LV_STRING.INFO')
			VERSTRING = orangeosver.text.strip()
			if VERSTRING == "2.0.0":
				print(Style.BRIGHT + Fore.GREEN + 'OrangeShell is updated to its latest version, which is '+ str(VERSTRING) +'.' + Style.RESET_ALL)
			else:
				print(Style.BRIGHT + Fore.YELLOW + 'OrangeShell is outdated! Version '+ str(VERSTRING) + ' is available. It is recommended that you update using the command "update"' + Style.RESET_ALL)
		except Exception as e:
			print(Style.BRIGHT + Fore.RED + 'Cannot check for updates! Will check for updates on next boot. Details: ' + str(e) + Style.RESET_ALL)
	else:
		print('Update checking was disabled in shellconfig.txt')
	Prompt()
except Exception as e:
	import os, sys
	# Kernel Panic
	os.system('cls') # clear screen
	print('[Kernel Panic] A fatal exception occured that caused OrangeShell to become very unstable, therefore it has been halted to prevent it from being corrupted.')
	print('This is most likely caused by missing/corrupted system files, a badly coded script or a misconfigured shellconfig.txt')
	print('If you see this more than once, please seek help using the details given below')
	print("")
	print('=== EXCEPTION DETAILS ===')
	print('The exception was: ' + str(e))
	print('')
	print('Kernel Panic Ended. Press any key to exit...')
	os.system('pause>nul')