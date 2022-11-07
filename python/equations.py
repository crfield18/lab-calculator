from operator import countOf
from typing import Union

class VariableError(ValueError):
    pass

class ncv_triangle:
    def __init__(self, mass:Union[float, None], mw:Union[float, None], vol:Union[float, None], conc:Union[float, None]):
        self.mass = mass
        self.mw = mw
        self.vol = vol
        self.conc = conc

        print(f'{type(mass)}, {type(mw)}, {type(vol)}, {type(conc)}')

    def find_conc(self, mass, mw, vol):
        return (mass/mw) * vol

    def find_vol(self, mass, mw, conc):
        return (mass/mw) / conc

    def find_mass(self, mw, conc, vol):
        return mw * conc * vol
            
    def missing_var(self):
        if all(value != None for value in vars(self).values()) or all(type(value) == Union[float, int] for value in vars(self).values()):
            raise ValueError(f'one variable must equal {None}. Current {None} count: {countOf(vars(self).values(), None)}')
        else:
            if self.conc == None:
                return ncv_triangle.find_conc(self, self.mass, self.mw, self.vol)
            elif self.vol == None:
                return ncv_triangle.find_vol(self, self.mass, self.mw, self.conc)
            elif self.mass == None:
                return ncv_triangle.find_mass(self, self.mw, self.conc, self.vol)

class c1v1:
    def __init__(self, c1:Union[float, None], v1:Union[float, None], c2:Union[float, None], v2:Union[float, None]):
        self.c1 = c1
        self.v1 = v1
        self.c2 = c2
        self.v2 = v2

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
