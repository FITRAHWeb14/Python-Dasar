data1 = 500
data2 = "1000"
data3 = 9990.0

print(type(data1))
print(type(data2))
print(type(data3))

# False 
print(data1 == data2) # integer dibandingkan string
print(data2 == data3) # string dibandingkan float
print(data1 == data3) # integer dibandingkan float
