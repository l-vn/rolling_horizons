from ..data_model.instance import Instance

class Model:

    def __init__(self, instance: Instance, big_m:float):
        self.instance = instance
        self.big_m = big_m
        self.number_hours = instance.get_scenario_tree().get_number_hours()


    def _add_variables(self):
        pass

    def _add_constraints(self):
        pass

    def _solve(self):
        pass