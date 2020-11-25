Sale_A = [60, 56, 63, 75, 48]
x_vals = range(len(Sale_A))
y =[x-0.14 for x in x_vals]
z = [x+0.14 for x in x_vals]
print(y, z)