from commands import (
    init,
    add,
    hash_file,
    cat_file
)

def register_commands(subparser):
    init.add_parser(subparser)
    cat_file.add_parser(subparser)
    hash_file.add_parser(subparser)
    add.add_parser(subparser)
