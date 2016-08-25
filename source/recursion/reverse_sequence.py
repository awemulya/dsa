class ReverseSeq(object):
    @staticmethod
    def reverse(sequence,rev_list=[]):
        if not sequence:
            return rev_list
        else:
            rev_list.append(sequence.pop())
            return ReverseSeq.reverse(sequence,rev_list)

    @staticmethod
    def good_reverse(sequence,start,stop):
        # at least two elements
        if start < stop-1:
            sequence[start], sequence[stop-1] = sequence[stop-1], sequence[start]
            ReverseSeq.good_reverse(sequence,start+1, stop-1)


if __name__ == '__main__':
    list_copy = list(range(10))
    # print(ReverseSeq.good_reverse(list_copy, 0, len(list_copy)))
    ReverseSeq.good_reverse(list_copy, 0, len(list_copy))
    print (list_copy)










