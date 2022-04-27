'''
Q-2) Find the Town Judge (5 marks)
https://leetcode.com/problems/find-the-town-judge/
(Easy)
In a town, there are n people labelled from 1 to n. There is a rumor that one of
these people is secretly the town judge.
If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person
labelled a trusts the person labelled b.
If the town judge exists and can be identified, return the label of the town judge.
Otherwise, return -1.
Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
'''

n=3
trust = [[1,3],[2,3]]
dptf={}
dpj={}
for i in range(len(trust)):
    for j in range(len(trust[0])):
        if trust[i][j] not in dptf:
            if j==0:
                dptf[trust[i][j]]= False
            if j==1:
                dptf[trust[i][j]]= True
                dpj[trust[i][j]]=[]
            dpj[trust[i][j]].append([trust[i][j-1]])
        else:
            if j==0:
                dptf[trust[i][j]]=False
                

c=0
for key,value in dptf.items():
    if value==True:
        judge=key
        for key1,value1 in dpj.items():
            if key1!=key:
                if key in value1:
                    c+=1
if c==n-1:
    print(judge)
else:
    print(-1)