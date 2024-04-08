class DataStream:

    def __init__(self, value: int, k: int):
        self.cnt = 0
        self.value=value
        self.k=k
    def consec(self, num: int) -> bool:
        if num == self.value:
            self.cnt+=1
            return self.cnt>=self.k
        else:
            self.cnt=0
            return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)