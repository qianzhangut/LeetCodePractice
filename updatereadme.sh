#!/bin/sh

REPO_DIR=/mnt/c/Users/zhang/LeetCodePractice
cd ${REPO_DIR}
python3 generatelist.py


message="update Readme file on $(date)"
GIT=`which git`


${GIT} add list Readme
${GIT} commit -m "$message"

gitPush=$(${GIT} push origin master)
echo "$gitPush"
