from interfaces import prefixy_structure


class Trie:
    def __init__(self):
        self.root = prefixy_structure.TrieNode()
        self.word_list = []

    def formTrie(self, keys):
        ##form trie with given word list
        for key in keys:
            self.insert(key)

    def insert(self, key):
        node = self.root

        for i in list(key):
            if not node.children.get(i):
                node.children[i] = prefixy_structure.TrieNode()
            node = node.children[i]
        node.last = True

    def search(self, key):
        node = self.root
        found = True

        for i in list(key):
            if not node.children.get(i):
                found = False
                break
            node = node.children[i]
        return node and node.last and found

    def suggestions(self, node, word):
        # recursively find the word in trie and show all suggested words
        if node.last:
            self.word_list.append(word)
        for a, n in node.children.items():
            self.suggestions(n, word + a)

    def printSuggested(self, key):
        # Return words with common prefix
        node = self.root
        not_found = False
        word_builder = ''
        for i in list(key):
            if not node.children.get(i):
                not_found = True
                break
            word_builder += i
            node = node.children[i]

        if not_found:
            return 0
        elif node.last and not node.children:
            return -1
        self.suggestions(node, word_builder)
        selector = {}
        i = 1
        for s in self.word_list:
            print(i, " : ", s)
            selector[i] = s
            i += 1
        return selector
