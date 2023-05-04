'''Antivirus Engine'''

import hashlib
import os

#Global Variable
malware_hashes = list(open("virusHash.unibit","r").read().split('\n'))
virusInfo = list(open("virusInfo.unibit","r").read().split('\n'))


#Get Hash Of File
def sha256_hash(filename):
    try:
        with open(filename,"rb") as f:
            bytes = f.read()
            sha256hash = hashlib.sha256(bytes).hexdigest()

            f.close()
        # print(sha256hash)
        return sha256hash
    except:
        return 0
    
#Malware Dectection By Hash
def malware_checker(pathOfFile):
    global malware_hashes
    global virusInfo
    
    hash_malware_check = sha256_hash(pathOfFile)
    counter = 0


    for i in malware_hashes:
        if i == hash_malware_check:
            return virusInfo[counter]
        counter += 1

    return 0


#Malware Dectection In Folder
virusName = []
virusPath = []

def virusScanner(path):

    # Get the list of all files in directory tree at given path
    dir_list = list()
    for (dirpath, dirnames, filenames) in os.walk(path):
        dir_list += [os.path.join(dirpath, file) for file in filenames]

    for i in dir_list:
        if malware_checker(i) != 0:
            print(i)
            virusName.append(malware_checker(i)+" :: File :: "+i)
            virusPath.append(i)


# Virus Remover
def virusRemover(path):
    virusScanner(path)
    if virusPath:
        for i in virusPath:
            os.remove(i)
    else:
        return 0
 


def juckFileRemover():

    # Temp Files Remover

    temp_list = list()

    # Windows username

    username = os.environ.get('USERNAME').upper().split(" ")

    for (dirpath, dirnames, filenames) in os.walk("C:\\Windows\\Temp"):
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath, file) for file in dirnames]

    for (dirpath, dirnames, filenames) in os.walk("C:\\Users\\{}~1\\AppData\\Local\\Temp".format(username[0])):
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath, file) for file in dirnames]
        

    for (dirpath, dirnames, filenames) in os.walk("C:\\Windows\\Prefetch"):
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath, file) for file in dirnames]


    if temp_list:
        
            for i in temp_list:
                print(i)

                try:
                    os.remove(i)

                except:
                    pass

                try:
                    os.rmdir(i)

                except:
                    pass
        
        

    else:
        return 0


def ramBooster():

    taskList = ["notepad.exe","AdobeUpdateService.exe","jenkins.exe","DropboxUpdate.exe","slack.exe",
                "Dropbox.exe","Creative Cloud.exe","TeamViewer_Service.exe","WhatsApp.exe", "cmd.exe",
                "msedge.exe","AutodeskDesktopApp.exe","GenuineService.exe","CCXProcess.exe","OneDrive",
                "SamsungDeX.exe","Update.exe","wps.exe","wpscenter.exe","Telegram.exe","CoreSync.exe","cmd.exe"]
                #"chrome.exe","brave.exe","explorer.exe"]

    # Task Kill

    for i in taskList:

            os.system("taskkill /f /im  {}".format(i))


