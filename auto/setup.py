def main():
    download_prereqs()
    make_noati()

"""
Runs sudo apt-get install make g++
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
    c1 = ["sudo", "touch", "/usr/include/stropts.h"] # There is some error that occurs (to do with C/C++) when this file is not there
    c2 = ["make", "noati"]
    p1 = subprocess.run(c1, text=True, cwd=directory)
    p2 = subprocess.run(c2, text=True, cwd=directory)
    return

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"The following exception has occured: \n{e}")
