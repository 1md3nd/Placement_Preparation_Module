class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = []
        for word in words:
            temp = ""
            for i in range(len(word)):
                index = ord(word[i]) - 97
                temp += morse[index]
            res.append(temp)
        count = collections.Counter(res)
        return len(count)
                    
        