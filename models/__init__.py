#!/usr/bin/python3
"""package construtor"""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
