def convert_to_str_arr(string):
    w = string.split()
    l = len(max(w, key=lambda w_: len(w_)))+2
    str_arr = []
    str_arr.append(" "*(l-len(w[0]))+w[0])
    str_arr.append(w[1]+" "*((l-len(w[2]))-1)+w[2])
    str_arr.append("-"*(l))
    r = str(eval(string))
    str_arr.append(" "*(l-len(r))+r)
    return str_arr


def validate_str(string):
    switcher = {
        "op": {"f": lambda w_a: w_a[1] in ["+", "-"],
               "e": "Error: Operator must be '+' or '-'."},
        "is_digits": {"f": lambda w_a: w_a[0].isdigit() and w_a[2].isdigit(),
                      "e": "Error: Numbers must only contain digits."},
        "is_length": {"f": lambda w_a: len(w_a[0]) <= 4 and len(w_a[2]) <= 4,
                      "e": "Error: Numbers cannot be more than four digits."}
    }
    s_a = string.split()
    for validation in switcher:
        if switcher[validation]["f"](s_a):
            pass
        else:
            return switcher[validation]["e"]
    return True


def combine_arr(arrays, state=False):
    lines = 4 if state else 3
    final = ""
    for line in range(0, lines):
        final += (((" " * 4).join([array[line]
                  for array in arrays],)).rstrip())+"\n"
    return final.rstrip()


def arithmetic_arranger(problems, state=False):
    if len(problems) > 4:
        return "Error: Too many problems."
    for problem in problems:
        result = validate_str(problem)
        if not result is True:
            return result

    return combine_arr([convert_to_str_arr(problem)for problem in problems], state)
