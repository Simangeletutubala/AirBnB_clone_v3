#!/usr/bin/python3
"""Creates a unique FileStorage instance for the application"""

from models.engine.file_storage import FileStorage
from os import getenv

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')
if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
