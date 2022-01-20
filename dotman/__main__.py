import sys
import argparse
import os


def main():

    username = os.getlogin()
    if os.path.exists("/home/" + username + "/.dotman") == False:
        print("~/.dotman folder does not exist setting up now...")
        firsttime_setup(username)


    argument_parser = create_parser()
    
    args = argument_parser.parse_args()
    
    process_args(args)


def create_parser():
    parser = argparse.ArgumentParser(description="Sync your dotfiles with one seamless CLI tool")
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("sync", help="sync your dotfiles with your current repo", nargs='?')
    parser.add_argument("diff", help="Find the diff between local and remote versions of all dotfiles")
    parser.add_argument("-s", "--set-repo=", help="Set the git repo of your dotfiles")
    group.add_argument("-v", "--verbose", help="increase the verbosity of your output", action="count",
                        default=0 )
    group.add_argument("-q", "--quiet", action="store_true")

    return parser

def process_args(args: argparse.Namespace):
    ...
   


def firsttime_setup(username: str):

    os.mkdir("/home/" + username + "/.dotman")
    touch("/home/" + username + "/.dotman/config.conf")

    



def touch(path: str):
    with open(path, 'a'):
        os.utime(path, None)



if __name__ == '__main__':
    main()
