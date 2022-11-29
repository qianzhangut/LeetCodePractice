class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n+1))
        ptr = -1
        while len(friends) > 1:
            ptr = (ptr + k) % len(friends)
            # print(friends[ptr])
            friends.pop(ptr)
            ptr -= 1
            
        return friends[0]  