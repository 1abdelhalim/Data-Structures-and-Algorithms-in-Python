def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
num1 = 48
num2 = 18
gcd = euclidean_algorithm(num1, num2)
print("GCD of", num1, "and", num2, "is:", gcd)
