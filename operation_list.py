animals =['tiger' , 'lion' , 'zebra', 'peacock' , 'adnan' ]
print("print the list  1 : " , animals)
human = ['aman', 'khan' , 'adnan' , 'anas', 'mine']
print("print the list  2 : " , human)
print("mutable operation  : ")
animals[4]="rabbit"
print("print the list  1 : " , animals)
human[4]= "samar"
print("print the list  2 : " , human)
print("slicing operation : ")
print(animals[2:4])
print(" concatination operaion : ")
human = human + ['kahala' , 'aunty' ]
print("print the list  2 : " , human)
print(" merging operaion : ")
animals=human + animals
print("print the list  1 : " , animals)
print(" convert a tuple or set or dictionary int a list by using list() operaion : ")
l=("amaan")
print(list(l))
print ("aliasing ND CLONNING operation :")
print(animals[3],human[4])
list1= []
list1 = animals+human
print(list1)
print("searching operation : ")
res = 'zebra' in animals
print("identity opertion ; ")
num1=10
num2=10
print (num1 is num2 )
