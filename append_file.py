'''
simple_programming_

This code opens a text file in append mode
and writes new content at the end of it  
''' 
with open("three_line_text_file.txt", "at") as f:
    f.write("\n") # Start new line 
    f.write("Fourth line")

with open("three_line_text_file.txt") as f:
    print(f.read())    

