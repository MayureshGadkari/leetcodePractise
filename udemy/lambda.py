# even_list = [x for x in range(1,10) if (lambda x:x%2==0)(x)]
# print(even_list)

undefined_lambda = lambda x,y=int(input("Enter the number:")):x*y
print(undefined_lambda(15))