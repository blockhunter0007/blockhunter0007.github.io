import json
import customtkinter as ctk
import threading
import time
import keyboard
from pathlib import Path
import sys
import ctypes
import random
import pyautogui

if getattr(sys, 'frozen', False):
    #PyInstaller
    appstandalone = Path(sys.executable).resolve()
    apppath = Path(sys.executable).resolve().parent
else:
    #Normal
    appstandalone = Path(__file__).resolve()
    apppath = Path(__file__).resolve().parent
DATA_DIR = apppath / "data"
if not DATA_DIR.exists():
    DATA_DIR.mkdir(parents=True)
config_path = DATA_DIR / "config.json"
if not config_path.exists():
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump({}, f, ensure_ascii=False, indent=4)
with open(config_path, "r", encoding="utf-8") as fd:
    try:
        config = json.load(fd)
    except:
        config = {}


my_theme = {"CTk":{"fg_color":["#2b2b2b","#1f1f1f"],"top_fg_color":["#1f1f1f","#2b2b2b"],"border_color":["#3d3d3d","#3d3d3d"],"text_color":["#ffffff","#ffffff"],"hover_color":["#a64dff","#b366ff"]},"CTkButton":{"fg_color":["#9b59b6","#8e44ad"],"hover_color":["#a86bd8","#9b59b6"],"text_color":["#ffffff","#ffffff"],"text_color_disabled":["#7f7f7f","#7f7f7f"],"corner_radius":8,"border_width":0,"border_color":["#8e44ad","#7a33a0"]},"CTkFrame":{"fg_color":["#1f1f1f","#2b2b2b"],"border_color":["#9b59b6","#8e44ad"],"corner_radius":8,"border_width":2},"CTkLabel":{"fg_color":["transparent","transparent"],"text_color":["#ffffff","#ffffff"],"corner_radius":2},"CTkEntry":{"fg_color":["#2b2b2b","#1f1f1f"],"text_color":["#ffffff","#ffffff"],"placeholder_text_color":["#a0a0a0","#b0b0b0"],"border_color":["#8e44ad","#7a33a0"],"corner_radius":8,"border_width":2},"CTkCheckBox":{"fg_color":["#9b59b6","#8e44ad"],"checkmark_color":["#ffffff","#ffffff"],"hover_color":["#a86bd8","#9b59b6"],"border_color":["#8e44ad","#7a33a0"],"corner_radius":4,"border_width":2,"text_color":["#ffffff","#ffffff"],"text_color_disabled":["#7f7f7f","#7f7f7f"]},"CTkSwitch":{"button_color":["#9b59b6","#8e44ad"],"button_hover_color":["#a86bd8","#9b59b6"],"fg_color":["#2b2b2b","#1f1f1f"],"progress_color":["#a64dff","#b366ff"],"border_color":["#8e44ad","#7a33a0"],"corner_radius":10,"border_width":2},"CTkSlider":{"button_color":["#9b59b6","#8e44ad"],"button_hover_color":["#a86bd8","#9b59b6"],"progress_color":["#a64dff","#b366ff"],"fg_color":["#2b2b2b","#1f1f1f"],"border_color":["#8e44ad","#7a33a0"],"corner_radius":10,"border_width":2,"button_corner_radius":10,"button_length":20,"button_width":20},"CTkProgressBar":{"progress_color":["#a64dff","#b366ff"],"fg_color":["#2b2b2b","#1f1f1f"],"corner_radius":8,"border_width":0,"border_color":["#8e44ad","#7a33a0"]},"CTkOptionMenu":{"fg_color":["#2b2b2b","#1f1f1f"],"button_color":["#9b59b6","#8e44ad"],"button_hover_color":["#a86bd8","#9b59b6"],"text_color":["#ffffff","#ffffff"],"text_color_disabled":["#7f7f7f","#7f7f7f"],"menu_fg_color":["#1f1f1f","#2b2b2b"],"menu_text_color":["#ffffff","#ffffff"],"corner_radius":8,"border_width":2,"border_color":["#8e44ad","#7a33a0"]},"CTkScrollbar":{"fg_color":["#2b2b2b","#1f1f1f"],"button_color":["#9b59b6","#8e44ad"],"button_hover_color":["#a86bd8","#9b59b6"],"border_color":["#8e44ad","#7a33a0"],"corner_radius":8,"border_width":2},"CTkToplevel":{"fg_color":["#2b2b2b","#1f1f1f"],"border_color":["#9b59b6","#8e44ad"],"corner_radius":10,"border_width":2},"CTkFont":{"family":"Arial","size":16,"weight":"normal"},"DropdownMenu":{"fg_color":["#1f1f1f","#2b2b2b"],"hover_color":["#9b59b6","#8e44ad"],"border_color":["#8e44ad","#7a33a0"],"text_color":["#ffffff","#ffffff"],"text_color_disabled":["#7f7f7f","#7f7f7f"],"corner_radius":6,"border_width":1},"CTkRadioButton":{"fg_color":["#9b59b6","#8e44ad"],"fg_color_checked":["#a64dff","#b366ff"],"hover_color":["#a86bd8","#9b59b6"],"border_color":["#8e44ad","#7a33a0"],"text_color":["#ffffff","#ffffff"],"text_color_disabled":["#7f7f7f","#7f7f7f"],"corner_radius":6,"border_width":2,"border_width_checked":2,"border_width_unchecked":2}}
standart_theme = False
client_theme = False
custom_theme = False
cheathub = False
try:
    cheathub_downloaded = apppath / ".cheathub"
    if not cheathub_downloaded.exists():
        theme_json_path = DATA_DIR / "theme.json"
        if not theme_json_path.exists():
            with open(theme_json_path, "w") as fp:
                json.dump(my_theme, fp)
        client_theme = True
    else:
        cheathub = True
        read_theme_json_path = apppath.parent.parent / "data" / "settings.json"
        cheathub_main_path = apppath.parent.parent
        try:
            with open(read_theme_json_path, "r") as fp:
                daten = json.load(fp)
            print(daten["theme"])
            if daten["theme"] in ["green", "blue", "dark-blue"]:
                standart_theme = True
                theme_json_path = None
            else:
                theme_json_path = cheathub_main_path / "themes" / daten["theme"]
                custom_theme = True
                ctk.set_default_color_theme(str(theme_json_path))
        except Exception as e:
            print(e)
            theme_json_path = DATA_DIR / "theme.json"
            if not theme_json_path.exists():
                with open(theme_json_path, "w") as fp:
                    json.dump(my_theme, fp)
            client_theme = True
except:
    theme_json_path = DATA_DIR / "theme.json"
    if not theme_json_path.exists():
        with open(theme_json_path, "w") as fp:
            json.dump(my_theme, fp)
    client_theme = True





MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
def robust_click(button_type):
    """
    uses ctypes to perform a mouse click with a hold time of 30ms
    button_type: "left" or "right"
    1. Press
    2. Hold for 30ms
    3. Release
    To bypass anti-cheat systems that detects win32 clicks we use user32.
    """
    if button_type == "left":
        down = MOUSEEVENTF_LEFTDOWN
        up = MOUSEEVENTF_LEFTUP
    else: # right
        down = MOUSEEVENTF_RIGHTDOWN
        up = MOUSEEVENTF_RIGHTUP

    # 1. Press
    start = time.perf_counter()
    ctypes.windll.user32.mouse_event(down, 0, 0, 0, 0)
    
    # 2. Hold for 30ms
    while (time.perf_counter() - start) < 0.03:
        pass
    
    # 3. Release
    ctypes.windll.user32.mouse_event(up, 0, 0, 0, 0)

def save_settings():
    global config
    with open(config_path, "w") as fp:
        json.dump(config, fp)







class AutoClickerGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        global config
        if "autoclicker" not in config:
            config["autoclicker"] = {}
        if "cps_min" not in config["autoclicker"]:
            config["autoclicker"]["cps_min"] = 15
        if "cps_max" not in config["autoclicker"]:
            config["autoclicker"]["cps_max"] = 20
        if "button" not in config["autoclicker"]:
            config["autoclicker"]["button"] = "left"
        if "trigger" not in config["autoclicker"]:
            config["autoclicker"]["trigger"] = "f8"
        if "low_high_level_click" not in config["autoclicker"]:
            config["autoclicker"]["low_high_level_click"] = "low"
        self.title("Clicker")
        self.geometry("200x500")
        print(client_theme, standart_theme, custom_theme, str(theme_json_path))
        if client_theme:
            print("Client Theme Loaded")
            ctk.set_default_color_theme(str(theme_json_path))
        elif standart_theme:
            print("Standard Theme Loaded")
            ctk.set_default_color_theme(daten["theme"])
        elif custom_theme:
            print("Custom Theme Loaded")
            theme_path = cheathub_main_path / "themes" / daten["theme"]
            ctk.set_default_color_theme(str(theme_path))
        #ctk.set_default_color_theme("blue")
        if cheathub:
            try:
                self.iconbitmap(str(apppath.parent.parent / "assets" / "icon.ico"))
            except:
                pass
        self.attributes("-topmost", True)
        config["autoclicker"]
        self.running = False
        self.thread = None
        self.resizable(False, False)
        # GUI Elemente
        self.low_high_level_click = config["autoclicker"]["low_high_level_click"]
        self.low_high_level_click_dropdown = ctk.CTkOptionMenu(self, values=["low", "high"], command=lambda event: self.set_low_high_level_click(event))
        self.low_high_level_click_dropdown.set(self.low_high_level_click)
        self.low_high_level_click_dropdown.pack(pady=10)
        self.cps_label = ctk.CTkLabel(self, text="CPS (Clicks per second):")
        self.cps_label.pack(pady=(20,0))
        self.cps_min_label = ctk.CTkLabel(self, text=f"CPS Min: {config["autoclicker"]["cps_min"]}")
        self.cps_min_label.pack(pady=(10,0))
        self.cps_min_slider = ctk.CTkSlider(
            self,
            from_=1,
            to=35,
            number_of_steps=4900,
            command=self.update_cps_min
        )
        self.cps_min_slider.set(config["autoclicker"]["cps_min"])
        self.cps_min_slider.pack(pady=5)

        # CPS Maximum Slider
        self.cps_max_label = ctk.CTkLabel(self, text=f"CPS Max: {config["autoclicker"]["cps_max"]}")
        self.cps_max_label.pack(pady=(10,0))
        self.cps_max_slider = ctk.CTkSlider(
            self,
            from_=1,
            to=35,
            number_of_steps=4900,
            command=self.update_cps_max
        )
        self.cps_max_slider.set(config["autoclicker"]["cps_max"])
        self.cps_max_slider.pack(pady=5)
        self.button_label = ctk.CTkLabel(self, text="Button:")
        self.button_label.pack(pady=(10,0))
        
        self.button_var = ctk.StringVar(value=config["autoclicker"]["button"])
        self.radio_frame = ctk.CTkFrame(self, fg_color="transparent", border_width=0)
        self.radio_frame.pack(pady=5)
        
        self.left_radio = ctk.CTkRadioButton(self.radio_frame, text="Left", variable=self.button_var, value="left")
        self.left_radio.pack(side="left", padx=10)
        self.right_radio = ctk.CTkRadioButton(self.radio_frame, text="Right", variable=self.button_var, value="right")
        self.right_radio.pack(side="left", padx=10)

        self.trigger_label = ctk.CTkLabel(self, text="Hotkey:")
        self.trigger_label.pack(pady=(10,0))
        self.trigger_entry = ctk.CTkEntry(self)
        self.trigger_entry.insert(1, config["autoclicker"]["trigger"])
        self.trigger_entry.pack(pady=5)

        self.save_btn = ctk.CTkButton(self, text="Save", command=self.save_settings)
        self.save_btn.pack(pady=10)

        self.status_label = ctk.CTkLabel(self, text="STATE: STOPPED", text_color="#ff5555", font=("Arial", 16, "bold"))
        self.status_label.pack(pady=10)


        self.monitor_thread = threading.Thread(target=self.monitor_trigger, daemon=True)
        self.monitor_thread.start()


    def set_low_high_level_click(self, value):
        global config
        self.low_high_level_click = value
        config["autoclicker"]["low_high_level_click"] = value
        save_settings()
        if value == "low":
            self.cps_max_slider.configure(from_=1, to=35, number_of_steps=4900)
            self.cps_min_slider.configure(from_=1, to=35, number_of_steps=4900)
            if float(self.cps_max_slider.get()) > 35:
                self.cps_max_slider.set(35)
            if float(self.cps_min_slider.get()) > 35:
                self.cps_min_slider.set(35)
        else:
            self.cps_max_slider.configure(from_=1, to=10000, number_of_steps=100000)
            self.cps_min_slider.configure(from_=1, to=10000, number_of_steps=100000)
        self.update_idletasks()

    def update_cps_min(self, value):
        value = round(float(value), 1)
        self.cps_min_label.configure(text=f"CPS Min: {value}")

    def update_cps_max(self, value):
        value = round(float(value), 1)
        self.cps_max_label.configure(text=f"CPS Max: {value}")


    def save_settings(self):
        global config
        try:
            max_cps_val = float(self.cps_max_slider.get())
            min_cps_val = float(self.cps_min_slider.get())
        except:
            max_cps_val = 10
            min_cps_val = 10
        
        config["autoclicker"]["cps_min"] = min_cps_val
        config["autoclicker"]["cps_max"] = max_cps_val
        config["autoclicker"]["button"] = self.button_var.get()
        config["autoclicker"]["trigger"] = self.trigger_entry.get()
        with open(config_path, "w") as fp:
            json.dump(config, fp)
        print("Einstellungen gespeichert.")


    def toggle_clicker(self):
        if self.running:
            self.running = False
            self.status_label.configure(text="STATE: STOPPED", text_color="#ff5555")
        else:
            self.running = True
            self.status_label.configure(text="STATE: RUNNING", text_color="#55ff55")
            self.thread = threading.Thread(target=self.run_clicker)
            self.thread.start()


    def monitor_trigger(self):
        while True:
            trig = config["autoclicker"]["trigger"]
            if trig and keyboard.is_pressed(trig):
                self.toggle_clicker()
                time.sleep(0.4) # Entprellen
            time.sleep(0.05)


    def run_clicker(self):
        min_cps = config["autoclicker"]["cps_min"]
        max_cps = config["autoclicker"]["cps_max"]
        btn = config["autoclicker"]["button"]
        if self.low_high_level_click == "low":
            while self.running:
                robust_click(btn)
                sleeping_time_random = random.uniform(min_cps, max_cps)
                print(sleeping_time_random)
                sleeping_time_divided = 1 / sleeping_time_random - 0.03
                if sleeping_time_divided < 0:
                    sleeping_time_divided = 0.001
                print(sleeping_time_divided)
                time.sleep(sleeping_time_divided)
        else:
            while self.running:
                pyautogui.click(button=btn)
                sleeping_time_random = random.uniform(min_cps, max_cps)
                sleeping_time_divided = 1 / sleeping_time_random
                time.sleep(sleeping_time_divided)


AutoClickerGUI().mainloop()