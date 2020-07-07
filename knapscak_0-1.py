#0-1 knapsack top down approach
def kanpsack(wt, val, w, n):
    t = [[0 for x in range(w + 1)] for x in range(n + 1)]
    print(t)
    for i in range(n+1):
        for j in range(w+1):
            if (i==0) or (j == 0):
                t[i][j]=0

            elif wt[i-1] <= w:
                t[i][j] = max(val[i-1] + t[i-1][j-wt[i-1]],  t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    print(t)
    return t[n][w]


val = [60, 100, 120]
wt = [10, 20, 30]
w= 50
n=len(wt)

res = kanpsack(wt,val,w,n)
print(res)

