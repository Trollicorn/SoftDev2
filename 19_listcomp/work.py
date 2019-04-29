#team arzeal mohammed uddin and the odor e peter
#union
u=lambda l,s:[i for i in s if i not in l]+l
print(u([1,2,3],[3,4,5]))
#intersection
i=lambda l,s:[i for i in s if i in l]
print(i([1,2,3],[3,4,5]))
#set_difference
d=lambda l,s:[i for i in l if i not in s]
print(d([1,2,3],[3,4,5]))
#symmetry
sd=lambda l,s:[i for i in s if i not in l]+[i for i in l if i not in s]
print(sd([1,2,3],[3,4,5]))
#cartesian product
cp=lambda l,s:[(i,j)for i in l for j in s]
print(cp([1,2,3],[3,4,5]))
#this makes a matrix okok
m=lambda l,s:[[i*j for i in l]for j in s]
print(m([1,2,3],[3,4,5]))
# dot prod uctr
dp=lambda l,s:sum(l[i]*s[i] for i in range(len(l)))if len(l)==len(s)else None
print(dp([1,2,3],[3,4,5]))
# normalzieds a set
nrmlz=lambda l:[i/(sum(j*j for j in l))**0.5 for i in l]
print(nrmlz([3,4]))
