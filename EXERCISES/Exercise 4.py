Write a program that asks the user “What is the capital of France?” and waits for their response.
qs1=input("whats is the captial of france:")
ans="france"
if qs1 == ans:
    print ("Correct!")

else:
    print("Wrong!")

#Advanced Requirements:

#Ignore Capitalization:
qs1=input("whats is the captial of france:")
ans="france"
if qs1.lower() == ans.lower():
    print ("Correct!")

else:
    print("Wrong!")

#Multiple Questions:
