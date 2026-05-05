from instance import Instance
from rolling_parameters import RollingParameters

class InputModel:

    def __init__(self, instance:Instance, rolling_parameters:RollingParameters):
        self.instance = instance
        self.rolling_parameters = rolling_parameters