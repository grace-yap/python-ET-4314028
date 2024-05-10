# argparse module - one of the python modules that help you read, parse, and use command-line arguments and values
# ArgumentParser() class - allows you to create an object that keeps track of all of the arguments your program accepts
from argparse import ArgumentParser 

# create new ArgumentParser() instance
parser = ArgumentParser()

# create new command-line argument called output
# as is convention, 2 dashes ('--') are in front because 'output' is a full word <==> one dash ('-') if just one letter
parser.add_argument('--output', '-o', required=True, help='The destination file for the output of this program')
# required - keyword argument to make new argument 'output' required
# help - keyword argument that provides some help text to the user that lets them know what the command is for
# -o - by convention, we want to give the user options for these arguments
#    - all of the different arguments you want to allow, you can put there there
parser.add_argument('--text', '-t', required=True, help='The text to write to the file')

# create args object using parse_args() method
# args - object that has all of our arguments as attributes on it
args = parser.parse_args()

# to access the filename
# where output is the name of our command-line argument from above
# print(args.output)
### COMMAND-LINE COMMAND (EITHER CMD OR GITBASH):
# python 11_1_writefile.py --output somefile.txt
### RESULT:
# somefile.txt

### COMMAND-LINE COMMAND (EITHER CMD OR GITBASH):
# python 11_1_writefile.py -h
### RESULT:
# usage: 11_1_writefile.py [-h] --output OUTPUT
#
# options:
#   -h, --help            show this help message and exit
#   --output OUTPUT, -o OUTPUT
#                         The destination file for the output of this program

### COMMAND-LINE COMMAND (EITHER CMD OR GITBASH):
# python 11_1_writefile.py
### RESULT:
# usage: 11_1_writefile.py [-h] --output OUTPUT
# 11_1_writefile.py: error: the following arguments are required: --output/-o

# write text to a new file
with open(args.output, 'w') as f:
    f.write(args.text+'\n')

print(f'Wrote "{args.text}" to file "{args.output}"')

### COMMAND-LINE COMMAND (EITHER CMD OR GITBASH):
# python 11_1_writefile.py -o somefile.txt -t "new text stuff trial"
# note: the quotes are NOT part of the string, but anytime you have a value with spaces in it,
# you need to put quotes around the string so that the terminal doesn't get confused what's a single value and what's potentially multiple values
### RESULT:
# Wrote "new text stuff trial" to file "somefile.txt"