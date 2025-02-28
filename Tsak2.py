def file_ops():
    with open("output.txt", "w") as f:
        f.write(input("Enter text: ") + "\n")
    print("Written.")
    with open("output.txt", "a") as f:
        f.write(input("Append text: ") + "\n")
    print("Appended.")
    with open("output.txt", "r") as f:
        print("\nContent:\n" + f.read())

file_ops()