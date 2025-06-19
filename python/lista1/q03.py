# num_A = int(input("digite um numero inteiro: "))
# num_B = int(input("digite outro numero inteiro: "))
# num_C = int(input("digite outro numero inteiro: "))

# if num_A > num_B and num_A > num_C:
#     print(num_A)
# elif num_B > num_A and num_B > num_C:
#     print(num_B)
# elif num_A == num_B == num_C: 
#     print("the numbers are equal")
# else:
#     print(num_C)

num_A = int(input("type a int number: "))
num_B = int(input("type another int number: "))
num_C = int(input("type one more int number: "))

greatest = num_A

if greatest < num_B:
    greatest = num_B
if greatest < num_C:
    greatest = num_C
    
print(greatest)