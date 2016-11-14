#!/bin/env python

DOCKER_REPO_PREFIX = 'jseabold'


def push(tag):
    p = subprocess.Popen(["docker", "push", tag], stdout=PIPE)
    for line in iter(p.stdout.readline, ''):
        sys.stdout.write(line.decode())


def main():
    dockerfiles = glob.glob("*/Dockerfile")
    for dockerfile in dockerfiles:
        base = os.path.dirname(dockerfile)
        tag = os.path.join(DOCKER_REPO_PREFIX, ':'.join((base, 'latest')))
        push(tag)


if __name__ == "__main__":
    main()
