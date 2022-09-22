class Solution: 
    def reverse(self, s):
        i = 0
        j = len(s)-1
        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i+=1
            j-=1
        str11 = "" 
        for ele in s: 
            str11 += ele
        return str11
        
        
    def reverseWords(self, s: str) -> str:
        words = []
        str1 = ""
        for x in s:
            if x.isspace():
                str1 += self.reverse(words)
                str1 += " "
                words = []
            else:
                words.append(x)
        str1 += self.reverse(words)
        words = []

        return str1
        