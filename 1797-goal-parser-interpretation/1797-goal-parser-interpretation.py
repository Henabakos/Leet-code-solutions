class Solution:
    def interpret(self, command: str) -> str:
        stack=[]
        s=""
        i,j=0,1
        while(j<=len(command)):
            if command[i]=="G":
                s+=command[i]
                i+=1
                j+=1
            elif command[i]=='(' and command[j]==')':
                s+="o"
                i+=2
                j+=2
            elif command[i]=='(' and command[j]=='a':
                s+="al"
                i+=4
                j+=4
        return s



