import sys
import random

ans = True

print "------------- Magic 8ball 🎱 -------------"

while ans:
    print ""
    question = raw_input("Ask The 8Ball your question |")
    
    answers = random.randint(1,8)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print ""
        print "It is certain"
    
    elif answers == 2:
        print ""
        print "Outlook good"
    
    elif answers == 3:
        print ""
        print "You may rely on it"
    
    elif answers == 4:
        print ""
        print "Ask again later"
    
    elif answers == 5:
        print ""
        print "Concentrate and ask again"
    
    elif answers == 6:
        print ""
        print "Reply hazy, try again"
    
    elif answers == 7:
        print ""
        print "My reply is no"
    
    elif answers == 8:
        print ""
        print "My sources say no"

