# use json file to load the data
# but json is encrypted

from dataclasses import dataclass

from object.history_search import History_Search
from object.download import Download

@dataclass
class Slibrary:
    current_type: str # home, search  # main toggle idx
    current_history_type: str # search, book # second toggle idx
    verify: bool # True or False
    dp: str # download path, where to put downloaded books
    cookie_from: int # index that
    searches: [History_Search] # all history searches
    downloads: [Download]
    recommend_cookie_idx: int # recommend cookie index

    # may be there we can define a classmethod to get instance
    
    # Slibrary(**dict)