import math 
class Frac:
    def __init__(self, nominator, denominator=1): # the default is denominator=1
        self.nominator = nominator
        self.denominator = denominator

    @property
    def nominator(self):
        return self._nominator

    @nominator.setter
    def nominator(self, value: int):
        if not isinstance(value, int):
            raise TypeError(f"Nominator should be integer, not {type(value)}")
        if not value >= 0:
            raise ValueError(f"Nominator should be non-negative number, not {value}")
        self._nominator = value

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, value: int):
        if not isinstance(value, int):          
            raise TypeError(f"Nominator should be integer, not {type(value)}")
        if not value > 0:
            raise ValueError(f"Denominator should be positive number, not {value}")
        self._denominator = value

    def simplify(self): # simplifies to most simple form unless value is given
        highest_common_factor = math.gcd(self.nominator, self.denominator)
        nominator_simplified = int(self.nominator / highest_common_factor)
        denominator_simplified = int(self.denominator / highest_common_factor)
        if nominator_simplified == 0:
            return 0
        elif nominator_simplified == denominator_simplified:
            return 1
        else: 
            return Frac(nominator_simplified, denominator_simplified)

 
    def __str__(self): # represent the fraction in a neat way for printing
        return f"{self.nominator}/{self.denominator}"

    def mixed(self): # represent the fraction in mixed terms 
        if self.nominator > self.denominator:
            whole_number_part = self.nominator//self.denominator
            fraction_part = self.nominator%self.denominator
            return (f"{whole_number_part} {fraction_part}/{self.denominator} (mixed)" )
        else:
            return self.simplify()
        
    def __eq__(self, other): # checks equality by overloading ==
        self_simplied = self.simplify()
        other_simplied = other.simplify()

        if  self_simplied.nominator == other_simplied.nominator  and self_simplied.denominator == other_simplied.denominator:
            return True
        else:
            return False
    
    def __add__(self, other):
        add_nominator = self.nominator*other.denominator+other.nominator*self.denominator
        #print(add_nominator)
        add_denominator = self.denominator * other.denominator
        #print(add_denominator)
        add_frac = Frac(add_nominator, add_denominator)
        #print(add_frac)
        return add_frac.simplify() 
   
    def __sub__(self, other):
        add_nominator = self.nominator*other.denominator - other.nominator*self.denominator
        add_denominator = self.denominator * other.denominator
        add_frac = Frac(add_nominator, add_denominator)
        return add_frac.simplify()
    
    def __truediv__(self, other):
        add_nominator = self.nominator*other.denominator
        add_denominator = self.denominator*other.nominator
        add_frac = Frac(add_nominator, add_denominator)
        return add_frac.simplify()

    def __mul__(self, other):
        add_nominator = self.nominator*other.nominator
        add_denominator = self.denominator*other.denominator
        add_frac = Frac(add_nominator, add_denominator)
        return add_frac.simplify()
