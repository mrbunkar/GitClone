from gitlib.objects.objects import object_read, object_find
from gitlib.repo import repo_find
import sys

def add_parser(subparser):
    parser = subparser.add_parser(
        "cat-file",
        help = "Provide content of a repository"
    )

    parser.add_argument(
        'type',
        metavar = 'type',
        choices = ['blob','commit','tag','tree'],
        help = "Specify the t=object type"
    )

    parser.add_argument(
        'object',
        metavar = 'Object',
        help = "Object to display"
    )

    parser.set_defaults(
        func = cat_file_cmd
    )

def cat_file_cmd(args):
    repo = repo_find()
    type = args.type.encode()
    object = args.object

    obj = object_read(repo, object_find(repo, object,type))
    sys.stdout.buffer.write(obj.serialize())
