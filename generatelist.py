import os
import re
from tkinter import Tcl


#work = "F:\github_project\LeetCodePractice\"

work = "/mnt/c/Users/zhang/LeetCodePractice/"
## read problem names
p = os.listdir(work + "problems")
pnew = [i.replace('.py','') for i in p]
pnew = Tcl().call('lsort', '-dict', pnew)

## write to list
with open(work+"list", 'w') as filehandle:
    for listitem in pnew:
        filehandle.write('%s\n' % listitem)
        

## parse readme markdown content
al = []
f = open(work +"list", "r")
lines = f.readlines()
for line in lines:
    al.append(line)
f.close()

header = """
<p align="center"><a href="https://www.leetcode.com"><img src="https://github.com/qianzhangut/LeetCodePractice/blob/master/leetcode.png" ></a></p>

# Solutions to Leetcode Challenges

This repository contains my solutions to LeetCode practice problems.

## Algorithms

| ID  	| Challenge   | Solution |
| :------| -------------------------------------------------------------------------------------- | ----------------------|
"""
with open(work+"README.md", 'w') as l:
    l.write(header)
    for i in range(len(al)):
        temp = re.findall(r"[\w+\ +\-*]+", al[i])
        leet = temp[1].lower().split()
        leet = '-'.join(leet)
        git_id = al[i].split()
        git_id = '%20'.join(git_id) + '.py'
        l.write(
            '|{0}|[{1}](https://www.leetcode.com/problems/{2}/) | [Solution](https://github.com/qianzhangut/LeetCodePractice/blob/master/problems/{3}) |'
            .format(temp[0], temp[1], leet, git_id)+'\n')