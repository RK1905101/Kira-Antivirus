from tkinter import *
import tkinter
from tkinter import filedialog
import random
import os
import time
import engine
from tkinter import font  
 
#def HomeViewDarkTheme(event):

os.startfile("real-time-protection_setting.bat")

window = Tk()

window.title("Kira")
window.geometry('1100x600')
window.maxsize("1100","600")
window.minsize("1100","600")

def HomeViewDarkTheme(event):
    global winFrame
    winFrame.destroy()

winFrame = Frame(window, width=1100, height = 600, bg="#ffffff" )
winFrame.pack()
winFrame.pack_propagate(0)

def mainFramewinFrame():

    global opring
    global quickScanImg
    global junkFileRemoverImg
    global ramBoosterImg
    global photoScan
    global winFrame

    winFrame.destroy()

    winFrame = Frame(window, width=1100, height = 600, bg="#ffffff") #####color bg
    winFrame.pack()
    winFrame.pack_propagate(0)



    def junkFileRemoverFunc():
        ri = engine.juckFileRemover
        ri()

    def ramBoosterFunc():
        ri = engine.ramBooster
        ri()

    def customScanFunc():
        source_path = filedialog.askdirectory(title='Select the Parent Directory')
        print(source_path)
        ri = engine.virusScanner
        ri(source_path)

    def writeFile(write):
        switch_check = open("real-time_switch.blink","w")
        switch_check.write(write)
        switch_check.close()

    def AV_switch():
        switch_check = open("real-time_switch.blink","r")
        Pos = switch_check.readline()
        switch_check.close()    
    

        if Pos == 1 or Pos == "1" :
            print(Pos)
            writeFile("0")
        
            tls.configure(image = photog)
        
    
        elif Pos == 0 or Pos == "0":
            print(Pos)
            writeFile("1")
        
            tls.configure(image = photoi)

    opring = 5

    def buleAnimation_():
        global opring

        buleAnimationPlus00.configure(image = buleAnimationPlusList[opring], bg="#ffffff")


        if opring == 0:
            opring = 5

        opring -= 1

        buleAnimationPlus00.after(200,buleAnimation_)



    photoi = PhotoImage(file = "res\\new1.png").subsample(2,2)
    photog = PhotoImage(file = "res\\new2.png").subsample(2,2)
    photoScan = PhotoImage(file = "res\\ds.png").subsample(2,2)
    junkFileRemoverImg = PhotoImage( file = "res\\jk3.png").subsample(2,2)
    quickScanImg = PhotoImage(file ="res\\qs.png").subsample(2,2)
    ramBoosterImg = PhotoImage(file = "res\\rb.png").subsample(2,2)

    buleAnimationPlus0 = PhotoImage( file = "res\\blue ani\\0.png").subsample(21,21)
    buleAnimationPlus1 = PhotoImage( file = "res\\blue ani\\1.png").subsample(21,21)
    buleAnimationPlus2 = PhotoImage( file = "res\\blue ani\\2.png").subsample(21,21)
    buleAnimationPlus3 = PhotoImage( file = "res\\blue ani\\3.png").subsample(21,21)
    buleAnimationPlus4 = PhotoImage( file = "res\\blue ani\\4.png").subsample(21,21)
    buleAnimationPlus5 = PhotoImage( file = "res\\blue ani\\5.png").subsample(21,21)


    buleAnimationPlusList = [buleAnimationPlus0,buleAnimationPlus1,buleAnimationPlus2,buleAnimationPlus3,buleAnimationPlus4,buleAnimationPlus5]


    kiraMainLabel = Label(winFrame, text = "Kira", font = "Times 30 bold",bg="#ffffff")
    kiraMainLabel.pack(side = TOP, pady = 20)

    tls = Button(winFrame, text = 'Click Me !', image = photoi, bd=0, command=AV_switch, bg="#ffffff")
    tls.pack(side = TOP, pady = 0)

    quickScan = Button(winFrame, image = quickScanImg, bd = 0, command = quickScanFrame, bg="#ffffff")
    quickScan.place( x = 90 , y = 410)
    
    fscan = Button(winFrame, image = photoScan, bd = 0, command = customScanFunc, bg="#ffffff")
    fscan.place(x = 350 , y = 410)

    junkFileRemover = Button(winFrame, image = junkFileRemoverImg ,bd = 0, command = junkFileRemoverFunc, bg="#ffffff")
    junkFileRemover.place( x = 610 , y = 410)

    ramBooster = Button(winFrame, image = ramBoosterImg , bd = 0, command = ramBoosterFunc, bg="#ffffff")
    ramBooster.place( x = 870 , y = 410)

    buleAnimationPlus00 = Label(winFrame, image = buleAnimationPlus0, bg="#ffffff")
    buleAnimationPlus00.place(x = 50, y = 10)

    buleAnimation_()


def quickScanFrame():
    global winFrame
    global backButtonImg
    global prog0
    global prog1
    global prog2
    global prog3
    global prog4
    global prog5
    global io
    global ranHashShower
    global samB
    global rMVirus

    with open("virusHash.unibit", "r") as nr:
        samB = nr.readlines()
        nr.close()



    winFrame.destroy()

    winFrame = Frame(window, width=1100, height = 600, bg="#ffffff")
    winFrame.pack()
    winFrame.pack_propagate(0)

    io = 0

    def removeVirusBtn():
        try : 
            with open("switch_virusscanner.bb","r") as bb:
                io = list(bb.readlines())
                bb.close()
        except:pass

        try:
            for i in io:
                i = i[0:len(i)-1]
                print(i," Removed")
                os.remove(i)
        except:pass


    def progressBarAni():
        global io
        
        progLabel.configure(image = progList[io])

        io += 1

        

        id = progLabel.after(500, progressBarAni)

        if io == 5:
            io = 0
            try : 
                with open("switch_io.bb","r") as nri:
                    xxc = nri.read()
                    nri.close()
                
                if xxc == "1" or xxc == 1:
                    progLabel.after_cancel(id)
            
            except:pass

    def textShower():
        global samB

        ranHashShower.configure(state='normal')
        ranHashShower.delete("1.0",END)
        ranHashShower.insert(INSERT,samB[random.randint(0,len(samB)-1)])

        id = ranHashShower.after(100, textShower)

        try : 
            with open("switch_io.bb","r") as nri:
                xxc = nri.read()
                nri.close()
                
            if xxc == "1" or xxc == 1:
                ranHashShower.after_cancel(id)
            
        except:pass

    def VirusFoundPathX():

        try:
            with open ("switch_virusscanner.bb","r") as X:
                cc = X.readlines()
                X.close()
        

            virusFoundPaths.configure(state='normal')
            virusFoundPaths.delete("1.0",END)
            virusFoundPaths.insert(INSERT,cc)


        except:pass

        id = virusFoundPaths.after(200, VirusFoundPathX)

    backButtonImg = PhotoImage(file = "res\\back button.png").subsample(4,4)
    prog0 = PhotoImage( file = "res\\progress bar\\0.png").subsample(1,3)
    prog1 = PhotoImage( file = "res\\progress bar\\1.png").subsample(1,3)
    prog2 = PhotoImage( file = "res\\progress bar\\2.png").subsample(1,3)
    prog3 = PhotoImage( file = "res\\progress bar\\3.png").subsample(1,3)
    prog4 = PhotoImage( file = "res\\progress bar\\4.png").subsample(1,3)
    prog5 = PhotoImage( file = "res\\progress bar\\5.png").subsample(1,3)
    progList = [prog0,prog1,prog2,prog3,prog4,prog5]

    kiraMainLabel = Label(winFrame, text = "Quick Scan", font = "Times 21 bold", bg="#ffffff")
    kiraMainLabel.pack(side = TOP, pady = 20)

    backButton = Button(winFrame, image = backButtonImg, bd = 0, command = mainFramewinFrame, bg="#ffffff")
    backButton.place(x = 10 , y = 10)

    progLabel = Label(winFrame, image = prog0, bg="#ffffff")
    progLabel.place(x = 250, y = 70)


    pathLabel = Label(winFrame, text = "Virus Scanner",font = "Times 20 bold",bg="#ffffff")
    pathLabel.place(x = 350, y = 130)

    ranHashShower = Text(winFrame, width=50, height=1, bd = 0, font= ('Sans Serif', 13, 'bold'),foreground="green")
    ranHashShower.place( x = 350 , y = 170)
    ranHashShower.insert(INSERT, "Write Something About Yourself")
    ranHashShower.configure(state='disabled')

    virusDetet = Label(winFrame, text = "Virus Found", font = "Times 20 bold")
    virusDetet.place(x = 350, y = 230)

    virusFoundPaths = Text(winFrame, width=100, height=10, bd = 0, font= ('Sans Serif', 13, 'bold'),foreground="red", bg="#e9e9e9")
    virusFoundPaths.place( x = 50 , y = 290)
    virusFoundPaths.insert(INSERT, "No Virus Found")
    virusFoundPaths.configure(state='disabled')

    rMVirus = Button(winFrame, text = "Remove Virus", font = "Times 20 bold", command = removeVirusBtn, bg="#e9e9e9")
    rMVirus.place(x = 350, y = 230)

    textShower()

    progressBarAni()

    os.startfile("scannerStartQuick.bat")

    VirusFoundPathX()


    # Get the list of all files in directory tree at given path

        




mainFramewinFrame()





window.mainloop()