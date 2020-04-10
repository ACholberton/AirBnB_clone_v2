#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""

from datetime import datetime
from fabric.api import local

def do_pack(self):
    """generates a .tgz archive from web_static"""
    local('mkdir -p versions')

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    path_storage = 'versions/web_static_{}.tgz'.format(format_time)

    r = local('tar cvfz {} web_static'.format(path_storage)

    if r.failed:
        return None
    else:
        return r
