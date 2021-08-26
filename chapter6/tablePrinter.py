def printTable(table):
    colWidths = [0] * len(table)
    
    for x in range(len(table)):
        for y in range(len(table[x])):
            if len(table[x][y]) > colWidths[x]:
                colWidths[x] = len(table[x][y])
    
    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(colWidths[y]) + ' ', end='')
        print()
        

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)