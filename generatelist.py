import os
import re

p = os.listdir("F:\github_project\LeetCodePractice\problems")
pnew = [i.replace('.py','') for i in p]
with open("F:\github_project\LeetCodePractice\list", 'w') as filehandle:
    for listitem in pnew:
        filehandle.write('%s\n' % listitem)
        

al = []
f = open("F:\github_project\LeetCodePractice\list", "r")
lines = f.readlines()
for line in lines:
    al.append(line)
f.close()
for i in range(len(al)):
    temp = re.findall(r"[\w+\ +\-*]+", al[i])
    leet = temp[1].lower().split()
    leet = '-'.join(leet)
    git_id = al[i].split()
    git_id = '%20'.join(git_id) + '.py'
    print(
        '|{0}|[{1}](https://www.leetcode.com/problems/{2}/) | [Solution](https://github.com/qianzhangut/LeetCodePractice/blob/master/problems/{3}) |'
        .format(temp[0], temp[1], leet, git_id))