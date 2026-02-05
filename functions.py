import sympy as sp
import scipy.integrate as spi
import json

def get_user_function():
    while True:
        print("Enter a mathematical function in terms of \"x\"")
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

def to_desmos_format(expression, degree = "", letter = ""):
    s = str(expression)
    s = s.replace("**", "^")
    s = s.replace("*", "")

    if degree == "":
        function_name = f"{letter}{degree}"
    else:
        function_name = f"{letter}_{degree}"

    s = f"{function_name}(x) = {s}"

    return s

def create_json(function, degree, legendre, taylor, left_endpoint, right_endpoint):
    interval = f"\\left\\{{{left_endpoint}\\le x\\le {right_endpoint}\\right\\}}"
    legendre_error  = f"\\sqrt{{\\int_{{{left_endpoint}}}^{{{right_endpoint}}}\\left(f\\left(x\\right)-P_{{{degree}}}\\left(x\\right)\\right)^{{2}}dx}}"
    taylor_error = f"\\sqrt{{\\int_{{{left_endpoint}}}^{{{right_endpoint}}}\\left(f\\left(x\\right)-T_{{{degree}}}\\left(x\\right)\\right)^{{2}}dx}}"

    with open("functions.json", "w") as f:
        json.dump({
            "function": to_desmos_format(function, "", "f"),
            "legendre": to_desmos_format(legendre, degree, "P"),
            "taylor": to_desmos_format(taylor, degree, "T"),
            "interval": interval,
            "legendre_error": legendre_error,
            "taylor_error": taylor_error
        }, f, indent = 4)
    
    print("Functions saved to functions.json")

def main():
    f = get_user_function()
    left_endpoint, right_endpoint = get_user_interval()
    n = get_user_polynomial_degree()

    legendre = legendre_approximation(f, n, left_endpoint, right_endpoint)
    taylor = taylor_approximation(f, n, left_endpoint, right_endpoint)

    print("Legendre approximation:")
    print(legendre)
    print("Taylor approximation:")
    print(taylor)

    create_json(f, n, legendre, taylor, left_endpoint, right_endpoint)

main()