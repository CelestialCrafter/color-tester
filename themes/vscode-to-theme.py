# made by fou3fou3, modified by celestial

import sys
import json

BACKGROUND = "editor.background"
SURFACE = "menu.background"
OVERLAY = "input.background"
MUTED = "terminalCursor.foreground"
SUBTLE = "icon.foreground"
TEXT = "input.foreground"
PRIMARY = "errorForeground"
SECONDARY = "textPreformat.foreground"
ACCENT = "button.background"
HIGHLIGHT = "panel.border"


def extract_colors(vsc_theme_data):
    color_data = vsc_theme_data["colors"]
    return {
        "background": color_data[BACKGROUND],
        "surface": color_data[SURFACE],
        "overlay": color_data[OVERLAY],
        "muted": color_data[MUTED],
        "subtle": color_data[SUBTLE],
        "text": color_data[TEXT],
        "primary": color_data[PRIMARY],
        "secondary": color_data[SECONDARY],
        "accent": color_data[ACCENT],
        "highlight": color_data[HIGHLIGHT]
    }

def write_theme(colors, output_path):
    template = open('template.toml', 'r').read()
    populated = template.format(**colors)
    open(output_path, 'w').write(populated)

if __name__ == "__main__":
    vsc_theme_data = json.load(open(sys.argv[1], 'r'))
    output_path = sys.argv[1].replace('.json', '.toml')
    colors =  extract_colors(vsc_theme_data)
    write_theme(colors, output_path)

