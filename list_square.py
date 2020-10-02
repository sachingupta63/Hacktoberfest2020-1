def list_square(l):
    square=[]
    for i in l:
        square.append(i*i)
    return square

n=int(input("Enter the length of string : "))
string=[]
for i in range(n):
    x=int(input())
    string.append(x)
print(list_square(string))
