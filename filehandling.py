text = "this is a sample text"

with open(r"C:\Users\Ankitha K\OneDrive\Documents\Besant-Data Analytics\Python\sample.txt", "w") as file:
    file.write(text) 
#first 'r' refers to the reference of the file path and 'w' is for write mode, which will create a new file or overwrite an existing file.

with open(r"C:\Users\Ankitha K\OneDrive\Documents\Besant-Data Analytics\Python\sample.txt", "a") as file:
    file.write("\nThis is an appended text")
#a is for append mode, which will add the new text to the already existing file without overwriting it.

with open(r"C:\Users\Ankitha K\OneDrive\Documents\Besant-Data Analytics\Python\sample.txt", "r") as file:
    print(file.read())
#r is for read mode, which will read the contents of the file.
#here no arguements are passed, a print statement is used to print the read contents
