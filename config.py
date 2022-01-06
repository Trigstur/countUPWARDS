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
    "count_default": 0,
    "count_max": 0,  # 0 means no limit
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
