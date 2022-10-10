# 948. Bag of Tokens

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        up, down = 0, len(tokens) - 1
        max_score, cur_score = 0, 0
		
        if not tokens or tokens[0] > power:
            return 0
        
        while up <= down:
            if tokens[up] <= power:
                power -= tokens[up]
                cur_score += 1
                up += 1
            else:
                power += tokens[down]
                cur_score -= 1
                down -= 1
            max_score = max(max_score, cur_score)
        
        return max_score

# The strategy is to collect as much score as possible while
# losing as less score as possible. To do this sorting the tokens
# becomes handy. After that if the token at the up pointer is lower
# than the power we have losing it and getting a score is a good trade
#. If we can't afford to lose power we try to "buy" power by spending score.
