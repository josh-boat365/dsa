size_of_input = 11 
num1 =  list(map(int, input("\nEnter 1 numbers: ").strip().split()))[:size_of_input]

num2 =  list(map(int, input("\nEnter 2 numbers: ").strip().split()))[:size_of_input]

x = sorted(str(num1))
y = sorted(str(num2))

string1 = " ".join(x)
string2 = " ".join(y)

if string1 == string2:
    print("Yes")
else:
    print("No")