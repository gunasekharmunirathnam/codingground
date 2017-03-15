# Hello World program in Python
#import subprocess
from subprocess import call
iam = "Sekhar"
print "Hello World!"
print iam
#call('main.py')
call('python main.py', shell=True)
