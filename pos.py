number = []
nums = int(input("Enter number of num you want to input: "))
for xy in range(nums):
    yz = int(input("Enter positive and negative numbers: "))
    number.append(yz)
    
for xc in number:
    if xc < 0 :
        print("negative: ", xc)
    elif xc > 0:
        print ("positive: ", xc)