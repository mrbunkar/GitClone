from gitlib.repo import GitRepository, repo_file
import os
import zlib
import hashlib
from util import key_value_parase, key_value_serialize
from collections import OrderedDict

class GitObject(object):

    def __init__(self, data = None) -> None:
        if data == None:
            self.init()
        else:
            self.deserialize(data)

    def deserialize(self, data):
        raise NotImplemented
    
    def serialize(self, repo):
        raise NotImplemented
    
    def init(self):
        pass

class GitBlob(GitObject):
    fmt = b"blob"

    def deserialize(self, data):
        self.biodata = data

    def serialize(self):
        return self.biodata
    
class GitCommit(GitObject):
    fmt = b"commit"

    def deserialize(self, data):
        print("Deserialize")
        self.key_value = data

    def serialize(self):
        return key_value_serialize(self.key_value)
    
    def inti(self):
        self.key_value = OrderedDict()

def objet_write(obj: GitObject, repo = None):
    object = obj.serialize()

    raw_data = obj.fmt + b' ' + str(len(object)).encode() + b'\x00' + object
    sha_hash = hashlib.sha1(raw_data).hexdigest()

    if repo:
        path = repo_file(repo, "object", sha_hash[:2],sha_hash[2:], mkdir= True)

        if not os.path.exists(path):
            with open(path, "wb") as file:
                file.write(zlib.compress(raw_data))

    return sha_hash

def object_read(repo, sha_hash) -> GitObject:
    path = repo_file(repo, "object", sha_hash[:2], sha_hash[2:])

    if not os.path.exists(path):
        return None
    
    with open(path, "rb") as file:
        raw_data = zlib.decompress(file.read())
        ind = raw_data.find(b" ")
        spc = raw_data.find(b'\x00', ind)

        file_type = raw_data[:ind]
        size = int(raw_data[ind:spc].decode('ascii'))

        if size != len(raw_data) - spc - 1:
            raise Exception("Malfromed file size")
        match file_type:
            case b"commit": c = GitCommit
            case b"blob": c = GitBlob
            case _: raise Exception(
                "Unkown type {0} for object {1}".format(
                    file_type, sha_hash
                )
            )
        return c(raw_data[spc+1:])

def object_find(repo, name, fmt = None, follow = None):
    return name

def object_hash(file, type, repo = None):
    """
    Hash the object and write to the repor if provided
    """

    data = file.read()

    match type:
        case b"commit": obj = GitCommit
        case b"blob": obj = GitBlob
        case _: raise Exception(f"Unknown object type: {type}")
   
    return objet_write(obj(data), repo)

