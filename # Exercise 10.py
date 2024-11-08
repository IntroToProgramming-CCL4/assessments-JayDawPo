# Exercise 10
def check_even_odd(number):
    if number % 2 == 0:
        return str(number) + " is even."
    else:
        return str(number) + " is odd."


def main():
    user_input = input("Enter a number: ")
    user_input = int(user_input)
    result = check_even_odd(user_input)
    print(result)
main()