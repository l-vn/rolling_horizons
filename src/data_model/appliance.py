from typing import List, Optional

class Appliance:

    def __init__(self, e_na:float, beta_max:float, start:int, end:int, inc_lambda: Optional[float]=None, inc_coeffs:Optional[List[float]]=None):
        self.e_na = e_na
        self.beta_max = beta_max
        self.start = start
        self.end = end
        self.inc_coeffs = inc_coeffs
        self.inc_lambda = inc_lambda
        if inc_coeffs is None:
            inc_coeffs = [h * inc_lambda for h in range(self.end-self.start+1)]
        if not self._is_feasible():
            print("An appliance was created, but that appliance will be problematic")

    def _is_feasible(self) -> bool:
        return ((self.e_na / (self.end - self.start + 1) ) <= self.beta_max) and (self.end >= self.start)