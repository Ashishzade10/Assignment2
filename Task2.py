sum=0
def range_sum(first, last):
    global sum
    for i in range(first,last+1):
        sum=sum+i
    print(f"The sum of number from {first} and {last} is: ", sum)    
range_sum(int(input("Enter first number: ")), int(input("Enter last number: ")))
