from typing import List

class ScenarioTree:

    def __init__(self, scenarios:List[List[float]], probas:List[float]):
        self.scenarios = scenarios
        self.probas = probas

    def __init__(self, base_scenarios: List[List[float]], transition_probas:List[List[float]], periods:List[int]):
        self.scenarios = []
        self.probas = []
