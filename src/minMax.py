numbers_list = input("enter a comma-separated list of numbers: ")
numbers_list = [int(x) for x in numbers_list.split(",")]

# print(max(numbers_list)) cannot use it
# print(min(numbers_list))

min = max = numbers_list[0]
for i in range(0, len(numbers_list)):
    if min > numbers_list[i]:
        min = numbers_list[i]

    if max < numbers_list[i]:
        max = numbers_list[i]

print("min: " + str(min))
print("max: " + str(max))
