class LinearSum(object):
    @staticmethod
    def sum(sequence,index):
        " calculate sum of sequence up to index length"
        if index == 0:
            return 0
        else:
            return LinearSum.sum(sequence,index-1) + sequence[index-1]