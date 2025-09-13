class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(substring):
            if substring in memo:
                return memo[substring]
            if not substring:
                return [""] 

            res = []
            for word in word_set:
                if substring.startswith(word):
                    rest_sentences = dfs(substring[len(word):])
                    for sentence in rest_sentences:
                        if sentence:
                            res.append(word + " " + sentence)
                        else:
                            res.append(word)
            memo[substring] = res
            return res

        return dfs(s)
        
