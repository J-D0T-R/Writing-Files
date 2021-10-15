###   Writing Files   ###
###   James Rutley   ###
###   Start date: 10/15/2021   ###
###   End date:


# Functions
def writing_to():
    #opens a text file in writing mode
    file = open('my_txt_file.txt', 'w')
    #gives visual confirmation that the code is working
    print("File opened for writing.")
    #Writes to the file
    file.write("Hello World!\n")
    file.write("I'm editing a file with code!\n")
    file.close()
    print("File closed.")
    
def append():
    file = open('my_txt_file.txt', 'a')
    print("File opened for appending.")
    file.write("\nI just appended my file!")
    file.close()
    print("File closed.")
    
    

def main():
    writing_to()
    append()
 
 
# Main Code
main()