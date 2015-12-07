# this script cleans up the Worktracker file 

from subprocess import call
import os
from termcolor import colored, cprint
try:
    print "Started Cleaning.......\n\n"
    os.chdir("/usr/local/lib/python2.7/dist-packages/")
    call(['rm', 'WorkTracker-0.1-py2.7.egg'])
    os.chdir("/projects/python/Worktracker/dist/")
    call(['rm', 'WorkTracker-0.1.-py2.7.egg'])
    os.chdir("/projects/python/Worktracker/")
    call(['sudo', 'python', 'setup.py', 'install'])

    cprint ("\n\n\nFinished cleaning\n\n\n", 'green', attrs=['bold'])

except:
    cprint ("Failed to clean files up", 'red')
    cprint ("Try running with sudo")
