def subset_diff(arr):
    n = len(arr)
    w = sum(arr)
    t = [[False for x in range( w+ 1)] for x in range(n + 1)]
    for i in range(n+1):
        t[i][0] = True
    for i in range(n+1):
        for j in range(w+1):
            if arr[i-1]<=j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    li = []
    for i in range(int((w/2)+1)):
        if t[n][i]== True:
            li.append(abs(w-(2*i)))
    for i in range()
    return min(li)




arr = [1,2,7,6,1]
res = subset_diff(arr)
print(res)