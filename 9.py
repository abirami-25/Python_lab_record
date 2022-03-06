# y={'carl':40,'alan':2,'bob':1,'danny':3}
# l=list(y.items())
# dict=dict(l)
# print("Dictionary",dict)
# l.sort()
# print('Ascending order is',l)
# l=list(y.items())
# l.sort(reverse=True)
# print('Descending order is',l)

# OR

d1={8:'eight',4:'four',10:'ten',0:'zero',2:'two'}
print("The dictionary to be sorted:")
print(d1)
l1=list(d1.items())
l1.sort()
d2=dict(l1)
print("The dictionary after sorting to ascending order:")
print(d2)
l2=list(d1.items())
l2.sort(reverse=True)
d3=dict(l2)
print("The dictionary after sorting to descending order:")
print(d3)