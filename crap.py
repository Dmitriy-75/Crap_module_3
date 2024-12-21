







test_list = [{(2, 'Urban', ('Urban2', 35))}]


print("The original list is : " , test_list)

res=[]
for i in test_list:
    x=[]
    for j in i:
        if type(j) is tuple:
            x.extend(list(j))
        else:
            x.append(j)
    res.append(tuple(x))
print("The unpacked nested tuple list is : " + str(res))



























