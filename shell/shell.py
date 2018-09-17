import os, sys, time, re, subprocess


def getArguments(line):
    # wc < ayabi.txt
    if re.findall(r'\b<\b', line):
        args = line.split("<")
        if len(args) == 1:
            return filter(None, line.split(" "))

        else:
            fileName = args[1].strip()
            # Read contents of file
            file = open(fileName, "r")
            contents = file.readlines()  # "bla bla bla".split(" ")

            fileContents = filter(None, contents)
            cmd = filter(None, args[0].split(" "))
            return cmd + fileContents

    if re.findall(r'\b|\b', line):
        args2 = line.split("|")
        if len(args2) == 1:
            return filter(None, line.split(" "))

        else:
            cmd = args2[1].strip()
            process = subprocess.Popen(line, stdout=subprocess.PIPE, shell=True)
            temp = process.communicate()[0]
            print(temp)
            return ""


def executeCmd(line, redirect=False, redirectSource=""):
    pid = os.getpid()
    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)

    elif rc == 0:  # child
        if redirect:
            os.close(1)  # redirect child's stdout
            sys.stdout = open(redirectSource, "w")
            # fd = sys.stdout.fileno()

        args = getArguments(line)
        if args == '':
            runShell()

        if args != '':
            for dir in re.split(":", os.environ['PATH']):  # try each directory in path
                program = "%s/%s" % (dir, args[0])
                try:
                    os.execve(program, args, os.environ)  # try to exec program
                except EnvironmentError:  # ...expected
                    pass  # ...fail quietly


        os.write(2, ("Child: Error: Could not exec %s\n" % args[0]).encode())
        sys.exit(1)  # terminate with errorq

    else:  # parent (forked ok)
        childPidCode = os.wait()


def runShell():
    while True:
        line = raw_input(os.environ['PS1'])
        if line == "q":
            break
        else:
            redirect = line.split(">")
            needsToRedirect = len(redirect) > 1
            executeCmd(redirect[0], needsToRedirect, redirect[1].strip() if needsToRedirect else "")


runShell()