import os
path=r'../picture'
fns=[os.path.join(root,fn) for root,dirs,files in os.walk(path) for fn in files]
for f in fns:
    print(f)
print(len(fns))
PERSONS = 
