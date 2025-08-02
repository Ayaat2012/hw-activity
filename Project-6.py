num = int(input("Enter a number"))

n = num
n_str = str(num)
n_digit = len(n_str)

sum = 0
for powers in n_str:
    digit = int(powers)
    sum += digit ** n_digit
    

if sum == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")