import sys
import argparse
import os
import re
import json
import git
from typing import Optional
from utils import utils
from set_repo import set_repo

def main():

    username = os.getlogin()
    if os.path.exists("/home/" + username + "/.config/dotman") == False:
        print("~/.config/dotman folder does not exist setting up now...")
        firsttime_setup(username)


    argument_parser = create_parser()
    
    args = argument_parser.parse_args()
    
    process_args(args)


def create_parser():
    parser = argparse.ArgumentParser(description="Sync your dotfiles with one seamless CLI tool")
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("sync", help="sync your dotfiles with your current repo", nargs='?')
    parser.add_argument("diff", help="Find the diff between local and remote versions of all dotfiles",
                        nargs = '?')
    parser.add_argument("-s", "--setrepo", help="Set the git repo of your dotfiles")
    
    group.add_argument("-q", "--quiet", action="store_true")

    return parser

def process_args(args: argparse.Namespace):
    setrepo = args.setrepo
    sync = args.sync
    diff = args.diff
    if setrepo is not None: 
        is_setrepo_valid = validate_repo(setrepo)
        if is_setrepo_valid:
            set_repo.set_repo(setrepo)
        else:
            print("Repo url is not valid. Check for any typos or spelling mistakes")

    





def firsttime_setup(username: str):

    config_dir = "/home/" + username + "/.config/dotman"

    os.mkdir(config_dir)
    touch(config_dir + "/config.json")

    data = {
        "url": None,
    }

    with open(config_dir + "/config.json", 'w') as f:
        json.dump(data, f)





def validate_repo(repo_url: str) -> Optional[bool]:
    """Return whether the given url points to an existing git
    repository 

    """
    
    match = re.match(r"((git|ssh|http(s)?)|(git@[\w\.]+))(:(//)?)([\w\.@\:/\-~]+)(\.git)?(/)?", repo_url)

    # Now I will check if the url points to a public git repo



    return match is not None

def lsremote(url: str):
    g = git.cmd.Git()

    try g.ls_remote(url):
        return True

    


def touch(path: str):
    with open(path, 'a'):
        os.utime(path, None)

       



if __name__ == '__main__':
    main()
