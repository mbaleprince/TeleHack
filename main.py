from Header import header
import argparse
import os
from colorama import init,Fore

init()
parser = argparse.ArgumentParser()
parser.add_argument('--start', type=int, required=True)
parser.add_argument('--stop', type=int, required=True)
args = parser.parse_args()
args1 = parser.parse_args()
start = args.start
stop = args.stop

print(Fore.RED + "[Info] " + Fore.GREEN + "Getting Ready...")
out = open("Tele-hack.txt", "w")
print(Fore.GREEN + "----------------------------------------------------------------------------------")
print(Fore.GREEN + "|  Name |\t\t| Telephone |\t\t\t| Status |")
print(Fore.GREEN + "----------------------------------------------------------------------------------")

while start < stop:
    out.write("077" + str(start) + "\n")
    print(Fore.GREEN +"MTN \t\t\t" + Fore.GREEN + "077" + str(start) + Fore.RED + "\t\t\t  Done!!!")
    out.write("078" + str(start) + "\n")
    print(Fore.GREEN +"MTN \t\t\t" + Fore.GREEN + "078" + str(start) + Fore.RED + "\t\t\t  Done!!!")
    out.write("076" + str(start) + "\n")
    print(Fore.GREEN +"MTN \t\t\t" + Fore.GREEN + "076" + str(start) + Fore.RED + "\t\t\t  Done!!!")
    out.write("075" + str(start) + "\n")
    print(Fore.GREEN +"Airtel \t\t\t" + Fore.GREEN + "075" + str(start) + Fore.RED + "\t\t\t  Done!!!")
    out.write("074" + str(start) + "\n")
    print(Fore.GREEN +"Airtel \t\t\t" + Fore.GREEN + "074" + str(start) + Fore.RED + "\t\t\t  Done!!!")
    out.write("070" + str(start) + "\n")
    print(Fore.GREEN +"Airtel \t\t\t" + Fore.GREEN + "070" + str(start) + Fore.RED + "\t\t\t  Done!!!")
    print(Fore.GREEN + "----------------------------------------------------------------------------------")
    start = start +1

print(Fore.RED + "[Info]" + Fore.GREEN + "Done!!!")

# This Piece Of Shit Was Coded By Mbale Prince
# For The Glory Of God
# Thanks