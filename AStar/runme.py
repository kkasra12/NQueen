try:
    from node import node
except ModuleNotFoundError:
    print("Please install numpy using\n\t$ pip install numpy --user")
    input("Press enter to exit...")
    exit()
except Exception as e:
    print("Ooops!! There is error:\n",e)
    input("Press enter to exit...")
    exit()
TABLE_SIZE=6
childs=[node(TABLE_SIZE)]
allChildSet=set()
allChildSet.add(childs[0])
while not childs[0].isGoal():
    newNodes=childs.pop(0).expand(discoveredNodes=allChildSet)
    for i in newNodes:
        allChildSet.add(i)
    childs+=newNodes
    childs.sort()
print(childs[0])
input("Press enter to exit...")
