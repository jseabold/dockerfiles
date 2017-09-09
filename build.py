#! /usr/bin/env python

import glob
import docker
import sys

from util import get_repo_and_tag


docker_client = docker.from_env()
raw_client = docker.APIClient()


def build(base, repo_tag):
    print("Building {}".format(repo_tag))
    stream = raw_client.build(pull=True, tag=repo_tag, path=base, decode=True)
    for line in stream:
        # i'm not sure where these returns are documented
        for line_type, output in line.items():
            sys.stdout.write(output)
            if line_type != 'stream':
                sys.stdout.write('\n')
    return docker_client.images.get(repo_tag)


def main():
    dockerfiles = glob.glob("*/Dockerfile")
    dockerfiles.sort()

    for dockerfile in dockerfiles:
        base, repo_tag = get_repo_and_tag(dockerfile)
        image = build(base, repo_tag)


if __name__ == "__main__":
    main()
