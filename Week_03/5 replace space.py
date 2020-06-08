class Solution:
    def replaceSpace(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        res = []
        for i in range(n):
            if s[i] == ' ':
                res.append('%20')
            else:
                res.append(s[i])
        return ''.join(res)