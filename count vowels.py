word=input("enter the word:")
word=list(word)
countvowel=0
countcon=0
countspl=0
countdigit=0

for i in word:
     if i in 'aeiou':
         countvowel+=1
     elif i in '1234567890':
         countdigit+=1
     elif i in '%$#@&*':
         countspl+=1
     else:
         countcon+=1
print("vowel=",countvowel)
print("con=",countcon)
print("spl=",countspl)
print("digit=",countdigit)
