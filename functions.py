def f_to_p(i, n, f=1):
    factor = 1/(1+i)**n
    return f*factor


# x = input() #for example: -400,100,120,130,200
# values = x.split(",")
# values = list(map(float,values))

# p = 0
# i = 0.1
# for n,f in enumerate(values):
#     p += f_to_p(i, n, f)

# print(p)