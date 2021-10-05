# anagram program
st = input("enter a word\n")
st1 = input("enter another word\n")
new = list(st)
# print(new)
new2 = list(st1)
# print(new2)
new.sort()
new2.sort()
if(new==new2):
    print("anagram")
else:
    print("not a anagram")
    
