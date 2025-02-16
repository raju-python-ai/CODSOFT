import random
lower="abcdefghijklmnopqrstuvwxyz" #smallletters
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ" #captitalletters
numbers="0123456789" 
symbols="!@#$%^&*()_-{}[]'?/><,"
all_character =lower+upper+numbers+symbols 
#Enter the input
len=int(input("Enter the length:"))
password =" ".join(random.sample(all_character,len))
print("GENERATE PASSWORD:",password) #output
