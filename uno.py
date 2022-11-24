import random
player_number=int(input('player number='))
card_number=int(input('card number='))
arr=["J+4","JC","JH"]*3
a=[]
p=0
colors=["r","g","y","b"]
nums=["0","1","2","3","4","5","6","7","8","9","R","+2","B"]
i=1
#give the cards
for c in colors:
  for n in nums:
    arr.append(f"{c}{n}")
#define floor
onfloor=arr[random.randint(0,len(arr)-1)]
print(onfloor)
loop=True

def givecards(num,p):
  for i in range(num):
    b = arr[random.randint(0, len(arr) - 1)]
    arr.remove(b)
    a[p].append(b)
    
def dropcard(card,p):
  global onfloor
  a[p].remove(card)
  arr.append(card)
  onfloor=card
  check_unique(card)
  
def check_unique(x):
  global p
  global i
  global onfloor
  if x[1:]=="+2" :
    givecards(2,(p+1)%player_number)
  elif x[1:]=="B":
    p+=i
  elif x[1:]=="R":
    i=-i
  elif x[0]=="J":
    if x[1:]=="+4":
      givecards(4,(p+1)%player_number)
    elif x[1:]=="H":
      hand=int(input())
      a[p%player_number],a[hand] =a[hand],a[p%player_number]
    onfloor=input()+" "
  
for k in range(player_number):
  a.append([])
  givecards(card_number,k)
  print(a[k])
print (arr)

while True :
  if len(a[p%player_number-1])<1:
    break
  
  print(onfloor,"player", p%player_number , a[p%player_number] )
  x=input()
  if x in a[p%player_number] and ((onfloor[0]==x[0] or onfloor[1:]==x[1:]) or x[0]=="J"):
    dropcard(x, p%player_number)
    
  elif x=="d":
    givecards(1,p%player_number)
    b=a[p%player_number][-1]
    if (onfloor[0]==b[0] or onfloor[1:]==b[1:]or b[0]=="J"):
      dropcard(b,p%player_number)
    elif len(a[p%player_number])==0:
      break
    
  else:
    print("ERROR")
    p-=i
  p+=i
print("Player",p%player_number,"WINS!!!")