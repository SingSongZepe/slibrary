# collect all data from self and construct a Slibrary object
import json

from object.slibrary import Slibrary
from value.strings import *


# ! now all data need to store
# self.current_type = home_  # for main toggle
# self.current_history_type = history_search_  # for history toggle
# self.verify = True
# self.dp = ''
# self.cookie_from = 0    # from which cookie to attempt to download a book 
# self.searches = []      # [object.history_search.History_Search]
# self.downloads = []     # [object.download.Download]
# self.recommend_cookie_idx = 0

def save(self):
    #
    slibrary = Slibrary(
        current_type=self.current_type,
        current_history_type=self.current_history_type,
        verify=self.verify,
        dp=self.dp,
        cookie_from=self.cookie_from,
        searches=self.searches,
        downloads=self.downloads,
        recommend_cookie_idx=self.recommend_cookie_idx,
    )
    with open(slibrary_file, 'w') as pf:
        try: # attempt to write file
            pf.write(json.dumps(slibrary.__dict__, indent=2))
            self.ln('')
        except PermissionError as pe:
            self.le('permission denied, maybe you haven\'t give the program permission')
            return
