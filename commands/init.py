from gitlib.repo import repo_create

def add_parser(subparser):
    parser= subparser.add_parser("init", help = "Will create the new repository")
    parser.add_argument(
        'path',
        metavar = "directory",
        nargs = "?",
        default = ".",
        help = "Where to create the repository"
    )
    parser.set_defaults(func = cmd_init)

def cmd_init(args):
    print(f"Creating git repository at {args.path}")
    repo_create(args.path)