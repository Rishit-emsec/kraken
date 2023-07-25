# Kraken A5/1 Cracking Project

## Aim 
To fully automate the process of finding the kc to crack a5/1 encryption

## Tech stack
- Python
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
4. Step 3 should take quite long
5. Check md5 hash of all *.dlt files in your hard drive with command (md5 *.md5 OR md5sum *.md5)
6. Match hashes with: https://jenda.hrach.eu/f2/tables.txt
7. If hashes do not match, please re-download that specific file (and not all of them)
### Kraken
8. Clone this repository to your local computer (Linux or download DragonOS and either dual-boot or use a VM)
9. Run `make noati` in the kraken directory
10. If in step 9 you get an error where you do not have stropts.h file, then run, `sudo touch /usr/include/stropts.h` and then repeat step 9
11. Next, `cd a5_cpu` and run `./a5cpu_test`
12. Check that the chains are made properly in steps 10 and 11
### Index rainbow tables
13. `cd indexes`
14. Run `sudo parted -l` to check where your hard drive with indexed rainbow tables is located. Note: you should not be able to see this hard drive in your file manager, as it would seem corrupted to your computer
15. Depending on step 14, replace the current location into the second line of your tables.conf file.
16. e.g: /dev/sdb, should be put into your tables.conf file
### Entering Kraken
18. `cd Kraken`
19. Run sudo `sudo ./kraken ../indexes`
20. This should allow you to access the Kraken server. Note: it should take some time for the tables to be allocated properly
21. Note that if allocation of rainbow tables is not done properly, one of your .idx files may be corrupt, you can reindex that particular file
### Automated version
- Complete till step 16 and run `python3 auto.py`
- Then give inputs asked for
- Refer to this video: https://www.youtube.com/watch?v=1KTSQOQWPsU&t=925s

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
