 # simple_intrest calculation
def simple_intrest(p, n, r):
    i =(p*n*r)/100
    amt = p + i
    return {"intrest": i,"amount": amt}

# Take input from user in console
p = float(input("please enter principle in INR: "))
n = int(input("please enter Numberof Years: "))
r = float(input("please enter rate of intrest in %p.a.:"))

# calculate intrest and amount
results = simple_intrest(p, n, r)

#print results
print(results)