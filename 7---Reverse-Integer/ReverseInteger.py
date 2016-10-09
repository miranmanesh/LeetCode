class Solution(object):
    def reverse(self, x):
        s =''
        if x<0:
            s = s+('-')
            x = x*-1
        elif x ==0:
            s = s+'0'
            return int(s)
        a = []    
        while (x!= 0):
            a.append(x%10)
            x = x/10

        for i in range(len(a)):
            s= s+str(a[i])
        s_final= int(s)
        if (s_final>2**31) or (s_final <-(2**31)-1):
            return 0 
        else:
            return s_final
sol = Solution()
print (sol.reverse(1534236469 ))
            