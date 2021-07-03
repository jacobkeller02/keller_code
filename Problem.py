# write a file that takes in a file name via user input and prints out an the words in alphabetical order but only one instance of each word.


def read_in()->str:
    """Take in a file and return the contents as one long string"""
    print("Please input a file name: ")
    user_in=input()
    open_file = open(user_in, "r")
    contents=open_file.read()
    open_file.close()
    return contents


def sort_file(jen: str) -> list:
    """Splits a string and sorts it into a list with no duplicates"""
    white_space= (jen.split(" "))
    sorted_list=sorted(list(set(white_space)))  # Puts B into a set to remove duplicates and then makes it a list and sorts it
    return sorted_list


if __name__ == "__main__":
    file_contents= read_in()
   
    for word in sort_file(file_contents):
        print (word)
    
