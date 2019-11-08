#!/usr/bin/python3
"""the script import fabric library to run the function
"""
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """the function creates "tgz" archive to pack all the web_static files
    """
    if not os.path.exists('./versions'):
        os.makedirs('./versions')
    _tgz = 'versions/web_static_{}.tgz'\
           .format(datetime.strftime(datetime.now(), "%Y%m%d%I%M%S"))
    _tar = 'tar -czvf {} web_static'.format(_tgz)
    _run = local(_tar)
    if _run.failed:
        return None
    return _tgz
