import os

destination = ""

print("Destination is set.")
print(f"Path: {destination}")

def remove(destination):
    for path, directory, file in os.walk(destination):
        for fileName in file:
            try:
                with open(path + "/" + fileName, "w") as f:
                    f.write("")
                print(path + "/" + fileName + " [status] : overwrote")
                os.remove(path + "/" + fileName)
                print(path + "/" + fileName + " [status] : removed")
            except Exception as e:
                print(e)

def main():
    isCorrect = input("Is it correct? [y/n] ")
    if (isCorrect == "y"):
        remove(destination)
        print("Done.")

if __name__ == "__main__":
    main()
