# Set {value}
# dictionary {key:value}
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
# 'intersection', 'intersection_update', 'isdisjoint', 'issubset',
# 'issuperset', 'pop', 'remove', 'symmetric_difference',
# 'symmetric_difference_update', 'union', 'update'

data = {5,6,7,8,6,7}
print(data)


new_data = [4,5,6,77,89,0,4,5]
print(list(set(new_data)))

print(dir(data))


print({5,6}.intersection({6,7}))