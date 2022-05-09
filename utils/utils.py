from git.repo import Repo

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
        Repo.clone_from(url, '/home/' + getpass.getuser() + '/.config/dotman/dotfiles')
        link_files()
    except git.exc.GitError:
        print('ERROR! Repo does not exist!')

def link_files():
    ...
    

def diff():
    breakpoint()
    username = os.getlogin()
    if os.path.exists("/home/" + username + "/.config/dotman") == False:
       print("Repo is not set. Invalid usage") 
    else:
        repo = Repo("/home/" + username + "/.config/dotman/dotfiles")
        branch = repo.active_branch.name
        commit_current = repo.commit(branch)
        commit_origin_current = repo.commit("origin/" + branch)
        diff_index = commit_origin_current.diff(commit_current)
        for diff_item in diff_index.iter_change_type('M'):
            # TODO: Figure out a way to format diff better like in 'git diff'
            print("A blob:\n{}".format(diff_item.a_blob.data_stream.read().decode('utf-8')))
            print("B blob:\n{}".format(diff_item.b_blob.data_stream.read().decode('utf-8')))

def sync():
    ...


