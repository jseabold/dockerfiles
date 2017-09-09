#! /usr/bin/env python

import glob
import os
from pprint import pprint
import sys
import urllib
import yaml

import docker
import requests


DOCKER_REPO_PREFIX = 'jseabold'
docker_client = docker.from_env()
raw_client = docker.APIClient()


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
    stream = raw_client.build(pull=True, tag=repo_tag, path=base, decode=True)
    for line in stream:
        # i'm not sure where these returns are documented
        for line_type, output in line.items():
            sys.stdout.write(output)
            if line_type != 'stream':
                sys.stdout.write('\n')


def push(repo_tag):
    print("Pushing {}".format(repo_tag))
    stream = docker_client.images.push(repo_tag, stream=True, decode=True)
    # not going to try to make this nice looking for now
    for items in stream:
        pprint(items)


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
        print(repo_tag)
        print("Building")
        print("Pushing")
        # build(base, repo_tag)
        # push(repo_tag)


if __name__ == "__main__":
    main()
