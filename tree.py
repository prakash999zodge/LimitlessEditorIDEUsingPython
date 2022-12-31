import wx


class Tree(wx.TreeCtrl):
    def __init__(self, parent, style):
        # Initialize the tree
        wx.TreeCtrl.__init__(self, parent, style)

        root = self.AddRoot('LEMITLESS_TREE')
        java = self.AppendItem(root, 'Java')
        c = self.AppendItem(root, 'C')
        cpp = self.AppendItem(root, 'CPP')
        image_list = wx.ImageList(16, 16)
        LEMITLESS_TREE = image_list.Add(wx.Image(
            "Resources/dd.png", wx.BITMAP_TYPE_PNG).Scale(16, 16).ConvertToBitmap())
        Java = image_list.Add(wx.Image(
            "Resources/java.png", wx.BITMAP_TYPE_PNG).Scale(16, 16).ConvertToBitmap())
        C = image_list.Add(wx.Image("Resources/c.png",
                           wx.BITMAP_TYPE_PNG).Scale(16, 16).ConvertToBitmap())
        CPP = image_list.Add(wx.Image(
            "Resources/cpp.png", wx.BITMAP_TYPE_PNG).Scale(16, 16).ConvertToBitmap())
        self.AssignImageList(image_list)
        self.SetItemImage(root, LEMITLESS_TREE, wx.TreeItemIcon_Normal)
        self.SetItemImage(java, Java, wx.TreeItemIcon_Normal)
        self.SetItemImage(c, C, wx.TreeItemIcon_Normal)
        self.SetItemImage(cpp, CPP, wx.TreeItemIcon_Normal)

        # Tree for Java

        Package = self.AppendItem(java, text='Package', data='')

        #Class = self.AppendItem(java,'Class')
        #Method = self.AppendItem(java,'Method')
        #AwtControls = self.AppendItem(java,'Awt Controls')

        # Packages for Java

        self.AppendItem(Package, text='io', data='import java.io.*;')
        self.AppendItem(Package, text='util', data='import java.util.*;')
        self.AppendItem(Package, text='awt', data='import java.awt.*;')
        self.AppendItem(Package, text='net', data='import java.net.*;')
        self.AppendItem(Package, text='event', data='import java.awt.event;')
        self.AppendItem(Package, text='lang', data='import java.lang.*;')
        self.AppendItem(Package, text='applet', data='import java.applet.*;')
        self.AppendItem(Package, text='swing', data='import javax.swing.*;')
        self.AppendItem(Package, text='swingEvent',
                        data='import javax.swing.event;')
        self.AppendItem(Package, text='servlet',
                        data='import javax.servlet.*;')
        self.AppendItem(Package, text='servletJsp',
                        data='import javax.servlet.jsp;')

        # Loops of Java
        Loops = self.AppendItem(java, text='Loops', data='')
        self.AppendItem(Loops, text='while()',
                        data='while(condition)\n{\n  \n}')
        self.AppendItem(Loops, text='for()', data='for(condition)\n{\n  \n}')
        self.AppendItem(Loops, text='do()',
                        data='do\n{\n  \n}while(condition);')

        Conditional = self.AppendItem(
            java, text='Conditional and Return Statements', data='')
        self.AppendItem(Conditional, text='if()',
                        data='if(condition)\n{\n  \n}')
        self.AppendItem(Conditional, text='if else()',
                        data='if(condition)\n{\n  \n}\nelse\n{\n  \n}')
        self.AppendItem(Conditional, text='else if()',
                        data='if(condition)\n{\n  \n}\nelse if(condition)\n{\n  \n}\nelse\n{\n  \n}')
        self.AppendItem(Conditional, text='try catch',
                        data='try\n{\n  \n}\ncatch(Exception e)\n{\n  \n}')
        self.AppendItem(Conditional, text='try catch finally',
                        data='try\n{\n  \n}\ncatch(Exception e)\n{\n  \n}\nfinally\n{\n  \n}')

        Functions = self.AppendItem(java, text='Functions', data='')

        StringFunctions = self.AppendItem(
            Functions, text='String Functions', data='')
        self.AppendItem(StringFunctions, text='compareTo()',
                        data='compareTo()')
        self.AppendItem(StringFunctions, text='equals()', data='equals()')
        self.AppendItem(StringFunctions, text='valueOf()', data='valueOf()')
        self.AppendItem(StringFunctions, text='substring()',
                        data='substring()')
        self.AppendItem(StringFunctions, text='replace()', data='replace()')
        self.AppendItem(StringFunctions, text='toString()', data='toString()')
        self.AppendItem(StringFunctions, text='charAt()', data='charAt()')
        self.AppendItem(StringFunctions, text='concat()', data='concat()')
        self.AppendItem(StringFunctions, text='endsWith()', data='endsWith()')
        self.AppendItem(StringFunctions, text='lastIndexOf()',
                        data='lastIndexOf()')
        self.AppendItem(StringFunctions, text='firstIndexOf()',
                        data='firstIndexOf()')
        self.AppendItem(StringFunctions, text='getChars()', data='getChars()')
        self.AppendItem(StringFunctions, text='getBytes()', data='getBytes()')
        self.AppendItem(StringFunctions, text='indexOf()', data='indexOf()')
        self.AppendItem(StringFunctions, text='length()', data='length()')
        self.AppendItem(StringFunctions, text='split()', data='split()')
        self.AppendItem(StringFunctions, text='startsWith()',
                        data='startsWith()')
        self.AppendItem(StringFunctions, text='toLowerCase()',
                        data='toLowerCase()')
        self.AppendItem(StringFunctions, text='toUppercase()',
                        data='toUpperCase()')

        MathFunctions = self.AppendItem(
            Functions, text='Math Functions', data='')
        self.AppendItem(MathFunctions, text='pow()', data='pow()')
        self.AppendItem(MathFunctions, text='sqrt()', data='sqrt()')
        self.AppendItem(MathFunctions, text='abs()', data='abs()')
        self.AppendItem(MathFunctions, text='ceil()', data='ceil()')
        self.AppendItem(MathFunctions, text='floor()', data='floor()')
        self.AppendItem(MathFunctions, text='floorDiv()', data='floorDiv()')
        self.AppendItem(MathFunctions, text='min()', data='min()')
        self.AppendItem(MathFunctions, text='max()', data='max()')
        self.AppendItem(MathFunctions, text='round()', data='round()')
        self.AppendItem(MathFunctions, text='random()', data='random()')

        ParsingFunctions = self.AppendItem(
            Functions, text='Parsing Functions', data='')
        self.AppendItem(ParsingFunctions,
                        text='Integer.parseInt()', data='Integer.parseInt()')
        self.AppendItem(ParsingFunctions,
                        text='Float.parseFloat()', data='Float.parseFloat()')
        self.AppendItem(
            ParsingFunctions, text='Double.parseDouble()', data='Double.parseDouble()')
        self.AppendItem(ParsingFunctions, text='Byte.praseByte()',
                        data='Byte.praseByte()')

        AWTFunctions = self.AppendItem(
            Functions, text='Parsing Functions', data='')
        self.AppendItem(AWTFunctions, text='setSize()', data='setSize()')
        self.AppendItem(AWTFunctions, text='setVisible()', data='setVisible()')
        self.AppendItem(AWTFunctions, text='setTitle()', data='setTitle()')
        self.AppendItem(AWTFunctions, text='setText()', data='setText()')
        self.AppendItem(AWTFunctions, text='setAlignment()',
                        data='setAlignment()')
        self.AppendItem(AWTFunctions, text='getAlignment()',
                        data='getAlignment()')
        self.AppendItem(AWTFunctions, text='setLabel()', data='setLabel()')
        self.AppendItem(AWTFunctions, text='getLabel()', data='getLabel()')
        self.AppendItem(AWTFunctions, text='setState()', data='setState()')
        self.AppendItem(AWTFunctions, text='getState()', data='getText()')
        self.AppendItem(AWTFunctions, text='getSelectedCheckBox()',
                        data='getSelectedCheckBox()')
        self.AppendItem(AWTFunctions, text='setSelectedCheckBox()',
                        data='setSelectedCheckBox()')
        self.AppendItem(AWTFunctions, text='add()', data='add()')
        self.AppendItem(AWTFunctions, text='getSelectedItem()',
                        data='getSelectedItem()')
        self.AppendItem(AWTFunctions, text='getSelectedItems()',
                        data='getSelectedItems()')
        self.AppendItem(AWTFunctions, text='select()', data='select()')
        self.AppendItem(AWTFunctions, text='getItemCount()',
                        data='getItemCount()')
        self.AppendItem(AWTFunctions, text='getItem()', data='getItem()')
        self.AppendItem(AWTFunctions, text='getSelectedText()',
                        data='getSelectedText()')
        self.AppendItem(AWTFunctions, text='isEditable()', data='isEditable()')
        self.AppendItem(AWTFunctions, text='apped()', data='apped()')
        self.AppendItem(AWTFunctions, text='insert()', data='insert()')
        self.AppendItem(AWTFunctions, text='getEchoChar()',
                        data='getEchoChar()')
        self.AppendItem(AWTFunctions, text='setEchoChar()',
                        data='setEchoChar()')
        self.AppendItem(AWTFunctions, text='replaceRange()',
                        data='replaceRange()')

        AppletFunctions = self.AppendItem(
            Functions, text='Applet Life Cycle Methods', data='')
        self.AppendItem(AppletFunctions, text='init()',
                        data='public void init()')
        self.AppendItem(AppletFunctions, text='start()',
                        data='public void start()')
        self.AppendItem(AppletFunctions, text='paint()',
                        data='public void paint()')
        self.AppendItem(AppletFunctions, text='stop()',
                        data='public void stop()')
        self.AppendItem(AppletFunctions, text='destroy()',
                        data='public void destroy()')
        self.AppendItem(AppletFunctions, text='repaint()', data='repaint()')

        OtherFunctions = self.AppendItem(
            Functions, text='Other Functions', data='')
        self.AppendItem(OtherFunctions, text='println()',
                        data='System.out.println();')
        self.AppendItem(OtherFunctions, text='main()',
                        data='public static void main(String ar[])\n{\n  \n}')
        self.AppendItem(AppletFunctions, text='finalize()', data='finalize()')

        AWTandSwingComponents = self.AppendItem(
            java, text='AWT and Swing Components', data='')
        self.AppendItem(AWTandSwingComponents, text='Label()',
                        data='Label l = new Label("");\n')
        self.AppendItem(AWTandSwingComponents, text='Button()',
                        data='Button b = new Button("");\n')
        self.AppendItem(AWTandSwingComponents, text='Choice()',
                        data='Choice c = new Choice();\n')
        self.AppendItem(AWTandSwingComponents, text='TextField()',
                        data='TextField t = new TextField("");\n')
        self.AppendItem(AWTandSwingComponents, text='TextArea()',
                        data='TextArea ta = new TextArea();\n')
        self.AppendItem(AWTandSwingComponents, text='Checkbox()',
                        data='Checkbox c = new Checkbox();\n')
        self.AppendItem(AWTandSwingComponents, text='CheckBoxGroup()',
                        data='Checkbox c = new Checkbox(String label, boolean state, CheckboxGroup cbg);\n')
        self.AppendItem(AWTandSwingComponents, text='List()',
                        data='List s = new List();\n')
        self.AppendItem(AWTandSwingComponents, text='MenuBar()',
                        data='MenuBar mb = new MenuBar();\n')
        self.AppendItem(AWTandSwingComponents, text='Menu()',
                        data='Menu m = new Menu("");\n')
        self.AppendItem(AWTandSwingComponents, text='MenuItem()',
                        data='MenuItem mi = new MenuItem("");\n')
        self.AppendItem(AWTandSwingComponents, text='JLabel()',
                        data='JLabel l = new JLabel("");\n')
        self.AppendItem(AWTandSwingComponents, text='JButton()',
                        data='JButton b = new JButton("");\n')
        self.AppendItem(AWTandSwingComponents, text='JTextField()',
                        data='JTextField t = new JTextField("");\n')
        self.AppendItem(AWTandSwingComponents, text='JTextArea()',
                        data='JTextArea t = new JTextArea("");\n')
        self.AppendItem(AWTandSwingComponents, text='JComboBox()',
                        data='JComboBox C = new JComboBox();\n')
        self.AppendItem(AWTandSwingComponents, text='JCheckBox()',
                        data='JCheckBox c = new JCheckBox("1");\n')
        self.AppendItem(AWTandSwingComponents, text='JRadioButton()',
                        data='JRadioButton r = new JRadioButton("1");\n')
        self.AppendItem(AWTandSwingComponents, text='JTree()',
                        data='JTree jt=new JTree(DefaultMutableTreeNodeObjectName);\n')
        self.AppendItem(AWTandSwingComponents, text='JPasswordField()',
                        data='JPasswordField p = new JPasswordField();\n')
        self.AppendItem(AWTandSwingComponents, text='JMenuBar()',
                        data='JMenuBar mb = new JMenuBar();\n')
        self.AppendItem(AWTandSwingComponents, text='JMenu()',
                        data='JMenu m = new JMenu("");\n')
        self.AppendItem(AWTandSwingComponents, text='JMenuItem()',
                        data='JMenuItem mi = new JMenuItem("");\n')

        # Tree for C
        libc = self.AppendItem(c, text='Library', data='')
        self.AppendItem(libc, text='stdio', data="#include<stdio.h>")
        self.AppendItem(libc, text='conio', data="#include<conio.h>")
        self.AppendItem(libc, text='string', data="#include<string.h>")
        self.AppendItem(libc, text='stdlib', data="#include<stdlib.h>")
        self.AppendItem(libc, text='math', data="#include<math.h>")
        self.AppendItem(libc, text='time', data="#include<time.h>")
        self.AppendItem(libc, text='ctype', data="#include<ctype.h>")
        self.AppendItem(libc, text='stdarg', data="#include<stdarg.h>")
        self.AppendItem(libc, text='signal', data="#include<signal.h>")
        self.AppendItem(libc, text='setjmp', data="#include<setjmp.h>")
        self.AppendItem(libc, text='locale', data="#include<locale.h>")
        self.AppendItem(libc, text='errno', data="#include<errno.h>")
        self.AppendItem(libc, text='assert', data="#include<assert.h>")

        io = self.AppendItem(c, text="Standard I/O", data='')
        self.AppendItem(io, text="printf()", data="printf("")")
        self.AppendItem(io, text="scanf()", data="scanf("")")
        self.AppendItem(io, text="getchar()", data="getchar()")
        self.AppendItem(io, text="putchar()", data="putchar()")
        self.AppendItem(io, text="fopen()", data="fopen()")
        self.AppendItem(io, text="fclose()", data="fclose()")

        sf = self.AppendItem(c, text="String Functions", data='')
        self.AppendItem(sf, text="strcmp()", data="strcmp()")
        self.AppendItem(sf, text="strcpy()", data="strcpy()")
        self.AppendItem(sf, text="strcat()", data="strcat()")

        mf = self.AppendItem(c, text="Math Functions", data='')
        self.AppendItem(mf, text="floor()", data="floor(double x)")
        self.AppendItem(mf, text="ceil()", data="ceil(double x)")
        self.AppendItem(mf, text="exp()", data="exp(double x)")
        self.AppendItem(mf, text="sqrt()", data="sqrt(double x)")
        self.AppendItem(mf, text="pow()", data="pow(int base,int power)")
        self.AppendItem(mf, text="fabs()", data="fabs(int x)")
        self.AppendItem(mf, text="log()", data="log(double x)")
        self.AppendItem(mf, text="sin()", data="sin(double x)")
        self.AppendItem(mf, text="cos()", data="cos(double x)")
        self.AppendItem(mf, text="tan()", data="tan(double x)")

        ch = self.AppendItem(c, text="Character Handling", data='')
        self.AppendItem(ch, text="isalpha()", data="isalpha()")
        self.AppendItem(ch, text="isdigit()", data="isdigit()")
        self.AppendItem(ch, text="isalnum()", data="isalnum()")
        self.AppendItem(ch, text="isupper()", data="isupper()")
        self.AppendItem(ch, text="islower()", data="islower()")
        self.AppendItem(ch, text="toupper()", data="tolower()")
        self.AppendItem(ch, text="tolower()", data="tolower()")
        self.AppendItem(ch, text="iscntrl()", data="iscntrl()")
        self.AppendItem(ch, text="isgraph()", data="isgraph()")
        self.AppendItem(ch, text="isprint()", data="isprint()")
        self.AppendItem(ch, text="ispunct()", data="ispunct()")
        self.AppendItem(ch, text="isspace()", data="isspace()")
        self.AppendItem(ch, text="isxdigit()", data="isxdigit()")

        cio = self.AppendItem(c, text="Console I/O", data="")
        self.AppendItem(cio, text="clrscr()", data="clrscr()")
        self.AppendItem(cio, text="getch()", data="getch()")

        loops = self.AppendItem(c, text='loops', data="")
        self.AppendItem(
            loops, text="while", data='while(Condition)\n{\n   Statement(s)\n    Increment/Decrement; \n}\n')
        self.AppendItem(
            loops, text="for", data='for(initialization; condition; incOrDec)\n{\n   Statement(s) \n}\n')
        self.AppendItem(loops, text="do-while",
                        data='do\n{\n   Statement(s)\n    Increment/Decrement;\n}while(Condition); \n')

        # Tree For CPP
        libcpp = self.AppendItem(cpp, text='Library', data='')
        self.AppendItem(libcpp, text='cmath', data='#include<cmath.h>')
        self.AppendItem(libcpp, text='iostream', data='#include<iostream.h>')
        self.AppendItem(libcpp, text='cstring', data='#include<cstring.h>')
        self.AppendItem(libcpp, text='cctype', data='#include<cctype.h>')
        self.AppendItem(libcpp, text='csignal', data='#include<csignal.h>')
        self.AppendItem(libcpp, text='clocale', data='#include<clocale.h>')
        self.AppendItem(libcpp, text='cwctype', data='#include<cwctype.h>')
        self.AppendItem(libcpp, text='cstdio', data='#include<cstdio.h>')
        self.AppendItem(libcpp, text='cwchar', data='#include<cwchar.h>')
        self.AppendItem(libcpp, text='cuchar', data='#include<cuchar.h>')
        self.AppendItem(libcpp, text='csetjmp', data='#include<csetjmp.h>')
        self.AppendItem(libcpp, text='cfenv', data='#include<cfenv.h>')
        self.AppendItem(libcpp, text='ctime', data='#include<ctime.h>')

        cppFunctions = self.AppendItem(cpp, text='NewFunction',
                                       data='void myFunction() \n{\n  // code to be executed\n}')
        cppClass = self.AppendItem(
            cpp, text='NewClass', data='class className\n{\n //Code\n};')
        cppObject = self.AppendItem(
            cpp, text='ClassObject', data='className ObjName = new className();')
        cppIO = self.AppendItem(cpp, text='Standard I/O Stream', data='')
        self.AppendItem(cppIO, text='Output Stream', data='cout<< ;')
        self.AppendItem(cppIO, text='Input Stream', data='cin>> ;')
        self.AppendItem(cppIO, text='Un-buffered error Stream',
                        data='cerr << ;')
        self.AppendItem(cppIO, text='Buffered error Stream', data='clog << ;')
        cppException = self.AppendItem(cpp, text='Try Catch',
                                       data='try\n{\n  //try code\n}\ncatch(ExceptionHere)\n{\n  //catch code\n}')
        cppMemory = self.AppendItem(
            cpp, text='Memory allocation & de-allocation', data='')
        self.AppendItem(cppMemory, text='New Operator',
                        data='pointer-variable = new data-type;')
        self.AppendItem(cppMemory, text='Delete Operator',
                        data='// Release memory pointed by pointer-variable \ndelete pointer-variable; ')
        cppInheritance = self.AppendItem(cpp, text='Inheritance', data='')
        self.AppendItem(cppInheritance, text='Single Inheritance',
                        data='class subclass_name : access_mode base_class_name\n{\n  //body of subclass\n};')
        self.AppendItem(cppInheritance, text='Multiple Inheritance',
                        data='class subclass_name : access_mode base_class1, access_mode base_class2, ....\n{\n  //body of subclass\n};')
