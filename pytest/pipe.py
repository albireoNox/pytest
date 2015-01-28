#!/usr/bin/env python

__author__ = 'nwilson'

import subprocess
import os
from subprocess import Popen, PIPE
from datetime import datetime
import threading
import sys


class LogPipe(threading.Thread):

    def __init__(self, tag, logfile):
        """Setup the object with a logger and a loglevel
        and start the thread
        """
        threading.Thread.__init__(self)
        self.daemon = False
        self.tag = " " + tag
        self.fdRead, self.fdWrite = os.pipe()
        self.pipeReader = os.fdopen(self.fdRead)
        self.logfile = logfile
        self.start()

    def fileno(self):
        """Return the write file descriptor of the pipe
        """
        return self.fdWrite

    def run(self):
        """Run the thread, logging everything.
        """
        for line in iter(self.pipeReader.readline, ''):
            # log5ging.log(self.level, line.strip('\n'))
            # print(datetime.now().strftime("[%H:%M:%S]") + self.tag + " Do you mean " + line.strip() + "?")
            self.logfile.write(datetime.now().strftime("[%H:%M:%S]") + self.tag + " Do you mean " + line.strip() + "?\n")

        self.pipeReader.close()

    def close(self):
        """Close the write end of the pipe.
        """
        os.close(self.fdWrite)
        self.logfile.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

def preExec(parentPid):
    print ("SUB: " + str(os.getpid()))
    print ("PARENT: " + str(parentPid))

if __name__ == "__main__":
    print ("MAIN: " + str(os.getpid()))
    logfile = open("log.txt", "w")
    pid = os.getpid()
    with LogPipe("NORMAL", logfile) as log, LogPipe("ERROR", logfile) as logerr:
        p = Popen("./slow.sh", stdout=log, stderr=logerr, preexec_fn=lambda: preExec(pid))
        p.wait()

    # popen = Popen(args="./slow.sh", stdout=PIPE)
    # output = popen.stdout
    # for line in output:
    #     log.write(line)
