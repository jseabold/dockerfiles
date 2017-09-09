#! /usr/bin/env python

import glob
from pprint import pprint

import docker

from util import get_repo_and_tag

docker_client = docker.from_env()


def push(repo_tag):
    stream = docker_client.images.push(repo_tag, stream=True, decode=True)
    # not going to try to make this nice looking for now
    for items in stream:
        pprint(items)


def main():
    dockerfiles = glob.glob("*/Dockerfile")
    dockerfiles.sort()

    for dockerfile in dockerfiles:
        _, repo_tag = get_repo_and_tag(dockerfile)
        push(repo_tag)


if __name__ == "__main__":
    main()
