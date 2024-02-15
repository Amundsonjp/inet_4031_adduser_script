#!/usr/bin/python3
import os
import re
import sys

def main():
    for line in sys.stdin:
        match = re.match("^#", line)
        fields = line.strip().split(':')
        if match or len(fields) !=5:
            #This if statement will skip the rest of the for loop if the line begins with # because it is an invalid entry or it doesn't have 5 fields, which would also make it an invallid entry and cause the function to fail
            continue
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," %  (fields[3],fields[2])
        groups = fields[4].split(',') #this function splits entry 4 (groups) into multiple sections, allowing an entry to be part of multiple groups
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        #print cmd
        os.system(cmd) #this will run the cmd output into the command line, which lets us automate typing this into the command line ourselves
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        #print cmd
        os.system(cmd)
        for group in groups: #this for loops adds groups to the user, so the user can have the permissions of those groups
            if group != '-':
                print ("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
