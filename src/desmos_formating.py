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