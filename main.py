import tkinter as tk

import keyboard

import config
from cogs.logs import Logger

root = tk.Tk()


class Display:
    def __init__(self, display):
        self.count = config.main['count_default']
        self.counter = tk.Label(display, text=self.count)
        self.counter.pack()
        keyboard.add_hotkey(config.keybind['increase'], self.increase)
        keyboard.add_hotkey(config.keybind['decrease'], self.decrease)

    def increase(self):
        if config.main['count_max'] > self.count or config.main['count_max'] == 0:
            self.count += 1
            Logger.log('Increasing count => %s' % self.count + ' (+)')
            self.counter['text'] = self.count
        else:
            Logger.note('Maximum count reached')

    def decrease(self):
        if self.count > 0:
            self.count -= 1
            Logger.log('Decreasing count => %s' % self.count + ' (-)')
            self.counter['text'] = self.count
        else:
            Logger.warn('Bottom reached')


Display(root)
root.mainloop()
