class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq = [0] * 26
        for i in range(len(s1)):
            freq[ord(s1[i]) - ord('a')] += 1
        windSize = len(s1)
        for i in range (len(s2)):
            windIdx = 0
            idx = i
            windFreq = [0] * 26
            while windIdx < windSize and idx < len(s2):
                windFreq[ord(s2[idx]) - ord('a')] += 1
                windIdx += 1
                idx += 1
            if freq == windFreq:
                return True
        return False        