from operator import countOf
from typing import Union
from python.exceptions import *

class ncv_triangle: # mass = mol/mw etc.
    def __init__(self, mw:Union[float, None], mass:Union[float, None], vol:Union[float, None], conc:Union[float, None]):
        self.mw = mw        # molecular weight        
        self.mass = mass    # mass in g
        self.vol = vol      # volume in l
        self.conc = conc    # conc in M

    def find_conc(self, mw, mass, vol):
        return (mass/mw) / vol

    def find_vol(self, mw, mass, conc):
        return (mass/mw) / conc

    def find_mass(self, mw, conc, vol):
        return mw * conc * vol

    def find_mw(self, mass, conc, vol):
        return mass / (conc*vol)
            
    def missing_var(self):
        try:
            none_count = countOf(vars(self).values(), None)
            if none_count != 1:
                raise VariableError(f'1 variable must equal {None}. Current {None} count: {none_count}')
            else:
                if self.conc == None:
                    return ncv_triangle.find_conc(self, self.mw, self.mass, self.vol)
                elif self.vol == None:
                    return ncv_triangle.find_vol(self, self.mw, self.mass, self.conc)
                elif self.mass == None:
                    return ncv_triangle.find_mass(self, self.mw, self.vol, self.conc)
                elif self.mw == None:
                    return ncv_triangle.find_mw(self, self.mass, self.vol, self.conc)
        except TypeError:
            print('Unsupported operand type used as function input. This function only accepts: int, float or None')

class c1v1: #c1v1 = c2v2
    def __init__(self, c1:Union[float, None], v1:Union[float, None], c2:Union[float, None], v2:Union[float, None]):
        self.c1 = c1    # conc 1
        self.v1 = v1    # vol 1
        self.c2 = c2    # conc 2
        self.v2 = v2    # vol 2

    def find_c1(self, v1, c2, v2):
        return (c2 * v2) / v1

    def find_v1(self, c1, c2, v2):
        return (c2 * v2) / c1

    def find_c2(self, c1, v1, v2):
        return (c1 * v1) / v2

    def find_v2(self, c1, v1, c2):
        return (c1 * v1) / c2

    def missing_var(self):
        try:
            none_count = countOf(vars(self).values(), None)
            if none_count != 1:
                raise VariableError
            else:
                if self.c1 == None:
                    return c1v1.find_c1(self, self.v1, self.c2, self.v2)
                elif self.v1 == None:
                    return c1v1.find_v1(self, self.c1, self.c2, self.v2)
                elif self.c2 == None:
                    return c1v1.find_c2(self, self.c1, self.v1, self.v2)
                elif self.v2 == None:
                    return c1v1.find_v2(self, self.c1, self.v1, self.c2)
        except VariableError:
            print(f'1 variable must equal {None}. Current {None} count: {none_count}')
        except TypeError:
            print('Unsupported operand type used as function input. This function only accepts: int, float or None')
