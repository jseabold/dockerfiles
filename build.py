#! /bin/env python

import glob
import os
import subprocess
from subprocess import PIPE
import sys

DOCKER_REPO_PREFIX = 'jseabold'


def build(base, tag):
    # use the go client
    p = subprocess.Popen(["docker", "build", "--pull", "-t", tag, base],
                         stdout=PIPE)
    for line in iter(p.stdout.readline, ''):
        sys.stdout.write(line.decode())


def main():
    dockerfiles = glob.glob("*/Dockerfile")
    for dockerfile in dockerfiles:
        base = os.path.dirname(dockerfile)
        tag = os.path.join(DOCKER_REPO_PREFIX, ':'.join((base, 'latest')))
        build(base, tag)


if __name__ == "__main__":
    main()
