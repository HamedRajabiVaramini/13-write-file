'''
simple_programming_

This code opens a text file in write mode
and overwrite old content with new one   
''' 
with open("existing_text_file.txt", "wt") as f:
    f.write("New first line")
    f.write("\n") # Start new line
    f.write("New second line") 

with open("existing_text_file.txt") as f:
    print(f.read())    

