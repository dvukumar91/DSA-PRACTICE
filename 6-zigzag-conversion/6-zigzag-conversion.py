class Solution:
    def convert(self, s: str, n: int) -> str:
        if n==1:
            return s
        
        arr = [[] for i in range(n)]
        curr = 0
        increment = 1
        i = 0
        res = ""
        while(i<(len(s))):
        
            if curr==0:
                increment = 1
            elif curr == n-1:
                increment = -1

            arr[curr].append(s[i])
            curr+=increment
            #print(curr)
            i+=1
        #print(arr)
        for i in arr:
            res +="".join(i)
        return res