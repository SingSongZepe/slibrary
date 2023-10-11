from dataclasses import dataclass

from object.search import Search

@dataclass
class History_Search:
    search: Search
    cover: str # pic url
    