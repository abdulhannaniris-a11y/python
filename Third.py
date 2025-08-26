print("Below are the marks of he student: ")
marks=[10,20,39,98,77]
marks.sort(reverse=True)
print(marks)
new=int(input("Enter a number to be inserted: "))
marks.insert(2,new)
print(marks)