# Kraken A5/1 Cracking Project

## Aim 
To fully automate the process of finding the kc to crack a5/1 encryption.
To learn more about GSM check out this paper: https://academicworks.cuny.edu/cgi/viewcontent.cgi?article=1872&context=cc_etds_theses

## Tech stack
- Python3
- C/C++

## Steps to obtain rainbow tables (.dlt)
### Items required:
- Two 2 terabyte hard disks. One is to store rainbow tables and another hard drive to store rainbow tables in their raw format.
- A laptop
- Linux system
### Steps to download
1. Go to this website: https://opensource.srlabs.de/projects/a51-decrypt/files
2. Download all the *.torrent files OR download the one *.tgz file
3. Use a BitTorrent client for step 2 OR you can attempt to find the google drive link to download the rainbow tables
4. Step 3 should take quite long. (or not if your internet connection is really good)
5. Check md5 hash of all *.dlt files in your hard drive with command (md5 *.md5 OR md5sum *.md5) 
6. Match hashes with: https://jenda.hrach.eu/f2/tables.txt 
7. If hashes do not match, please re-download that specific file (and not all of them) 
### Kraken
8. Clone this repository to your local computer (OS should be Ubuntu/Linux/DragonOS and either dual-boot or use a VM)
9. Run `make noati` in the kraken directory (might have some warnings can usually ignore them)
10. If in step 9 you get an error where you do not have stropts.h file, then run, `sudo touch /usr/include/stropts.h` and then repeat step 9
11. Next, `cd a5_cpu` and run `./a5cpu_test`
12. Check that the chains are made properly in steps 10 and 11
### Index rainbow tables
13. `cd ..` + `cd indexes` (goto kraken/indexes)
14. Run `sudo parted -l` to check where your hard drive with indexed rainbow tables is located. Note: you should not be able to see this hard drive in your file manager, as it would seem corrupted to your computer
15. Depending on step 14, replace the current location into the second line of your tables.conf file.
16. e.g: /dev/sdb, should be put into your tables.conf file. Make it one line if you want to index all 40 tables into one hard drive
17. Then run sudo python2 Behemoth.py /home/media/name_of_harddrive_with_.dltrainbowtables
18. check the md5 checksum of *.idx files formed
19. simply reindex the files that have the wrong checksum, or you could repeat the whole process and hope for the best
### Entering Kraken
18. `cd Kraken`
19. Run sudo `sudo ./kraken ../indexes`
20. This should allow you to access the Kraken server. Note: it should take some time for the tables to be allocated properly
21. Note that if allocation of rainbow tables is not done properly, one of your .idx files may be corrupt, you can reindex that particular file
### Automated version
- Run setup.py in "kraken/auto/"
- Index rainbow tables (from step 13 onwards)
- Run auto.py in "kraken/auto/"
- Enter inputs required
- Refer to this video for inputs required: https://www.youtube.com/watch?v=1KTSQOQWPsU&t=925s

## Theoretical aspect
### A5/1 encryption
- a **sycnhronous**, **stream** **cipher** used in GSM networks
- used to encrypt both **********voice********** and ******************************signalling data******************************
- A5/2 is ***********delibrately*********** weaker version, A5/3 is stronger version
- GSM transmission
    - organised as a series of bursts
    - one burst every 4.615 milliseconds
    - one burst contains 114 bits of information
- A5/1 encryption is used to produce 114 bit sequence of keystream which is XORed with 114 bits prior to modulation
- A5/1 is initialised using a 64-bit [key](https://en.wikipedia.org/wiki/Key_(cryptography)) together with a publicly known 22-bit frame number
    - older generations had 10 bits fixed at 0 resulting in a key length of 54, which is weaker than 64. this was eventually fixed
- A5/1 is based on a combination of three linear feedback shift registers with irregular clocking
- a LFSR is just a stream of bits and we have rules for how to move these bits about
- A5/1 has three LFSRs
    - The total number of bits in these LFSRs is 19+22+23=64.

### A5/1 Keystream Generation
- all three registers are set to 0
- for 64 cycles, key bits are fed into the LFSRs (without majority function)
- for 22 additional cycles, a 22-bit frame number is fed to the LFSRs (without majority function)
- 100 additional clocks with majority function are performed to obtain the initial state
    - majority function?
    - there are 3 LFSRs. so we look at a specific position in each LFSR. the LFSR with the majority bit (two 1s and one 0, which means 1 is a majority bit) is clocked (shift occurs)
- 228 clocks are performed to produce 228 bits of keystream (which is XORed with the plaintext)
- after XOR with the plaintext the ciphertext is obtained

### A5/1 Decryption: TMTO attack
- store the plaintext -> hashed value
- use rainbow tables to crack
- for more in-depth explanation check online

### Important links and videos to watch
- https://www.youtube.com/watch?v=8MWzFyE4k8s&t=702s
- https://www.youtube.com/watch?v=1KTSQOQWPsU
- Crazy danish hacker videos on Kraken
