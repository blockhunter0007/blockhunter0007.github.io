import os
import json
import customtkinter as ctk
import pyautogui
import threading
import time
import keyboard
from pathlib import Path
import sys

if getattr(sys, 'frozen', False):
    # Wenn mit PyInstaller gebaut
    appstandalone = Path(sys.executable).resolve()
    apppath = Path(sys.executable).resolve().parent
else:
    # Wenn als normales Python-Skript ausgeführt
    appstandalone = Path(__file__).resolve()
    apppath = Path(__file__).resolve().parent
my_theme = {"CTk":{"fg_color":["#2b2b2b","#1f1f1f"],"top_fg_color":["#1f1f1f","#2b2b2b"],"border_color":["#3d3d3d","#3d3d3d"],"text_color":["#ffffff","#ffffff"],"hover_color":["#a64dff","#b366ff"]},"CTkTextbox": {"fg_color": ["#2b2b2b","#1f1f1f"],"text_color": ["#ffffff","#ffffff"],"placeholder_text_color": ["#a0a0a0","#b0b0b0"],"border_color": ["#8e44ad","#7a33a0"],"corner_radius": 8,"border_width": 2,"scrollbar_button_color": ["#9b59b6","#8e44ad"],"scrollbar_button_hover_color": ["#a86bd8","#9b59b6"],"scrollbar_fg_color": ["#2b2b2b","#1f1f1f"],"scrollbar_border_color": ["#8e44ad","#7a33a0"]},"CTkRadioButton":{"fg_color":["#2b2b2b","#1f1f1f"],"fg_color_checked":["#9b59b6","#8e44ad"],"hover_color":["#a86bd8","#9b59b6"],"checkmark_color":["#ffffff","#ffffff"],"border_color":["#8e44ad","#7a33a0"],"border_width_checked":3,"border_width_unchecked":2,"text_color":["#ffffff","#ffffff"],"text_color_disabled":["#7f7f7f","#7f7f7f"],"corner_radius":8},"CTkButton":{"fg_color":["#9b59b6","#8e44ad"],"hover_color":["#a86bd8","#9b59b6"],"text_color":["#ffffff","#ffffff"],"text_color_disabled":["#7f7f7f","#7f7f7f"],"corner_radius":8,"border_width":0,"border_color":["#8e44ad","#7a33a0"]},"CTkFrame":{"fg_color":["#1f1f1f","#2b2b2b"],"top_fg_color": ["#2b2b2b","#1f1f1f"],"border_color":["#9b59b6","#8e44ad"],"corner_radius":8,"border_width":2},"CTkLabel":{"fg_color":["transparent","transparent"],"text_color":["#ffffff","#ffffff"],"corner_radius":0},"CTkEntry":{"fg_color":["#2b2b2b","#1f1f1f"],"text_color":["#ffffff","#ffffff"],"placeholder_text_color":["#a0a0a0","#b0b0b0"],"border_color":["#8e44ad","#7a33a0"],"corner_radius":8,"border_width":2},"CTkCheckBox":{"fg_color":["#9b59b6","#8e44ad"],"checkmark_color":["#ffffff","#ffffff"],"hover_color":["#a86bd8","#9b59b6"],"border_color":["#8e44ad","#7a33a0"],"corner_radius":4,"border_width":2,"text_color":["#ffffff","#ffffff"],"text_color_disabled":["#7f7f7f","#7f7f7f"]},"CTkSwitch":{"button_color":["#9b59b6","#8e44ad"],"button_hover_color":["#a86bd8","#9b59b6"],"fg_color":["#2b2b2b","#1f1f1f"],"progress_color":["#a64dff","#b366ff"],"border_color":["#8e44ad","#7a33a0"],"corner_radius":10,"border_width":2},"CTkSlider":{"button_color":["#9b59b6","#8e44ad"],"button_hover_color":["#a86bd8","#9b59b6"],"progress_color":["#a64dff","#b366ff"],"fg_color":["#2b2b2b","#1f1f1f"],"border_color":["#8e44ad","#7a33a0"],"corner_radius":10,"border_width":2},"CTkProgressBar":{"progress_color":["#a64dff","#b366ff"],"fg_color":["#2b2b2b","#1f1f1f"],"corner_radius":8,"border_width":0,"border_color":["#8e44ad","#7a33a0"]},"CTkOptionMenu":{"fg_color":["#2b2b2b","#1f1f1f"],"button_color":["#9b59b6","#8e44ad"],"button_hover_color":["#a86bd8","#9b59b6"],"text_color":["#ffffff","#ffffff"],"text_color_disabled":["#7f7f7f","#7f7f7f"],"menu_fg_color":["#1f1f1f","#2b2b2b"],"menu_text_color":["#ffffff","#ffffff"],"corner_radius":8,"border_width":2,"border_color":["#8e44ad","#7a33a0"]},"CTkScrollbar":{"fg_color":["#2b2b2b","#1f1f1f"],"button_color":["#9b59b6","#8e44ad"],"button_hover_color":["#a86bd8","#9b59b6"],"border_color":["#8e44ad","#7a33a0"],"corner_radius":8,"border_width":2},"CTkToplevel":{"fg_color":["#2b2b2b","#1f1f1f"],"border_color":["#9b59b6","#8e44ad"],"corner_radius":10,"border_width":2},"CTkFont":{"family":"Arial","size":16,"weight":"normal"},"DropdownMenu":{"fg_color":["#1f1f1f","#2b2b2b"],"hover_color":["#9b59b6","#8e44ad"],"border_color":["#8e44ad","#7a33a0"],"text_color":["#ffffff","#ffffff"],"text_color_disabled":["#7f7f7f","#7f7f7f"],"corner_radius":6,"border_width":1}}

DATA_DIR = apppath / "data"
DATA_FILE = DATA_DIR / "data.json"
theme_json_path = DATA_DIR / "theme.json"
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

if not DATA_DIR.exists():
    DATA_DIR.mkdir(parents=True)
if not DATA_FILE.exists():
    with open(DATA_FILE, "w") as fp:
        json.dump({"cps": 10, "button": "left", "trigger": "f8"}, fp)
if not theme_json_path.exists():
    with open(theme_json_path, "w") as fp:
        json.dump(my_theme, fp)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme(str(theme_json_path))
with open(DATA_FILE, "r") as fp:
    settings = json.load(fp)

class AutoClickerGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Autoclicker GUI")
        self.geometry("800x400")
        self.running = False
        self.thread = None

        self.cps_label = ctk.CTkLabel(self, text="Klicks pro Sekunde (CPS):")
        self.cps_label.pack()
        self.cps_entry = ctk.CTkEntry(self)
        self.cps_entry.insert(0, str(settings.get("cps", 10)))
        self.cps_entry.pack()

        self.button_label = ctk.CTkLabel(self, text="Maustaste:")
        self.button_label.pack()
        self.button_var = ctk.StringVar(value=settings.get("button", "left"))
        self.left_radio = ctk.CTkRadioButton(self, text="Links", variable=self.button_var, value="left")
        self.left_radio.pack(side="left", padx=20)
        self.right_radio = ctk.CTkRadioButton(self, text="Rechts", variable=self.button_var, value="right")
        self.right_radio.pack(side="left", padx=20)

        self.trigger_label = ctk.CTkLabel(self, text="Trigger-Taste (z. B. 'f8'):")
        self.trigger_label.pack()
        self.trigger_entry = ctk.CTkEntry(self)
        self.trigger_entry.insert(0, settings.get("trigger", "f8"))
        self.trigger_entry.pack()

        self.save_btn = ctk.CTkButton(self, text="Einstellungen Speichern", command=self.save_settings)
        self.save_btn.pack(pady=(10, 5))

        self.status_label = ctk.CTkLabel(self, text="Status: gestoppt")
        self.status_label.pack(pady=(5, 0))

        self.toggle_btn = ctk.CTkButton(self, text="Manuell starten", command=self.toggle_clicker)
        self.toggle_btn.pack(pady=(5, 10))

        # Start trigger key monitor thread
        self.monitor_thread = threading.Thread(target=self.monitor_trigger, daemon=True)
        self.monitor_thread.start()

    def save_settings(self):
        cps_value = max(1, int(self.cps_entry.get()))
        button_value = self.button_var.get()
        trigger_value = self.trigger_entry.get()
        with open(DATA_FILE, "w") as fp:
            json.dump({"cps": cps_value, "button": button_value, "trigger": trigger_value}, fp)
        settings["cps"] = cps_value
        settings["button"] = button_value
        settings["trigger"] = trigger_value

    def toggle_clicker(self):
        if self.running:
            self.running = False
            self.status_label.configure(text="Status: gestoppt")
            self.toggle_btn.configure(text="Manuell starten")
        else:
            self.running = True
            self.status_label.configure(text="Status: läuft")
            self.toggle_btn.configure(text="Manuell stoppen")
            self.thread = threading.Thread(target=self.run_clicker)
            self.thread.start()

    def monitor_trigger(self):
        while True:
            if keyboard.is_pressed(settings["trigger"]):
                self.toggle_clicker()
                time.sleep(0.5)  # debounce so toggling isn't instant
            time.sleep(0.05)

    def run_clicker(self):
        click_button = settings["button"]
        while self.running:
            pyautogui.click(button=click_button)
            #if settings["cps"] >=100:
            #    pass
            #else:
            #    time.sleep(1 / settings["cps"])
            time.sleep(1 / settings["cps"])
        self.thread = None

if __name__ == "__main__":
    app = AutoClickerGUI()
    app.mainloop()