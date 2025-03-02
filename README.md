# Module 5: Files, Exceptions, and Errors in Python


## Task 1: Read a File and Handle Errors
### Description:
- This program attempts to open and read a text file named `sample.txt`.
- It reads and prints the content of the file **line by line**.
- If the file does not exist, it gracefully handles the error and displays a message.

### Code Explanation:
- The program tries to open `sample.txt` in read mode (`'r'`).
- If the file is found, it reads each line and prints it with line numbers.
- If the file is not found, a `FileNotFoundError` is raised, and an error message is displayed.

### How to Run:
1. Ensure that `sample.txt` exists in the same directory as the Python script.
2. Run `read_file.py` in any Python environment.
3. The program will print the contents of `sample.txt` or display an error if the file is missing.

### Example Output:
**If the file exists (`sample.txt`):**

Reading file content: Line 1: Hey Jenni how are you Line 2: So where are you

**If the file does not exist:**
Error: The file 'sample.txt' was not found.



## Task 2: Write and Append Data to a File
### Description:
- This program allows the user to input text, which is written to a file named `output.txt`.
- The user can then append additional text to the same file.
- Finally, the program reads and displays the entire content of `output.txt`.

### Code Explanation:
- The program first opens `output.txt` in write mode (`'w'`) to write the user's input.
- Then, it appends additional input to the file using append mode (`'a'`).
- The program finally opens the file in read mode (`'r'`) and displays the full content.

### How to Run:
1. Run `file_ops.py` in any Python environment.
2. Enter text when prompted to write and append to the file.
3. View the final content of `output.txt`.

### Example Output:
**When running the program:**

Enter text: Hello from Bharat Written. Append text: We like to contact with you Appended.
Content: Hello from Bharat We like to contact with you
