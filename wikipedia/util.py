import uuid
import hashlib
import itertools

# Maximum number of items to return per chunk in `grouper`
MAX_CHUNK_SIZE = 50000

def grouper(iterable, max_chunk_size=MAX_CHUNK_SIZE):
    """Via http://stackoverflow.com/a/8991553"""
    it = iter(iterable)
    while True:
       chunk = list(itertools.islice(it, MAX_CHUNK_SIZE))
       if not chunk:
           return
       yield chunk

def article_uuid(name):
    h = hashlib.blake2b(name.encode("utf8"), digest_size=16)
    return uuid.UUID(bytes=h.digest())
