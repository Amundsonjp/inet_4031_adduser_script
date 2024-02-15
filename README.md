## INET 4031 adduser Script
inet_4031_adduser_script

### Description:
This repository contains code for lab 4. This code will be adding users with a script.
There are two files in this repository. create-users.input is a file that is to be edited to add users. create-users.py is a python script used to run through the create-users.input file and add the users from that file.

### Operation:
To operate this repository, a user must access the file create-users.input through code such as 'nano create-users.input' while in the directory with the file.
While in the create-users.input file, the user can create a line such as user01:pass01:Last01:First01:group01,group2 for each user that needs to be added. A username can be placed in the first spot, followed by a ':' after each entry, then the password, then the last name, then the first name. After the first name the last ':' is placed and a group can be added or '-' could be placed. Multiple groups can be added by placing a ',' after a group and then entering the new group. After the file is set with the users to be added, save and exit.
To finalize adding the users run the following in the command line 'sudo ./create-users.py < create-users.input'. This will run the code and create the new users.
