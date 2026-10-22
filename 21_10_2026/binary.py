def binary(n):
    b=""
    while n>0:
        b=str(n%2)+b
        n//=2
    return b
if __name__=="__main__":
    print(binary(76))