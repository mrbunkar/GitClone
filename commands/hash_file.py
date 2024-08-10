from gitlib.repo import repo_find
from gitlib.objects import object_hash

def add_parser(subparser):
    parser = subparser.add_parser(
        "hash-file",
        help = "Compute object ID and optionally creates a blob from a file"
    )

    parser.add_argument(
        "-t",
        metavar="type",
        dest="type",
        choices=["blob", "commit", "tag", "tree"],
        default="blob",
        help="Specify the type"
    )
    parser.add_argument(
        "-w",
        dest="write",
        action="store_true",
        help="Actually write the object into the database"
    )
    parser.add_argument(
        "path",
        help="Read object from <file>"
    )
    parser.set_defaults(
        func = hash_file_cmd
    )

def hash_file_cmd(args):

    if args.write:
        repo = repo_find(required=True)
    else:
        repo = None

    with open(args.path, 'rb') as file:
        has = object_hash(file, args.type.encode(), repo)
        print(has)