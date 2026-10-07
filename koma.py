class Koma:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

    def change_state(self):
        if self.state == "W":
            self.state = "B"
        else:
            self.state = "W"