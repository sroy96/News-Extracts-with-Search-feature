from services import scrap_function
import time
import sys
from config import configs


if __name__ == '__main__':
    load = scrap_function.ScrapFunction(configs.url)
    repo = load.page_loader()
    content_create = {}
    try:
        content_create = load.show_results(repo)
    except ModuleNotFoundError:
        sys.exit("Crashing....")
    content_list = []
    for i in content_create:
        content_list.append(i.upper())
    content_trie = load.preCompiler(list(content_create))
    while True:
        try:
            search_key = input("We are ready!! Shoot__: ")
        except KeyboardInterrupt:
            pass
        print("We are fetching data for you....Please wait___")
        time.sleep(1)
        index = {}
        try:
            index = load.showSuggestions(search_key.upper(), content_trie)
        except Exception:
            print("No data Found...")
            pass
        try:
            ack = int(input("choose the word: "))
            load.bomb_cluster(index[ack], content_create, repo)
        except Exception:
            print("Ooops we don't have anything for you... ")
