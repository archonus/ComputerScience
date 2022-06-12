
n = int(input("Enter a number..."))
i = 0
num_counted = 0
while num_counted < n:
    i+=1
    digits = []
    str_i = str(i) # String representation of i
    for str_digit in str_i: # Add each digit to list of digits
        digits.append(int(str_digit))
    sum_digits = sum(digits) # sum of the digits
    if i % sum_digits == 0:
        num_counted += 1
print(f"Harshad number {n} is {i}")