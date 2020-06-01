from copy import deepcopy
class matrice(object):
    def __init__(self, order):
        assert type(order) == tuple
        self.order = order
        self.matrix = []
        for i in range(order[0]):
            self.matrix.append([None for i in range(order[1])])
        
        self.rows = self.matrix
        self.columns = [[] for i in range(order[1])]
        for row in self.matrix:
            for index in range(len(row)):
                self.columns[index].append(row[index])

    def addelement(self, element, row, column):
        self.matrix[row][column] = element
        self.columns[column][row] = element
        return self.matrix


    def getelement(self, row, column):
        return self.matrix[row][column]

    def creatematrice(self, listobject):
        rows = len(listobject)
        columns = len(listobject[0])
        newmatrice = matrice((rows,columns))
        for row in range(rows):
            for column in range(columns):
                newmatrice.addelement(listobject[row][column], row, column)
        newmatrice.rows = listobject
        for firstindex in range(len(newmatrice.columns)):
            for secondindex in range(len(newmatrice.columns[firstindex])):
                newmatrice.columns[firstindex][secondindex] = listobject[secondindex][firstindex]
        return newmatrice

    def multiplylistpair(self, list1, list2):
        returnsum = 0
        assert len(list1) == len(list2)
        for index, number in enumerate(list1):
            returnsum += number * list2[index]
        return returnsum

    def __str__(self):
        returnstring = ""
        for row in self.matrix:
            returnstring += str(row)
            returnstring += '\n'
        return returnstring

    def __mul__(self,other):
        if type(other) == int:
            returnmatrix = self.get()
            for row in returnmatrix:
                for i in range(len(row)):
                    row[i] *= other
            return self.creatematrice(returnmatrix)
        elif type(other) == matrice:
            assert self.order[1] == other.order[0]
            newarray = matrice((self.order[0], other.order[1]))
            for rowindex in range(len(newarray.rows)):
                for columnindex in range(len(newarray.rows[rowindex])):
                    temp = self.multiplylistpair(self.rows[rowindex], other.columns[columnindex])
                    newarray.addelement(temp, rowindex, columnindex)
            return newarray
    
    def __add__(self, other):
        assert type(other) == matrice
        newarray = self.get()
        assert self.order == other.order
        for rowindex, row in enumerate(newarray):
            for columnindex, column in enumerate(row):
                newarray[rowindex][columnindex] += other.getelement(rowindex,columnindex)
        return self.creatematrice(newarray)


    def __sub__(self, other):
        assert type(other) == matrice
        newarray = self.get()
        assert self.order == other.order
        for rowindex, row in enumerate(newarray):
            for columnindex, column in enumerate(row):
                newarray[rowindex][columnindex] -= other.getelement(rowindex,columnindex)
        return self.creatematrice(newarray) 

    def get(self):
        return deepcopy(self.matrix)
