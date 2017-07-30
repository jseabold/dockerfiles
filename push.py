#!/bin/env python

import glob
import os
import sys
import subprocess
from subprocess import PIPE

from util import get_repo_and_tag


def push(repo_tag):
    p = subprocess.Popen(["docker", "push", repo_tag], stdout=PIPE)
    for line in iter(p.stdout.readline, ''):
        sys.stdout.write(line.decode())


def main():
    dockerfiles = glob.glob("*/Dockerfile")
    dockerfiles.sort()

    for dockerfile in dockerfiles:
        _, repo_tag = get_repo_and_tag(dockerfile)
        push(repo_tag)


if __name__ == "__main__":
    main()
