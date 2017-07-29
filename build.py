#! /usr/bin/env python

import glob
import os
import subprocess
from subprocess import PIPE
import sys

DOCKER_REPO_PREFIX = 'jseabold'


def build(base, repo):
    print("Building {}".format(repo))
    # use the go client
    p = subprocess.Popen(["docker", "build", "--pull", "-t", repo, base],
                         stdout=PIPE)
    for line in iter(p.stdout.readline, b''):
        sys.stdout.write(line.decode())


def main():
    dockerfiles = glob.glob("*/Dockerfile")
    dockerfiles.sort()

    for dockerfile in dockerfiles:
        base = os.path.dirname(dockerfile)
        tag = os.environ.get("TAG", "latest")
        repo = os.path.join(DOCKER_REPO_PREFIX, ':'.join((base, tag)))
        build(base, repo)


if __name__ == "__main__":
    main()
