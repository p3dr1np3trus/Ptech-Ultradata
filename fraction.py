class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator


    def toNumber(self):
        result = self.numerator / self.denominator
        return result
    
    def approximate(self, decimalcases):
        result = self.numerator / self.denominator
        return round(result, decimalcases)


    def invert(self):
        temporaryContainer = self.denominator
        self.denominator = self.numerator
        self.numerator = temporaryContainer

    def invertedValue(self):
        temporaryContainer = self.denominator
        denominator = self.numerator
        numerator = temporaryContainer
        return(Fraction(numerator, denominator))
                    

    def __repr__(self):
        return f'fraction: {self.numerator}/{self.denominator}'


    def sum(self, otherfraction):
        if not isinstance(otherfraction, Fraction):
            print(f"error: otherfraction (second argument) needs to be a'fraction' instance not {otherfraction.__class__}")
            return 1
        if self.denominator == otherfraction.denominator:
            nextDenominator = self.denominator
            nextNumerator = self.numerator + otherfraction.numerator
            return Fraction(nextNumerator, nextDenominator)
        else:
            nextDenominator = self.denominator * otherfraction.denominator
            nextNumerator = (self.numerator * otherfraction.denominator) + (self.denominator * otherfraction.numerator)
            return Fraction(nextNumerator, nextDenominator)
 
    def sub(self, otherfraction):
        if not isinstance(otherfraction, Fraction):
            print(f"error: otherfraction (second argument) needs to be a'fraction' instance not {otherfraction.__class__}")
            return Fraction(1, 1)
        if self.denominator == otherfraction.denominator:
            nextDenominator = self.denominator
            nextNumerator = self.numerator - otherfraction.numerator
            return Fraction(nextNumerator, nextDenominator)
        else:
            nextDenominator = self.denominator * otherfraction.denominator
            nextNumerator = (self.numerator * otherfraction.denominator) - (self.denominator * otherfraction.numerator)
            return Fraction(nextNumerator, nextDenominator)
    
    def mul(self, otherfraction):
        if not isinstance(otherfraction, Fraction):
            print(f"error: otherfraction (second argument) needs to be a'fraction' instance not {otherfraction.__class__}")
            return Fraction(1, 1)
        
        nextDenominator = self.denominator * otherfraction.denominator
        nextNumerator = self.numerator * otherfraction.numerator
        return Fraction(nextNumerator, nextDenominator)

    def div(self, otherfraction):
        if not isinstance(otherfraction, Fraction):
            print(f"error: otherfraction (second argument) needs to be a'fraction' instance not {otherfraction.__class__}")
            return Fraction(1, 1)
        
        nextDenominator = self.denominator * otherfraction.invertedValue().denominator
        nextNumerator = self.numerator * otherfraction.invertedValue().numerator
        return Fraction(nextNumerator, nextDenominator)
