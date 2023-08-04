import os
import sys
import time
import subprocess

def main():
    # data = input_data()
    data = ["100000110100111111001110010101110101011111111010111011101101100000001001101101100001111000111010000110110001110000", "1152173", "1152140", "111111010101101110100001101011111100000000111101011000011111101001100100111101100001100111000110011000010000000010"]
    found = allocate_tables(data[0])
    while not found:
        data = input_data()
        found = allocate_tables(data[0])
   
    print(f"Found values: {found}")
    kc_value = find_kc(found, data)

    # Reformat the kc_value
    kc_value = kc_value.split()[1:-3]
    kc_value = "".join(kc_value)
    kc_value = kc_value.upper()
    print(f"We can return this output: {kc_value}")

def input_data():
    data = input("Enter target stream: "), input("Enter target frame: "), input("Enter guessed frame: "), input("Enter XOR-ed stream: ")
    bitstream1 = input("Enter unencrypted bitstream: ")
    bitstream2 = input("Enter encrypted bitstream: ")
    
    # util_dir = "/home/rishit/kraken/Utilities"
    util_dir = str(os.getcwd()[0:-4]) + "Utilities"
    print(util_dir)
    xor_command = ["./xor.py", bitstream1, bitstream2] 
    xor_proc = subprocess.run(c2, capture_output=True, text=True, cwd=util_dir)
    return data

def allocate_tables(target_stream):

    # kraken_dir = "/home/ubuntu/kraken/Kraken"
    kraken_dir = str(os.getcwd()[0:-4]) + "Kraken"
    print(kraken_dir)
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

    return found.split()

def find_kc(found, data):
    # util_dir = "/home/rishit/kraken/Utilities"
    util_dir = str(os.getcwd()[0:-4]) + "Utilities"
    print(util_dir)
    c2 = ["./find_kc", found[1], found[3], data[1], data[2], data[3]]
    t2 = subprocess.run(c2, capture_output=True, text=True, cwd=util_dir)

    kc_val = ""
    for line in t2.stdout.split("\n"):
        if "MATCHED" in line:
            kc_val = line

    if kc_val:
        print(f"Kc value found is: {kc_val}")
    else:
        print("No Kc value could be found, please recheck your inputs.")
        return None

    return kc_val


if __name__ == "__main__":
    try:
        start_time = time.time()
        main()
        print(time.time() - start_time)

    except KeyboardInterrupt:
        print("\nExiting after keyboard interruption")
        sys.exit()
