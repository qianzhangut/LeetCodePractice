class Solution:
    def minimizeResult(self, expression: str) -> str:
        ans, cur = '', 1e8
        
        p = expression.find('+')
        
        for i in range(0, len(expression[:p])):
            for j in range(p+2, len(expression)+1):
                y = (expression[:i] if expression[:i] else "1") + "*(" + expression[i:j] + ")*" + (expression[j:] if expression[j:] else "1")
                if eval(y) < cur:
                    ans, cur = expression[:i] + "(" + expression[i:j] + ")" + expression[j:], eval(y)
                
        return ans