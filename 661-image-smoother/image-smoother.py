class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def inbound(row,col):
            return 0 <= row < len(img) and 0<= col < len(img[0])

        directions = [(0,0),(0,1),(0,-1),
                      (1,0), (1,1),(1,-1),
                      (-1,0),(-1,1),(-1,-1)
                      ]   

        answer = [[0 for i in range(len(img[0]))] for j in range(len(img)) ] 


        for i in range(len(img)):
            for j in range(len(img[0])):

                numerOfElements,totalSum = 0,0  

                for dx,dy in directions:
                    newRow,newCol   = i + dx ,j + dy

                    if inbound(newRow,newCol):
                        numerOfElements += 1
                        totalSum += img[newRow][newCol]

                average = totalSum  // numerOfElements

                answer[i][j] = average

        return answer               

        