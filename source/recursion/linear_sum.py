class LinearSum(object):
    @staticmethod
    def sum(sequence,index):
        " calculate sum of sequence up to index length"
        if index == 0:
            return 0
        else:
            return LinearSum.sum(sequence, index-1) + sequence[index-1]


class BinarySum(object):
    @staticmethod
    def sum(sequence,start=0,stop=None):
        if stop is None:
            stop = len(sequence)
        if start == stop:
            return 0
        elif start == stop -1:
            return sequence[start]
        else:
            mid = (start + stop ) // 2
            return BinarySum.sum(start,mid) + BinarySum.sum(mid,stop)

