a = 1
n = int(input("Enter a number whose factorial is to be calculated:"))
for i in range(1,n+1):
    sum  = a*i
    a = sum

print(a)
