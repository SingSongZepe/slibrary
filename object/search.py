from dataclasses import dataclass
from datetime import datetime

from object.time import Time
from utils.common.encode_sha1 import encode_sha1

@dataclass
class Search:
    q: str # key word
    time: Time
    search_type: str
    year_from: str
    year_to: str
    languages: [str]
    extensions: [str]
    exact_matching: str # '1' '0'
    book_nums: str # '10' '15'
    
    def __post_init__(self):
        self.sha1_id = encode_sha1(datetime.now().__str__())

    def exact_matching_bool(self):
        return False if self.exact_matching == '0' else True
        