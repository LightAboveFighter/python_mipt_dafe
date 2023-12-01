from typing import Iterable, Union
from numbers import Real

from regressors.regressor_abc import RegressorABC


class NonparametricRegressor(RegressorABC):

    _abscissa = None
    _ordinates = None

    def __init__(self, k_neighbours):
        k_neighbours = int(k_neighbours)
        if k_neighbours < 1:
            raise RuntimeError("K_neighbours must be >=1")
        self._k_neighbours = k_neighbours

    def fit(self, abscissa: Iterable, ordinates: Iterable) -> None:
        if len(abscissa) == 0:
            raise RuntimeError("Abscissa  must be not empty")
        if len(ordinates) == 0:
            raise RuntimeError("Ordinata  must be not empty")
        if len(abscissa) != len(ordinates):
            raise RuntimeError("Abscissa and ordinate must have equal size")
        
        self._abscissa = abscissa
        self._ordinates = ordinates
        

    def predict(self, abscissa_list: Union[Real, Iterable]) -> list:
        
        if isinstance(abscissa_list, (list, Real)):
            abscissa_list = list(abscissa_list)
        ordinata_list = []
        for abscissa in abscissa_list:

            if self._abscissa == None:
                raise RuntimeError("Fit method must be called before predict")
            
            distances = list( abs(abscissa - Xi) for Xi in self._abscissa)
            distances = sorted(distances)
            h = distances[self._k_neighbours - 1]
            weights = self._calc_weights(distances, h)

            numerator = sum(Wi*Yi for Wi, Yi in zip(weights, self._ordinates))
            denumerator = sum(weights)
            ordinata = numerator/denumerator
            ordinata_list.append(ordinata)

        return ordinata_list
    
    def _calc_weights(self, distances, h):
        kernel = lambda z: 0.75 * ( 1 - z**2 ) if abs(z) < 1 else 0
        weights = [kernel(Ri/h) for Ri in distances]
        return weights

