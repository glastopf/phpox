# Copyright (C) 2012  Lukas Rist
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from random import choice
from datetime import datetime
import time


# TODO replace random string with actual content
# Linux shanwu-pc 3.0.0-12-generic #20-Ubuntu SMP Fri Oct 7 14:50:42 UTC 2011 i686 athlon i386 GNU/Linux
# linux hostname number  version choice name      date                       kernel            operating
#       [  0   ] [ 1  ]  [    2       ] [ 3 ] SMP [ 4 ]                      [  5  ]           [   6   ]


hosts = ["Linux", "Server", "WebServer", "FTP", "SMTP", "POP3", "Unix"]
version_numbers = [
    "3.0.0-14",
    "2.6.24-29",
    "2.6.32-41",
    "2.6.35-30",
    "2.6.38-7",
    "3.1.0-2",
]
str1 = ["#41", "#42", "#43", "#44", "#45", "#46", "#47", "#48", "#49"]
version_name = [
    "Fedora",
    "Redhat",
    "CentOs",
    "FreeBSD",
    "Mandriva",
    "Debian",
    "Gentoo",
    "SUSE",
    "Ubuntu",
]
# print time.tzname
time_zone = choice(time.tzname)
date = datetime.now().strftime("%a %b %d %H:%M:%S {0} %Y".format(time_zone))
kernel_version = ["i386", "i686"]
operating_system = ["GNU/Linux", "GNU/Unix"]


def call():
    hostname = choice(hosts)
    number = choice(version_numbers)
    version_choice = choice(str1)
    name = choice(version_name)
    kernel = choice(kernel_version)
    operating = choice(operating_system)
    # if name = ubuntu, we add '-generic' right after version number
    if "Ubuntu" in name:
        number = number + "-generic"
    ret = """
    \treturn 'Linux {0} {1} {2}-{3} SMP {4} {5} {6}';
    """.format(
        hostname, number, version_choice, name, date, kernel, operating
    )
    return ret
