import os

destination = ""
def remove(destination):
    for path, directory, file in os.walk(destination):
        for fileName in file:
            try:
                with open(path + "/" + fileName, "w") as f:
                    f.write("")
                print(path + "/" + fileName + " [status] : overwrote")
                os.remove(path + "/" + fileName)
                print(path + "/" + fileName + " [status] : removed")
            except:
                print("An unknown error occurred.")

def main():
    remove(destination)

if __name__ == "__main__":
    main()
