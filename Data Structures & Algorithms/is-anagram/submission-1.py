class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = Counter(s)
        s2 = Counter(t)
        for c in s:
            if s1[c] != s2[c]:
                return False
        return True
        