class Frac:
    def __init__(self, nominator, denominator):
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
        if self.nominator==0:
            return ("0")
            
        elif self.nominator !=0 and self.nominator >= self.denominator:
            result_part1 = str(self.nominator//self.denominator)
            result_part2 = str(self.nominator%self.denominator)
            return (f"{result_part1} {result_part2}/{self.denominator}" )

        elif self.nominator !=0 and self.nominator < self.denominator:
            if self.denominator % self.nominator == 0:
                result = self.denominator//self.nominator
                return (f"1/{result}" )
            else:
                return (f"{self.nominator}/{self.denominator}" )


    
    def __str__(self): # represent the fraction in a neat way for printing
        return f"{self.nominator}/{self.denominator}"

    def mixed(self): # represent the fraction in mixed terms 
        if self.nominator >= self.denominator:
            result_part1 = str(self.nominator//self.denominator)
            result_part2 = str(self.nominator%self.denominator)
            return (f"{self.nominator}/{self.denominator} --> {result_part1} {result_part2}/{self.denominator} (mixed)" )
        
    def __eq__(self, other): # checks equality by overloading ==
        if self.simplify() == other.simplify():
            return(f"{self.nominator}/{self.denominator} == {other.nominator}/{other.denominator}  --> True")
        else:
            return(f"{self.nominator}/{self.denominator} == {other.nominator}/{other.denominator}  --> False")
    
    def __add__(self, other):
        add_nominator = self.nominator*other.denominator+other.nominator*self.denominator
        #print(add_nominator)
        add_denominator = self.denominator * other.denominator
        #print(add_denominator)
        add_frac = Frac(add_nominator, add_denominator)
        #print(add_frac)
        return (add_frac) 
   
    def __sub__(self, other):
        add_nominator = self.nominator*other.denominator - other.nominator*self.denominator
        add_denominator = self.denominator * other.denominator
        add_frac = Frac(add_nominator, add_denominator)
        return (add_frac)
    
    def __truediv__(self, other):
        add_nominator = self.nominator*other.denominator
        add_denominator = self.denominator*other.nominator
        add_frac = Frac(add_nominator, add_denominator)
        return (add_frac)

    def __mul__(self, other):
        add_nominator = self.nominator*other.nominator
        add_denominator = self.denominator*other.denominator
        add_frac = Frac(add_nominator, add_denominator)
        return (add_frac)

# test negative numbers
try:
    frac1 = Frac(4,-8)
except TypeError as err:
    print(err)
except ValueError as err:
    print(err)


# test str
try:
    frac1 = Frac("4",8)
except TypeError as err:
    print(err)
except ValueError as err:
    print(err)

# test denominator should not be zero
try:        
    frac_test = Frac(16,0)
except ValueError as err:
    print(err)

try:
    print(f"Simply gets: {Frac(16,0).simplify()}")
except ValueError as err:
    print(err)

# test nominator=0
try:        
    frac_test = Frac(0,18)
except ValueError as err:
    print(err)

try:
    print(f"Simply {Frac(0,18)} gets: {Frac(0,18).simplify()}")
except ValueError as err:
    print(err)


frac1 = Frac(8,5)
print(frac1)
print(f"Simply {frac1} gets: {frac1.simplify()}")

frac2 = Frac(4,8)
print(frac2)
print(f"Simply {frac2} gets: {frac2.simplify()}")

print(f"{Frac(1,2)} + {Frac(1,3)} = {Frac(1,2) + Frac(1,3)}")

print(f"{Frac(1,2)} - {Frac(1,3)} = {Frac(1,2) - Frac(1,3)}")

print(f"{Frac(7,6).mixed()}") 

print(f"{Frac(3,1)}*{Frac(1,2)} = {Frac(3,1)*Frac(1,2)}") 

print(f"{Frac(1,2)}*{Frac(3,1)} = {Frac(1,2)*Frac(3,1)}") 

print(f"{Frac(1,4)}+{Frac(2,1)} = {Frac(1,4)+Frac(2,1)}") 

print(f"{Frac(1,4)}/{Frac(1,2)} = {Frac(1,4)/Frac(1,2)}") 

print(f"{Frac(2,4)}=={Frac(1,2)} --> {Frac(2,4)==Frac(1,2)}") 

print(f"{Frac(3,4)}+={Frac(2,1)} = {Frac(3,4)+Frac(2,1)}")

