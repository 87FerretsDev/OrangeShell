#!/bin/bash

no_encrypt() {
  DATE=`date +"%d-%b-%Y"`
  if test -f "./System/shellconfig.old"; then
    BACKUP_NAME="./System/shellconfig.old.$DATE"
  else
    BACKUP_NAME="./System/shellconfig.old"
  fi
  echo -e "\nEncryption is disabled due to the lack of encryption software. \nRewriting shellconfig to match this. \nNOTE: A backup will be saved as $BACKUP_NAME"
  cp "./System/shellconfig.txt" "$BACKUP_NAME"
  echo "
  # Sentences beginning with a hashtag (\"#\") is considered a comment and will be ignored.
  # You may wish to uncomment configuration values if you are certain it wont break your
  # system by putting a hashtag and a space (\"# \") in front of them

  # Shell configuration file for OrangeShell

  # IN THIS SECTION, THE STATES ARE EITHER \"YES\" or \"NO\", CAPITILAZATION DOES MATTER!
  # Once the shell is started, the values here are set until you restart the shell.

  # check for updates on startup
  # it is reccommended to check if you want to stay updated on security and feature updates!
  CheckForUpdates = YES

  # Encrypting your home directory.

  # Error: You do not have proper software to encrypt your home directory so it is disabled

  EncryptHome = NO

  # Remove OrangeSH_Cache folder on exit.
  # YES ==> The cache folder will be removed so it will save you space (it respawns on restart of OrangeShell)
  # NO ==> The cache will not be removed, this may be handy if you experience errors often and want to check logs in the cache
  RemoveCache = YES" > ./System/shellconfig.txt
}

echo "Starting shell..."
echo -e "\np7zip-full must be installed to use encryption. Checking for that now..."

if ! dpkg-query -l p7zip-full > /dev/null; then
   echo -e "p7zip-full not found! \nEnter sudo password to install, else press CTRL+C to cancel."
    sudo apt-get install p7zip-full
    echo -e "\nRechecking..."
    if ! dpkg-query -l p7zip-full > /dev/null; then
      no_encrypt
    fi
else
    echo -e "\np7zip-full Installed!"
fi

echo -e "\nLaunching shell!"
cd System
python3 shell.py
