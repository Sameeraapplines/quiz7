#fizzbuzz program

for i in range(101):
    if(i % 3 == 0 and i % 5 == 0):
        print("fizzbuzz")
        continue
    elif (i % 3 == 0) :
        print("fizz")
        continue
    elif(i% 5==0):
        print("buzz")
        continue
    else:
        print(i)

# another methods
    
# new = int(input("enter the starting number"))
# for i in range(new, 101, 1):
#     if(i % 3 == 0 and i % 5 == 0):
#         print("fizzbuzz")
#         continue
#     elif (i % 3 == 0) :
#         print("fizz")
#         continue
#     elif(i% 5==0):
#         print("buzz")
#         continue
#     else:
#         print(i)


# start = int(input("enter the starting number"))
# end = int(input("enter the ending number"))
# for i in range(start, end, 1):
#     if(i % 3 == 0 and i % 5 == 0):
#         print("fizzbuzz")
#         continue
#     elif (i % 3 == 0) :
#         print("fizz")
#         continue
#     elif(i% 5==0):
#         print("buzz")
#         continue
#     else:
#         print(i)

