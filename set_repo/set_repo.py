
from git.repo import Repo
import git
import os
import json
import getpass

def set_repo(url: str):

    """
    Set the repo for the dotfiles in the json config file

    Precondition:
        - The config file is created with the proper format
        - The url has been validated as repo for a git repository

    """
    username = os.getlogin()
    config_path = "/home/" + username + "/.config/dotman/config.json"
    
    with open(config_path, "r") as config_file:
        data = json.load(config_file)

    data['url'] = url
    data['system_path'] = config_path

    with open(config_path, "w") as config_file:
        json.dump(data, config_file)

    

def clone(url: str):
    """Clone the git repo into the home directory
    using the repo url

    Precondition:
        - url points to a valid and existing git repo
        - ~/.config/dotman exists

    """
    try:
        breakpoint()
        Repo.clone_from(url, '/home/' + getpass.getuser() + '/.config/dotman/dotfiles')
        set_paths()
    except git.exc.GitError:
        print('ERROR! Repo does not exist!')

def set_paths():
    ...
     

      


