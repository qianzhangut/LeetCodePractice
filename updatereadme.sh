#!/bin/sh

REPO_DIR=`pwd`
cd ${REPO_DIR}
python3 generatelist.py


message1="update Readme file on $(date)"
message2="update list file on $(date)"
GIT=`which git`

${GIT} add list
${GIT} commit -m "$message2"
${GIT} add README.md
${GIT} commit -m "$message1"

gitPush=$(${GIT} push origin master)
echo "$gitPush"
