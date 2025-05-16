with open("first_script.py", "r") as f:
    for line in f:
        print(line, end="")


with open("out.txt", "w") as f:
    f.write("hello world\n")
    f.write("test")
