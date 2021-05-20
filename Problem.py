print ("pie")
print("Jen is a boss")
#jen is distracted 
#write a file that takes in a file name via user input and prints out an the words in alphabetical order but only one instance of each word.
def my_function():
    """This is a DOCSTRING"""
    x=input()
    print (x)
    f = open(x, "r")
    b= (f.read().split(" "))
    d=sorted(list(set(b)))

    for i in d:
        print (i)
    #print(g)

if __name__ == "__main__":
    #my_function()
    assert(==b.sorted)
