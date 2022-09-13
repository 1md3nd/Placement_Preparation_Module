class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        N = len(data)
        def check(num,i):
            if num &( 1 << (i-1)) == 0:
                return True
            return False
        # for 
        c = 0
        for i in range(N):
            if c > 0:
                if not check(data[i],8) and check(data[i],7):
                    c -=1
                    if c < 0:
                        return False
                    continue
                else:
                    return False
            else:
                if check(data[i],8): #0
                    continue
                else:
                    if check(data[i],7): #10
                        return False
                    if check(data[i],6): #110
                        c = 1
                        continue
                    if check(data[i],5): #1110
                        c = 2
                        continue
                    if check(data[i],4): #11110
                        c = 3
                        continue
                    return False
        if c != 0:
            return False
        return True
                
