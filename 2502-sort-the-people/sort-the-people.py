class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        def bubble_sort(arr):
            for i in range(len(arr)):
                for j in range(1,len(arr)):
                    if arr[j-1]>arr[j]:
                        arr[j],arr[j-1]=arr[j-1],arr[j]

        tall={}
        for i in range(len(names)):
            tall.update({heights[i]:names[i]})

        bubble_sort(heights)
        a=[]
        for i in heights:
            for key,value in tall.items():
                if i==key:
                    a.append(value)
        return a[::-1]




    