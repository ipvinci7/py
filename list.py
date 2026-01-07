names = ["vinci","elisha"]

def printname(arrayexamples):
    for x in names:
     print(x.upper())

def addname(name,namee):
    namee.append(name)

def putpos(arr,pos,name):
   arr.insert(pos,name)

putpos(names,7,"kuti")
#addname('kuti',names)
print(len(names))
printname(names)

    