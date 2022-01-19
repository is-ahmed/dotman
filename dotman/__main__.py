import sys
import argparse
import os


def main():

    username = os.getlogin()
    if os.path.exists("/home/" + username + "/.dotman") == False:
        print("~/.dotman folder does not exist setting up now...")
        first_setup(username)
    else:
        print("does exist")


    parser = argparse.ArgumentParser(description="Sync your dotfiles with one monolithic CLI tool")
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("x", help="the base", type=int)
    parser.add_argument("y", help="the exponent", type=int)
    group.add_argument("-v", "--verbose", help="increase the verbosity of your output", action="count",
                        default=0 )
    group.add_argument("-q", "--quiet", action="store_true")
    args = parser.parse_args()
    answer = args.x ** args.y
   
    if args.quiet:
        print(answer)
    elif args.verbose:
        print(f"{args.x} to the power of {args.y} equals {answer}")
    else:
        print(f"{args.x}^{args.y} == {answer} ")


def first_setup(username: str):
    ...

    os.mkdir("/home/" + username + "/.dotman")
    



if __name__ == '__main__':
    main()
