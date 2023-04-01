from tkinter import *
from tkinter import filedialog
import tkinter as tk
import networkx as nx
import random
import matplotlib.pyplot as plt

root = Tk()
root.title('Foodchain Program')
root.minsize(height=600,width=1200)
font = ('Times_New_Roman',25)
font2 = ('Times_New_Roman',15)
font3 = ('Times_New_Roman',10)

def swap(l):return[l[1],l[0]]
def findpath(src,des):return [path for path in nx.all_simple_paths(network, source=src, target=des)]

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def f1():
    delete_pages()
    f1_frame = tk.Frame(main_frame)
    alllt = network.nodes()
    count = 0
    alllt1,alllt2,alllt3,alllt4,alllt5="","","","",""
    for i in alllt:
        if count%5 == 0:alllt1+='    '+i
        elif count%5 == 1:alllt2+='    '+i
        elif count%5 == 2:alllt3+='    '+i
        elif count%5 == 3:alllt4+='    '+i
        elif count%5 == 4:alllt5+='    '+i
        count += 1
    lb1 = tk.Label(f1_frame,text=alllt1,font=font2)
    lb2 = tk.Label(f1_frame,text=alllt2,font=font2)
    lb3 = tk.Label(f1_frame,text=alllt3,font=font2)
    lb4 = tk.Label(f1_frame,text=alllt4,font=font2)
    lb5 = tk.Label(f1_frame,text=alllt5,font=font2)
    lb1.pack()
    lb2.pack()
    lb3.pack()
    lb4.pack()
    lb5.pack()
    f1_frame.pack()

def f2():
    delete_pages()
    f2_frame = tk.Frame(main_frame)
    colist = ["gold","violet","pink","violet","orange","yellow","cyan"]
    color_list = [random.choice(colist) for _ in range(network.number_of_nodes())]
    plt.figure(figsize=(8, 6))
    plt.title('Food Web', size=10)
    nx.draw_networkx(network,node_color=color_list,with_labels=True,arrows=True,arrowstyle='->',arrowsize=15,node_size=1000,font_size=9,pos=nx.circular_layout(network))
    plt.show()
    f2_frame.pack()

def f3():
    def f3submit():
        res1,resmin,resmax = [],[],[]
        lc = e1.get()
        fc = e2.get()
        allpath = findpath(lc,fc)
        for i in allpath:res1.append(len(i))
        if res1 != []:
            lb3 = tk.Label(f3_frame,text="\nAll path",font=font3)
            lb3.pack()
            count = 0
            allpt1,allpt2,allpt3="","",""
            for i in allpath:
                if count%3 == 0:allpt1+='    '+str(i)
                elif count%3 == 1:allpt2+='    '+str(i)
                elif count%3 == 2:allpt3+='    '+str(i)
                count += 1
            lb4 = tk.Label(f3_frame,text=allpt1,font=font3)
            lb4.pack()
            lb5 = tk.Label(f3_frame,text=allpt2,font=font3)
            lb5.pack()
            lb6 = tk.Label(f3_frame,text=allpt3,font=font3)
            lb6.pack()
            for i in allpath:
                if len(i) == min(res1):resmin.append(i)
                if len(i) == max(res1):resmax.append(i)
            lb7 = tk.Label(f3_frame,text='\n-Min path',font=font3)
            lb7.pack()
            allmn1,allmn2 = '',''
            for i in resmin:
                if count%2 == 0:allmn1+='    '+str(i)
                elif count%2 == 1:allmn2+='    '+str(i)
            lb8 = tk.Label(f3_frame,text=allmn1,font=font3)
            lb8.pack()
            lb9 = tk.Label(f3_frame,text=allmn2,font=font3)
            lb9.pack()
            lb10 = tk.Label(f3_frame,text='\n-Max path',font=font3)
            lb10.pack()
            allmx1,allmx2 = '',''
            for i in resmax:
                if count%2 == 0:allmx1+='    '+str(i)
                elif count%2 == 1:allmx2+='    '+str(i)
            lb11 = tk.Label(f3_frame,text=allmx1,font=font3)
            lb11.pack()
            lb12 = tk.Label(f3_frame,text=allmx2,font=font3)
            lb12.pack()
        if res1 == []:
            lb13 = tk.Label(f3_frame,text="\nThere is no path",font=font3)
            lb13.pack()
    delete_pages()
    f3_frame = tk.Frame(main_frame)
    lb1 = tk.Label(f3_frame,text="Source",font=font3)
    lb1.pack()
    e1 = Entry(f3_frame,width=50)
    e1.pack()
    lb2 = tk.Label(f3_frame,text="Destination",font=font3)
    lb2.pack()
    e2 = Entry(f3_frame,width=50)
    e2.pack()
    Submit = Button(f3_frame,text="Submit",command=f3submit)
    Submit.pack()
    f3_frame.pack()

def f4():
    def f4submit():
        liseat,liseaten = [],[]
        lt = e1.get()
        for i in lisedg:
            if i[0] == lt:liseaten.append(i[1])
            elif i[1] == lt:liseat.append(i[0])
        if liseat == []:
            lb2 = tk.Label(f4_frame,text=lt+' not eat any livingthing',font=font2)
            lb2.pack()
        elif liseat != []:
            lb3 = tk.Label(f4_frame,text=lt+' eat '+str(liseat),font=font2)
            lb3.pack()
        if liseaten == []:
            lb4 = tk.Label(f4_frame,text=lt+' is not eaten by any livingthing',font=font2)
            lb4.pack()
        elif liseaten != []:
            lb4 = tk.Label(f4_frame,text=lt+' is eaten by '+str(liseaten),font=font2)
            lb4.pack()
    delete_pages()
    f4_frame = tk.Frame(main_frame)
    lb4 = tk.Label(f4_frame,text="Please input 1 living thing\nthat you want to know information",font=font2)
    lb4.pack()
    e1 = Entry(f4_frame,width=50)
    e1.pack()
    Submit = Button(f4_frame,text="Submit",command=f4submit)
    Submit.pack()
    f4_frame.pack()

def p1():
    global label1,label2,button1
    label1 = Label(root,text = '\nFoodchain Program\n',font=font)
    label1.pack()
    label2 = Label(root,text = '\nPlease choose txt file\n',font=font)
    label2.pack()
    button1 = Button(root,text='Ok',font=font,command=p2)
    button1.pack()

def p2():
    global main_frame
    readfile()

    label1.destroy()
    label2.destroy()
    button1.destroy()

    options_frame = tk.Frame(root,bg='grey')

    label3 = Label(options_frame,text='Please choose function',font=font2)
    button2 = Button(options_frame,text='1.Show all names',font=font2,command=f1)
    button3 = Button(options_frame,text='2.Display graph',font=font2,command=f2)
    button4 = Button(options_frame,text='3.Find min-max path',font=font2,command=f3)
    button5 = Button(options_frame,text='4.Find relation',font=font2,command=f4)
    label3.place(x=10,y=50)
    button2.place(x=10,y=200)
    button3.place(x=10,y=300)
    button4.place(x=10,y=400)
    button5.place(x=10,y=500)

    options_frame.pack(side=tk.LEFT)
    options_frame.pack_propagate(False)
    options_frame.configure(height=1200,width=250)

    main_frame = tk.Frame(root)
    main_frame.pack(side=tk.LEFT)
    main_frame.pack_propagate(False)
    main_frame.configure(height=600,width=1200)

def readfile():
    global lisedg
    lisedg,lisnod = [],[]
    filepath = filedialog.askopenfilename(title="Choose txt file to read",
                                          filetypes=(("text files","*.txt"),
                                                     ("all files","*.*")))
    filer = open(filepath,'r')
    line = filer.readline().rstrip('\n').lower()
    while line != '':
        if len(line.split()) == 2:lisedg.append(tuple(swap(line.split())))
        elif len(line.split()) == 1:lisnod.append(line)
        line = filer.readline().rstrip('\n').lower()
    filer.close()
    network.add_nodes_from(lisnod)
    network.add_edges_from(lisedg)

network = nx.DiGraph()
p1()
root.mainloop()