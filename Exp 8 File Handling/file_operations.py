# Open the input file in read mode
input_file = open("input.txt", "r")

# Read all lines into a list
lines = input_file.readlines()

# Count the number of lines
line_count = len(lines)

print("Number of lines:", line_count)

# Extract the first two lines
first_two_lines = lines[:2]

# Open the output file in write mode
output_file = open("output.txt", "w")

# Write the first two lines to the output file
output_file.writelines(first_two_lines)

# Close both files
input_file.close()
output_file.close()

print("First two lines written to output.txt")