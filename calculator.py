'''
This program uses Legendre polynomials to approximate a function f(x) on an 
interval [a, b] using a polynomial of a degree n, p_n(x). It does this by 
minimizing something called the L^2 norm, which is the defined as the integral of 
[f(x) - p_n(x)]^2 on [a,b]. A common assumption would be to use the Taylor 
polynomial of degree, n T_n(x), however this is does not minimize the L^2 error on 
an interval.

To find the optimal soluton, we need to turn to linear algebra. It is useful to 
think of functions in terms of vector spaces. Consider a vector space consisting 
of all the functions continuous on [a, b]. One subspace of this vector space is 
non-polynomials, such as exponential, logarithmic, and trigonometric functions;
lets call this subspace V. Another subspace of this vector space would be all 
of the polynomials; lets call this subspace U. Lets say we take a vector v from
subspace V, meaning a specific function (take sin(x) for example), and we want 
to find any vector u from subpace U, that is any polynomial, that minimizes the 
distance between the two vectors. The best option is something called an orthogonal
projection. Esentially, this meaning casting a shadow of the vector v onto the
subspace U.

First we need to find an orthonormal basis for U. Orthonormal means that for any
two vectors in the subspace, their dot product is 0. However, defining the dot
product for functions is slightly more difficult. This can be done by computing 
something the inner product of two functions f(x) and g(x): 
<f, g> = integral of f(x)*g(x) over [a, b].

This is where the Legendre polynomials come in. These polynomials have
the unique property that for any two polynomials P_n(x) and P_m(x) of degree n and m,
respectively, the integral of P_m(x)*P_n(x) over [-1, 1] is 0. Legendre polynomials
are orthogonal on t ∈ [-1, 1]. To use them on an interval x ∈ [a, b], we need to map
x onto t using t = (2*x - a - b)/(b - a).

The best approximation p_n(x) is represented as a linear combination of Legendre
polynomails of degree up to n. p_n(x) is the sum of c_k*P_k*(2*x - a - b)/(b-a), where
c_k = <f, P_k>/<P_k, P_k> = (2*k + 1)/(b-a)*integral of f(x)*P_k[(2*x - a - b)/(b - a)]
on [a,b]

Note: to input e^x enter E**(x) and to input x! input gamma(x+1)

Dependecies: you must have SymPy and SciPy installed before running this program. Run:
py -m pip install sympy
py -m pip install scipy
'''

import sympy as sp
import scipy.integrate as spi

def get_user_function():
    while True:
        print("Enter a mathematical function in temrs of \"x\"")
        user_function = input("f(x) = ")

        try:
            return sp.sympify(user_function)
        except:
            print("Invalid mathematical function")

def get_user_interval():
    while True:
        left_endpoint = input("Enter the left endpoint: ")
        right_endpoint = input("Enter the right endpoint: ")

        try:
            left_endpoint = float(left_endpoint)
            right_endpoint = float(right_endpoint)

            if left_endpoint < right_endpoint:
                return left_endpoint, right_endpoint
            else:
                print("Left endpoint must be less than right endpoint.")
        except ValueError:
            print("Please enter a valid interval.")

def get_user_polynomial_degree():
    MIN_DEGREE = 2
    MAX_DEGREE = 5
    
    while True:
        degree = input(f"Please enter the degree of the polynomial approximation ({MIN_DEGREE}-{MAX_DEGREE}): ")

        try:
            degree = int(degree)

            if MIN_DEGREE <= degree <= MAX_DEGREE:
                return degree
            else:
                print(f"Degree must be between {MIN_DEGREE} and {MAX_DEGREE}")
        except ValueError:
            print("Please enter a valid number")

x = sp.symbols("x")

def legendre_approximation(function, degree, left_endpoint, right_endpoint):
    t = (2*x - left_endpoint - right_endpoint)/(right_endpoint - left_endpoint)
    
    polynomial = 0

    f_numeric = sp.lambdify(x, function, "numpy")

    for i in range(degree + 1):
        P_i_sym = sp.legendre(i, t)
        P_i_num = sp.lambdify(x, P_i_sym, "numpy")

        integrand = lambda s: f_numeric(s) * P_i_num(s)

        integral, _ = spi.quad(integrand, left_endpoint, right_endpoint)

        coefficient = (2*i + 1)/(right_endpoint - left_endpoint)

        polynomial += coefficient * integral * P_i_sym
    
    return sp.simplify(polynomial)

def taylor_approximation(function, degree, left_endpoint, right_endpoint):
    centre = (left_endpoint + right_endpoint)/2

    polynomial = 0

    f_numeric = sp.lambdify(x, function, "numpy")

    for i in range(degree + 1):
        derivative = sp.diff(function, x, i).subs(x, centre)

        term = (derivative/sp.factorial(i))*(x - centre)**i

        polynomial += term

    return sp.simplify(polynomial)

def main():
    f = get_user_function()
    left_endpoint, right_endpoint = get_user_interval()
    n = get_user_polynomial_degree()

    legendre = legendre_approximation(f, n, left_endpoint, right_endpoint)
    taylor = taylor_approximation(f, n, left_endpoint, right_endpoint)

    print("Legenre approximation:")
    print(legendre)

    print("Taylor approximation:")
    print(taylor)

main()