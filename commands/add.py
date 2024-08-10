def add_parser(subparser):
    parser = subparser.add_parser(
        'add',
        help = "Add the files for the commit"
    )

    parser.add_argument(
        "path",
        metavar = "path",
        nargs = "+",
        help = "Files to add to the staging area"
    )

    parser.set_defaults(
        func = add_cmd
    )

def add_cmd(args):
    files = get_files(args.path)


def get_files(path):

    if path == ".":
        pass