import re
import math
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source: 
     print("Speak Anything :")
     audio = r.listen(source)
     try:
         a= r.recognize_google(audio)
         j=str(a)
         print("You said : {}".format(a))
     except:
         print("Sorry could not recognize your voice")



def pls(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def sqrt(a):
    print(a*a)


# calc1={'sum','plus',"add","+"}
# calc2={"subtraction","sub","minus","-"}
# calc3={"Multiplication","int","*","multiply "}
# calc4={"divid","/","division"}

# a=input ("Enter the value for calculation==: ")
temp = re.findall(r'\d+', j)
b=len(j.split())
print("total n.of words in:",b)
print("total int value is:",temp)
lenth=len(temp)
print(lenth)

if lenth==2:
    print(temp[0],"and" ,temp[1])
    if ("sum" in a or "+" in a or "plus" in a) and lenth==2 :
        print("sum of output ")
        pls(int(temp[0]),int(temp[1]))
    if "subtract" in a :
        print("subract of output ")
        sub(int(temp[0]),int(temp[1]))

    if "multiply" in a :
        print("multiply of output ")
        mul(int(temp[0]),int(temp[1]))
    if "divid" in a:
        print("divid of output ")
        div(int(temp[0]),int(temp[1]))
elif lenth==1 :
    print(temp[0])
    if "square" in a:
        print("sqrt of output")
        sqrt(int(temp[0]))
elif lenth>=3:
    bad_chars = ['calculate', 'what', 'is', "the",'value','sum','of'] 
    #test_string = " what is the value of 1+3+4"
    print ("Original String : " + j) 
    for i in bad_chars : 
	    j = j.replace(i, '') 
    print ("Resultant list is : " + str(j)) 
    total=eval(str(j))
    print(total)
else:
    print("check input value or operator")
