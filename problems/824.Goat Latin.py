class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sent = sentence.split(" ")
        for i in range(len(sent)):
            if sent[i][0].lower() in ('a','e','i','o','u'):
                sent[i] = sent[i] + 'ma' + 'a'*(i+1)
            else:
                sent[i] = sent[i][1:]+sent[i][0]+'ma' + 'a'*(i+1)
                
        return ' '.join(sent)