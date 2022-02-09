#!/usr/bin/python

import os
import datetime

bash = os.system

os.chdir("/usr/local/portage/local_overlay/sys-auth/polkit")
now = datetime.datetime.today().strftime("%Y%m%d")
bash("wget https://www.freedesktop.org/software/polkit/releases/")
with open("index.html", "r") as htmlfile:
    polkit_html = htmlfile.readlines()
gitversion = str(polkit_html[-6].replace('polkit-', '~').split("~")[1].replace('.tar.gz">', ''))
bash("eix sys-auth/polkit | grep 'Available versions:' > polkit_latest")
with open("polkit_latest") as file:
    polkit_file = file.readlines()
last_version = str(polkit_file[0].replace("-", "~").split("~")[-2])

if gitversion > last_version:
    bash("cp polkit-{}.ebuild polkit-{}-r9.ebuild".format(last_version, gitversion))
    bash("sudo ebuild polkit-{}-r9.ebuild digest".format(gitversion))
    print("\n")
    print("ebuild update")
else:
    print("No updates available")

bash("rm index* polkit_latest")
