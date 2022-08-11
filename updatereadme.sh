#!/bin/sh

REPO_DIR=`pwd`
cd ${REPO_DIR}
python3 generatelist.py


message="update Readme file on $(date)"
GIT=`which git`


${GIT} add list README.md
${GIT} commit -m "$message"

gitPush=$(${GIT} push origin master)
echo "$gitPush"
