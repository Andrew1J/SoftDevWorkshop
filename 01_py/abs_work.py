import random

f = open("names.txt", "r")
contents = f.read();

def main():
    lines = contents.splitlines()
    students = []

    for i in range(len(lines)):
        lines[i] = lines[i].split('\t')[1]
        if len(lines[i].split(' ')) > 1:
            students.append(lines[i].split(' ')[0] + " " + lines[i].split(' ')[1])

    rand_ind = random.randint(0,len(students)-1)
    print(students[rand_ind])

main()
