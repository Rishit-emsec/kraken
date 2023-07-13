import os
import sys
import subprocess

def main():
    data = input_data()
    found = allocate_tables(data[0])
    kc_value = find_kc(found, data)

    if kc_value:
        print(f"Kc value found is: {kc_value}")
    else:
        print("No Kc value could be found, please recheck your inputs.")

def input_data():
    data = input("Enter target stream: "), input("Enter target frame: "), input("Enter guessed frame: "), input("Enter XOR-ed stream: ")
    return data

def allocate_tables(target_stream):

    kraken_dir = "/home/ubuntu/kraken/Kraken"

    print("Running kraken")
    c1 = ["sudo", "./kraken", "../indexes/"]
    t1 = subprocess.Popen(c1, stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True, 
            cwd=kraken_dir)
    
    t1.stdin.write(f"crack {target_stream}" + "\n" + "quit" + "\n")
    t1.stdin.flush()
    out, err = t1.communicate()
    found = ""
    for line in out.split("\n"):
        if "Found" in line:
            found = line
   
    if found == "":
        print("Kraken could not find the kc. Exiting program.")
        sys.exit()
    print(f"Kraken found this: {found}")
    return found.split()

def find_kc(found, data):
    util_dir = "/home/live/kraken/Utilities"
    c2 = ["./find_kc", found[1], found[3], data[1], data[2], data[3]]
    t2 = subprocess.run(c2, capture_output=True, text=True, cwd=util_dir)
    
    kc_val = ""
    for line in t2.stdout.split("\n"):
        if "MATCHED" in line:
            kc_val = line

    return kc_val


if __name__=="__main__":
    main()
