OrangeShell Status: RELEASED V1.5.0
OrangeShell 2.0.0 is in production! Due release: End of August
=============================

DOWNLOAD OrangeShell 1.5.0 FROM HERE AND NOT USING THE COMMAND "update" --> UpdateManager had a small syntax error which caused the update to fail. This should fix it.

IF YOU ALREADY HAVE OrangeShell 1.5.0 OR HIGHER, YOU DO NOT NEED TO DOWNLOAD A NEW VERSION FROM HERE! A
BUILT IN COMMAND CALLED "update" WILL UPDATE OrangeShell FOR YOU !

OrangeShell README

Hello and thanks for your interest in Orange Shell! I will give you a full walkthrough of my Python program in
this README file...

What is Orange Shell?

OrangeShell is a small python program which provides a commandline
interface on your Windows PC. This command line interface (in version 0.5.0 at least) is very primitive and
should not replace your regular cmd.exe or powershell.exe.

Still with us? Good.

SETUP

Setup is partly user dependent. You have to extract the files into any directory (v1.0.0+ has a dynamic root directory) 
and have Python3 installed.

If you have a pre 2.0.0 release of OrangeShell (then called OrangeOS) then you must have these python modules installed:
colorama, hashlib, getpass, requests, importlib, zipfile

OrangeShell 2.0.0+ auto installs all needed modules for you,
OrangeOS 1.5.0+ has a user setup which takes the pressure of setting up OrangeShell partially off you.

How you can get these python packages (after installing Python3 and pip3):
COLORAMA = pip3 install colorama
HASHLIB = pip3 install hashlib
GETPASS = pip3 install getpass
REQUESTS = pip3 install requests
IMPORTLIB = pip3 install importlib
ZIPFILE = pip3 install zipfile

GET PYTHON HERE: https://www.python.org/ftp/python/3.7.8/python-3.7.8-amd64.exe

Once you do that just run launch.cmd and log in to the default user account. Login details:

CREDENTIALS FOR ORANGESHELL 0.5.0 TO 1.5.0:
Username = default
Password = orangeos

CREDENTIALS FOR ORANGESHELL 2.0.0+:
USERNAME = default
PASSWORD = orangeshell

You are advised to change your password or make a new account entirely.
To assure you, passwords are stored HASHED on your computer in ROOT\System\UMS (after you
extract) so nothing ever leaves your computer.

RETRIEVING FILES FROM HERE:

All files are in .zip format. The latest version of OrangeShell would be in this directory called 
"OrangeShell-X.X.X.zip" (where X.X.X is the version string) (PRE 2.0.0 releases of OrangeShell will be called
OrangeOS) where older versions will live in the Old/
directory. The latest and most updated source code will be in this directory called OrangeShell-src.zip and you
can use that to make your own fork of OrangeShell.

Feedback!
We would LOVE to hear feedback from you! Please tell us about what you like about OrangeShell and what we
could improve as well as bugs here: https://forms.gle/nYbKQJzbgnwedrqH7

If you would like to contribute code, please contribute it here: orangeosdev@gmail.com. We welcome
everyone who wants to contribue

OrangeShell ONLY WORKS ON WINDOWS!!

Read the changelog document for updates on what changed

Releases:
0.5 releases such as OrangeShell 1.5.0 and 0.5.0 are usually small releases with bug fixes and patches
1.0 releases such as OrangeShell 1.0.0 and 2.0.0 are large updates that take longer to arrive