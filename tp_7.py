"""Module providing a classe fraction which give different methodes to use with it"""


class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : Receive 2 integers which correspond to the numerator and denumerator
        POST : store values in 2 internal variable : self.num and self.den
        """
        if den == 0:
            raise ZeroDivisionError("denominator is null")
        num = int(round(num))
        den = int(round(den))
        counter = -1 if num >= 0 else 1
        for i in range(num, 0, counter):
            if num % i == 0 and den % i == 0:
                (num, den) = (num / abs(i), den / abs(i))
        self.__num = int(num)
        self.__den = int(den)

    @property
    def numerator(self):
        """Return the numerator's value

        PRE : Call himself as a parameter
        POST : Return the value stocked in self.__num
        """
        return self.__num

    @property
    def denominator(self):
        """Return the denominator's value

        PRE : Call himself as a parameter
        POST : Return the value stocked in self.den
        """
        return self.__den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : None
        POST : Return a reduced version of the fraction given
        """
        if self.__den == 0:
            raise ZeroDivisionError("denominator is null")
        return f"{self.__num}/{self.__den}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : Call himself as a parameter
        POST : Return a reduced version of the fraction given in a mixed form
        """
        if self.__den == 0:
            raise ZeroDivisionError("denominator is null")
        num = self.__num
        den = self.__den
        operande = ""
        integer = 0
        counter = -1 if self.__num >= 0 else 1
        while abs(num) > abs(den):
            integer += 1 if (num >= 0 and den > 0) or (num < 0 and den < 0) else -1
            num += -den if (num > den > 0) or (num < 0 and den < 0) else den
        for i in range(self.__num, 0, counter):
            if num % i == 0 and den % i == 0:
                (num, den) = (num / i, den / i)
        if (num < 0 and den < 0) or num > 0 and den > 0:
            (num, den) = (abs(num), abs(den))
            operande = "+"
        elif den < 0:
            den = abs(den)
            operande = "-"
        else:
            num = abs(num)
            operande = "-"
        return f"{integer} {operande} {int(num)}/{int(den)}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

        PRE : Call himself and a parameter "other" which is a object "Fraction"
        POST : Return a numerator and denominator from a addition
        RAISE : - ZeroDivisionError ==> If the denominator of one of the two object
                or both are equal to zero
        """
        if self.__den == 0 or other.denominator == 0:
            raise ZeroDivisionError("denominator is null")
        n1 = self.__num * other.denominator
        n2 = self.__den * other.numerator
        den = self.__den * other.denominator
        new_num = n1 + n2
        return Fraction(new_num, den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : Call himself and a parameter "other" which is a object "Fraction"
        POST : Return a numerator and a denominator from a subtraction
        RAISE : - ZeroDivisionError ==> If the denominator of one of the two object
                or both are equal to zero
        """
        if self.__den == 0 or other.denominator == 0:
            raise ZeroDivisionError("denominator is null")
        n1 = self.__num * other.denominator
        n2 = self.__den * other.numerator
        den = self.__den * other.denominator
        new_num = n1 - n2
        return Fraction(new_num, den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : Call himself and a parameter "other" which is a object "Fraction"
        POST : Return a numerator and a denominator from a multiplication
        RAISE : - ZeroDivisionError ==> If the denominator of one of the two object
                or both are equal to zero
        """
        if self.__den == 0 or other.denominator == 0:
            raise ZeroDivisionError("denominator is null")
        return Fraction(self.__num * other.numerator, self.__den * other.denominator)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : Call himself and a parameter "other" which is a object "Fraction"
        POST : Return a numerator and a denominator from a division
        RAISE : - ZeroDivisionError ==> If the denominator of one of the two object
                or both are equal to zero, the same goes for the other's numerator
        """
        if self.__den == 0 or other.denominator == 0 or other.numerator == 0:
            raise ZeroDivisionError("denominator is null")
        return Fraction(self.__num * other.denominator, self.__den * other.numerator)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : Call himself and a parameter "other" which is a object "Fraction"
        POST : Return a numerator and denominator from by powering the self with the other
        RAISE : - ZeroDivisionError ==> If the denominator of one of the two object
                or both are equal to zero
        """
        if self.__den == 0 or other.denominator == 0:
            raise ZeroDivisionError("denominator is null")
        return Fraction(
            (self.__num / self.__den) ** (other.numerator / other.denominator)
        )

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : Call himself and a parameter "other" which is a object "Fraction"
        POST : Return true if the two object are equal, return false otherwise
        RAISE : - ZeroDivisionError ==> If the denominator of one of the two object
                or both are equal to zero
        """
        if self.__den == 0 or other.denominator == 0:
            raise ZeroDivisionError("denominator is null")
        return self.__num * other.denominator == self.__den * other.numerator

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : Call himself as a parameter
        POST : Return a float value of his fraction
        RAISE : - ZeroDivisionError ==> If the denominator is equal to zero
        """
        if self.__den == 0:
            raise ZeroDivisionError("denominator is null")
        return self.__num / self.__den

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : Call himself as a parameter
        POST : Return a message saying if the value is equal to zero or not
        RAISE : - ZeroDivisionError ==> If the denominator is equal to zero
        """
        if self.__den == 0:
            raise ZeroDivisionError("denominator is null")
        if self.__num:
            return "This fraction is not equal to zero."
        else:
            return "This fraction is equal to zero."

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : Call himself as a parameter
        POST : Return integer or float depending on the result
        RAISE : - ZeroDivisionError ==> If the denominator is equal to zero
        """
        if self.__den == 0:
            raise ZeroDivisionError("denominator is null")
        if self.__num == 0 or (self.__num % self.__den == 0 and self.__num != 0):
            return "Integer"
        else:
            return "Float"

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : Call himself as a parameter
        POST : Return a message "Fraction's absolute value is under/above 1" with
               the the value of the fraction
        RAISE : - ZeroDivisionError ==> If the denominator is equal to zero
        """
        if self.__den == 0:
            raise ZeroDivisionError("denominator is null")
        result = self.__num / self.__den
        if -1 < result < 1:
            return f"Fraction's absolute value is under 1 : {result}"
        else:
            return f"Fraction's absolute value is above 1 : {result}"

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : Call himself as a parameter
        POST : Return a message "Reduced form is/isn't 1" with either the final numerator
               or a 'good' if the reduced form is 1
        RAISE : - ZeroDivisionError ==> If the denominator is equal to zero
        """
        if self.__den == 0:
            raise ZeroDivisionError("denominator is null")
        if self.__num == 0:
            return False
        num = self.__num
        den = self.__den
        counter = -1 if self.__num >= 0 else 1
        for i in range(self.__num, 0, counter):
            if num % i == 0 and den % i == 0:
                (num, den) = (num / i, den / i)
        if num == 1:
            return "Reduced form is 1 ==> Good"
        else:
            return f"Reduced form isn't 1 ==> {num}"

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : Call himself and a parameter "other" which is a object "Fraction"
        POST : Return True if the absolute value of the difference between the two
               objects is a unit fraction, return False otherwise
        """
        if self.__den == 0 or other.denominator == 0:
            raise ZeroDivisionError("denominator is null")
        n1 = self.__num * other.denominator
        n2 = self.__den * other.numerator
        new_den = self.__den * other.denominator
        new_num = n1 - n2
        result = Fraction(abs(new_num), abs(new_den))
        final_return = result.is_unit()
        return final_return
