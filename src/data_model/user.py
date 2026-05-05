from typing import List

from device import Device

class User:

    def __init__(self, devices:List[Device], inc_factor:float):
        self.devices = devices
        self.inc_factor = inc_factor