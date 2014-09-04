finalAnswer = 0
naturalNumber = 0
while naturalNumber < 1000:
    if (naturalNumber % 3 == 0) | (naturalNumber % 5 == 0):
        finalAnswer += naturalNumber
    naturalNumber += 1
print "answer is", finalAnswer 
