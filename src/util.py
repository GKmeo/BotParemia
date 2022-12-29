
def readtoken():
    with open("token.txt", "r") as f:
        return f.readline().strip("\n")
