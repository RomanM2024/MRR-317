import os


root = r'nested1\nested2'
objs = os.listdir(root)
print(objs)

print(sorted(objs, reverse=True))

