
import gc
import time
import sys

# Check garbage collection status
print("Garbage Collection Enabled:", gc.isenabled())

# Create objects
class Student:
    pass

a = Student()
b = Student()

# Create circular reference
a.ref = b
b.ref = a

# Delete objects
del a
del b

# Check garbage collection count
print("\nGarbage Collection Count:")
print(gc.get_count())

# Measure time before collection
start = time.time()

# Perform manual garbage collection
collected = gc.collect()

end = time.time()

print("\nObjects Collected:", collected)
print("Time Taken:", end - start)

# Disable garbage collection
gc.disable()
print("\nGarbage Collection Disabled:", gc.isenabled())

# Enable garbage collection
gc.enable()
print("Garbage Collection Enabled:", gc.isenabled())

print("\nProgram Completed!")

