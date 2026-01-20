def change_number(x):
    x = 100

def change_list(lst):
    lst[0] = 999

num = 20
print("Before change_number:", num) # before running the function x was 20

change_number(num)

print("After change_number:", num) # after running the function x became 100


numbers = [2, 4, 5]
print("Before change_list:", numbers) # before changing the list first number in the list was 2

change_list(numbers)

print("After change_list:", numbers) # after changing the list first number in the list became 999
