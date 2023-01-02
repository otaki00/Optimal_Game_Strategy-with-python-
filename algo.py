# this file have the code of algorithm 
# optimal solution for game strategy 

def optimalStrategy(arr):
    
    n = len(arr)
    # craete inital table and fill with zeros 
    table = [[0 for i in range(n)] for i in range(n)]
    
    for gap in range(n):
        for j in range(gap , n):
            i = j - gap
            
            x = 0 
            if((i + 2) <= j):
                x = table[i+2][j]
            
            y = 0
            if((i + 1) <= (j - 1)):
                y = table[i + 1][j - 1]
            
            z = 0
            if( i <= (j - 2)):
                z = table[i][ j - 2]
            table[i][j] = max(arr[i] + min(x , y), arr[j] + min(y , z))
    return table,table[0][n-1]
arr = [5,8,7,12,6]
print(optimalStrategy(arr))