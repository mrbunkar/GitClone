import os
import configparser

class GitRepository(object):
    """A git repository"""

    worktree = None
    gitdir = None
    config = None

    def __init__(self, path, force = False):
        self.worktree = path
        self.gitdir = os.path.join(path, ".git")

        if not (force or os.path.isdir(path)):
            raise Exception(f"{path} is not a directory")
        
        self.config = configparser.ConfigParser()
        cf = repo_path(self, "config")

        if cf and os.path.exists(cf):
            self.config.read(cf)
        elif not force:
            raise Exception("Config file missing")
        
        if not force:

            version = int(self.config.get("core", "repositoryformatversion"))
            if version != 0:
                raise Exception("Unsupported repository version %s" % version)
            

def repo_path(repo: GitRepository, *path):
    return os.path.join(repo.gitdir, *path)

def repo_file(repo: GitRepository, *path, mkdir = False):

    if repo_dir(repo, *path[:-1], mkdir = mkdir):
        return repo_path(repo, *path)
    
def repo_dir(repo: GitRepository, *path, mkdir = False):

    path = repo_path(repo, *path)
    if os.path.exists(path):
        if os.path.isdir(path):
            return path
        else:
            raise Exception("Not a directtory")
        
    if mkdir:
        os.makedirs(path)
        return path
    else:
        return None
    
def repo_create(path):
    repo = GitRepository(path, True)

    if os.path.exists(repo.worktree):
        if not os.path.isdir(repo.worktree):
            raise Exception(f"{repo.worktree} not a directory")
    
    if os.path.exists(repo.gitdir) and os.listdir(repo.gitdir):
        raise Exception(f"{repo.gitdir} not a empty directory")
    
    assert repo_dir(repo, "branches",mkdir = True)
    assert repo_dir(repo, "objects", mkdir=True)
    assert repo_dir(repo, "refs", "tags", mkdir=True)
    assert repo_dir(repo, "refs", "heads", mkdir=True)

    with open(repo_file(repo, "description"), "w") as file:
        file.write("Edit this file for repo description \n")

    with open(repo_file(repo, "refs/heads/master"), "w") as file:
        file.write("ref: refs/heads/master \n")

    with open(repo_file(repo, "config"), "w") as file:
        config = default_config()
        config.write(file)
        
    return repo

def default_config():
    """Default configuration"""

    config = configparser.ConfigParser()

    config.add_section("core")
    config.set("core", "repositoryformatversion","0")
    config.set("core", "filemode", "false")
    config.set("core", "bare", "false")

    return config

def repo_find(path = ".", required = False):

    path = os.path.realpath(path)

    if os.path.isdir(os.path.join(path, ".git")):
        return GitRepository(path)
    
    parent = os.path.realpath(os.path.join(path,".."))

    if parent == path:
        if required:
            raise Exception("No git repository found")
        else:
            return None
    
    return repo_find(path, required=required)