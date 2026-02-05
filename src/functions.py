import sympy as sp
import scipy.integrate as spi

def legendre_approximation(function, degree, left_endpoint, right_endpoint):
    x = sp.symbols("x")

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
    x = sp.symbols("x")

    centre = (left_endpoint + right_endpoint)/2

    polynomial = 0

    for i in range(degree + 1):
        derivative = sp.diff(function, x, i).subs(x, centre)

        term = (derivative/sp.factorial(i))*(x - centre)**i

        polynomial += term

    return sp.simplify(polynomial)