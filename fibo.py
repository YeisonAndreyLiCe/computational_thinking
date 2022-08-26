""" def fibonacci(n):  
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2) """

def fibonacci_din(n, memo = {}):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        result = fibonacci_din(n-1, memo) + fibonacci_din(n-2, memo)
        memo[n] = result
        return result
    
def main():
    n = int(input("Enter a number: "))
    print(fibonacci_din(n))

if __name__ == '__main__':
    main()