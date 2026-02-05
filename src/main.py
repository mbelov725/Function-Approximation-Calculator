from create_json import create_json
from create_html import create_html
from getters import get_user_function, get_user_interval, get_user_polynomial_degree
from functions import legendre_approximation, taylor_approximation

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
    create_html()

    print("All done! Now just run \"py -m http.server 8000\", then open\n" 
          "http://localhost:8000/web/desmos.html in your local browser")

main()