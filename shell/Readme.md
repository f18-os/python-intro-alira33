##Shell Lab
 
This lab is running on a Windows environment setup. Use build-in Python version 2.7.14 in Cygwin.

#####__Note__: If this env is not set up on Cygwin, shell will not run how its supposed to.

Requirements met:
- Shell terminates when it reaches EOF. Use Ctrl+D to exit shell.

- Prompt takes the PS1 environment variable into account. 

######Run shell on Cygwin: `$ python shell.py` or `./shell.py`

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