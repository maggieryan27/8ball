import time
import random

#for the record I made this first Lewin just wanted it :P
def ballOne():
    print("""       
           ____
        ,dP9CGG88@b,
      ,IP  _   Y888@@b,
     dIi  (_)   G8888@b
    dCII  (_)   G8888@@b
    GCCIi     ,GG8888@@@
    GGGGCCCGGGG88888@@@@...
    Y8GGGGGG8888888@@@@P.....
     Y88888888888@@@@@P......
     `Y8888888@@@@@@@P'......
        `@@@@@@@@@P'.......
            """"........""")
    time.sleep(0.3)

def ballTwo():
    print("""       
           ____
        ,dP9CGG88@b,
      :  _    YY888@@b,
     d  (_)   GGG8888@b
    dC  (_)   GGG8888@@b
    GCC     ,,GGG8888@@@
    GGGGCCCGGGG88888@@@@...
    Y8GGGGGG8888888@@@@P.....
     Y88888888888@@@@@P......
     `Y8888888@@@@@@@P'......
        `@@@@@@@@@P'.......
            """"........""")
    time.sleep(0.3)

def ballThree():
    print("""       
           ____
        ,dP9CGG88@bb,
       _    'YYYYY8888@,
      (_)   GGGGG88888@b
      (_)   ,GGGGG8888@@@
    :     ,,GGG8888888@@@
    GGGGCCCGGGG88888@@@@...
    Y8GGGGGG8888888@@@@P.....
     Y88888888888@@@@@P......
     `Y8888888@@@@@@@P'......
        `@@@@@@@@@P'.......
            """"........""")
    time.sleep(0.3)

def ballFour():
    print("""       
           ____
        ,dP9CGG8888b,
      YYYYYYYYY88Y88@@,
     8888888GGGGG88888@b
    :88888GGGGGGG8888@@@b
    :88888GGGGG8888888@@@
    GGGGCCCGGGG88888@@@@@...
    Y8GGGGGG88888888@@@@P.....
     Y88888888888@@@@@@P......
     `Y8888888@@@@@@@PP'......
        `@@@@@@@@@PP'.......
            """"........""")
    time.sleep(0.3)
    

def ballSix():
    print("""       
              ____
         ,dP9CGG88@b,
      ,IPPPPPPP'   _   ,
     dIiiiiiiii   (_)  G,
    dCIIIIIIIII   (_)  G8,
    GCCIiiiiiiii      ,GG,
    GGGGCCCGGGG888888@@@@...
    Y8GGGGGG88888888@@@@P.....
     Y888888888888@@@@@P......
     `Y8888888@@@@@@@@P'......
        `@@@@@@@@@@P'.......
            """"........""")
    time.sleep(0.3)    

def ballSev():
    print("""       
              ____
        ,ddP9CGG88@b,
      ,PPPP   _   Y888,
     dIIIi   (_)   GGGG,
    dCIIII   (_)   GGG88,
    GCCIIii      ,GGGG88,
    GGGGCCCGGGG888888@@@...
    Y8GGGGGG88888888@@@@.....
     Y888888888888@@@@@......
     `Y8888888@@@@@@@'......
        `@@@@@@@@@@'.......
            """"........""")
    time.sleep(0.3)
    


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days = random.choice(days)

num = (1,10)
num = random.randint(1,10)

trueFalse = ["True", "False"]
trueFalse = random.choice(trueFalse)

answers = ["Without a doubt.", "Outlook good.", "Reply hazy, try again.", "Don't count on it.", "Outlook not so good." ]
answers = random.choice(answers)


a = 0
while a != 1:
    ballOne
    print("Hello. I'm the 𝑀𝒶𝑔𝒾𝒸 8 Ball.")
    x = 0
    while x != 1:
        question = input("What is your question? ")
        ansType = input("Should I answer in [d]ays of the week, [r]andom number range, [t]rue/false, or [s]tandard answers? ")
        ansType = ansType.lower()
        if ansType not in ("d","r","t","s"):
            print("Invalid input. Try again. ")
        else:
            x = 1
    ballOne()
    ballTwo()
    ballThree()
    ballFour()
    ballSix()
    ballSev()
    if ansType == "d":
        print(days)
        print(" ")
    elif ansType == "r":
        print(num)
        print(" ")
    elif ansType == "t":
        print(trueFalse)
        print(" ")
    elif ansType == "s":
        print(answers)
        print(" ")


