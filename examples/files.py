with open("imports.py", "r") as f:
    for line in f:
        if line.startswith("#"):
            continue
        print(line, end="")


with open("out.txt", "w") as f:
    f.write("test\n")
    f.writelines(["hello\n", "world\n"])
