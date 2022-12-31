import wx
import wx.adv
import os
import wx.stc as stc
import pyautogui
import tree
import speech_recognition as sr
import pyttsx3

from gtts import gTTS

global name
name = 0
global fileloc
fileloc = 0


screen_width, screen_height = pyautogui.size()
ls = []
ls1 = []
global flag
flag = False
lista = ['public static void main{}', 'actions', 'static', 'void', 'main', 'protected', "#include<stdio.h>", "#include<conio.h>", "if(condition){}",
         "#include<string.h>", "#include<stdlib.h>", "#include<math.h>", "#include<time.h>", "#include<ctype.h>", "#include<stdarg.h>",
         "#include<signal.h>", "#include<setjmp.h>", "#include<locale.h>", "#include<errno.h>", 'assert', "#include<assert.h>", "printf("")",
         "scanf("")", "getchar()", "putchar()", "fopen()", "fclose()", "if(condition){}", 'while(condition){}''for(condition){}', 'do()',
         'do{}while(condition);', "printf("")", "scanf("")", "getchar()", "putchar()", "putchar()", "fopen()", "fopen()", "fclose()", "fclose()", "clrscr()",
         "getch()", "getch()", 'while(Condition){Statement(s)Increment/Decrement;}', 'for(initialization; condition; incOrDec){ }',
         'import java.io.*;', 'import java.util.*;', 'import java.awt.*;', 'import java.net.*;', 'import java.awt.event;', 'import java.lang.*;',
         'import java.applet.*;', 'import javax.swing.*;', 'import javax.swing.event;,Label()', 'Label l = new Label("");', 'return 0', 'Button b = new Button("");\n', 'Choice c = new Choice();', 'TextField t = new TextField("");', 'TextArea();', 'Checkbox obj = new Checkbox();\n',
         'Checkbox obj = new Checkbox(String label, boolean state, CheckboxGroup obj);', 'cin>>my_value;', 'cout<<statement;', 'List s = new List();\n',
         'MenuBar mb = new MenuBar();\n', 'Menu m = new Menu("");\n', 'MenuItem mi = new MenuItem("");\n', 'JLabel obj = new JLabel("");\n',
         'JButton b = new JButton("");\n', 'JTextField t = new JTextField("");\n', 'JTextArea t = new JTextArea("");\n',
         'JComboBox C = new JComboBox();\n', 'JCheckBox c = new JCheckBox("1");\n', 'JTree jt=new JTree(DefaultMutableTreeNodeObjectName);\n', 'JPasswordField p = new JPasswordField();\n'
         'JMenuBar mb = new JMenuBar();\n', 'JMenu m = new JMenu("");\n', 'JMenuItem mi = new JMenuItem("");\n', 'int main(){}', "__"
         ]


class Editor(wx.Frame):
    lineNumbersEnabled = True

    def __init__(self, parent, title):
        self.leftMarginWidth = 25

        wx.Frame.__init__(self, parent, title=title,
                          size=(screen_width, screen_height))

        self.CreateStatusBar()
        self.StatusBar.SetBackgroundColour((220, 220, 220))

        panel1 = wx.Panel(self)
        self.control = stc.StyledTextCtrl(
            panel1, style=wx.TE_MULTILINE | wx.TE_WORDWRAP)
        self.control1 = stc.StyledTextCtrl(
            panel1, style=wx.TE_MULTILINE | wx.TE_WORDWRAP)

        self.control.CmdKeyAssign(
            ord("+"), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMIN)
        self.control.CmdKeyAssign(
            ord("-"), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMOUT)

        self.control.SetViewWhiteSpace(False)
        self.control.SetMargins(5, 0)
        self.control.SetMarginType(1, stc.STC_MARGIN_NUMBER)
        self.control.SetMarginWidth(1, self.leftMarginWidth)

        self.control.Bind(stc.EVT_STC_CHANGE, self.sug)
        self.control.Bind(wx.EVT_KEY_UP, self.dell)
        self.control1.Bind(wx.EVT_LEFT_DCLICK, self.copy)
        self.control1.SetReadOnly(True)
        self.tree1 = tree.Tree(panel1, wx.TR_HIDE_ROOT)
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(self.tree1, 1, wx.EXPAND, 20)
        box.Add(self.control, 4, wx.EXPAND, 20)
        box.Add(self.control1, 2, wx.EXPAND, 20)
        panel1.SetSizer(box)
        panel1.Fit()

        filemenu = wx.Menu()
        menuNew = wx.MenuItem(filemenu, wx.ID_NEW,
                              '&New\tCtrl+N', kind=wx.ITEM_NORMAL)
        menuNew.SetBitmap(wx.Bitmap('Resources/newfile.png'))
        filemenu.Append(menuNew)

        menuOpen = wx.MenuItem(filemenu, wx.ID_OPEN,
                               '&Open\tCtrl+O', "Open an Existing Document")
        menuOpen.SetBitmap(wx.Bitmap('Resources/openfile.png'))
        filemenu.Append(menuOpen)

        menuSave = wx.MenuItem(filemenu, wx.ID_SAVE,
                               '&Save\tCtrl+S', "Save the Current Document")
        menuSave.SetBitmap(wx.Bitmap('Resources/save.png'))
        filemenu.Append(menuSave)

        menuSaveAs = wx.MenuItem(
            filemenu, wx.ID_SAVEAS, '&Save As\tCtrl+Shift+S', "Save the New Document")
        menuSaveAs.SetBitmap(wx.Bitmap('Resources/saveas.png'))
        filemenu.Append(menuSaveAs)

        filemenu.AppendSeparator()
        menuClose = wx.MenuItem(filemenu, wx.ID_EXIT,
                                '&Exit\tCtrl+Alt+X', "Close the Application")
        menuClose.SetBitmap(wx.Bitmap('Resources/exit.png'))
        filemenu.Append(menuClose)

        editmenu = wx.Menu()
        menuUndo = wx.MenuItem(editmenu, wx.ID_UNDO,
                               "&Undo\tCtrl+Z", "Undo Last Action")
        menuUndo.SetBitmap(wx.Bitmap('Resources/undo.png'))
        editmenu.Append(menuUndo)
        menuRedo = wx.MenuItem(editmenu, wx.ID_REDO,
                               "&Redo\tCtrl+R", "Redo Last Action")
        menuRedo.SetBitmap(wx.Bitmap('Resources/redo.png'))
        editmenu.Append(menuRedo)
        editmenu.AppendSeparator()
        menuCut = wx.MenuItem(editmenu, wx.ID_CUT,
                              '&Cut\tCtrl+X', "Cut Selected Text")
        menuCut.SetBitmap(wx.Bitmap('Resources/cut.png'))
        editmenu.Append(menuCut)
        menuCopy = wx.MenuItem(editmenu, wx.ID_COPY,
                               "&Copy\tCtrl+C", "Copy Selected Text")
        menuCopy.SetBitmap(wx.Bitmap('Resources/copy.png'))
        editmenu.Append(menuCopy)
        menuPaste = wx.MenuItem(
            editmenu, wx.ID_PASTE, "&Paste\tCtrl+V", "Paste the Text from Clipboard")
        menuPaste.SetBitmap(wx.Bitmap('Resources/paste.png'))
        editmenu.Append(menuPaste)
        formatmenu = wx.Menu()
        menuFont = wx.MenuItem(formatmenu, wx.ID_ANY,
                               "&Font\tCtrl+F", "Change the Font Settings")
        menuFont.SetBitmap(wx.Bitmap('Resources/font.png'))
        formatmenu.Append(menuFont)

        runmenu = wx.Menu()
        menuRunJava = wx.MenuItem(
            runmenu, wx.ID_ANY, "&Run Java Program\tShift+J", "Run Java Program")
        menuRunJava.SetBitmap(wx.Bitmap('Resources/jar.png'))
        runmenu.Append(menuRunJava)
        menuRunC = wx.MenuItem(
            runmenu, wx.ID_ANY, "&Run C Program\tShift+C", "Run C Program")
        menuRunC.SetBitmap(wx.Bitmap('Resources/class.png'))
        runmenu.Append(menuRunC)

        prefmenu = wx.Menu()
        menulinenumbers = wx.MenuItem(
            prefmenu, wx.ID_ANY, "&Toggle Line Numbers", "Show/Hide Line Numbers Column")
        menulinenumbers.SetBitmap(wx.Bitmap('Resources/options.png'))
        prefmenu.Append(menulinenumbers)

        helpmenu = wx.Menu()
        menuhowto = wx.MenuItem(
            helpmenu, wx.ID_ANY, "&How To..\tCtrl+H", "Get Help Using the Editor")
        menuhowto.SetBitmap(wx.Bitmap('Resources/how.png'))
        helpmenu.Append(menuhowto)
        menuabout = wx.MenuItem(
            helpmenu, wx.ID_ABOUT, "&About\tShift+A", "Read About Editor and its Making")
        menuabout.SetBitmap(wx.Bitmap('Resources/about.png'))
        helpmenu.Append(menuabout)

        voicemenu = wx.Menu()
        menuvaish = wx.MenuItem(voicemenu, wx.ID_ANY,
                                "&Female\tCtrl+Shift+F", "Voice")
        menuvaish.SetBitmap(wx.Bitmap('Resources/female.png'))
        voicemenu.Append(menuvaish)
        menuvaish2 = wx.MenuItem(voicemenu, wx.ID_ANY,
                                 "&Male\tCtrl+Shift+M", "voice")
        menuvaish2.SetBitmap(wx.Bitmap('Resources/male.png'))
        voicemenu.Append(menuvaish2)

        menubar = wx.MenuBar()
        menubar.Append(filemenu, '&File')
        menubar.Append(editmenu, '&Edit')
        menubar.Append(prefmenu, '&Preferences')
        menubar.Append(formatmenu, '&Format')
        menubar.Append(runmenu, '&Run')
        menubar.Append(voicemenu, '&Voice')
        menubar.Append(helpmenu, '&Help')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.newproj, menuNew)
        self.Bind(wx.EVT_MENU, self.open1, menuOpen)
        self.Bind(wx.EVT_MENU, self.save_as, menuSaveAs)
        self.Bind(wx.EVT_MENU, self.save, menuSave)
        self.Bind(wx.EVT_MENU, self.OnUndo, menuUndo)
        self.Bind(wx.EVT_MENU, self.OnRedo, menuRedo)
        self.Bind(wx.EVT_MENU, self.OnCut, menuCut)
        self.Bind(wx.EVT_MENU, self.OnCopy, menuCopy)
        self.Bind(wx.EVT_MENU, self.OnPaste, menuPaste)
        self.Bind(wx.EVT_MENU, self.run, menuRunJava)
        self.Bind(wx.EVT_MENU, self.runc, menuRunC)
        self.Bind(wx.EVT_MENU, self.howto, menuhowto)
        self.Bind(wx.EVT_MENU, self.OnToggleLineNumbers, menulinenumbers)
        self.Bind(wx.EVT_MENU, self.Fontbox, menuFont)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.select)
        self.Bind(wx.EVT_MENU, self.tts, menuvaish)
        self.Bind(wx.EVT_MENU, self.SpeechDef, menuvaish2)
        self.control.Bind(wx.EVT_KEY_UP, self.UpdateLineCol)
        self.control.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuabout)
        toolbar1 = wx.ToolBar(self, -1)
        self.ToolBar = toolbar1
        t1 = toolbar1.AddTool(
            wx.ID_ANY, '', wx.Bitmap('Resources/newfile.png'))
        t2 = toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('Resources/cut.png'))
        t3 = toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('Resources/copy.png'))
        t4 = toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('Resources/paste.png'))
        t5 = toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('Resources/undo.png'))
        t6 = toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('Resources/redo.png'))
        toolbar1.Realize()
        # End of Toolbar
        self.Bind(wx.EVT_MENU, self.newproj, t1)
        self.Bind(wx.EVT_MENU, self.OnCut, t2)
        self.Bind(wx.EVT_MENU, self.OnCopy, t3)
        self.Bind(wx.EVT_MENU, self.OnPaste, t4)
        self.Bind(wx.EVT_MENU, self.OnUndo, t5)
        self.Bind(wx.EVT_MENU, self.OnRedo, t6)
        self.Show()

    def sug(event, e):
        event.control1.SetReadOnly(False)
        global flag
        global text
        aa = float(event.control.GetCurrentPos())
        if aa > 0.0:
            a = str(event.control.GetRange(float(int(aa - 1.0)),
                    float(event.control.LastPosition)))

        else:
            a = str(event.control.GetRange(float(int(aa - 0.1)),
                    float(event.control.LastPosition)))

        event.control1.DeleteRange(0.0, float(event.control1.LastPosition))
        if a.__contains__(" "):
            if aa > 0.0:
                a = str(event.control.GetRange(float(int(aa - 1.0)),
                        float(event.control.LastPosition)))
            else:
                a = str(event.control.GetRange(float(int(aa - 0.1)),
                        float(event.control.LastPosition)))
            i = 0
            b1 = ""
            b2 = ""
            ls = a.split(" ")
            a1 = ls[ls.__len__() - 1]
            a1 = a1.rstrip()
            ls1 = a1.split("\n")
            a2 = ls1[0]
            text = a2
            event.control1.DeleteRange(0.0, float(event.control1.LastPosition))
            while (i < lista.__len__() - 1):
                b = str(lista[i])

                if b.__len__() > 1 and a2.__len__() == 2:
                    b1 = b[0] + b[1]
                if b.__len__() > 2 and a2.__len__() == 3:
                    b2 = b[0] + b[1] + b[2]

                if a2.__contains__(b[0]) and a2.__len__() == 1:
                    event.control1.InsertText(0.0, lista[i] + "\n")
                if a2.__contains__(b1) and a2.__len__() == 2:
                    event.control1.InsertText(0.0, lista[i] + "\n")
                if a2.__contains__(b2) and a2.__len__() == 3:
                    event.control1.InsertText(0.0, lista[i] + "\n")

                i = i + 1
            a = ""

        else:
            b1 = ""
            b2 = ""
            z = str(event.control.GetRange(
                0.0, float(event.control.LastPosition)))
            event.control1.DeleteRange(0.0, float(event.control1.LastPosition))
            if flag == True:
                if z.__len__() == 2:
                    a = str(event.control.GetRange(
                        aa - 1.0, float(event.control.LastPosition)))
                elif z.__len__() == 3:
                    a = str(event.control.GetRange(
                        aa - 2.0, float(event.control.LastPosition)))
                else:
                    a = str(event.control.GetRange(
                        aa - 0.1, float(event.control.LastPosition)))
                flag = False
            else:
                if z.__len__() == 2:
                    a = str(event.control.GetRange(
                        aa - 1.0, float(event.control.LastPosition)))
                elif z.__len__() == 3:
                    a = str(event.control.GetRange(
                        aa - 2.0, float(event.control.LastPosition)))
                else:
                    a = str(event.control.GetRange(
                        aa - 0.1, float(event.control.LastPosition)))

            i = 0
            text = a
            while (i < lista.__len__() - 1):
                b = str(lista[i])
                if b.__len__() > 1 and a.__len__() == 2:
                    b1 = b[0] + b[1]
                if b.__len__() > 2 and a.__len__() == 3:
                    b2 = b[0] + b[1] + b[2]

                if a.__contains__(b[0]) and a.__len__() == 1:
                   # print(1)
                    event.control1.InsertText(0.0, lista[i] + "\n")

                if a.__contains__(b1) and a.__len__() == 2:
                   # print(2)
                    event.control1.InsertText(0.0, lista[i] + "\n")

                if a.__contains__(b2) and a.__len__() == 3:
                   # print(3)
                    event.control1.InsertText(0.0, lista[i] + "\n")

                i = i + 1

            if a.__contains__(" ") or a.__len__() == 1:
                event.control1.DeleteRange(
                    0.0, float(event.control1.LastPosition))
            a = ""
            event.control1.SetReadOnly(True)

    def dell(event, e):
        if e.GetKeyCode() == 13:
            print("delete wala")
            event.control1.SetReadOnly(False)
            event.control1.DeleteRange(0.0, float(event.control1.LastPosition))
            global flag
            flag = True
            event.control1.SetReadOnly(True)
            e.Skip()
        else:
            pass

    def copy(event, e):
        global text
        print("copy wala")
        event.control1.SetReadOnly(False)
        i = 0
        ind = float(event.control.GetCurrentPos())
        a = event.control1.GetRange(
            float(event.control1.GetCurrentPos()), float(event.control1.LastPosition))
        ls = a.split("\n")
        b = str(event.control1.GetRange(
            0.0, float(event.control1.LastPosition)))
        ls1 = b.split("\n")
        while (True):
            if ls[1] == ls1[i]:
                break
            i = i + 1
        c = ls1[i - 1]
        c1 = ""
        ind2 = 0.0
        ii = str(ind)
        if str(event.control.GetRange(float(int(ind - 1.0)), float(event.control.LastPosition))).__contains__(" "):
            if text.__len__() == 1:
                c1 = c[0]
                ind2 = ind - 1.0
            if text.__len__() == 2:
                c1 = c[0] + c[1]
                ind2 = ind - 2.0
            if text.__len__() == 3:
                c1 = c[0] + c[1] + c[2]
                ind2 = ind - 3.0

        else:
            if text.__len__() - 1 == 1:
                c1 = c[0]
                ind2 = ind - 1.0
            if text.__len__() - 1 == 2:
                c1 = c[0] + c[1]
                ind2 = ind - 2.0
            if text.__len__() - 1 == 3:
                c1 = c[0] + c[1] + c[2]
                ind2 = ind - 3.0

        if text.__contains__(c1):
            event.control.Replace(ind2-1, ind, c)
        event.control1.SetReadOnly(True)

    def save(self, e):
        global name
        global fileloc
        print(type(name))
        print(type(fileloc))
        if (name == 0):
            if (fileloc == 0):
                initial_dir = r"C:\Users\vaish"
                # the filetype mask (default is all files)
                mask = [("Text and Python files", "*.txt *.py "),
                        ("C files", '*.c'),
                        ("cpp files", '*.cpp'),
                        ("HTML files", "*.htm"),
                        ("All files", "*.*")]
                dig = wx.FileDialog(self, "Save File As", initial_dir, "Untitled", "*.*",
                                    wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
                if (dig.ShowModal() == wx.ID_OK):
                    name = dig.GetFilename()
                    dirname = dig.GetDirectory()
                    text = str(self.control.GetValue())

                    # location of file
                    fileloc = dig.GetPath()
                    print("fileloc", fileloc)
                    file = open(os.path.join(dirname, name), "w")
                    file.write(text)
                    # path of file
                    f = name
                    print('f', f)
                    file.close()
                    # yaha milta hai.txt
                    e = os.path.splitext(f)
                    ext = e[1]
                    print(ext)
                    ch = ext
                    # abhi ke leye aapne jaha bat file save ki vaha ka path dalo uska solution hai //fileloc se hota vo mai kal
                    # send karti
                    if (ext == '.java'):
                        ob = open("Resources\\file.bat", "r")
                        dat = ob.read()
                        ob.close()
                        ob = open("Resources\\file.bat", "r")
                        data = ob.readlines()
                        ob.close()
                        ob = open("Resources\\file.bat", "a")
                        n = f + "\n"

                        print('data:', data)
                        print('dat:', dat)
                        for j in data:
                            # bat file mai jo data leya hai vo space se split keya hai so jaha space hai vo list mai jaye
                            ls = list(j.split(" "))
                            if ls[0] == "javac":
                                print(ls[0])
                                # so ls of 1 pe sib file ka nam or extension aayega
                                a = ls[1]
                                dat = dat.replace(a, str(f) + "\n")
                                print('dat1' + dat)
                            if ls[0] == "java":
                                ll = f.split(".")
                                a = ls[1]

                                dat = dat.replace(a, ll[0] + "\n")
                                print('dat2' + dat)
                            if ls[0] == "cd":
                                a = ls[1]
                                print('a' + a)
                                s = dat[0] + dat[1]
                                print('s' + s)
                                s1 = fileloc[0] + fileloc[1]
                                print('s1' + s1)
                                dat = dat.replace(a, str(fileloc) + "\n")
                                dat = dat.replace(f, "", 1)
                                dat = dat.replace(s, s1, 1)
                                print('dat3' + dat)

                        ob.close()
                        print(dat)
                        ob = open("Resources\\file.bat", "w")
                        ob.write(dat)
                        ob.close()

                    if (ext == '.c' or ext == '.cpp'):
                        ob = open("Resources\\c.bat", "r")
                        dat = ob.read()
                        ob.close()
                        ob = open("Resources\\c.bat", "r")
                        data = ob.readlines()
                        ob.close()
                        ob = open("Resources\\c.bat", "a")
                        n = f + "\n"

                        print('data:', data)
                        print('dat:', dat)
                        for j in data:
                            # bat file mai jo data leya hai vo space se split keya hai so jaha space hai vo list mai jaye
                            ls = list(j.split(" "))

                            if ls[0] == "gcc" or ls[0] == "g++":
                                print(ls[0])
                                # so ls of 1 pe sib file ka nam or extension aayega
                                a = ls[1]
                                b = ls[3]
                                dat = dat.replace(a, str(f))
                                dat = dat.replace(b, str(e[0]) + '\n')
                                print('dat1' + dat)
                            if (ext == '.cpp' and ls[0] == 'gcc'):
                                g = ls[0]
                                print('g==' + g)
                                dat = dat.replace(g, "g++")
                            if (ext == '.c' and ls[0] == "g++"):
                                g = ls[0]
                                print('g' + g)
                                dat = dat.replace(g, "gcc")
                            if ls[0] == "cd":
                                a = ls[1]
                                print('a' + a)
                                # s=dat[11]+dat[12] if using deactivate
                                s = dat[0] + dat[1]
                                print('s' + s)
                                s1 = fileloc[0] + fileloc[1]
                                print('s1' + s1)
                                dat = dat.replace(a, str(fileloc) + "\n")
                                dat = dat.replace(f, "", 1)
                                dat = dat.replace(s, s1, 1)
                                print('dat3' + dat)

                        ob.close()
                        print(dat)
                        ob = open("Resources\\c.bat", "w")
                        ob.write(dat)
                        ob.close()
                dig.Destroy()

        else:
            print("enter in else")
            fileloc = fileloc
            print("fileloc", fileloc)
            f = name
            text = str(self.control.GetValue())
            file = open(os.path.join(fileloc), "w")
            file.write(text)
            print('f', f)
            # yaha milta hai.txt
            e = os.path.splitext(f)
            print(e)
            ext = e[1]
            print(ext)
            ch = ext
            # abhi ke leye aapne jaha bat file save ki vaha ka path dalo uska solution hai //fileloc se hota vo mai kal
            # send karti
            if (ext == '.java'):
                ob = open("Resources\\file.bat", "r")
                dat = ob.read()
                ob.close()
                ob = open("Resources\\file.bat", "r")
                data = ob.readlines()
                ob.close()
                ob = open("Resources\\file.bat", "a")
                n = f + "\n"

                print('data:', data)
                print('dat:', dat)
                for j in data:
                    # bat file mai jo data leya hai vo space se split keya hai so jaha space hai vo list mai jaye
                    ls = list(j.split(" "))
                    if ls[0] == "javac":
                        print(ls[0])
                        # so ls of 1 pe sib file ka nam or extension aayega
                        a = ls[1]
                        dat = dat.replace(a, str(f) + "\n")
                        print('dat1' + dat)
                    if ls[0] == "java":
                        ll = f.split(".")
                        a = ls[1]

                        dat = dat.replace(a, ll[0] + "\n")
                        print('dat2' + dat)
                    if ls[0] == "cd":
                        a = ls[1]
                        print('a' + a)
                        s = dat[0] + dat[1]
                        print('s' + s)
                        s1 = fileloc[0] + fileloc[1]
                        print('s1' + s1)
                        dat = dat.replace(a, str(fileloc) + "\n")
                        dat = dat.replace(f, "", 1)
                        dat = dat.replace(s, s1, 1)
                        print('dat3' + dat)

                ob.close()
                print(dat)
                ob = open("Resources\\file.bat", "w")
                ob.write(dat)
                ob.close()

            if (ext == '.c' or ext == '.cpp'):
                print("enter in cpp")
                ob = open("Resources\\c.bat", "r")
                dat = ob.read()
                ob.close()
                ob = open("Resources\\c.bat", "r")
                data = ob.readlines()
                ob.close()
                # ..
                ob = open("Resources\\c.bat", "a")
                n = f + "\n"

                print('data:', data)
                print('dat:', dat)
                for j in data:
                    # bat file mai jo data leya hai vo space se split keya hai so jaha space hai vo list mai jaye
                    ls = list(j.split(" "))

                    if ls[0] == "gcc" or ls[0] == "g++":
                        print(ls[0])
                        # so ls of 1 pe sib file ka nam or extension aayega
                        a = ls[1]
                        b = ls[3]
                        dat = dat.replace(a, str(f))
                        dat = dat.replace(b, str(e[0]) + '\n')
                        print('dat1' + dat)
                    if (ext == '.cpp' and ls[0] == 'gcc'):
                        g = ls[0]
                        print('g==' + g)
                        dat = dat.replace(g, "g++")
                    if (ext == '.c' and ls[0] == "g++"):
                        g = ls[0]
                        print('g' + g)
                        dat = dat.replace(g, "gcc")
                    if ls[0] == "cd":
                        a = ls[1]
                        print('a' + a)
                        # s=dat[11]+dat[12] if using deactivate
                        s = dat[0] + dat[1]
                        print('s' + s)
                        s1 = fileloc[0] + fileloc[1]
                        print('s1' + s1)
                        dat = dat.replace(a, str(fileloc) + "\n")
                        dat = dat.replace(f, "", 1)
                        dat = dat.replace(s, s1, 1)
                        print('dat3' + dat)

                ob.close()
                print(dat)
                ob = open("Resources\\c.bat", "w")
                ob.write(dat)
                ob.close()

    def save_as(self, e):
        global fileloc
        global name
        initial_dir = r"C:\Users\vaish"
        # the filetype mask (default is all files)
        mask = [("Text and Python files", "*.txt *.py "),
                ("C files", '*.c'),
                ("cpp files", '*.cpp'),
                ("HTML files", "*.htm"),
                ("All files", "*.*")]
        dig = wx.FileDialog(self, "Save File As", initial_dir,
                            "Untitled", "*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if (dig.ShowModal() == wx.ID_OK):
            name = dig.GetFilename()
            dirname = dig.GetDirectory()
            text = str(self.control.GetValue())

            # location of file
            fileloc = dig.GetPath()
            print("fileloc", fileloc)
            file = open(os.path.join(dirname, name), "w")
            file.write(text)
            # path of file
            f = name
            print('f', f)
            file.close()
            # yaha milta hai.txt
            e = os.path.splitext(f)
            ext = e[1]
            print(ext)
            ch = ext
            # abhi ke leye aapne jaha bat file save ki vaha ka path dalo uska solution hai //fileloc se hota vo mai kal
            # send karti
            if (ext == '.java'):
                ob = open("Resources\\file.bat", "r")
                dat = ob.read()
                ob.close()
                ob = open("Resources\\file.bat", "r")
                data = ob.readlines()
                ob.close()
                ob = open("Resources\\file.bat", "a")
                n = f + "\n"

                print('data:', data)
                print('dat:', dat)
                for j in data:
                    # bat file mai jo data leya hai vo space se split keya hai so jaha space hai vo list mai jaye
                    ls = list(j.split(" "))
                    if ls[0] == "javac":
                        print(ls[0])
                        # so ls of 1 pe sib file ka nam or extension aayega
                        a = ls[1]
                        dat = dat.replace(a, str(f) + "\n")
                        print('dat1' + dat)
                    if ls[0] == "java":
                        ll = f.split(".")
                        a = ls[1]

                        dat = dat.replace(a, ll[0] + "\n")
                        print('dat2' + dat)
                    if ls[0] == "cd":
                        a = ls[1]
                        print('a' + a)
                        s = dat[0] + dat[1]
                        print('s' + s)
                        s1 = fileloc[0] + fileloc[1]
                        print('s1' + s1)
                        dat = dat.replace(a, str(fileloc) + "\n")
                        dat = dat.replace(f, "", 1)
                        dat = dat.replace(s, s1, 1)
                        print('dat3' + dat)

                ob.close()
                print(dat)
                ob = open("Resources\\file.bat", "w")
                ob.write(dat)
                ob.close()

            if (ext == '.c' or ext == '.cpp'):
                ob = open("Resources\\c.bat", "r")
                dat = ob.read()
                ob.close()
                ob = open("Resources\\c.bat", "r")
                data = ob.readlines()
                ob.close()
                ob = open("Resources\\c.bat", "a")
                n = f + "\n"

                print('data:', data)
                print('dat:', dat)
                for j in data:
                    # bat file mai jo data leya hai vo space se split keya hai so jaha space hai vo list mai jaye
                    ls = list(j.split(" "))

                    if ls[0] == "gcc" or ls[0] == "g++":
                        print(ls[0])
                        # so ls of 1 pe sib file ka nam or extension aayega
                        a = ls[1]
                        b = ls[3]
                        dat = dat.replace(a, str(f))
                        dat = dat.replace(b, str(e[0]) + '\n')
                        print('dat1' + dat)
                    if (ext == '.cpp' and ls[0] == 'gcc'):
                        g = ls[0]
                        print('g==' + g)
                        dat = dat.replace(g, "g++")
                    if (ext == '.c' and ls[0] == "g++"):
                        g = ls[0]
                        print('g' + g)
                        dat = dat.replace(g, "gcc")
                    if ls[0] == "cd":
                        a = ls[1]
                        print('a' + a)
                        # s=dat[11]+dat[12] if using deactivate
                        s = dat[0] + dat[1]
                        print('s' + s)
                        s1 = fileloc[0] + fileloc[1]
                        print('s1' + s1)
                        dat = dat.replace(a, str(fileloc) + "\n")
                        dat = dat.replace(f, "", 1)
                        dat = dat.replace(s, s1, 1)
                        print('dat3' + dat)

                ob.close()
                print(dat)
                ob = open("Resources\\c.bat", "w")
                ob.write(dat)
                ob.close()
        dig.Destroy()

    def select(self, e):
        id = self.tree1.GetSelection()
        if id == 'root' or id == 'java' or id == 'c' or id == 'cpp' or id == 'Syntax' or id == 'Package' or id == 'Class' or id == 'Method':
            pass
        else:
            text = self.tree1.GetItemData(id)
            self.control.AddText(text)

    def open1(self, e):
        global name
        global fileloc
        initial_dir = "C:\Temp"
        # the filetype mask (default is all files)
        mask = [("Text and Python files", "*.txt *.py "),
                ("HTML files", "*.htm"),
                ("C files", '*.c'),
                ("cpp files", '*.cpp'),
                ("All files", "*.*")]
        dig = wx.FileDialog(self, "Choose a File",
                            initial_dir, "", "*.*", wx.FD_OPEN)
        if (dig.ShowModal() == wx.ID_OK):
            name = dig.GetFilename()
            dirname = dig.GetDirectory()
            fileloc = dig.GetPath()
            f = open(os.path.join(dirname, name), "r")
            self.control.SetValue(f.read())
        dig.Destroy()
        print("enter in else")
        fileloc = fileloc
        print("fileloc", fileloc)
        f = name
        text = str(self.control.GetValue())
        file = open(os.path.join(fileloc), "w")
        file.write(text)
        print('f', f)
        # yaha milta hai.txt
        e = os.path.splitext(f)
        print(e)
        ext = e[1]
        print(ext)
        ch = ext
        # abhi ke leye aapne jaha bat file save ki vaha ka path dalo uska solution hai //fileloc se hota vo mai kal
        # send karti
        if (ext == '.java'):
            ob = open("Resources\\file.bat", "r")
            dat = ob.read()
            ob.close()
            ob = open("Resources\\file.bat", "r")
            data = ob.readlines()
            ob.close()
            ob = open("Resources\\file.bat", "a")
            n = f + "\n"

            print('data:', data)
            print('dat:', dat)
            for j in data:
                # bat file mai jo data leya hai vo space se split keya hai so jaha space hai vo list mai jaye
                ls = list(j.split(" "))
                if ls[0] == "javac":
                    print(ls[0])
                    # so ls of 1 pe sib file ka nam or extension aayega
                    a = ls[1]
                    dat = dat.replace(a, str(f) + "\n")
                    print('dat1' + dat)
                if ls[0] == "java":
                    ll = f.split(".")
                    a = ls[1]

                    dat = dat.replace(a, ll[0] + "\n")
                    print('dat2' + dat)
                if ls[0] == "cd":
                    a = ls[1]
                    print('a' + a)
                    s = dat[0] + dat[1]
                    print('s' + s)
                    s1 = fileloc[0] + fileloc[1]
                    print('s1' + s1)
                    dat = dat.replace(a, str(fileloc) + "\n")
                    dat = dat.replace(f, "", 1)
                    dat = dat.replace(s, s1, 1)
                    print('dat3' + dat)

            ob.close()
            print(dat)
            ob = open("Resources\\file.bat", "w")
            ob.write(dat)
            ob.close()

        if (ext == '.c' or ext == '.cpp'):
            print("enter in cpp")
            ob = open("Resources\\c.bat", "r")
            dat = ob.read()
            ob.close()
            ob = open("Resources\\c.bat", "r")
            data = ob.readlines()
            ob.close()
            ob = open("Resources\\c.bat", "a")
            n = f + "\n"

            print('data:', data)
            print('dat:', dat)
            for j in data:
                # bat file mai jo data leya hai vo space se split keya hai so jaha space hai vo list mai jaye
                ls = list(j.split(" "))

                if ls[0] == "gcc" or ls[0] == "g++":
                    print(ls[0])
                    # so ls of 1 pe sib file ka nam or extension aayega
                    a = ls[1]
                    b = ls[3]
                    dat = dat.replace(a, str(f))
                    dat = dat.replace(b, str(e[0]) + '\n')
                    print('dat1' + dat)
                if (ext == '.cpp' and ls[0] == 'gcc'):
                    g = ls[0]
                    print('g==' + g)
                    dat = dat.replace(g, "g++")
                if (ext == '.c' and ls[0] == "g++"):
                    g = ls[0]
                    print('g' + g)
                    dat = dat.replace(g, "gcc")
                if ls[0] == "cd":
                    a = ls[1]
                    print('a' + a)
                    # s=dat[11]+dat[12] if using deactivate
                    s = dat[0] + dat[1]
                    print('s' + s)
                    s1 = fileloc[0] + fileloc[1]
                    print('s1' + s1)
                    dat = dat.replace(a, str(fileloc) + "\n")
                    dat = dat.replace(f, "", 1)
                    dat = dat.replace(s, s1, 1)
                    print('dat3' + dat)

            ob.close()
            print(dat)
            ob = open("Resources\\c.bat", "w")
            ob.write(dat)
            ob.close()

    def exitmethod(self, e):
        m = wx.MessageDialog(
            self, "Confirm Exit", "Are you sure you want to exit?", wx.YES_NO | wx.ICON_QUESTION)

        if m.ShowModal() == wx.ID_YES:
            m.Destroy()
        else:
            m.SetMessage("Decision", "Good Decision, continue in application")

    def newproj(self, e):
        m = wx.MessageDialog(
            self, "Confirm Exit", "do you want save the existing file?", wx.YES_NO | wx.ICON_QUESTION)
        if m.ShowModal() == wx.ID_NO:
            self.control.SetValue("")
        else:
            self.save(e)
            self.control.SetValue("")

    def OnCut(self, e):
        self.control.Cut()

    def OnCopy(self, e):
        self.control.Copy()

    def OnPaste(self, e):
        self.control.Paste()

    def OnRedo(self, e):
        self.control.Redo()

    def OnUndo(self, e):
        self.control.Undo()

    def run(self, e):
        global name
        r = r"Resources\\"
        n = "file.bat"
        r = r + n
        os.startfile(r)

    def runc(self, e):
        global name
        r = r"Resources\\"
        n = "c.bat"
        r = r + n
        os.startfile(r)

    def tts(self, e):
        text = str(self.control.GetValue())
        b = text.replace("{", "open brace")
        c = b.replace("}", "close brace")
        d = c.replace("\n", " ")
        e = d.replace(":", "colon")
        f = e.replace(";", "semicolon")
        g = f.replace("(", "open parentheses")
        h = g.replace(")", "close parentheses")
        ee = pyttsx3.init()
        rare = ee.getProperty("rate")
        ee.setProperty("rate", 100)
        volum = ee.getProperty("volume")
        ee.setProperty("volume", 3.0)
        voice = ee.getProperty("voices")
        ee.setProperty("voice", voice[1].id)
        ee.say(h)
        ee.runAndWait()

    def OnToggleLineNumbers(self, e):
        if (self.lineNumbersEnabled):
            self.control.SetMarginWidth(1, 0)
            self.lineNumbersEnabled = False
        else:
            self.control.SetMarginWidth(1, self.leftMarginWidth)
            self.lineNumbersEnabled = True

    def Fontbox(self, e):
        fontdialog = wx.FontDialog(self)
        fontdialog.CenterOnParent()
        if fontdialog.ShowModal() == wx.ID_OK:
            data = fontdialog.GetFontData()
            myFont = data.GetChosenFont()
            self.control.StyleSetFont(0, font=myFont)
        fontdialog.Destroy()

    def UpdateLineCol(self, e):
        line = self.control.GetCurrentLine() + 1
        col = self.control.GetColumn(self.control.GetCurrentPos())
        stat = "Line %s, Column %s" % (line, col)
        self.StatusBar.SetStatusText(stat, 0)

    def SpeechDef(self, e):
        text = str(self.control.GetValue())
        b = text.replace("{", "open brace")
        c = b.replace("}", "close brace")
        d = c.replace("\n", " ")
        e = d.replace(":", "colon")
        f = e.replace(";", "semicolon")
        g = f.replace("(", "open parentheses")
        h = g.replace(")", "close parentheses")
        e = pyttsx3.init()
        rare = e.getProperty("rate")
        e.setProperty("rate", 100)
        volum = e.getProperty("volume")
        e.setProperty("volume", 3.0)
        voice = e.getProperty("voices")
        e.setProperty("voice", voice[0].id)
        e.say(h)
        e.runAndWait()

    def OnLeftUp(self, e):
        # This way if you click on another position in the text box
        # it will update the line/col number in the status bar (like it should)
        self.UpdateLineCol(self)
        e.Skip()

    def howto(self, e):
        print("file")
        r = r"Resources\\"
        n = 'manual.pdf'
        r = r+n
        os.startfile(r)

    def OnAbout(self, e):
        # Simple display a modal window telling about the application
        dlg = wx.MessageDialog(self, "An elegant, yet simple, text editor made with Python and wxPython.\n\nCreated by:\n"
                               "\n1. Vaishnavi Nighvekar"
                               "\n2. Om Agrawal"
                               "\n3. Prakash Zodge"
                               "\n3. Yash Jaiswal"
                               "\n\nVersion 1.0.0\n\n",
                               "About Limitless Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()


app = wx.App(False)
Demo = Editor(None, "Limitless Editor")
Demo.SetIcon(wx.Icon('Resources/le.png'))
app.MainLoop()
