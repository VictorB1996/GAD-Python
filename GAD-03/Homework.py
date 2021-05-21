print("Function with undefinite numbers of params which returns the sum of integers and floats")
def custom_sum(*args):
    total = 0
    for parameter in args:
        try:
            total += parameter
            print(f"Added {parameter} to sum.")
        except TypeError as e:
            print(f"Element {parameter} could not be added to sum. Skipping.")
            continue
    print(total)
    return total

custom_sum(1,5,3,'abc', [12,56,'cad'])
custom_sum()


print("\nRecursive function which returns the sum of all elements up to (including) n")
def recursive_all_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_all_sum(n-1)
print(recursive_all_sum(10))

print("\nRecursive function which returns the sum of all even elements up to (including) n")
def recursive_even_sum(n):
    if n <= 0:
        return 0
    if n % 2 != 0:
        return recursive_even_sum(n-1)
    else:
        return n + recursive_even_sum(n-2)
print(recursive_even_sum(9))

print("\nRecursive function which returns the sum of all odd elements up to (including) n")
def recursive_odd_sum(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        return recursive_odd_sum(n-1)
    else:
        return n + recursive_odd_sum(n-1)
print(recursive_odd_sum(8))

print("\nFuntion which reads value from input and returns it if whole number, else returns 0")
def get_return_input():
    try:
        user_input = input("Enter a number: ")
        print(f"You entered {user_input}")
        return int(user_input)
    except ValueError as e:
        print("You did not enter a whole number.")
        return 0
get_return_input()