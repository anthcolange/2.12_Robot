import json

class Trie:

    def __init__(self):
        self.frequency, self.children = 0, {}

    def insert(self, word, frequency=None):
        if not word: return
        t = self.children.setdefault(word[0], Trie())
        if not word[1:]: t.frequency = frequency or t.frequency + 1
        else: t.insert(word[1:], frequency)

    def find(self, prefix):
        if not prefix:
            return self
        elif prefix[0] in self.children:
            return self.children[prefix[0]].find(prefix[1:])

    def __contains__(self, word):
        f = self.find(word)
        return False if not f else bool(f.frequency)

    def __iter__(self):
        def generate_strings(trie):
            for (k, v) in trie.children.items():
                yield k
                yield from (k + x for x in generate_strings(v))
        for s in generate_strings(self):
            f = self.find(s)
            if f and f.frequency: yield [s, f.frequency]
        if self.frequency: yield ["", self.frequency]

    def __str__(self):
        return str(
            {k: (v.frequency, str(v)) for (k, v) in self.children.items()}
        ).replace("\\", "")
        
    def autocomplete(self, prefix, N):
        f = self.find(prefix)
        if not f: return []

        l = [(prefix + s, freq) for s, freq in f]
        l.sort(key=lambda x: x[1], reverse=True)
        return [x[0] for x in l[:N]]

    def autocorrect(self, prefix, N):
        """
        Prefix is a string to be corrected.
        N is the maximum number of suggestions to return.
        """
        def valid_edits():
            letters, length = "abcdefghijklmnopqrstuvwxyz".upper(), len(prefix)
            yield from (
                #add letter
                prefix[:i] + l + prefix[i:] for i in range(length+1)
                                            for l in letters
            )
            yield from (
                #delete letter
                prefix[:i] + prefix[i+1:] for i in range(length)
            )
            yield from (
                #replace letter
                prefix[:i] + l + prefix[i+1:] for i in range(length)
                                              for l in letters
            )
            yield from (
                #swap letters
                prefix[:i]+prefix[j]+prefix[i+1:j]+prefix[i]+prefix[j+1:]
                for i in range(length) for j in range(i+1, length)
            )

        edits = []
        for e in valid_edits():
            f = self.find(e)
            if f and f.frequency: edits.append((e, f.frequency))
        edits.sort(key=lambda x: x[1])

        #Ensure no duplicates by using set.
        l = set(self.autocomplete(prefix, N))
        while len(l) < N and edits: l.add(edits.pop()[0])
        return list(l)
        
        
## Make word trie
with open("words.json") as f:
    WORDS = json.load(f)

TRIE = Trie()
for w in set(WORDS):
    TRIE.insert(w.upper(), WORDS.count(w))


if __name__ == '__main__':
    print(TRIE.autocorrect("roobot".upper(), 7))
    print(TRIE.autocorrect("opn".upper(), 7))
