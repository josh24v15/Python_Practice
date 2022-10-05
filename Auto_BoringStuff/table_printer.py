"""Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right justified.
"""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']]

def printTable(tables):
    
    colWidths = [0]*len(tables)
    for i in range(len(colWidths)):
        for j in range(len(tables[0])):
            if len(tables[i][j]) > colWidths[i]:
                colWidths[i] = len(tables[i][j])
    
    for j in range(len(tables[0])):
        for i in range(len(tables)):
            print(tables[i][j].rjust(colWidths[i]) + ' ', end='')
        print('')
    

printTable(tableData)