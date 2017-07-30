import os

DOCKER_REPO_PREFIX = 'jseabold'

def get_repo_and_tag(dockerfile):
    base = os.path.dirname(dockerfile)
    tag = os.environ.get("TAG", "latest")
    repo = os.path.join(DOCKER_REPO_PREFIX, ':'.join((base, tag)))
    return base, repo
