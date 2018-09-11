import os, sys, time, re

def executeCmd(args, redirect = False, redirectSource = ""):
    pid = os.getpid() 
    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)

    elif rc == 0:                   # child
        if redirect:
            os.close(1)                 # redirect child's stdout
            sys.stdout = open(redirectSource, "w")
            fd = sys.stdout.fileno()

        for dir in re.split(":", os.environ['PATH']): # try each directory in path
            program = "%s/%s" % (dir, args[0])
            try:
                os.execve(program, args, os.environ) # try to exec program
            except EnvironmentError:             # ...expected
                pass                              # ...fail quietly 

        os.write(2, ("Child: Error: Could not exec %s\n" % args[0]).encode())
        sys.exit(1)                 # terminate with error

    else:                           # parent (forked ok)
        childPidCode = os.wait()

def runShell():
    while True:
        line = raw_input("$ ")
        if line == "q":
            break
        else:
            redirect = line.split(">")
            needsToRedirect = len(redirect) > 1
            executeCmd(filter(None, redirect[0].split(" ")), needsToRedirect, redirect[1].strip() if needsToRedirect else "")
    
runShell()