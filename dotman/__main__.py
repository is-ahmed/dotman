import sys
import argparse
import os
import re
from typing import Optional
import json

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
    group.add_argument("-v", "--verbose", help="increase the verbosity of your output", action="count",
                        default=0 )
    group.add_argument("-q", "--quiet", action="store_true")

    return parser

def process_args(args: argparse.Namespace):
    verbosity = args.verbose
    setrepo = args.setrepo
    sync = args.sync
    diff = args.diff


    if setrepo and validate_url(setrepo):
        set_repo(setrepo)






def firsttime_setup(username: str):

    config_dir = "/home/" + username + "/.config/dotman"

    os.mkdir(config_dir)
    touch(config_dir + "/config.json")

    data = {
        "url": None,
    }

    with open(config_dir + "/config.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)



def set_repo(url: str):
    """

    Precondition:
        - The config file is created with the proper format

    """
    ...

    username = os.getlogin()
    config_path = "/home/" + username + "/.config/dotman/config.json"

    file = open(config_path, 'rw')

    json_data = json.load(file)

    json_data['url'] = url

    json.dump(json_data, file)

    file.close()




def validate_url(repo_url: str) -> Optional[bool]:

    match = re.match(r"((git|ssh|http(s)?)|(git@[\w\.]+))(:(//)?)([\w\.@\:/\-~]+)(\.git)(/)?", repo_url)

    return match is not None


def touch(path: str):
    with open(path, 'a'):
        os.utime(path, None)

       



if __name__ == '__main__':
    main()
