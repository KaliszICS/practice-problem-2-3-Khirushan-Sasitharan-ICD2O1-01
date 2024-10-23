

def q1(): 
  word = input("In: ")
  if word[-3:] == "ife":
        print("-ives")
  elif word[-2:] == "ey":
        print("-eys")
  elif word[-1] == "y":
        print("-ies")
  else:
        print("-s")

def q2(): 
  sigma = int(input("In: "))
  if  sigma > 0:
    print (f"{sigma} is positive")
  elif sigma < 0: 
    print (f"{sigma} is negative")
  elif sigma == 0:
    print ()
  

def q3():
  word = float(input("Input a number: "))
  w0rd = float(input("Input a number: "))
  ord = float(input("Input a number: "))
  if word == w0rd and ord == word:
    print ("Equilateral")
  elif word == w0rd or w0rd == ord or word == ord:
    print ("Isosceles")
  elif word + w0rd < ord or ord + w0rd < word or ord + word < w0rd:
    print ("No Triangle") 
  else: 
    print ("Scalene")




#Do not alter the following code
#Comment out the following code when running your tests

#q1()
#q2()
#q3()


