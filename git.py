import argparse
import sys
from register import register_commands

argparser = argparse.ArgumentParser()
sub_argparser = argparser.add_subparsers(dest = "command")
sub_argparser.required = True

def main(args = sys.argv[1:]):
    register_commands(sub_argparser)

    args = argparser.parse_args(args)
    if hasattr(args, 'func'):
        args.func(args)
    else:
        argparser.print_help()