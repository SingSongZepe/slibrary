# this function is use to hash a string to get a identification of a Search object
# or in the future will be use in different context

import hashlib

def encode_sha1(txt: str) -> str:
    hasher = hashlib.sha1()
    hasher.update(txt.encode('utf-8'))
    return hasher.hexdigest()


