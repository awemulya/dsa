class EnglihRuler(object):
    """Class to draw english ruler"""
    def __init__(self,inches, tick_length):

        if not isinstance(inches, int):
            raise TypeError(" Inches must be tye Int")

        if not isinstance(tick_length, int):
            raise TypeError(" Thick length must be tye Int")
        self._inches = inches
        self._tick_length = tick_length

    def run(self):
        self.draw_line(self._tick_length,"0")
        for j in range(1,self._inches+1):
            self.draw_interval(self._tick_length-1)
            self.draw_line(j, str(j))

    def draw_line(self, tick_length, label=''):
        line = "-" * tick_length
        if label:
            line +=  ''+ label
        print(line)

    def draw_interval(self,central_length):
        if central_length > 0:
            self.draw_interval(central_length-1)
            self.draw_line(central_length)
            self.draw_interval(central_length-1)


if __name__ == '__main__':
    r = EnglihRuler(1,5)
    r.run()

