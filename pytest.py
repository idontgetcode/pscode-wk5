largest = 0

for counter in range(1, 6):
    input_number = int(input(f"Enter number {counter}: "))
    
    if input_number > largest:
        largest = input_number

print("Largest number:", largest)
