from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
from threading import Thread
from pathlib import Path
#from PIL import ImageTk, Image
#from multiprocessing import Process

import os, subprocess
import webbrowser
import time
import tkinter.font

 
root = Tk()
manul = Frame(root)
root.title('locust auto Runner')
file_path = ""
#testCase = ["-ddos","-password","-penen"]
local_host = "8089"

def executeFile():
    global file_path

    if(file_path==""):
        print("file not exist!")
    else:
        #file_dir = Path(file_path)
        os.chdir(Path(file_path).parent)
        result = subprocess.run(['locust', '-f',file_path], stdout=subprocess.PIPE, encoding="utf8")
    """
    #os.chdir("C:/Users/hansa/OneDrive/바탕 화면/gitTest/testScript")
    #여기에 스크립트 파일 있는 디렉토리 주소 입력, \가 아닌 / 으로 해야 한다.
    print("run script file")
    result = subprocess.run(['locust', '-f','test.py'], stdout=subprocess.PIPE, encoding="utf8")
    """
#디렉토리로 이동 후 파일 실행시키는 메서드
#명령어 및 옵션, 파일 이름은 변수로 대체하여 넣을 예정
    

def openURL():
    webbrowser.open("http://localhost:" + local_host)
    #foundURL = result.stdout.find("http")
#만약 UI모드로 실행 시 결과값에서 URL을 찾아 실행시키도록 함

def runBoth():
    if __name__ == "__main__":
        excuteTH = Thread(target=executeFile)
        openTH = Thread(target=openURL)
        
        excuteTH.start()
        time.sleep(2)
        openTH.start()

        excuteTH.join()
        openTH.join()
        #root.destroy()


def open():
    global file_path
    root.filename = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(
    ('python files', '*.py'), ('text files', '*.txt'), ('all files', '*.*')))
    #py파일을 파일탐색기에서 찾아 여는 명령어

    Label(manul, text=root.filename,background="#FFFFFF",highlightcolor="#43864E",highlightthickness=2).grid(row=2,column=2,columnspan=3) # 파일경로 라벨 표시

    file_path = root.filename
    #my_image = ImageTk.PhotoImage(Image.open(root.filename))
    #Label(image=my_image).pack() #사진 view
 
def runShellCommand():

    global file_path
    if(file_path == ""):
        print("no file exist!")
    else:
        os.system("echo Hi!")
        os.system("echo " + root.filename)

def runDDos():
    def ddos():
        result = subprocess.run(['locust', '-f',"ddos"], stdout=subprocess.PIPE, encoding="utf8")
    if __name__ == "__main__":
        print("run DDos Test")
        excuteTH = Thread(target=ddos)
        openTH = Thread(target=openURL)
        
        excuteTH.start()
        time.sleep(2)
        openTH.start()

        openTH.join()
        excuteTH.join()

        #root.destroy()

def runBasic():
    def basic():
        result = subprocess.run(['locust', '-f',"basic"], stdout=subprocess.PIPE, encoding="utf8")
    if __name__ == "__main__":
        print("run Basic Test")
        excuteTH = Thread(target=basic)
        openTH = Thread(target=openURL)
        
        excuteTH.start()
        time.sleep(2)
        openTH.start()

        excuteTH.join()
        openTH.join()

        #root.destroy()

def runPassword():
    def passwd():
        result = subprocess.run(['locust', '-f',"password"], stdout=subprocess.PIPE, encoding="utf8")
    if __name__ == "__main__" :
        print("run Password Test")
        excuteTH = Thread(target=passwd)
        openTH = Thread(target=openURL)
        
        excuteTH.start()
        time.sleep(2)
        openTH.start()

        excuteTH.join()
        openTH.join()
        #root.destroy()

root.configure(background="#43864E")
manul.configure(background="#43864E",highlightbackground="#BCEEC4", highlightthickness=2)
root.resizable(width = False, height= False)


dir_name = os.path.dirname(os.path.realpath(__file__))
basic = PhotoImage(file = dir_name + "/basic.png")
ddos = PhotoImage(file = dir_name + "/ddos.png")
pwd = PhotoImage(file = dir_name + "/pwd.png")
my_font = tkinter.font.Font(family="Arial", weight="bold",size=10)

#basic_image = Label(root, image=basic).grid(row=0, column=1)
#ddos_image = Label(root, image=ddos).grid(row=0, column=3)
#pwd_image = Label(root, image=pwd).grid(row=0, column=5)

run_basic = Button(root, image=basic,text='Basic Test',command=runBasic,width=80,background="#BCEEC4",relief="flat",highlightcolor="#BCEEC4",highlightthickness=2).grid(row=1, column=1)
run_ddos = Button(root, image=ddos, text='DDos Test',command=runDDos,width=80,background="#BCEEC4",relief="flat",highlightcolor="#BCEEC4",highlightthickness=2).grid(row=1, column=3)
run_pwd = Button(root, image=pwd, text='Password Test',command=runPassword,width=80,background="#BCEEC4",relief="flat",highlightcolor="#BCEEC4",highlightthickness=2).grid(row=1, column=5)
basic_image = Label(root, text='basic Test',font=my_font,background="#43864E",foreground="#BCEEC4").grid(row=2, column=1)
ddos_image = Label(root, text='ddos test',font=my_font,background="#43864E",foreground="#BCEEC4").grid(row=2, column=3)
pwd_image = Label(root, text='password test',font=my_font,background="#43864E",foreground="#BCEEC4").grid(row=2, column=5)
root.grid_columnconfigure(0,minsize=20)
root.grid_columnconfigure(2,minsize=20)
root.grid_columnconfigure(4,minsize=20)
root.grid_columnconfigure(6,minsize=20)
"""
manul_label = Label(root, text='수동 실행 모드',background="#43864E",foreground="#BCEEC4").grid(row=3, column=1,columnspan=1)
my_btn = Button(root, text='파일열기', command=open, width=10).grid(row=5, column=3)
test_btn3 = Button(root, text='파일 실행',command=runBoth, width=10).grid(row=5, column=5)
"""
manul_label = Label(root, text='manul mode',font=my_font,background="#43864E",foreground="#BCEEC4").grid(row=4, column=1,columnspan=5)
find_btn = Button(manul, text='open script',font=my_font, command=open, width=10,relief="flat",background="#BCEEC4",foreground="#43864E").grid(row=4, column=2)
run_btn = Button(manul, text='run script',font=my_font,command=runBoth, width=10,relief="flat",background="#BCEEC4",foreground="#43864E").grid(row=4, column=4)
manul.grid_columnconfigure(1,minsize=10)
manul.grid_columnconfigure(3,minsize=10)
manul.grid_columnconfigure(5,minsize=10)
manul.grid_rowconfigure(1,minsize=10)
manul.grid_rowconfigure(3,minsize=5)
manul.grid_rowconfigure(5,minsize=10)

manul.grid(row=5,column=1,columnspan=5,rowspan=1)
root.grid_rowconfigure(0,minsize=30)
root.grid_rowconfigure(3,minsize=30)
root.grid_rowconfigure(6,minsize=20)

root.mainloop()