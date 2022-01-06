"""
Config file handeling all the configurable options.
"""

'''
Main configuration

Holds all main application settings.
'''
main = {
    "name": "countUPWARDS",
    "version": "0.1.0",

    # Value to start at
    "start_value": 0,
    # Value to reset to
    "reset_value": 0,

    # Change value on keybind press by => [increase, decrease]
    "keybind_value_update": [1, 1],

    # Value (int) to max out at
    "count_max": False,  # False means no limit

    # Value (int) to be the lowest you can go
    'count_bottom': 0,  # False means no limit
}

'''
Keybind configuration
'''
keybind = {
    "increase": "ctrl+up",
    "decrease": "ctrl+down",
    "reset": "ctrl+r",
}

'''
Log configuration

Controls logging behaviour.
'''
logs = {
    "log_dir": "logs",
    "expire_days": 3,
}

'''
Display configurationpp

Holds all display settings.
'''
display = {
    "font_size": 500,
    "foreground": "#ffffff",  # please insert a valid hex color
}
