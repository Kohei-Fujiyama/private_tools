# -*- coding: utf-8 -*-

import Tkinter as Tk
import time

# max_inter = 50
# interv = 1
# ini_time = 0
# final_time = time.time()
# count = 0
# status = 0

class StopWatch(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('Simple Stop Watch')
        self.tcount = Tk.Label(self, text=u'00:00', font='Times, 25')
        b1 = Tk.Button(self, text='Start', command=self.start)
        b2 = Tk.Button(self, text='Pause', command=self.pause)
        b3 = Tk.Button(self, text='Reset', command=self.reset)
        b1.grid(row=1, column=0, columnspan=2, padx=5, pady=2, sticky=Tk.W + Tk.E)
        b2.grid(row=1, column=2, columnspan=2, padx=5, pady=2, sticky=Tk.W + Tk.E)
        b3.grid(row=1, column=4, columnspan=2, padx=5, pady=2, sticky=Tk.W + Tk.E)
        self.tcount.grid(row=2, column=0, columnspan=6, padx=0, pady=0, sticky=Tk.W + Tk.E)
        self.pausedt = 0
        self.started = False

    def start(self):
        if self.started == False:
            # ini_time = time.time()
            self.initime = time.time()
            self.started = True
            self.count()

    def count(self):
        if self.started:
            t = time.time() - self.initime + self.pausedt
            self.tcount.config(text='%02d:%02d' % (t / 60, t % 60))
            self.after(100, self.count)
            # self.after(10000, self.count)

    def pause(self):
        if self.started:
            self.pausedt = time.time() - self.initime + self.pausedt
            self.started = False
            # self.tokei.config(text='00:00')

    def reset(self):
        self.initime = time.time()
        self.pausedt = 0
        self.tcount.config(text='00:00')


# for i in range(max_inter):
#     print time.time()
#     time.sleep(interv)
#     final_time = time.time()
#     count = count+1
#
# diff = final_time - (init_time + count)
# ft_fixed = final_time - diff
#
# print ('diff: ' + str(diff))
# print ('fixed time: ' + str(ft_fixed))

if __name__ == '__main__':
    f = StopWatch()
    f.pack()
    f.mainloop()