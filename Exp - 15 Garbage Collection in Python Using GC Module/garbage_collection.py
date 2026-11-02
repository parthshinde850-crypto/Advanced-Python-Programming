import gc
import sys

# Function to create some objects
def create_objects():
    objects = []
    for i in range(1000):
        objects.append([i] * 100)
    return objects

# Function to display memory usage
def display_memory():
    print("Garbage objects:", gc.get_count())
    print("Memory usage:", sys.getsizeof(create_objects()), "bytes")

# Display initial memory usage
print("Initial Memory Usage:")
display_memory()

# Create objects and display memory usage
objects = create_objects()
print("\nAfter Creating Objects:")
display_memory()

# Delete objects
del objects

# Enable garbage collection debugging
gc.set_debug(gc.DEBUG_STATS)

# Collect garbage and display memory usage
print("\nGarbage Collection:")
collected = gc.collect()
print("Objects collected:", collected)

# Disable garbage collection debugging
gc.set_debug(0)

print("\nGarbage Collection Completed.")