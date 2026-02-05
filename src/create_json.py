import os
import json
from desmos_formating import to_desmos_format

def create_json(function, degree, legendre, taylor, left_endpoint, right_endpoint):
    interval = f"\\left\\{{{left_endpoint}\\le x\\le {right_endpoint}\\right\\}}"
    legendre_error  = f"\\sqrt{{\\int_{{{left_endpoint}}}^{{{right_endpoint}}}\\left(f\\left(x\\right)-P_{{{degree}}}\\left(x\\right)\\right)^{{2}}dx}}"
    taylor_error = f"\\sqrt{{\\int_{{{left_endpoint}}}^{{{right_endpoint}}}\\left(f\\left(x\\right)-T_{{{degree}}}\\left(x\\right)\\right)^{{2}}dx}}"

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    WEB_DIR = os.path.join(BASE_DIR, "web")

    with open(os.path.join(WEB_DIR, "functions.json"), "w") as f:
        json.dump({
            "function": to_desmos_format(function, "", "f"),
            "legendre": to_desmos_format(legendre, degree, "P"),
            "taylor": to_desmos_format(taylor, degree, "T"),
            "interval": interval,
            "legendre_error": legendre_error,
            "taylor_error": taylor_error
        }, f, indent = 4)

    print("web/functions.json created.")