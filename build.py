#! /usr/bin/env python

import glob
import os
import subprocess
from subprocess import PIPE
import sys

from util import get_repo_and_tag

def build(base, repo_tag):
    print("Building {}".format(repo_tag))
    # use the go client
    p = subprocess.Popen(["docker", "build", "--pull", "-t", repo_tag, base],
                         stdout=PIPE)
    for line in iter(p.stdout.readline, b''):
        sys.stdout.write(line.decode())


def main():
    dockerfiles = glob.glob("*/Dockerfile")
    dockerfiles.sort()

    for dockerfile in dockerfiles:
        base, repo_tag = get_repo_and_tag(dockerfile)
        build(base, repo_tag)


if __name__ == "__main__":
    main()
