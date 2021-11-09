h= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word= "mango"
count=0
listt=['_','_','_','_','_']
def ans():
    for i in range(len(word)):
        if user == word[i]:
            listt[i] = user

while True:
    user = input("enter the letter")
    if user in word:
        ans()
        print(*listt)
    else:
        print(h[count])
        count+=1

    if count==7:
        break




'''def hang():
    global count
    for i in range(len(a)):
      if (a[i] != user):
        print(h[count])
        count += 1
def inp():
    global user
    for i in range(len(a)):
        if(a[i]==user):
            listt[i]=user
        else:
            hang()
for i in range(len(a)):
    print(listt)
    inp()
'''



