from scipy.stats import rankdata
list = [0, 2, 3, 2]
print(f'list : {list}')

print(f"rankdata method='min' : {rankdata(list,method='min')}")
print(f"rankdata method='max' : {rankdata(list,method='max')}")
print(f"rankdata method='dense' : {rankdata(list,method='dense')}")
print(f"rankdata method='ordinal' : {rankdata(list,method='ordinal')}")