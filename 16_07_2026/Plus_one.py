"""You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits."""
digits = [1,2,3]
a=""
for i in digits:
    a+=str(i)
a=int(a)+1
b=[int(i) for i in str(a)]
print(b)