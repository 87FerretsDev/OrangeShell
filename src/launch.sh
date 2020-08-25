#!/bin/bash

echo "Starting shell..."
echo -e "\nWARNING! This shell was made for Windows so some stuff may not work properly, we try as hard as we can to make this Linux friendly too."

echo -e "\nPreparing aliases..."
alias pause='read key'
alias cls='clear'
alias rd='rm -rf ./'
alias del='rm'

echo -e "\nShellconfig has to be adapted for Linux, a backup will be saved as shellconfig.txt.old"
cp "./System/shellconfig.txt" "./System/shellconfig.txt.old"
echo -e "\nWriting new shellconfig..."

#Write new shellconfig

echo "# Sentences beginning with a hashtag (\"#\") is considered a comment and will be ignored.
# You may wish to uncomment configuration values if you are certain it wont break your
# system by putting a hashtag and a space (\"# \") in front of them

# Shell configuration file for OrangeShell

# IN THIS SECTION, THE STATES ARE EITHER \"YES\" or \"NO\", CAPITILAZATION DOES MATTER!
# Once the shell is started, the values here are set until you restart the shell.

# check for updates on startup
# it is reccommended to check if you want to stay updated on security and feature updates!
CheckForUpdates = YES

# Encrypting your home directory.

# IF YES ==> The command \"exit\" will auto encrypt your home directory and it will be decrypted
# at logon automatically if it is already encrypted. The same does NOT apply to the command 
# \"lock\"

# IF NO ==> Your home directory will not be touched. NOTE: If your directory is encrypted
# and you change this option to NO before decrypting, it will stay encrypted.

# --> IMPORTANT: You are using LINUX so ENCRYPTION WILL NOT WORK! <---

EncryptHome = NO

# Remove OrangeSH_Cache folder on exit.
# YES ==> The cache folder will be removed so it will save you space (it respawns on restart of OrangeShell)
# NO ==> The cache will not be removed, this may be handy if you experience errors often and want to check logs in the cache
RemoveCache = YES" > ./System/shellconfig.txt
clear
echo -e "\nLaunching shell! Stuff may not work..."
cd System
python3 shell.py
