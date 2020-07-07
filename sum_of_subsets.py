class DP:
    def __init__(self, wt ,val,w):
        self.wt = wt
        self.val = val
        self.w = w

    def sum_of_subsets(self):
        n = len(self.wt)
        t = [[False for x in range(self.w+1)] for x in range(n+1)]

        #intialisation
        for i in range(n+1):
            for j in range(self.w+1):
                if i == 0:
                    t[i][j] = False
                if j ==0:
                    t[i][j] = True
        print(t)
        for i in range(n + 1):
            for j in range(self.w + 1):

                if self.wt[i-1] <= j:
                    t[i][j] = (t[i-1][j-self.wt[i-1]] or t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]

        return t[n][self.w],t
def equal_partion_sum(wt,val):
    n = len(wt)
    s = sum(wt)
    print(s)
    if s % 2 != 0:
        return False
    else:
        obj = DP(wt,val,int(s/2))
        res = obj.sum_of_subsets()
        return res
wt=[5,1,5,10]
val = [2,3,4,1]
w =9
res = equal_partion_sum(wt, val)
print("ans"+str(res))



