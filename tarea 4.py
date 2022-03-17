import numpy as np
import sys

print("int",sys.getsizeof(int()));
print("float",sys.getsizeof(float()));
print("str",sys.getsizeof(str()));
a = input("int a: ");
c = input("float c: ");
d = input("str d: ");
print("int a" ,sys.getsizeof(int(a)));
print("float c",sys.getsizeof(float(c)));
print("str d",sys.getsizeof(str(d)));
