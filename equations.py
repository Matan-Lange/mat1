
def exponent(x: float) -> float:
    result = 1
    factorial = 1
    p_x = x

    for i in range(1,100):
        factorial = factorial * i
        result = result + (x / factorial)
        x = x * p_x

    return result


def Ln(x: float) -> float:
    if x<= 0:
        return 0

    y0 = -1
    y1 = 0

    for i in range(1,100):
        y0 = y1
        y1 = y0 + 2 * (x - exponent(y0)) / (x + exponent(y0))
    return float('%0.6f' % y1)


def XtimesY(x: float, y: float) -> float:
    if x <= 0:
        return 0

    power = y * Ln(x)
    return_value = float('%0.6f' % exponent(power))
    return return_value


def sqrt(x: float, y: float) -> float:
    if x <= 0:
        return 0

    return float('%0.6f' % XtimesY(y, 1/x))


def calculate(x: float) -> float:
    if x< 0 :
        return 0
    rvalue = exponent(x) * XtimesY(7, x) * XtimesY(x, -1) * sqrt(x, x)
    return  float('%0.6f' % rvalue)




