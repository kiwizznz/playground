def toPig(start):
  vowels="aeiou"
  new=""
  start = start.split(" ")
  
  for word in start:
    first = word[0]
    if(first in vowels):
      new+=first
      
    for i in range(1,len(word)):
      new+=word[i]
    
    if(not (first in vowels)):
      new+=first
      
    new+="ay "
  return new


def fromPig(start):
  if(not ("ay" in start)):
    return "Error: No pygLatin found!"
  new=""
  start = start.split(" ")
  for word in start:
    if(not word==""):
      last = word[len(word)-3]
      new+=last
      for i in range(len(word)-3):
        new+=word[i]
      new+=" "
    
  return new
  
original = str(input("Enter a string: "))
if("ay" in original):
  print(fromPig(original))
else:
  print(toPig(original))