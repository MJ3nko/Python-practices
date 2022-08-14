import sys


print("Used to manipulate PYTHONPATH, where python will look for modules and packages.")

for entry in sys.path:
    print(entry)
