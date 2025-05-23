def grep(text, file):
    lines_matching = []
    with open(file) as f:
        for line in f:
            if text in line:
                lines_matching.append(line)
    return lines_matching


if __name__ == "__main__":
    with open("imports.py", "r") as f:
        for line in f:
            if line.startswith("#"):
                continue
            print(line, end="")

    with open("out.txt", "w") as f:
        f.write("test\n")
        f.writelines(["hello\n", "world\n"])
