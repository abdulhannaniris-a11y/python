# print("Hello")
# def mul(a, b):
#     a=int(input("Enter the value of a: "))
#     b=int(input("Enter the value of b: "))
#     sum=a+b
#     print(sum)
# a=0
# b=0
# mul(a,b)

# def fun(list):
#     print("The lenght of the list is: ",len(list))
#     print(list)
# list=[]
# i=0
# while i<4:
#     value=int (input("Enter the value in the list: "))
#     list.append(value)
#     i+=1
# fun(list)

# #function to find the factorial of a number
# def fact():
#     n=int(input("Enter the value of n: "))
#     i=1
#     fact=1
#     while i<=n:
#         fact=fact*i
#         i+=1
#     print(fact)
# fact()    

#function of conversion


# def fun():
#     a=int(input("Enter the value in USD: "))
#     rupee=a*207
#     print(rupee)
# fun()

#homework

# def funct():
#     a=int(input("Enter a number: "))
#     str1="Even"
#     str2 ="Odd"
#     if(a%2==0):
#         return str1
#     else:
#         return str2
# result=print(funct())    

#some practice questions 
# def fun(tupp):
#     i=0
#     while i<len(tupp):
#         print(tupp[i])
#         i+=1
# tupp=("Apple","Bannana","Grapes")
# fun(tupp)

# def fun(list):
    
#     val=int(input("Enter the value that should be checked in the list: "))   
#     if val in list:
#          print("Yes founded on index: ",list.index(val))
#     else: 
#          print("Not founded")
# list=[1,2,3,4,5,67,78,99]
# fun(list)

# def long_name(list):
#     i=0
#     longest=list[0]
#     while i<len(list):
#         if(len(list[i])>len(longest)):
#             longest=list[i]
        
#         i+=1
#     print("Longest name: ",longest)
        

# list=["Hannan","Falak hannan","Arham","Talha hannan hannan"]
# long_name(list)

# def fun(list):
#     i=0
#     while i<len(list):
#         j=i+1
#         while j<len(list):
#             if(list[i]==list[j]):
#                 list.pop(j)
#             else:
#                 j+=1
            
#         i+=1
#     print(list)
# list=[1,2,3,4,5,1,2,3,4,5] #removing the duplicates 
# fun(list)   

# def ev_od(list):
#     i=0
#     count1=0
#     count2=0
#     while i<len(list):
#         if(list[i]%2==0):
#             count1+=1
#         else:
#             count2+=1
#         i+=1
#     print("The count of even: ",count1)
#     print("The count of odd nums: ",count2)
             
# list=[1,2,3,4,5,6,7,8,9]
# ev_od(list)



# def av(marks):
#     i=0
#     sum=0
#     while i<len(marks):
#         sum+=marks[i]
#         i+=1
#     print("The total marks: ",sum)
#     avg=sum/len(marks)    
#     print("The total avg: ",avg)




# marks=(20,22,21,23)
# av(marks)