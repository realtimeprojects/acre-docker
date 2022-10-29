import os


def get_docker_path(image="base"):
    return os.path.join(os.path.dirname(__file__), image)
