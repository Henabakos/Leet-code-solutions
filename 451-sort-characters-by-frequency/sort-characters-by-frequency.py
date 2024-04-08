class Solution:
    def frequencySort(self, s: str) -> str:
        a=Counter(s)
        sr=""
        sorted_str=sorted(a.items(),key=lambda x:x[1],reverse=True)
        sorted_strByvalue=dict(sorted_str)

        for key,value in sorted_strByvalue.items():
            for i in range(value):
                sr+=key

        return sr
