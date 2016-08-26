from collections import MutableMapping


class HashTrie(MutableMapping):

    def __init__(self, *args, **kwargs):
        super(HashTrie, self).__init__()
        self.dictionary = {}
        self.dictionary.update(*args, **kwargs)

        self.children = {}
        self.is_terminal = False
        self.value = None
        self.length = len(kwargs)

    def __getitem__(self, key):
        if key == "":
            if not self.is_terminal:
                raise KeyError('key not in found in Trie.')
            return self.value
        head, tail = key[0], key[1:]
        if head not in self.children:
            raise KeyError('key not in found in Trie.')
        return self.children[tail]

        return self.dictionary[key]

    def __setitem__(self, key, value):
        self.dictionary[key] = value

        if key not in self:
            self.length += 1
        if key == "":
            self.is_terminal = True
            self.value = value
            return
        head, tail = key[0], key[1:]
        self.children[head] = self.children.get(head, HashTrie())
        self.children[head][tail] = value

    def __iter__(self):
        return iter(self.dictionary)

    def __delitem__(self, key):
        del self.dictionary[key]

    def __len__(self):
        return self.length

    def prefix_match(self, prefix):
        for key in self.dictionary:
            if key.startswith(prefix):
                return True
        return False
