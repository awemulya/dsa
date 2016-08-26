class Power(object):
    def __init__(self, x, n):
        """ calculates power of x to the power x ^n
        """
        self._x = x
        self._n = n
        self._result = self.calculate_power()

    def calculate_power(self):
        return True

    def get_result(self):
        return self._result
