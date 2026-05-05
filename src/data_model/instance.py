from typing import List

from battery import Battery
from scenario_tree import ScenarioTree
from user import User

class Instance:

    def __init__(self, users:List[User], battery:Battery, scenario_tree:ScenarioTree, prices_vs:List[float], energy_cost:List[float]):
        self.users = users
        self.battery = battery
        self.scenario_tree = scenario_tree
        self.prices_vs = prices_vs
        self.energy_cost = energy_cost