import tkinter
import tkinter.messagebox

def main():
    flag = True
    def change():
        nonlocal flag
        flag = not flag
        color,msg =("red","hello,world!") if flag else ("blue","goodbye,world!")
        label.config(text=msg,fg=color)
    def quit():
        if tkinter.messagebox.askokcancel("温馨提示：确认退出！"):
            top.quit()

    top = tkinter.Tk()
    top.geometry("240x240")
    top.title("Frist游戏")
    label = tkinter.Label(top,text = "hello,world!",font = "粗体",fg = "green")
    label.pack(expand=1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel,text="修改",command=change)
    button1.pack(side = "left")
    button2 = tkinter.Button(panel,text = "退出",command=quit)
    button2.pack(side = "right")
    panel.pack(side = "bottom")
    tkinter.mainloop()
if __name__ == '__main__':
    main()
