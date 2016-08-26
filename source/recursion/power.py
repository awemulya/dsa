class Power(object):
    def __init__(self, x, n):
        """ calculates power of x to the power x ^n
        """
        if not isinstance(x,int):
            raise TypeError("x must be type Int")
        if not isinstance(n,int):
            raise TypeError("n must be type int")
        self._x = x
        self._n = n

    def calculate_power(self, n=None):
        if n is None:
            n = self._n
        if n == 0 :
            return 1
        else:
            partial = self.calculate_power(n//2)
            result = partial * partial
            if n % 2: #n odd
                return result * self._x
            return result

