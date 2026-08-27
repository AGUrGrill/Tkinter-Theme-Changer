import tkinter as tk
from tkinter import ttk, colorchooser, filedialog
from enum import Enum

PROGRAM_NAME = "Theme Changer"
VERSION_NUMBER = "v6"

f"""
{PROGRAM_NAME} {VERSION_NUMBER}
Created by Ashton Erkl.

Provides a way to easily swap between color themes for any tkinter program.

Features:
    Classes: 
        ThemeChanger() - The main utility of the package. Allows for setting global theme, updating all widgets to specified theme, and adding new themes to global list.
        Theme() - Used for creating and modifying custom themes.
        ThemeChoiceWindow() - GUI for swapping between themes that have been added to the passed ThemeChanger class.
        ThemeCreatorWindow() - GUI for creating your own custom themes and allows for saving and adding of created theme to program.
    
    Enums:
        ThemeType - Used to specify the foreground color of a widget. 
            [Ex: label = tk.Label(root, text="Issue")     label.theme_type = ThemeType.ERROR     label.pack()]
        
"""

GLOBAL_X_PADDING: int = 25
GLOBAL_Y_PADDING: int = 10
STANDARD_WIDTH: int = 35
STANDARD_ENTRY_WIDTH: int = 20

class ThemeType(Enum):
    """
    ThemeType - Used to specify the foreground color of a widget. 
        [Ex: label = tk.Label(root, text="Issue")     
        label.theme_type = ThemeType.ERROR     
        label.pack()]
    """
    ERROR = 0
    SUCCESS = 1
    ACCEPT = 2

class Theme():
    """
    Used for creating and modifying custom themes.
    """
    name: str = "None"
    bg_color: str = ""
    bg_color_alt: str = ""
    btn_color: str = ""
    btn_color_active: str = ""
    btn_fg_color: str = ""
    fg_color: str = ""
    fg_color_disabled: str = ""
    fg_color_error: str = ""
    fg_color_success: str = ""
    fg_color_accept: str = ""

    def __init__(self, theme_name=name, background_color=bg_color, background_color_alt=bg_color_alt, button_color=btn_color, button_color_active=btn_color_active, button_foreground_color=btn_fg_color,
                    foreground_color=fg_color, foreground_color_disabled=fg_color_disabled, foreground_color_error=fg_color_error, foreground_color_success=fg_color_success, foreground_color_accept=fg_color_accept):
        self.name = theme_name
        self.bg_color = background_color
        self.bg_color_alt = background_color_alt
        self.btn_color = button_color
        self.btn_color_active = button_color_active
        self.btn_fg_color = button_foreground_color
        self.fg_color = foreground_color
        self.fg_color_disabled = foreground_color_disabled
        self.fg_color_error = foreground_color_error
        self.fg_color_success = foreground_color_success
        self.fg_color_accept = foreground_color_accept

    def update_bg_color(self, color: str):
        self.bg_color = color
    
    def update_bg_color_alt(self, color: str):
        self.bg_color_alt = color
    
    def update_btn_color(self, color: str):
        self.btn_color = color
    
    def update_btn_color_active(self, color: str):
        self.btn_color_active = color

    def update_btn_fg_color(self, color: str):
        self.btn_fg_color = color

    def update_fg_color(self, color: str):
        self.fg_color = color

    def update_fg_color_disabled(self, color: str):
        self.fg_color_disabled = color

    def update_fg_color_error(self, color: str):
        self.fg_color_error = color

    def update_fg_color_success(self, color: str):
        self.fg_color_success = color

    def update_fg_color_accept(self, color: str):
        self.fg_color_accept = color

light_theme = Theme(
    theme_name="light", 
    background_color="white", 
    background_color_alt="snow", 
    button_color="ghostwhite", 
    button_color_active="gainsboro", 
    button_foreground_color="black", 
    foreground_color="black", 
    foreground_color_disabled="gray60", 
    foreground_color_error="red", 
    foreground_color_success="green",
    foreground_color_accept="blue"
)
dark_theme = Theme(
    theme_name="dark", 
    background_color="gray40", 
    background_color_alt="gray45", 
    button_color="gray50", 
    button_color_active="gray55",
    button_foreground_color="whitesmoke",  
    foreground_color="whitesmoke", 
    foreground_color_disabled="lightgray",
    foreground_color_error="firebrick3", 
    foreground_color_success="lawngreen",
    foreground_color_accept="blue"
)
girly_pop_theme = Theme(
    theme_name="girlypop", 
    background_color="mediumorchid1", 
    background_color_alt="darkorchid1", 
    button_color="deeppink", 
    button_color_active="hotpink", 
    button_foreground_color="whitesmoke", 
    foreground_color="whitesmoke", 
    foreground_color_disabled="lightpurple",
    foreground_color_error="deeppink4", 
    foreground_color_success="seagreen",
    foreground_color_accept="blue"
)
coffee_theme = Theme(
    theme_name="coffee", 
    background_color="peachpuff4", 
    background_color_alt="bisque4", 
    button_color="bisque3",
    button_color_active="bisque4", 
    button_foreground_color="ghostwhite",
    foreground_color="ghostwhite", 
    foreground_color_disabled="gray90",
    foreground_color_error="red3", 
    foreground_color_success="green3",
    foreground_color_accept="cornflowerblue"
)
torrent_theme = Theme(
    theme_name="torrent", 
    background_color="#4d6a9c", 
    background_color_alt="#2e4a7c", 
    button_color="whitesmoke",
    button_color_active="SystemButtonFace", 
    button_foreground_color="#2e4a7c",
    foreground_color="white", 
    foreground_color_disabled="lightsteelblue",
    foreground_color_error="red3", 
    foreground_color_success="springgreen3",
    foreground_color_accept="royalblue3"
)
snowwitch_theme = Theme(
    theme_name="snowwitch", 
    background_color="white", 
    background_color_alt="snow", 
    button_color="#F1E1FE", 
    button_color_active="#E6C5FF", 
    button_foreground_color="darkorchid4", 
    foreground_color="darkorchid4", 
    foreground_color_disabled="purple4", 
    foreground_color_error="red", 
    foreground_color_success="green",
    foreground_color_accept="blue"
)

class ThemeChanger():
    """
    The main utility of the package. Allows for setting global theme, updating all widgets to specified theme, and adding new themes to global list.
    """
    name: str = ""
    bg_color: str = ""
    bg_color_alt: str = ""
    btn_color: str = ""
    btn_color_active: str = ""
    btn_fg_color: str = ""
    fg_color: str = ""
    fg_color_disabled: str = ""
    fg_color_error: str = ""
    fg_color_success: str = ""
    fg_color_accept: str = ""

    default_themes: list[Theme] = [light_theme, dark_theme, girly_pop_theme, torrent_theme, coffee_theme, snowwitch_theme]
    curr_theme: Theme = None
    prev_theme: Theme = None

    def add_theme_to_defaults(self, theme: Theme):
        """
        Adds theme to default theme list that is loaded with the theme changer UI.
        """
        self.default_themes.append(theme)

    def set_global_theme(self, theme_choice: Theme):
        """
        Sets the global theme to use with update_theme_widgets.
        """
        
        self.prev_theme = self.curr_theme
        if self.prev_theme == None:
            self.prev_theme = theme_choice
        self.curr_theme = theme_choice
        self.name = theme_choice.name
        self.bg_color = theme_choice.bg_color
        self.bg_color_alt = theme_choice.bg_color_alt
        self.btn_color = theme_choice.btn_color
        self.btn_color_active = theme_choice.btn_color_active
        self.btn_fg_color = theme_choice.btn_fg_color
        self.fg_color = theme_choice.fg_color
        self.fg_color_disabled = theme_choice.fg_color_disabled
        self.fg_color_error = theme_choice.fg_color_error
        self.fg_color_success = theme_choice.fg_color_success
        self.fg_color_accept = theme_choice.fg_color_accept
        
    def update_theme_widgets(self, parent: tk.Tk):
        """
        Updates all widgets and nested widgets with the selected theme (if none, chooses from global automatically).

        Special color codes can be applied via: .theme_type = ThemeType.(COLOR TYPE HERE):
            ERROR -> foreground_color_error [For errors, cancellation, etc...]
            SUCCESS -> foreground_color_success [For success, correctness, etc...]
            ACCEPT -> foreground_color_accept [For accepting, guiding user, etc...]
        """
        parent.configure(background=self.bg_color)
        self._change_all_menu_colors(parent)
        self._change_all_listbox_colors(parent)
        self._change_all_label_colors(parent)
        self._change_all_entry_colors(parent)
        self._change_all_frame_colors(parent)
        self._change_all_button_colors(parent)
        self._change_all_text_colors(parent)
        self._change_all_radiobutton_colors(parent)
        self._change_all_checkbutton_colors(parent)
        self._change_all_spinbox_colors(parent)
        self._change_all_scale_colors(parent)
        self._change_all_treeview_colors(parent)
    
    def _change_all_button_colors(self, parent: tk.Tk):
        for widget in parent.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(background=self.btn_color, activebackground=self.btn_color_active) 
                self._determine_text_color(widget)
            if widget.winfo_children():
                self._change_all_button_colors(widget)

    def _change_all_frame_colors(self, parent: tk.Tk):
        for widget in parent.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.configure(background=self.bg_color) 
            if widget.winfo_children():
                self._change_all_frame_colors(widget)

    def _change_all_label_colors(self, parent: tk.Tk):
        for widget in parent.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(background=self.bg_color) 
                self._determine_text_color(widget)
            if widget.winfo_children():
                self._change_all_label_colors(widget)

    def _change_all_entry_colors(self, parent: tk.Tk):
        for widget in parent.winfo_children():
            if isinstance(widget, tk.Entry):
                try:
                    widget.configure(background=self.bg_color_alt, disabledbackground=self.bg_color) 
                    self._determine_text_color(widget)
                except:
                    None
            if widget.winfo_children():
                self._change_all_entry_colors(widget)

    def _change_all_text_colors(self, parent: tk.Tk):
        for widget in parent.winfo_children():
            if isinstance(widget, tk.Text):
                widget.configure(background=self.bg_color_alt) 
                self._determine_text_color(widget)
            if widget.winfo_children():
                self._change_all_text_colors(widget)

    def _change_all_radiobutton_colors(self, parent: tk.Tk):
        for widget in parent.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.configure(background=self.bg_color, activebackground=self.bg_color, activeforeground=self.fg_color, selectcolor=self.bg_color) 
                self._determine_text_color(widget)
            if widget.winfo_children():
                self._change_all_radiobutton_colors(widget)

    def _change_all_checkbutton_colors(self, parent: tk.Tk):
        for widget in parent.winfo_children():
            if isinstance(widget, tk.Checkbutton):
                widget.configure(background=self.bg_color, activebackground=self.bg_color, selectcolor=self.bg_color_alt)
                self._determine_text_color(widget)
            if widget.winfo_children():
                self._change_all_checkbutton_colors(widget)

    def _change_all_listbox_colors(self, parent: tk.Tk):
        for widget in parent.winfo_children():
            if isinstance(widget, tk.Listbox):
                widget.configure(background=self.bg_color_alt, activestyle="none") 
                self._determine_text_color(widget)
            if widget.winfo_children():
                self._change_all_listbox_colors(widget)

    def _change_all_spinbox_colors(self, parent: tk.Tk):
        for widget in parent.winfo_children():
            if isinstance(widget, tk.Spinbox):
                widget.configure(background=self.btn_color, activebackground=self.btn_color_active, buttonbackground=self.btn_color) 
                self._determine_text_color(widget)
            if widget.winfo_children():
                self._change_all_spinbox_colors(widget)

    def _change_all_scale_colors(self, parent: tk.Tk):
        for widget in parent.winfo_children():
            if isinstance(widget, tk.Scale):
                widget.configure(background=self.bg_color_alt, activebackground=self.bg_color_alt) 
                self._determine_text_color(widget)
            if widget.winfo_children():
                self._change_all_scale_colors(widget)

    def _change_all_treeview_colors(self, parent: tk.Tk):
        for widget in parent.winfo_children():
            if isinstance(widget, ttk.Treeview):
                style = self.get_treeview_style()
                widget.configure(style="Custom.Treeview") 
            if widget.winfo_children():
                self._change_all_treeview_colors(widget)

    def _change_all_menu_colors(self, parent: tk.Tk):
        for widget in parent.winfo_children():
            if isinstance(widget, tk.Menu):
                widget.configure(background=self.bg_color_alt, activebackground=self.bg_color_alt) 
                self._determine_text_color(widget)
            if widget.winfo_children():
                self._change_all_menu_colors(widget)

    def _determine_text_color(self, widget: tk.Widget):
        theme_type = None
        try:
            theme_type = widget.theme_type
        except:
            pass
        if theme_type == ThemeType.ERROR:
            widget.configure(foreground=self.fg_color_error) 
        elif theme_type == ThemeType.SUCCESS:
            widget.configure(foreground=self.fg_color_success) 
        elif theme_type == ThemeType.ACCEPT:
            widget.configure(foreground=self.fg_color_accept) 
        else:
            if isinstance(widget, tk.Button) or isinstance(widget, tk.Spinbox):
                widget.configure(foreground=self.btn_fg_color) 
            else:
                widget.configure(foreground=self.fg_color) 
        try:
            widget.configure(disabledforeground=self.fg_color_disabled)
        except:
            None
        try:
            widget.configure(activeforeground=self.fg_color)
        except:
            None

    def get_treeview_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Custom.Treeview",
            background=self.bg_color,
            foreground=self.fg_color,
            fieldbackground=self.bg_color_alt,
            selectbackground=self.btn_color_active,
            selectforeground=self.fg_color
        )
        style.configure(
            "Custom.Treeview.Heading",
            background=self.btn_color,
            foreground=self.btn_fg_color
        )
        style.map("Custom.Treeview.Heading", background=[('active', self.btn_color_active)])
        return style

class ThemeChoiceWindow():
    """
    GUI for swapping between themes that have been added to the passed ThemeChanger class.
    """
    def __init__(self, tc: ThemeChanger, subroot: tk.Tk):
        self.root = tk.Toplevel(subroot)
        self.root.title(f"{PROGRAM_NAME} {VERSION_NUMBER}")

        self.lbl = tk.Label(self.root, text="Choose your theme:", font=("Lato", 14, "bold"), width=STANDARD_WIDTH)

        self.theme_lst = tk.Listbox(self.root, width=STANDARD_WIDTH)
        self.refresh_theme_list(tc)

        self.submit = tk.Button(self.root, text="Submit Choice", command=lambda: self.exit(tc, subroot), width=STANDARD_ENTRY_WIDTH)

        self.create = tk.Button(self.root, text="Create Theme", command=lambda: self.create_theme(tc), width=STANDARD_ENTRY_WIDTH)
        
        self.lbl.grid(row=0, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING, columnspan=2)
        self.theme_lst.grid(row=1, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING, columnspan=2)
        self.submit.grid(row=2, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)
        self.create.grid(row=2, column=1, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)

        tc.update_theme_widgets(self.root)

        self.root.mainloop()

    def refresh_theme_list(self, tc: ThemeChanger):
        self.theme_lst.delete(0, self.theme_lst.size())
        i = 1
        for theme in tc.default_themes:
            self.theme_lst.insert(i, theme.name)
            i+=1

    def create_theme(self, tc: ThemeChanger):
        ThemeCreatorWindow(tc, self.root, self)
    
    def exit(self,  tc: ThemeChanger, subroot: tk.Tk):
        tc.set_global_theme(tc.default_themes[self.theme_lst.curselection()[0]])
        tc.update_theme_widgets(subroot)
        self.root.destroy()

class ThemeCreatorWindow():
    """
    GUI for creating your own custom themes and allows for saving and adding of created theme to program.
    """
    theme: Theme = None
    def __init__(self, tc: ThemeChanger, subroot: tk.Tk, tcw: ThemeChoiceWindow = None):
        self.theme = Theme("Temp", tc.curr_theme.bg_color, tc.curr_theme.bg_color_alt, tc.curr_theme.btn_color, tc.curr_theme.btn_color_active, 
                           tc.curr_theme.btn_fg_color, tc.curr_theme.fg_color, tc.curr_theme.fg_color_disabled, tc.curr_theme.fg_color_error, tc.curr_theme.fg_color_success, tc.curr_theme.fg_color_accept)

        root = tk.Tk()
        root.title(f"{PROGRAM_NAME} {VERSION_NUMBER}")

        lbl_name = tk.Label(root, text="Name:", width=STANDARD_WIDTH)
        self.entry_name = tk.Entry(root, width=STANDARD_ENTRY_WIDTH)
        self.entry_name.insert("0", self.theme.name)
        lbl_name.grid(row=0, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)
        self.entry_name.grid(row=0, column=1, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)

        btn_panel = tk.Frame(root)

        btn_bg_color = tk.Button(btn_panel, text="Bg Color", command=lambda: self.choose_color(root, tc, self.theme.update_bg_color),width=STANDARD_ENTRY_WIDTH)
        btn_bg_color.grid(row=1, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)

        btn_bg_color_alt = tk.Button(btn_panel, text="Bg Color Alt", command=lambda: self.choose_color(root, tc, self.theme.update_bg_color_alt),width=STANDARD_ENTRY_WIDTH)
        btn_bg_color_alt.grid(row=2, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)

        btn_btn_color = tk.Button(btn_panel, text="Btn Color", command=lambda: self.choose_color(root, tc, self.theme.update_btn_color),width=STANDARD_ENTRY_WIDTH)
        btn_btn_color.grid(row=3, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)

        btn_btn_color_active = tk.Button(btn_panel, text="Btn Color Active", command=lambda: self.choose_color(root, tc, self.theme.update_btn_color_active),width=STANDARD_ENTRY_WIDTH)
        btn_btn_color_active.grid(row=4, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)

        btn_btn_fg_color = tk.Button(btn_panel, text="Btn Fg Color", command=lambda: self.choose_color(root, tc, self.theme.update_btn_fg_color),width=STANDARD_ENTRY_WIDTH)
        btn_btn_fg_color.grid(row=5, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)

        btn_fg_color = tk.Button(btn_panel, text="Fg Color", command=lambda: self.choose_color(root, tc, self.theme.update_fg_color),width=STANDARD_ENTRY_WIDTH)
        btn_fg_color.grid(row=6, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)

        btn_fg_color_disabled = tk.Button(btn_panel, text="Fg Color Disabled", command=lambda: self.choose_color(root, tc, self.theme.update_fg_color_disabled),width=STANDARD_ENTRY_WIDTH)
        btn_fg_color_disabled.grid(row=7, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)
        
        btn_fg_color_error = tk.Button(btn_panel, text="Fg Color Error", command=lambda: self.choose_color(root, tc, self.theme.update_fg_color_error),width=STANDARD_ENTRY_WIDTH)
        btn_fg_color_error.grid(row=8, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)
        
        btn_fg_color_success = tk.Button(btn_panel, text="Fg Color Success", command=lambda: self.choose_color(root, tc, self.theme.update_fg_color_success),width=STANDARD_ENTRY_WIDTH)
        btn_fg_color_success.grid(row=9, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)

        btn_fg_color_accept = tk.Button(btn_panel, text="Fg Color Accept", command=lambda: self.choose_color(root, tc, self.theme.update_fg_color_accept),width=STANDARD_ENTRY_WIDTH)
        btn_fg_color_accept.grid(row=10, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)
        
        btn_panel.grid(row=1, column=0)


        demo_panel = tk.Frame(root)
        
        disabled_label = tk.Label(demo_panel, text="Disabled Text", width=STANDARD_ENTRY_WIDTH, state="disabled")
        disabled_label.grid(row=0, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)
        error_label = tk.Label(demo_panel, text="Error Text", width=STANDARD_ENTRY_WIDTH, fg="red")
        error_label.theme_type = ThemeType.ERROR
        error_label.grid(row=1, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)
        success_label = tk.Label(demo_panel, text="Success Text", width=STANDARD_ENTRY_WIDTH, fg="green")
        success_label.theme_type = ThemeType.SUCCESS
        success_label.grid(row=2, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)
        accept_label = tk.Label(demo_panel, text="Accept Text", width=STANDARD_ENTRY_WIDTH, fg="blue")
        accept_label.theme_type = ThemeType.ACCEPT
        accept_label.grid(row=3, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)
        tk.Button(demo_panel, text="Button", width=STANDARD_ENTRY_WIDTH).grid(row=4, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)
        tk.Checkbutton(demo_panel, text="Check Button", width=STANDARD_ENTRY_WIDTH).grid(row=5, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)
        entry_demo = tk.Entry(demo_panel, width=STANDARD_ENTRY_WIDTH)
        entry_demo.insert(0, "Entry")
        entry_demo.grid(row=6, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)
        lstbx_demo = tk.Listbox(demo_panel, width=STANDARD_ENTRY_WIDTH)
        lstbx_demo.insert(0, "Element 1", "Element 2", "Element 3")
        lstbx_demo.grid(row=7, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)
        tk.Radiobutton(demo_panel, text="Radio Button", width=STANDARD_ENTRY_WIDTH).grid(row=8, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)
        tk.Spinbox(demo_panel, text="Spinbox", width=STANDARD_ENTRY_WIDTH).grid(row=9, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)

        demo_panel.grid(row=1, column=1)

        btn_save = tk.Button(root, text="Save Theme to File", command=self.save, width=STANDARD_WIDTH)
        btn_save.theme_type = ThemeType.ACCEPT
        btn_save.grid(row=2, column=1, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)
        btn_exit = tk.Button(root, text="Exit & Apply Theme", command=lambda: self.apply_and_exit(root, tc, subroot, tcw), width=STANDARD_WIDTH)
        btn_exit.theme_type = ThemeType.SUCCESS
        btn_exit.grid(row=2, column=0, padx=GLOBAL_X_PADDING, pady=GLOBAL_Y_PADDING)

        tc.update_theme_widgets(root)
        root.mainloop()

    def choose_color(self, root: tk.Tk, tc: ThemeChanger, command: function):
        command(colorchooser.askcolor(title="Choose Color")[1])
        self.theme = Theme(self.theme.name, self.theme.bg_color, self.theme.bg_color_alt, self.theme.btn_color, self.theme.btn_color_active, 
                           self.theme.btn_fg_color, self.theme.fg_color, self.theme.fg_color_disabled, self.theme.fg_color_error, self.theme.fg_color_success, self.theme.fg_color_accept)
        self.theme.name = self.entry_name.get()
        tc.set_global_theme(self.theme)
        tc.update_theme_widgets(root)
        root.attributes('-topmost', True)
        root.attributes('-topmost', False)

    def save(self):
        outstr = f"Name: {self.theme.name}\nBackground Color: {self.theme.bg_color}\nBackground Color Alt: {self.theme.bg_color_alt}\n"
        outstr += f"Foreground Color: {self.theme.fg_color}\nForeground Color Disabled: {self.theme.fg_color_disabled}\nForeground Color Error: {self.theme.fg_color_error}\nForeground Color Success: {self.theme.fg_color_success}\nForeground Color Accept: {self.theme.fg_color_accept}\n"
        outstr += f"Button Color: {self.theme.btn_color}\nButton Foreground Color: {self.theme.btn_fg_color}\nButton Active Color: {self.theme.btn_color_active}"
        with open(filedialog.asksaveasfilename(initialdir="/", title="Save Your Document", filetypes=[("Text Files", "*.txt")], defaultextension=".txt"), "w") as f:
            f.write(outstr)
    
    def apply_and_exit(self, root: tk.Tk, tc: ThemeChanger, subroot: tk.Tk, tcw: ThemeChoiceWindow = None):
        self.theme.name = self.entry_name.get()
        tc.add_theme_to_defaults(self.theme)
        tc.set_global_theme(self.theme)
        tc.update_theme_widgets(subroot)
        root.destroy()
        if tcw != None:
            tcw.refresh_theme_list(tc)
            tcw.root.attributes('-topmost', True)
            tcw.root.attributes('-topmost', False)
