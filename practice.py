# name=input("Enter your name: ") #problem no 1
# index=0
# i=0
# while(index<len(name)):
#     if name[index]=='a'or name[index]=='e'or name[index]=='i'or name[index]=='o'or name[index]=='u':
#         i+=1
#     index+=1

# print("Number of vowels: ",i )


# list1=[2,4,6,8,10,100] # problem no 2
# list2=[]
# index=0
# a=0
# while index<len(list1):
#     list2.insert(a,list1[index]*list1[index])
#     index+=1
#     a+=1
# print("List 2 that consists of squares of first: ",list2)


# tup=(1,2,3,999,100,87) #problem no 3
# index=0
# max=tup[0]
# while index<len(tup):
#     if tup[index]>max:
#         max=tup[index]
#     index+=1
# print("The maximum is ",max)   

# i=0
# sent=input('Enter a sentence: ')  #problem no 6
# words=sent.split()
# freq={}
# freq["sentence: "]=words
# print(freq)
# while i<len(words):
#     if words[i] in freq:
#         freq[words[i]]+=1
#     else:
#         freq[words[i]] =1
#     i+=1
# print("Word freq: ",freq)    
       

# set1=set()   #question no 7

# while True:
#     i=int(input("Enter the value: "))
#     if i==0:
#         break
#     else:
#         set1.add(i)
# print(set1)    

#question no 7
# list=["Hannan",10000]
# list2=["Arham",12000]
# list3=["Anaya",19000]
# index=0
# while True:
#     print("Enter your choice: ")
#     print("1. Transact", "2.deposit","3. End")
#     entry=int(input("Enter: "))
#     if entry==3:
#         break
#     if entry==1:
#         name=input("Enter your name: ")
#         if name in list:
#             print("Here are the details: ",list)
#             money=int(input("Enter the amount: "))
#             if money>list[1]:
#                 print("Trans... not possible!!")
#             else: 
#                 print("Trasnsaction successful ")
#                 list[1]=list[1]-money
#                 print("New balance: ",list[1])
#         if name in list2:
#             print("Here are the details: ",list2)
#             money=int(input("Enter the amount: "))
#             if money>list2[1]:
#                 print("Trans... not possible!!")
#             else: 
#                 print("Trasnsaction successful ")
#                 list2[1]=list2[1]-money
#                 print("New balance: ",list2[1])  
#         if name in list3:
#             print("Here are the details: ",list3)
#             money=int(input("Enter the amount: "))
#             if money>list3[1]:
#                 print("Trans... not possible!!")
#             else: 
#                 print("Trasnsaction successful ")
#                 list3[1]=list3[1]-money
#                 print("New balance: ",list3[1])                
#question no 8

# score=[]
# total=0

# x=int(input("Enter the number of overs you want to play: "))
# for over in range(0,x):
#     i=0
#     while i<6:
#          over1=int(input("Ball "))
#          score.insert(i,over1)
#          total+=over1
#          if i==5:
#           break
#          i+=1
# print("Here is the over outline: ",score)    
# print("Total: ",total)



    
