import math

from typing import List

class ScenarioTree:

    def __init__(self, scenarios:List[List[float]], probas:List[float]):
        self.scenarios = scenarios
        self.probas = probas

    @classmethod
    def from_base_scenarios(cls, base_scenarios: List[List[float]], transition_probas:List[List[float]], periods_input:List[int]):
        scenarios = []
        probas = []
        # Define useful numbers
        number_base_scenarios = len(base_scenarios)
        number_periods = len(periods_input)
        number_scenarios = math.pow(number_base_scenarios, number_periods)
        number_hours = len(base_scenarios[0])
        periods = periods_input.copy()
        if periods[-1] != number_hours:
            periods.append(number_hours) # Should always happen
        else:
            print("Warning: the indicated time periods do not correspond to the standard input")
        

        for scenario_number in range(number_scenarios):
            current_scenario_number = scenario_number
            scenario_to_add = []
            proba = 0
            base_scenario_sequence = []
            for pow in range(number_periods):
                base_scenario_sequence.append(current_scenario_number%number_base_scenarios)
                current_scenario_number /= number_base_scenarios
                print(f"CAREFUL HERE: right division? {current_scenario_number}")
            for period in range(number_periods):
                if period != 0:
                    proba *= transition_probas[base_scenario_sequence[period]][base_scenario_sequence[period-1]]
                else:
                    proba = 1/number_base_scenarios
                for hour in range(periods[period], periods[period+1]):
                    scenario_to_add.append(base_scenarios[base_scenario_sequence[period]][hour])
            scenarios.append(scenario_to_add)
            probas.append(proba)

        if not cls._is_sum_of_probas_one(probas):
            print("Warning: problem with probabilities")

        return cls(scenarios, probas)


    @staticmethod
    def _is_sum_of_probas_one(probas:List[float]):
        return sum(probas) == 1

    def normalize_probabilities(self):
        if (sum_probas:=sum(self.probas)) == 0:
            raise Warning("Sum of probabilities is 0, normalization impossible")
        self.probas = [proba/sum_probas for proba in self.probas]

    def get_sub_scenario_tree(self, start: int, end: int, input_probas: List[float]) -> ScenarioTree:
        scenarios = [[self.scenarios[s][h] for h in range(start, end+1)] for s in self.number_scenarios]
        return ScenarioTree(scenarios, input_probas)

    def get_average_scenario(self) -> ScenarioTree:
        unique_scenario = [sum(self.probas[s] * self.scenarios[s][h] for s in self.number_scenarios) for h in range(self.number_hours)]
        return ScenarioTree([unique_scenario], [1])

    @property
    def number_hours(self):
        return len(self.scenarios[0])
    
    @property
    def number_scenarios(self):
        return len(self.probas)
    
