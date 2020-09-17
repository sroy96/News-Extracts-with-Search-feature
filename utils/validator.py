import nltk
#nltk.download('all')


class Validate:

    def isnoun(self, topic: str) -> list:
        tokenized = nltk.word_tokenize(topic)
        nounlist = [word for (word, pos) in nltk.pos_tag(tokenized) if lambda pos: pos[:2] == 'NN']
        return nounlist
