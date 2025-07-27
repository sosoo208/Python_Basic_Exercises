def factorial(n):
    if n == 0:
        return 1 
    else:
        return n * factorial(n - 1)
    
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"5! (재귀) = {factorial(5)}")
print(f"5! (반복) = {factorial_iterative(5)}")
print(f"7! (재귀) = {factorial(7)}")
print(f"7! (반복) = {factorial_iterative(7)}")