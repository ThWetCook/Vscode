import sys
import time
from decimal import Decimal, getcontext

getcontext().prec = 10000  # Set precision to a sufficiently large value

def print_large_number(number):
    number_str = str(number)
    chunk_size = 1000  # Adjust the chunk size as needed
    for i in range(0, len(number_str), chunk_size):
        print(number_str[i:i+chunk_size])

while True:
    user_input = input("Enter a number or exponentiation expression (or 0 to exit): ")
    if user_input == "0":
        break

    start_time = time.time()

    if "^" in user_input:
        base, exponent = user_input.split("^")
        base = Decimal(base)
        exponent = int(exponent)
        result = base ** exponent
    else:
        result = Decimal(user_input)

    steps = 0
    original_number = result

    while result != 1:
        if result % 2 == 0:
            result = result // 2
        else:
            result = result * 3 + 1
        steps += 1
        print_large_number(result)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"The exponentiation {base}^{exponent} reached 1 after {steps} steps.")
    print(f"Time taken: {elapsed_time:.6f} seconds\n")
