class RollingParameters:

    def __init__(self, step:int, length_frozen:int, length_rolling:int):
        self.step = step
        self.length_frozen = length_frozen
        self.length_rolling = length_rolling