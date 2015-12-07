from nose.tools import *
from WorkTracker import txt2xlsx
from datetime import datetime
from subprocess import call
from termcolor import colored, cprint
import os


def setup():

    cprint ("\nStarting Test.....\n", 'green')
    job_num = "1234"
    item = "1"
    
    for i in range(1, 21):
        pcmk = "%s" % str(i)
        welder = "david"
        plate = "hello"
        pipe = "how are you"
        now = datetime.now()
        txt2xlsx.txt2xl(job_num, item, pcmk, welder, plate, pipe, now)

setup()

