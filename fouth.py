list1=[1,2,1]
list2=[1,2,3]
copy=list1.copy()
copy.reverse()
copy2=list2.copy()
copy2.reverse()
if(list1==copy):
    print("Yes list1 it is palindrome")
elif(list1!=copy):
    print("list 1 Not a palindrome") 
if(list2==copy2):
    print("Yes it is palindrome")
elif(list2!=copy2):
    print("Not a palindrome")      