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


def clean_here(number=0):
    """function to clean tar achieve files in this computer"""
    line = local('ls -1t versions', capture=True)
    if not line:
        return
    line = line.split('\n')
    n = int(number)
    if n == 0:
        n = 1
    if n >= len(line):
        return
    print(len(line[n:]))
    for i in line[n:]:
        local('rm versions/' + i)


def clean_there(number=0):
    """function to clean tar achieve files in remote computer"""
    line = run('ls -1t /data/web_static/releases')
    if not line:
        return
    line = line.split('\r\n')
    print(line)
    n = int(number)
    if n == 0:
        n = 1
    if n < 2:
        n = 1
    if n >= len(line):
        return
    print(len(line[n:]))
    for i in line[n:]:
        if i == 'test':
            continue
        run('rm -rf /data/web_static/releases/' + i)


def do_clean(number=0):
    """clean function to call helper function to do the work"""
    clean_here(number)
    clean_there(number)
