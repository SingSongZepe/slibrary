
import json

from object.slibrary import Slibrary
from value.strings import *

def read(self) -> Slibrary:
    with open(slibrary_file, 'r') as pf:
        json_dict = json.loads(pf.read())
        try:
            return Slibrary(**json_dict)
        except (TypeError, ValueError) as e:
            self.le('error while parsing json data file, may be it is corrupted')
            self.ln('now attempting to load default data file')

            return None

