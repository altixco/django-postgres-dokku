import os


def get_secret(key):
    if key in os.environ:  # Secret inside environment (Usually dokku)
        return os.environ.get(key)
    else:  # Secret inside file (Docker secrets)
        with open(os.environ.get(key + '_FILE')) as file:
            return file.read().strip()
