from core import autocomplete


class Prefixy:
    def __init__(self):
        pass

    def preCompiler(self, newlist):
        t = autocomplete.Trie()
        t.formTrie(newlist)
        return t

    def showSuggestions(self, word, trie):
        computed = trie.printSuggested(word)
        return computed
