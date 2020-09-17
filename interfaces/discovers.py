from utils import validator


class Discoverer:

    def __init__(self, keyword, repo):
        self.keyword = keyword
        self.repo = repo

    def show_results(self, repo: dict) -> dict:
        word_dict = {}
        validate = validator.Validate()
        for lines in repo:
            newlist = validate.isnoun(lines)
            for i in newlist:
                word_dict.setdefault(i.upper(), []).append(lines)
        return word_dict

    def bomb_cluster(self, searchkey: str, storage: dict, container: dict):
        topics_list = storage[searchkey]
        for itr in topics_list:
            print(itr, " : ", container[itr])
            print("\n")
