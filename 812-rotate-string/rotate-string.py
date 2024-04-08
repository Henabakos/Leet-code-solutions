class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)==len(goal):
            a=goal+goal
            if s in a:
                return True
        return False

                    
