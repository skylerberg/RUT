from collections import MutableMapping


class HashTrie(MutableMapping):

    def __init__(self, *args, **kwargs):
        super(HashTrie, self).__init__()
        self.dictionary = {}
        self.dictionary.update(*args, **kwargs)

    def __getitem__(self, key):
        return self.dictionary[key]

    def __setitem__(self, key, value):
        self.dictionary[key] = value

    def __iter__(self):
        return iter(self.dictionary)

    def __delitem__(self, key):
        del self.dictionary[key]

    def __len__(self):
        return len(self.dictionary)

    def prefix_match(self, prefix):
        for key in self.dictionary:
            if key.startswith(prefix):
                return True
        return False
