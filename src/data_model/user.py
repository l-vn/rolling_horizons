from typing import List

from appliance import Appliance

class User:

    def __init__(self, appliances:List[Appliance], inc_factor:float):
        self.appliances = appliances
        self.inc_factor = inc_factor