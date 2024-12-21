
d = ((), [{(2, 'Urban', ('Urban2', 35))}])


def split_tuple(m):
    res=[]
    for i in m:
        x = []
        for j in i:
            if  isinstance(j, tuple):
                x.extend(list(j))
            else:
                x.append(j)
        res.append(x)
    return res


print(split_tuple(d))
y=split_tuple(d)
for i in y:
    if type(i) is not int or str:
        split_tuple(i)
print(split_tuple(i))



# for j in i:
       #      if isinstance(j, int):
       #          list_int.append(int(j))
       #      if isinstance(j, str):
       #          list_str.append(str(j))