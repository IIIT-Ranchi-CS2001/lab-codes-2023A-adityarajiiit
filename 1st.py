#1...........


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
if num2 != 0:
    int_quotient = num1 // num2  
    remainder = num1 % num2      
    fractional_quotient = num1 / num2  
else:
    int_quotient = "undefined"
    remainder = "undefined"
    fractional_quotient = "undefined"


print("\nResults:")
print(f"Numbers Entered: {num1} and {num2}")
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Integer Quotient: {int_quotient}")
print(f"Remainder: {remainder}")
print(f"Fractional Quotient: {fractional_quotient}")



#Output..................
"""
Enter the first number: 25
Enter the second number: 4

Results:
Numbers Entered: 25.0 and 4.0
Sum: 29.0
Difference: 21.0
Product: 100.0
Integer Quotient: 6.0
Remainder: 1.0
Fractional Quotient: 6.25
"""




#2....................


import math


def calculate_area(a, b, c):
    s = (a + b + c) / 2  
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def calculate_perimeter(a, b, c):
    return a + b + c


def calculate_angles(a, b, c):
    angle_A = math.degrees(math.acos((b*2 + c2 - a*2) / (2 * b * c)))
    angle_B = math.degrees(math.acos((a*2 + c2 - b*2) / (2 * a * c)))
    angle_C = math.degrees(math.acos((a*2 + b2 - c*2) / (2 * a * b)))
    return angle_A, angle_B, angle_C


a = float(input("Enter the length of the first side (a): "))
b = float(input("Enter the length of the second side (b): "))
c = float(input("Enter the length of the third side (c): "))


if a + b > c and b + c > a and c + a > b:
   
    area = calculate_area(a, b, c)
    perimeter = calculate_perimeter(a, b, c)
    
    
    angle_A, angle_B, angle_C = calculate_angles(a, b, c)
    
    
    print("\nResults:")
    print(f"Side lengths: a = {a}, b = {b}, c = {c}")
    print(f"Area of the triangle: {area:.2f} square units")
    print(f"Perimeter of the triangle: {perimeter:.2f} units")
    print(f"Angle A (opposite side a): {angle_A:.2f} degrees")
    print(f"Angle B (opposite side b): {angle_B:.2f} degrees")
    print(f"Angle C (opposite side c): {angle_C:.2f} degrees")
else:
    print("The given sides do not form a valid triangle.")



#Output..............

"""
Enter the length of the first side (a): 7
Enter the length of the second side (b): 10
Enter the length of the third side (c): 5

Results:
Side lengths: a = 7.0, b = 10.0, c = 5.0
Area of the triangle: 16.25 square units
Perimeter of the triangle: 22.00 units
Angle A (opposite side a): 34.99 degrees
Angle B (opposite side b): 90.00 degrees
Angle C (opposite side c): 55.01 degrees

"""



#3......................


def parallel_impedance(Z1, Z2):
    Z_eq = 1 / ((1 / Z1) + (1 / Z2))  


z1_real = float(input("Enter the real part of Z1: "))
z1_imag = float(input("Enter the imaginary part of Z1: "))
Z1 = complex(z1_real, z1_imag)

z2_real = float(input("Enter the real part of Z2: "))
z2_imag = float(input("Enter the imaginary part of Z2: "))
Z2 = complex(z2_real, z2_imag)


Z_eq = parallel_impedance(Z1, Z2)


print("\nResults:")
print(f"Z1 = {Z1}")
print(f"Z2 = {Z2}")
print(f"Equivalent Impedance (Z_eq) = {Z_eq}")
print(f"Real part of Z_eq: {Z_eq.real:.2f}")
print(f"Imaginary part of Z_eq: {Z_eq.imag:.2f}")




#output:
"""
Enter the real part of Z1: 5
Enter the imaginary part of Z1: 3
Enter the real part of Z2: 4
Enter the imaginary part of Z2: -2

Results:
Z1 = (5+3j)
Z2 = (4-2j)
Equivalent Impedance (Z_eq) = (2.62+1.32j)
Real part of Z_eq: 2.62
Imaginary part of Z_eq: 1.32


"""