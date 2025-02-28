try:
    # Open and read the file
    with open('sample.txt', 'r') as file:
        print("Reading file content:")
        # Print content line by line with line number
        for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line.strip()}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
