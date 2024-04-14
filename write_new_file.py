'''
simple_programming_

This code makes new text file and opens it 
in write mode to write new content   
''' 
with open("new_text_file.txt", "wt") as f:
    f.write("First line")
    f.write("\n") # Start new line
    f.write("Second line") 

with open("new_text_file.txt") as f:
    print(f.read())    

