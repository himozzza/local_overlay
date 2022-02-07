#!/usr/bin/python

import os
import datetime

bash = os.system

os.chdir("/usr/local/portage/local_overlay/sys-auth/polkit")
now = datetime.datetime.today().strftime("%Y%m%d")
bash("wget https://www.freedesktop.org/software/polkit/releases/")
with open("index.html", "r") as htmlfile:
    polkit_html = htmlfile.readlines()
gitversion = str(polkit_html[-6].split('-')[1].split(".")[0]) + "." + str(polkit_html[-6].split('-')[1].split(".")[1])
bash("emerge -s sys-auth/polkit | grep ' Latest version available:' > polkit_installed")
with open("polkit_installed") as file:
    polkit_file = file.readlines()
last_version = str(polkit_file[0].split(" ")[-1].split("\n")[-2])

if gitversion > last_version:
    bash("cp polkit-{}.ebuild polkit-{}-p{}.ebuild".format(last_version, gitversion, now))
    bash("sudo ebuild polkit-{}-p{}.ebuild digest".format(gitversion, now))
else:
    print("No updates available")
bash("rm index* polkit_installed")
