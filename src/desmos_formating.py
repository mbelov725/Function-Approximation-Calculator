def to_desmos_format(expression, degree = "", letter = ""):
    s = str(expression)
    s = s.replace("**", "^")
    s = s.replace("*", "")
    s = s.replace("(x)", "{x}")
    s = s.replace("sin", "\\sin")
    s = s.replace("cos", "\\cos")
    s = s.replace("tan", "\\tan")
    s = s.replace("csc", "\\csc")
    s = s.replace("sec", "\\sec")
    s = s.replace("cot", "\\cot")
    s = s.replace("asin", "\\arcsin")
    s = s.replace("acos", "\\arccos")
    s = s.replace("atan", "\\arctan")
    s = s.replace("acsc", "\\arccsc")
    s = s.replace("asec", "\\arcsec")
    s = s.replace("acot", "\\arccot")
    s = s.replace("log", "\\ln")

    if degree == "":
        function_name = f"{letter}{degree}"
    else:
        function_name = f"{letter}_{degree}"

    s = f"{function_name}(x) = {s}"

    return s