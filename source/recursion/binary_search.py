class BinarySearch(object):

    def __init__(self, seq):

        if not isinstance(seq,list):
            raise TypeError("seq value must be type list")

        self._seq = seq

    def search(self,value,low=None,high=None):
        if not (isinstance(value,int) or isinstance(value, float)):
            raise TypeError("search item value must be type integer or float")
        if low is None: low =  0
        if high is None: high = len(self._seq)-1
        if low > high:
            return False

        medium = (low + high) // 2
        if value == self._seq[medium]:
            return True
        elif value > medium:
            return self.search(value,medium+1,high)
        else:
            return self.search(value,low,medium-1)

if __name__ == '__main__':
    r = BinarySearch(list(range(10)))
    print("found "+ str(5)) if r.search(5) else print("not found")


