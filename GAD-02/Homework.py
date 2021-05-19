initial_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

ascending_list = sorted(initial_list)
print("Ascending order: ")
print(ascending_list)

descending_list = sorted(initial_list, reverse = True)
print("\nDescending order: ")
print(descending_list)

print("\nEven numbers using slice: ")
print(ascending_list[1::2])

print("\nOdd numbers using slice: ")
print(ascending_list[::2])

print("\nMultiples of 3: ")
print(ascending_list[2::3])