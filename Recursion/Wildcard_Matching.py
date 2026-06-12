class Solution:
    def isMatch(self, s, p):
        string_len = len(s)
        pattern_len = len(p)

        dp = [[False] * (pattern_len + 1) for _ in range(string_len + 1)]
        dp[0][0] = True

        for j in range(1, pattern_len + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        for i in range(1, string_len + 1):
            for j in range(1, pattern_len + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[string_len][pattern_len]