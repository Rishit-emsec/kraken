def main():
    download_prereqs()
    make_noati()

"""
Runs sudo apt-get install make and g++
"""
def download_prereqs():
    # Since file will be in the auto directory
    directory = os.getcwd()[0:-4]
    directory = "/home/rishit/kraken"
    print(directory)
    command1 = ["sudo", "apt-get", "install", "make"]
    command2 = ["sudo", "apt-get", "install", "g++"]
    process1 = subprocess.run(command1, text=True, cwd=directory)
    process2 = subprocess.run(command2, text=True, cwd=directory)
    return

"""
This function helps run the make noati function required to run kraken
"""
def make_noati():
    directory = os.getcwd()[0:-4]
    directory = "/home/rishit/kraken"
    print(directory)
    command = ["make", "noati"]
    process = subprocess.run(command,text=True, cwd=directory)
    return

if __name__ == "__main__":
    main()
