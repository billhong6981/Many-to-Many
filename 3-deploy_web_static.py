#!/usr/bin/python3
"""the script import fabric library to run the function
"""
from fabric.api import *
from datetime import datetime
import os


env.hosts = ["35.231.16.81", "35.243.203.94"]


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


def do_deploy(archive_path):
    """Deploys the web contents"""
    if not os.path.exists(archive_path):
        return False
    _ar = archive_path.split('/')[1]
    _name = _ar.split('.')[0]
    r = put(archive_path, '/tmp/{}'.format(_ar))
    if r.failed:
        return False
    r = run('mkdir -p /data/web_static/releases/{}'.format(_name))
    if r.failed:
        return False
    r = run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'
            .format(_ar, _name))
    if r.failed:
        return False
    r = run('rm /tmp/{}'.format(_ar))
    if r.failed:
        return False
    s = 'mv /data/web_static/releases/{0}/web_static/*'
    s += ' /data/web_static/releases/{0}/'
    r = run(s.format(_name))
    if r.failed:
        return False
    r = run('rm -rf /data/web_static/releases/{}/web_static'.format(_name))
    if r.failed:
        return False
    r = run('rm -rf /data/web_static/current')
    if r.failed:
        return False
    r = run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(_name))
    if r.failed:
        return False
    print('New version deployed!')
    return True


def deploy():
    """the function call the subfunction to deploy web contents"""
    _ar = do_pack()
    if _ar is None:
        return False
    _run = do_deploy(_ar)
    return _run
