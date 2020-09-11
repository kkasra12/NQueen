import numpy as np
from itertools import combinations
class node:
    def __init__(self,size,g=0,ones=[]):
        self.board=np.zeros((size,size))
        self.size=size
        self.freeCells=None
        self.g=g
        # root nodes father is none
        # this is the point where adam was created in the heaven,
        # this show how computers,known as logical way of thought, can describe god
        # which means there is no need to use logic to believe god
        # NOTE: if u accept the mentioned thought u r a super idiot guy go kill urself for humanity sake
        try:
            for i,j in ones:
                self.board[i,j]=1
        except (TypeError, ValueError, IndexError):
            raise ValueError("ones list is not correct")
    def reservedCells(size,row,col):
        reservedCellsMat=np.zeros((size,size),np.int8)
        reservedCellsMat[:,col]=1
        reservedCellsMat[row,:]=1
        for i in [-1,1]:
            for j in [-1,1]:
                m,n=row,col
                while 0<=m<size and 0<=n<size:
                    reservedCellsMat[m,n]=1
                    m+=i
                    n+=j
        reservedCellsMat[row,col]=0
        return reservedCellsMat
    def isCorrect(self):
        assert set(self.board.ravel()).issubset({0,1}),self
        # for i,j in np.array(self.board.nonzero()).T:
        #     assert self.board[i,j]==1,f"board[{i},{j}]={self.board[i,j]},\n{self.board}"
        #     t=self.board+node.reservedCells(self.size,i,j)
        #     if set(t.ravel())!={0,1}:
        #         return False
        for (i_row,i_col),(j_row,j_col) in combinations(np.array(self.board.nonzero()).T.tolist(),2):
            if abs(i_row-j_row)==abs(i_col-j_col):
                return false
        return True
    def isGoal(self):
        return self.isCorrect() and \
               len(self.board[self.board==1])==self.size
    def findFreeCells(self):
        if isinstance(self.freeCells,np.ndarray):
            return self.freeCells
        freeCells=self.board.copy()
        for i,j in np.array(self.board.nonzero()).T:
            assert self.board[i,j]==1,f"board[{i},{j}]={self.board[i,j]},\n{self.board}"
            freeCells+=node.reservedCells(self.size,i,j)
        freeCells[freeCells!=0]=1
        self.freeCells=np.logical_not(freeCells)
        return self.freeCells
    def heuristic(self):
        return self.size**2-len(self.findFreeCells().nonzero()[0])
    def copy(self):
        newCopy=node(self.size,g=self.g)
        newCopy.board=self.board.copy()
        return newCopy
    def expand(self,discoveredNodes=set()):
        self.childs=[]
        for i,j in np.array(self.findFreeCells().nonzero()).T:
            t=self.copy()
            t.board[i,j]=1
            if t in discoveredNodes:
                continue
            t.g+=1
            t.father=self
            self.childs.append(t)
        return self.childs
    def __str__(self):
        return f"\n{self.board}\n  g(n){self.g}\n"
    def __repr__(self):
        return str(self)
    def __lt__(self,other):
        return self.g+self.heuristic()<other.g+other.heuristic()
    def __eq__(self,other):
        return (self.board==other.board).all()
    def __hash__(self):
        return hash(self.board.astype(np.uint8).tostring())
if __name__ == '__main__':
    # print(node.reservedCells(9,3,4))
    # test node.isCorrect
    myNode=node(9)
    # myNode.board=np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 1, 0, 0, 1, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 1, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.int8)
    # print(myNode.isCorrect())
    # myNode.board=np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 1, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 1, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.int8)
    # print(myNode.isCorrect())
    # myNode.board=np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 1, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 1, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.int8)
    # print(myNode.isCorrect())
    # myNode.board=np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 1, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 1, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.int8)
    # print(myNode.isCorrect())
    # test node.findFreeCells
    # print(myNode.findFreeCells()+myNode.board,'\n\n')
    # print(np.logical_not(myNode.findFreeCells())+0)
    # test expand
    myNode.board=np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 1, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 0],
                           [0, 0, 0, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.int8)

    myNode.expand()
    print(myNode.childs)
