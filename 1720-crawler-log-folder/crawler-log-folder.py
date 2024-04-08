class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for i in logs:
            if i != "../" and i!="./":
                stack.append(i)
            elif i == "../":
                if stack:
                    stack.pop()
            else:
                pass
        return len(stack)