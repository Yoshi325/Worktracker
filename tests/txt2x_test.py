from nose.tools import *
from WorkTracker import txt2x
from datetime import datetime
from subprocess import call
import os

def setup():
    print "Starting test\n\n"
    job_num = "1234"
    item = "1"
    for i in range(21,40):

        pcmk = "%s" % str(i)
        welder = "david"
        plate = "plate"
        pipe = "pipe"
        now = datetime.now()
        print (job_num, item, pcmk,welder,plate,pipe,now)
        txt2x.txt2x(job_num, item, pcmk, welder, plate, pipe, now)
        print "\n Ran txt2x.Txt2x()\n"
setup()
