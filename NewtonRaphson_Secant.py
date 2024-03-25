"""
 * Authors: Aaron Hajaj (ID: 311338198) 
 *  
 * Newton-Raphson Method and Secant Method
 *  
 * git: https://github.com/Aaronha1/analysis_hw3.git
"""

def newton_raphson(f, test_range, epsilon=0.0001):
    def derivative(x):
        h = 1e-6
        return (f(x + h) - f(x)) / h

    iterations = 0
    a, b = test_range
    x = (a + b) / 2

    while abs(f(x)) > epsilon:
        x -= f(x) / derivative(x)
        iterations += 1

    print("\nNewton-Raphson method:")
    print(f"Root found at: {x:.4f}")
    print("Number of iterations:", iterations)


def secant_method(f, test_range, epsilon=0.0001):
    iterations = 0
    a, b = test_range
    x0, x1 = a, b

    while abs(f(x1)) > epsilon:
        x1, x0 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0)), x1
        iterations += 1

    print("\nSecant method:")
    print(f"Root found at: {x1:.4f}")
    print("Number of iterations:", iterations)


if __name__ == "__main__":
    f = lambda x: x**2 - 7*x + 12
    test_range = (1, 8)
    
    newton_raphson(f, test_range)
    secant_method(f, test_range)
