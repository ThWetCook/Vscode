import sys



while True:
    user_input = input("Enter a number or exponentiation expression (or 0 to exit): ")
    if user_input == "0":
        break

    if "^" in user_input:
        base, exponent = user_input.split("^")
        base = int(base)
        exponent = int(exponent)
        result = base ** exponent
    else:
        result = int(user_input)

    steps = 0
    original_number = result

    while result != 1:
        if result % 2 == 0:
            result = result // 2
        else:
            result = result * 3 + 1
        steps += 1
        print(result)

    print("The exponentiation", base, "^", exponent, "reached 1 after", steps, "steps.\n")
