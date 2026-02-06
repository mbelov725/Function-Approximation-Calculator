import os
from dotenv import load_dotenv
import sympy as sp

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
    MAX_DEGREE = 7
    
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

def get_API_KEY():
    dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
    load_dotenv(dotenv_path)

    YOUR_API_KEY = os.getenv("API_KEY")

    if YOUR_API_KEY is None:
        raise ValueError("API_KEY not found in .env! Make sure .env exists in the project root.")

    return YOUR_API_KEY