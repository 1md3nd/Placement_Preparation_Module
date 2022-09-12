class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i = 0
        j = len(tokens)-1
        ans = score = 0
        while i <= j:
            # print(power,score)
            if power >= tokens[i]:
                power -=tokens[i]
                score +=1
                i +=1
                ans = score
            # print(score,ans)
            elif power < tokens[j] and score > 0:
                score-=1
                power +=tokens[j]
                j -=1
            else:
                i +=1


        return ans
