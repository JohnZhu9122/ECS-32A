#parrot.py
#Jiawei Zhu
#
#Upper output and quiet with differnt vision 

while True:
    #Prompt the input that type whatever you want
    type_input = input(">")
    #The quiet can be QuiEt,Quiet,quiet. But their lower() are same.
    if type_input.lower() == 'quiet':
        #Breaking the loop
        break
    else:
        #Let the input all be upper() that helps print the upper version text
        type_input = type_input.upper()
        #Make the output
        print(type_input)
        #It doesn't suitable for quiet,so with countinue don let it become infinite
        continue
