class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        import bisect
        def isMatch(word):
          if word in m: return m[word]
          l = -1
          for c in word:
            index = bisect.bisect_left(pos[c], l + 1)
            if index == len(pos[c]): 
              m[word] = 0
              return 0
            l = pos[c][index]

          m[word] = 1
          return 1

        m = {}
        pos = {chr(i + ord('a')) : [] for i in range(26)}
        for i, c in enumerate(S):
          pos[c].append(i)

        return sum(map(isMatch, words))