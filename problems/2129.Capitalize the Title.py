class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join([i.capitalize() if len(i)>2 else i.lower() for i in title.split()])