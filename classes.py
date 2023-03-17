import numpy as np


class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(
                type(self).__name__, type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        else:
            raise TypeError("unsupported operand type(s) for -: '{}' and '{}'".format(
                type(self).__name__, type(other).__name__))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Complex(self.real * other, self.imag * other)
        elif isinstance(other, Complex):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return Complex(real, imag)
        else:
            raise TypeError("unsupported operand type(s) for *: '{}' and '{}'".format(
                type(self).__name__, type(other).__name__))

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Complex(self.real / other, self.imag / other)
        elif isinstance(other, Complex):
            conj = other.conjugate()
            num = self * conj
            denom = other * conj
            return Complex(num.real/denom.real, num.imag/denom.real)
        else:
            raise TypeError("unsupported operand type(s) for /: '{}' and '{}'".format(
                type(self).__name__, type(other).__name__))

    def __repr__(self):
        return f"Complex({self.real}, {self.imag})"

    def __str__(self):
        if self.real and self.imag:
            if self.imag > 0:
                return f"{self.real:.2f}+j{self.imag:.2f}"
            else:
                return f"{self.real}-j{abs(self.imag)}"
        elif self.real:
            return f'{self.real}'
        else:
            return f'-j{abs(self.imag)}'

    def conjugate(self):
        return Complex(self.real, -self.imag)


class Polar:
    def __init__(self, mag=0, phase=0):
        self.mag = mag
        self.phase = phase

    def __add__(self, other):
        if isinstance(other, Polar):
            real = self.mag * np.cos(self.phase) + \
                other.mag * np.cos(other.phase)
            imag = self.mag * np.sin(self.phase) + \
                other.mag * np.sin(other.phase)
            mag = np.sqrt(real**2 + imag**2)
            phase = np.arctan2(imag, real)
            return Polar(mag, phase)
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(
                type(self).__name__, type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, Polar):
            real = self.mag * np.cos(self.phase) - \
                other.mag * np.cos(other.phase)
            imag = self.mag * np.sin(self.phase) - \
                other.mag * np.sin(other.phase)
            mag = np.sqrt(real**2 + imag**2)
            phase = np.arctan2(imag, real)
            return Polar(mag, phase)
        else:
            raise TypeError("unsupported operand type(s) for -: '{}' and '{}'".format(
                type(self).__name__, type(other).__name__))

    def __mul__(self, other):
        if isinstance(other, Polar):
            return Polar(self.mag * other.mag, self.phase + other.phase)

    def __truediv__(self, other):
        if isinstance(other, Polar):
            new_mag = self.mag / other.mag
            new_phase = self.phase - other.phase
            return Polar(mag=new_mag, phase=new_phase)
        elif isinstance(other, (int, float)):
            new_mag = self.mag / other
            return Polar(mag=new_mag, phase=self.phase)
        else:
            raise TypeError("unsupported operand type(s) for /: '{}' and '{}'".format(
                type(self).__name__, type(other).__name__))

    def __str__(self):
        return f"{self.mag:.2f}∠{self.phase:.2f}°"

    def __repr__(self):
        return f"Polar({self.mag}, {self.phase})"


# def stringDebug(prmt):
#    print(f"\n\t-> {prmt}")
