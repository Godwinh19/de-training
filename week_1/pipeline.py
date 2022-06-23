import sys
import pandas as pd

print(sys.argv)
day = None
try:
    day =  sys.argv[1]
except:
    print("No date given")

print(f"job finished successfully for day = {day}")
