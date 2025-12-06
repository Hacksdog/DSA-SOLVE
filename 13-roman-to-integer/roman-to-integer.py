class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        n = len(s)
        for i,ch in enumerate(s):
            if i+1 < n and m[ch] < m[s[i+1]]:
                res -= m[ch]
            else:
                res += m[ch]
        return res
