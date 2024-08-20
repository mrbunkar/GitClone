from gitlib.repo import repo_find
from gitlib.objects.refs import get_refs, show_refs

def add_parser(subparser):
    parser = subparser.add_parser(
        "show-refs",
        help = "Print all the references"
    )

    parser.set_defaults(
        func = refs_cmd
    )


def refs_cmd(args):
    repo = repo_find()
