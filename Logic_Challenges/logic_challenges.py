
def challenge1(n):
    output = []
    for num in range(1, n+1):
        if num % 15 == 0:
            output.append("fizz buzz")
            print("fizz buzz")
        elif num % 3 == 0:
            output.append("fizz")
            print("fizz")
        elif num % 5 == 0:
            output.append("buzz")
            print("buzz")
        else:
            output.append(str(num))
            print(num)
    return output

def challenge2(n):
    def fibonacci(n):
        if n < 0:
            raise ValueError("Invalid input. Please enter a non-negative integer.")
        elif n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)  
    fib_value = fibonacci(n)  
    print(fib_value)    
    return fib_value

def challenge3(text):
    import re
    from collections import Counter

    words = re.findall(r'\w+', text.lower())    
    return Counter(words)

if __name__ == "__main__":
    for challenge, input in ((challenge1,100), (challenge2,10), 
                             (challenge3, "Hi how are things? How are you? Are you a developer? I am also a developer")):
        challenge(input)
        print("*.*.*.*.*.*.*.*.*.*.*.*.*")
    