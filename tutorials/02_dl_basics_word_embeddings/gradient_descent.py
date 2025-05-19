# for task 2


def f(x):
    """ Function f. """
    return 3 * x**3 + 6 * x**2 + x - 3

def df(x):
    """ Derivative of f. """
    return 9 * x**2 + 12 * x + 1

def update_rule(x, lr, gradient):
    """ Gradient descent update rule.

    Args:
        x [float]: position of current iteration
        lr [float]: learning rate
        gradient [function]: gradient of function that is minimized
    """

    return x - (lr * gradient(x))

if __name__ == "__main__":

    # starting point
    x0 = 1
    # x0 = -2
    # learning rate
    psi = 0.1

    # print starting point
    print("STARTING POINT:", x0)
    print("LEARNING RATE:", psi)
    print()

    # minimize!
    x = x0
    for i in range(10):
        x = update_rule(x, psi, df)
        print("ITERATION", i+1)
        print("x =", x)
        print()
