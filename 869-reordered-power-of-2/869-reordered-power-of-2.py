class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        allpow = set()
        for i in range(32):
            temp = "".join(sorted(str(pow(2,i))))
            allpow.add(temp)
        check = "".join(sorted(str(n)))
        if check in allpow:
            return True
        return False