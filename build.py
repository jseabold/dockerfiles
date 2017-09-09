#! /usr/bin/env python

import glob
import os
import requests
import subprocess
from subprocess import PIPE
import sys
import urllib
import yaml


DOCKER_REPO_PREFIX = 'jseabold'


def write_subprocess(p):
    for line in iter(p.stdout.readline, b''):
        sys.stdout.write(line.decode())


def get_repo_and_tag(dockerfile):
    base = os.path.dirname(dockerfile)
    repo = os.path.join(DOCKER_REPO_PREFIX, base)
    return base, repo


def get_manifest_auth_token(repo):
    # https://docs.docker.com/registry/spec/auth/token/

    query = urllib.parse.urlencode({
        'service': 'registry.docker.io',
        'scope': 'repository:{repo}:pull'.format(repo=repo)
    })

    login = urllib.parse.urlunsplit((
        'https',
        'auth.docker.io',
        'token',
        query,
        ''
    ))

    token = requests.get(login, json=True).json()["token"]
    return token


def get_tags(repo):
    token = get_manifest_auth_token(repo)
    url = "https://registry.hub.docker.com/v2/{repo}/tags/list"
    tags = requests.get(
        url.format(repo=repo),
        headers={
            'Authorization': 'Bearer {}'.format(token)
        },
        json=True
    ).json()['tags']
    return tags


def build(base, repo_tag):
    print("Building {}".format(repo_tag))

    # use the go client. the python client requires unix sockets
    #
    p = subprocess.Popen(["docker", "build", "--pull", "-t", repo_tag, base],
                         stdout=PIPE)
    write_subprocess(p)


def push(repo_tag):
    print("Pushing {}".format(repo_tag))

    p = subprocess.Popen(["docker", "push", repo_tag], stdout=PIPE)
    write_subprocess(p)


def main():
    dockerfiles = glob.glob("*/Dockerfile")
    dockerfiles.sort()

    with open('tags.yaml') as tags:
        tags = yaml.load(tags)

    for dockerfile in dockerfiles:
        base, repo = get_repo_and_tag(dockerfile)
        pushed_tags = get_tags(repo)
        tag = str(tags[base])
        if tag in pushed_tags:
            print("Not updating {}".format(repo))
            continue

        repo_tag = ":".join((repo, tag))
        build(base, repo_tag)
        if os.environ["CIRCLE_BRANCH"] == "master":
            push(repo_tag)

        # err on the side of removing everything for now
        p = subprocess.Popen(["docker", "rmi", repo_tag], stdout=PIPE)
        write_subprocess(p)


if __name__ == "__main__":
    main()
