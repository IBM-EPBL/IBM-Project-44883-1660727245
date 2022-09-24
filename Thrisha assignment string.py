#concatenate
str1 = "Hello "
str2 = "Sharmila"
str3 = str1 + str2
print(str3)

#reverse
def reverse(str):
    string = " "
    for i in str:
        string = i + string
    return string
str = "Read books"
print("The original string is:",str)
print("The reverse string is:", reverse(str))

#slice
str = "Hello, World!"
print(str[2:5])