from objects import GitObject
from gitlib.util import key_value_parase, key_value_serialize
from collections import OrderedDict

class GitCommit(GitObject):
    fmt = b"commit"

    def deserialize(self, data):
        print("Deserialize")
        self.key_value = data

    def serialize(self):
        return key_value_serialize(self.key_value)
    
    def inti(self):
        self.key_value = OrderedDict()



