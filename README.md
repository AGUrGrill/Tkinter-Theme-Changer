# Tkinter-Theme-Changer

Theme Changer V6
Created by AGU.

Provides a drop in solution to quickly swap between and create custom themes for any tkinter program.

Features:
    
    Classes: 
        ThemeChanger() - The main utility of the package. Allows for setting global theme, updating all widgets to specified theme, and adding new themes to global list.
        Theme() - Used for creating and modifying custom themes.
        ThemeChoiceWindow() - GUI for swapping between themes that have been added to the passed ThemeChanger class.
        ThemeCreatorWindow() - GUI for creating your own custom themes and allows for saving and adding of created theme to program.
    
    Enums:
        ThemeType - Used to specify the foreground color of a widget. 
            [Ex: label = tk.Label(root, text="Issue")     label.theme_type = ThemeType.ERROR     label.pack()]
        
