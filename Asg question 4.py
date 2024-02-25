def maximum_length(str1,str2):
    len1=len(str1)
    len2=len(str2)
    if (len1>len2):
        print("String with maximum length:",str1)
    elif(len1>len2):
        print("String with maximum length:",str2)
    else:
        print("Both are equal..")

str1=(input("Enter the first string:"))
str2=(input("Enter the second string:"))

maximum_length(str1,str2)