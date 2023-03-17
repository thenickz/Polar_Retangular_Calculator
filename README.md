![Polar_🖩_Retangular_➗✖️Calculator➖➕](https://user-images.githubusercontent.com/71512544/225834676-9767fa44-0408-475d-8831-e5287e34ed26.png)


# 🧮Polar & Retangular Calculator Classes (Working in Progress)
This Python module contains two classes: Complex and Polar. These classes allow you to represent complex numbers in rectangular and polar form, respectively.
Just write the circuit equations to solve, and the Lib (by now is just a lib) will automatically make all the conversions to solve rectangular and polar incompatible expressions, like solving a parallel circuit:
$\frac{(R_1 +jX_1) \cdot (R_2 +jX_2)}{(R_1 +jX_1) + (R_2 +jX_2)}$



## Installation
To use this module, simply download classes.py and import it into your Python code:

```python
from classes import Complex, Polar
``` 

## Usage
### Complex Class
The Complex class represents a complex number in rectangular form, with a real and imaginary component. You can create a Complex object by passing in the real and imaginary parts as arguments:

```Python
c = Complex(3, 4)  # Creates a complex number with real part 3 and imaginary part 4
```

You can perform addition, subtraction, multiplication, and division operations between Complex objects and with integers and floats:

```python
c1 = Complex(1, 2)
c2 = Complex(3, 4)

c3 = c1 + c2  # Adds two complex numbers
c4 = c1 * c2  # Multiplies two complex numbers
c5 = c1 / 2  # Divides a complex number by an integer or float

```

You can also get the complex conjugate of a Complex object:

```python
c6 = c1.conjugate()  # Gets the complex conjugate of c1
```


### Polar Class
The Polar class represents a complex number in polar form, with a magnitude and phase. You can create a Polar object by passing in the magnitude and phase as arguments:


```python
p = Polar(5, np.pi/4)  # Creates a complex number with magnitude 5 and phase pi/4
```
You can perform addition, subtraction, multiplication, and division operations between Polar objects and with integers and floats:


```python
p1 = Polar(3, np.pi/6)
p2 = Polar(4, np.pi/3)

p3 = p1 + p2  # Adds two complex numbers
p4 = p1 * p2  # Multiplies two complex numbers
p5 = p1 / 2  # Divides a complex number by an integer or float
```


## Contributing
If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request!

## License
This module is licensed under the MIT License. See LICENSE for details.

