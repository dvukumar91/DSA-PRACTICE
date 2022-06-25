class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def palindrom(left,right,s):
            arr = []
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
                res = s[left+1:right]
                arr.append(res)
            return len(arr)
        
        count = 0
        for i in range(len(s)):
            temp = palindrom(i,i,s)
            
            count+=temp
            
            res = palindrom(i,i+1,s)
            
            count+=res
        return count
            