import sys
import argparse
import os
import re
import json
import git
from typing import Optional

from git.refs import remote
from utils import utils

def main():

    username = os.getlogin()
    if os.path.exists("/home/" + username + "/.config/dotman") == False:
        print("~/.config/dotman folder does not exist setting up now...")
        firsttime_setup(username)


    argument_parser = create_parser()

    if len(sys.argv) == 1:
        print("usage")
        sys.exit()

    args = argument_parser.parse_args()
    
    process_args(args)


def create_parser():
    parser = argparse.ArgumentParser(description="Sync your dotfiles with one seamless CLI tool")

    parser.add_argument("sync", help="sync your dotfiles with your current repo", nargs='?')

    # Changes need to be commited first 
    # BUG: if just 'dotman diff' is run it gets assigned to sync since it's a positional argument
    parser.add_argument("diff", help="Find the diff between local and remote versions of all dotfiles", const=1, nargs='?')

    git_group = parser.add_mutually_exclusive_group()
    git_group.add_argument("add", help="Stage dotfiles for commits", nargs='?')
    git_group.add_argument("commit", help="Commit your staged changes", nargs='?')

    parser.add_argument("-s", "--setrepo", help="Set the git repo of your dotfiles")
    

    return parser

def process_args(args: argparse.Namespace):
    setrepo = args.setrepo
    sync = args.sync
    diff = args.diff
    breakpoint()
    if setrepo is not None: 
        is_setrepo_valid = validate_repo(setrepo)
        if is_setrepo_valid:
            utils.set_repo(setrepo)
            utils.clone(setrepo)
        else:
            print("Repo url is not valid. Check for access rights and typos")
    if sync is not None:
        ...
    if diff is not None:
       utils.diff() 

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

    # Checks if the url points to a public git repo
    if match is not None:
        return exists(repo_url)
    else:
        return False



def exists(url: str):
    remote_refs = {}
    g = git.cmd.Git()
    try:
        refs = g.ls_remote(url).split('\n')
        for ref in refs:
            hash_ref_list = ref.split('\t')
            remote_refs[hash_ref_list[1]] = hash_ref_list[0]
        return remote_refs != {}
    except (git.exc.GitCommandError):
        print("Cannot access repo pointed to by url or repo may not exist...")



def touch(path: str):
    with open(path, 'a'):
        os.utime(path, None)

       



if __name__ == '__main__':
    main()
