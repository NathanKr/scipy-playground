from scipy.stats import percentileofscore
list = [0, 2, 3, 2]
print(f'list : {list}')

print(percentileofscore(list, 3))
print(percentileofscore(list, 2))
print(percentileofscore(list, 1))
print(percentileofscore(list, 0))
