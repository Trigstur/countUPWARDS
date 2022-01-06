import tkinter as tk

import keyboard

import config
from cogs.logs import Logger

root = tk.Tk()


def flip_hex(hex_value: str) -> str:
    hex_value = hex_value[1:]
    rgb = (hex_value[0:2], hex_value[2:4], hex_value[4:6])
    comp = ['%X' % (0 if (15 - int(a, 16)) <= 7 else 15) for a in rgb]
    return '#' + ''.join(comp)


class Display:
    def __init__(self, display):
        self.count = config.main['start_value']
        self.counter = tk.Label(
            display,
            text=self.count,
            fg=config.display['foreground'],
            bg=flip_hex(config.display['foreground']),
            font=("Helvetica", config.display['font_size'])
        )
        self.counter.pack()
        keyboard.add_hotkey(config.keybind['increase'], self.increase)
        keyboard.add_hotkey(config.keybind['decrease'], self.decrease)
        keyboard.add_hotkey(config.keybind['reset'], self.reset)

    def increase(self):
        try:
            if config.main['count_max'] > self.count + config.main['keybind_value_update'][0] or config.main[
                'count_max'] == False:
                self.count += config.main['keybind_value_update'][0]
                Logger.log('Increasing count => %s' % self.count + ' (+)')
                self.counter['text'] = self.count
            else:
                self.count = config.main['count_max']
                self.counter['text'] = self.count
                Logger.log('Setting count => %s' % self.count + ' ( set )')
                Logger.note('Maximum count reached')
        except Exception as e:
            Logger.error(e)

    def decrease(self):
        try:

            if self.count - config.main['keybind_value_update'][1] > config.main['count_bottom'] or config.main[
                'count_bottom'] == True:
                self.count -= config.main['keybind_value_update'][1]
                Logger.log('Decreasing count => %s' % self.count + ' (-)')
                self.counter['text'] = self.count
            else:
                self.count = config.main['count_bottom']
                self.counter['text'] = self.count
                Logger.log('Setting count => %s' % self.count + ' ( set )')
                Logger.note('Bottom count reached')
        except Exception as e:
            Logger.error(e)

    def reset(self):
        try:
            self.count = config.main['reset_value']
            Logger.warnnote('Resetting count => %s' % self.count + ' ( reset )')
            self.counter['text'] = self.count
        except Exception as e:
            Logger.error(e)

Display(root)
root.mainloop()
