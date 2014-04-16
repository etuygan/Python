#list_to_file

def list_to_file(f):
    dosya = open("week1.txt", "w")
    for i in f:
        dosya.write(str(i) + "\n")

list_to_file([1,2,3])

#file_to_list

def file_to_list(x):
    l=[]
    for j in x:
        l = l + [j]
    return l 

print file_to_list(open("week1.txt", "r"))

#file_to_str

def file_to_str(y):
    string = ""
    for m in y:
        string = string + (m.split(" ")[0] + "\n")
    return string

print file_to_str(open("notlar.txt", "r"))


def list_to_folder(l1,l2):
    dosya = open("dosya.txt", "w")
    if len(l1) == len(l2):
        for i in range(len(l1)):
            dosya.write(str(l1[i]) + " " + str(l2[i]) + "\n")
    else:
        print "empty"


list_to_folder([1,2,3],[4,5,6])

def from_file_to_file(f1,f2):
    for i in f1:
        f2.write(str(i.split(" ")[1]) + "\n")       

print from_file_to_file(open("a.txt", "r"),open("b.txt", "w"))



