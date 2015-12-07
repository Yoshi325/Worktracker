from subprocess import call
from termcolor import colored, cprint
import os
import openpyxl

# change to Documents directory
os.chdir("/home/yojimbo/Documents/")


def txt2xl(job_num, item, pcmk, welder, plate, pipe, now): 
    print "Trying to open %sitem%s.xlsx" % (job_num, item)  #### for testing
        
    try:
        wb = openpyxl.load_workbook('%sitem%s.xlsx' % (job_num, item))
        ws = wb.get_sheet_by_name('Sheet')
        print "Opened file.....\n"
        #for i in range(2, ws.get_highest_row()):
         #   print ws.cell.value
          #  txt2xl()
    except:
        cprint ("\nSomething went wrong!\n", 'red')
        exit(0)

