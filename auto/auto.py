import os
import sys
import time
import subprocess
from collections import Counter

def main():
    # data = ["100000110100111111001110010101110101011111111010111011101101100000001001101101100001111000111010000110110001110000", "1152173", "1152140", "111111010101101110100001101011111100000000111101011000011111101001100100111101100001100111000110011000010000000010"]
    bitstream1 = str(input('Enter keystream to crack: '))
    frame1 = str(input('Enter frame 1: '))
    frame2 = str(input('Enter frame 2: '))
    bitstream2 = str(input('Enter keystream: '))
    data = [bitstream1, frame1, frame2, bitstream2]
    
    '''
    datas = input_data()
    for data in datas:
        found = allocate_tables(data[0])
        if found:
            break
    if not found:
        print("Not able to find match in rainbow table")
        sys.exit()
    '''
    found = allocate_tables(data[0])
    print(f"Found values: {found}")
    kc_value = find_kc(found, data)

    # Reformat the kc_value
    kc_value = kc_value.split()[1:-3]
    kc_value = "".join(kc_value)
    kc_value = kc_value.upper()
    print(f"We can return this output: {kc_value}")

'''
@params: Absolute path of the burst.txt file
@return: List of XOR-ed bitstreams to try with Kraken and their
corresponding modified frame number from the first and second encrypted burst
'''
'''
def input_data():
    target = list()
    guess = list()
    
    with open("burst.txt") as burst:
        burstArr = burst.readlines()
        # Simply get an unencrypted burst from the front of the file
        for i in range(0, len(burstArr) - 12):
            freq = Counter("".join(burstArr[i:i+12]).split())
            if freq["C0"] == 3 and freq["C1"] == 1 and freq["P0"] == 3 and freq["P1"] == 1 and freq["S0"] == 3 and freq["S1"] == 1:
                target = burstArr[i:i+12]
        # Get an encrypted burst from the back of the file
        burstArr = burstArr[::-1] 
        for i in range(0, len(burstArr) - 12):
            freq = Counter("".join(burstArr[i:i+12]).split())
            if freq["C0"] == 3 and freq["C1"] == 1 and freq["P0"] == 3 and freq["P1"] == 1 and freq["S0"] == 3 and freq["S1"] == 1:
                guess = burstArr[i:i+12][::-1]

    if not target or not guess:
        print("Unable to find appropriate data to find the kc value")
        return

    # Look at the whole block with the frame number, 
    # and take only the four lines that start with "Cx"
    target = list(filter(lambda line:"C1" or "C0" in line, target))
    target = list(map(lambda s:s.split(), target))
    # burst1, burst2, burst3, burst4 = target
    
    guess = list(filter(lambda line:"C1" or "C0" in line, guess))
    guess = list(map(lambda s:s.split(), guess))
    # c1, c02, c03, c04 = guess

    testing_bitstreams = list()
    for unencrypted, encrypted in target, guess:
        # util_dir = "/home/rishit/kraken/Utilities"
        util_dir = str(os.getcwd()[0:-4]) + "Utilities"
        print(util_dir)
        print(f"XOR-ing {encrypted[3]} and {unencrypted[3]}")
        xor_command = ["./xor.py", unencrypted[3], encrypted[3]] 
        xor_proc = subprocess.run(c2, capture_output=True, text=True, cwd=util_dir)
        testing_bitstreams.append(str(xor_proc.stdout))
    
    print(testing_bitstreams)
    datas = [[testing_bitstreams[0], guess[0][2][0:-1], guess[-1][2][0:-1], testing_bitstreamsp[-1]], [testing_bitstreams[1], guess[1][2][0:-1], guess[0][2][0:-1], testing_bitstreamsp[0]], [testing_bitstreams[2], guess[2][2][0:-1], guess[1][2][0:-1], testing_bitstreamsp[1]], [testing_bitstreams[3], guess[3][2][0:-1], guess[2][2][0:-1], testing_bitstreamsp[2]] 

    return datas
'''

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
