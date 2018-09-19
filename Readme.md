## Introductory Lab

This repository contains the code for the python introduction lab. The
purpose of this lab is to have a fairly simple python assignment that introduces
the basic features and tools of python

The following program `wordCount.py` does the following (working with the `speech.txt` and `speechKey.txt`) :

* Takes as input the name of an input file and output file

  To run program run command:
  
           $ python wordCount.py speech.txt output.txt
      e.g. $ python <program_file> <input_file> <output_file>
* Keeps track of the total number of times each word occurs in the text file 
* Excludes white space and punctuation
* Is case-insensitive
* Prints out to the output file (overwriting if it exists) the list of
  words sorted in descending order with their respective totals
  separated by a space, one word per line

Testing this program uses `wordCountTest.py` which takes the output file and notes any
differences within the key file. To test run command:

            $ python wordCountTest.py speech.txt output.txt speechKey.txt
        e.g $ python <program_file> <input_file> <output_file> <key_file>

If `declaration.txt` and `declarationKey` would like to be used `wordCount.py` needs to be modified on `line 27`
        
        document_key = open('speechKey.txt')       # speech.txt example TO
        document_key = open('declarationhKey.txt') # declaration.txt example
           

The re regular expression library and python dictionaries are
used in the program. 

Note this program is using Python 3.0 version.

References: 

* https://code.tutsplus.com/tutorials/counting-word-frequency-in-a-file-using-python--cms-25965

## Shell Lab

Shell lab is located under the shell directory. `shell/`
 
This lab is running on a Windows environment setup. Use build-in Python version 2.7.14 in Cygwin.

##### __Note__: If this env is not set up on Cygwin Python v.2.7, shell will not run how its supposed to.

Requirements met:
- Shell terminates when it reaches EOF. Use Ctrl+D to exit shell.

- Prompt takes the PS1 environment variable into account. 

###### Run shell on Cygwin: `$ python shell.py` or `./shell.py`

Run shell and execute command for redirect to: `>`

            $ echo hi > output.txt
Run shell and execute command for redirect from: `<`

            $ wc < output.txt

Run shell and execute command to list files in directory and word count on `ls`: `|`
        
            $ ls | wc
            

References: 

* *https://stackoverflow.com/questions/24426451/how-to-terminate-loop-gracefully-when-ctrlc-was-pressed-in-python/24426816*
* *https://docs.python.org/2/library/subprocess.html*
* *https://www.poftut.com/execute-shell-command-python/*
* *https://github.com/robustUTEP/os-demos*