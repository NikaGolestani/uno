import random
arr=[]
a=[]
colors=["r","g","y","b"]
nums=["0","1","2","3","4","5","6","7","8","9","R","+2","B"]
#give the cards
for c in colors:
 for n in nums:
  arr.append(f"{c}{n}")
for p in range(3):
 a.append([])
 for i in range(5):
  b=arr[random.randint(0,len(arr)-1)]
  arr.remove(b)
  a[p].append (b)
 print(a[p])
print (arr)
floor=arr[random.randint(0,len(arr)-1)]
print(floor)
loop=True
while loop==True:
 i=0
 while i< len(a):
  x=input()
  if x in a[i] and (floor[0]==x[0] or    floor[1:]==x[1:]):
   a[i].remove(x)
   arr.append(b)
   floor=x
  elif x=="d":
   b=arr[random.randint(0,len(arr)-1)]
   arr.remove(b)
   a[i].append (b)
  elif len(a[i])==0:
   loop=False
  else:
   print("ERROR")
   i-=1
  i+=1
  print("p",i,a[i-1])
print("We have a winner")
