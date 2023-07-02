def sorter(item):
    return item['name']


persenters = [
    {'name': 'wangqijai', 'age': 24},
    {'name': 'yangchangjiang', 'age': 24}
]

persenters.sort(key=sorter)
print(sorter)
print(persenters)
