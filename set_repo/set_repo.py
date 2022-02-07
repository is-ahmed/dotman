
from git.repo import Repo
import git
import os
import json

def set_repo(url: str):

    """Precondition:
        - The config file is created with the proper format
        - The url has been validated as repo for a git repository

    """
    username = os.getlogin()
    config_path = "/home/" + username + "/.config/dotman/config.json"
    
    with open(config_path, "r") as config_file:
        data = json.load(config_file)

    data['url'] = url

    with open(config_path, "w") as config_file:
        json.dump(data, config_file)

    

def clone(url: str):
    """Clone the git repo into the home directory
    using the repo url

    Precondition:
        - url points to a valid and existing git repo

    """
    try:
        Repo.clone_from(url, "~/")
        set_paths()
    except git.exc.GitError:
        print('ERROR! Repo does not exist!')

def set_paths():

    ...
     

      


