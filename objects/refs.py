from gitlib.repo import repo_file
from collections import OrderedDict
import os

def create_ref(repo, sha, ref_name):
    """
    Creates reference with ref_name for the give objects SHA-1 hash value
    """
    with open(repo_file(repo, "refs/", ref_name), "w") as file:
        file.write(sha + "/")

def get_refs(repo, path = None):
    """
    Get all the referecne in the Ordered dict format
    """

    if not path:
        path = repo_file(repo, "refs")

    refs = OrderedDict()
    for ref in os.listdir(path):
        if os.path.isdir(path):
            refs[ref] = get_refs(repo, path)
        else:
            refs[ref] = resolve_refs(ref)

def resolve_refs(repo,ref):
    ref = repo_file(repo, ref)

    if not os.path.isfile(ref):
        return None
    
    with open(ref, "r") as f:
        data = f.read().strip()

    if data.startswith("ref: "):
        ref = data.split(" ")[-1]
        return resolve_refs(repo, ref)
    else:
        return data

def show_refs(refs, prefix = ""):
    for k, v in refs.items():
        if isinstance(v, dict):
            show_refs(v, prefix+k+"/")
        else:
            print(f"{prefix}{k}: {v}")
