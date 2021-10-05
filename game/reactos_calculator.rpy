# Оформление
style ros_calc_frame:
    background Frame("gui/window/calculator/window.png")
    xsize 260 ysize 252
style ros_calc_header:
    font "gui/font/tahomabd.ttf"
    color "#fff"
    size 11
    xpos 22 ypos 4
style ros_calc_menu:
    idle_background "ros_calc_menu_idle"
    hover_background "ros_calc_menu_idle"
    insensitive_background "ros_calc_menu_idle"
    selected_background "ros_calc_menu_selected"
image ros_calc_menu_idle:
    Solid("#d4d0c8")
    xsize 38 ysize 18
image ros_calc_menu_selected:
    "gui/window/notepad/menu_button_selected.png"
    xsize 38 ysize 18
    xpos -6
style ros_calc_menu_edit:
    idle_background "ros_calc_menu_idle"
    hover_background "ros_calc_menu_idle"
    insensitive_background "ros_calc_menu_idle"
    selected_background "ros_calc_menu_selected_edit"
image ros_calc_menu_selected_edit:
    "gui/window/notepad/menu_button_selected.png"
    xsize 45 ysize 18
    xpos -6
style ros_calc_menu_view:
    idle_background "ros_calc_menu_idle"
    hover_background "ros_calc_menu_idle"
    insensitive_background "ros_calc_menu_idle"
    selected_background "ros_calc_menu_selected_view"
image ros_calc_menu_selected_view:
    "gui/window/notepad/menu_button_selected.png"
    xsize 28 ysize 18
    xpos -6
style ros_calc_menu_help:
    idle_background "ros_calc_menu_idle"
    hover_background "ros_calc_menu_idle"
    insensitive_background "ros_calc_menu_idle"
    selected_background "ros_calc_menu_selected_help"
image ros_calc_menu_selected_help:
    "gui/window/notepad/menu_button_selected.png"
    xsize 53 ysize 18
    xpos -6
style ros_calc_menu_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    insensitive_color "#808080"
    insensitive_outlines [(0, "#fff", 1, 1)]
    ypos 2
style ros_calc_input:
    background Frame("gui/window/calculator/input.png")
    xsize 239 ysize 23
style ros_calc_input_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    xpos 4 ypos 4
style ros_calc_backspace_button:
    idle_background "ros_calc_backspace_button_idle"
    hover_background "ros_calc_backspace_button_idle"
image ros_calc_backspace_button_idle:
    "gui/window/calculator/ce_button.png"
    xsize 63 ysize 29
style ros_calc_ce_button:
    idle_background "ros_calc_ce_button_idle"
    hover_background "ros_calc_ce_button_idle"
image ros_calc_ce_button_idle:
    "gui/window/calculator/ce_button.png"
    xsize 62 ysize 29
style ros_calc_backspace_button_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#ff0000"
    xpos 16 ypos 10
style ros_calc_ce_button_text is ros_calc_backspace_button_text:
    xpos 21
style ros_calc_c_button_text is ros_calc_backspace_button_text:
    xpos 25
style ros_calc_memory:
    background Frame("gui/window/calculator/memory_status.png")
    xsize 27 ysize 26
style ros_calc_memory_buttons:
    idle_background "ros_calc_memory_buttons_idle"
    hover_background "ros_calc_memory_buttons_idle"
image ros_calc_memory_buttons_idle:
    "gui/window/calculator/button.png"
style ros_calc_memory_buttons_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#ff0000"
    xpos 11 ypos 7
style ros_calc_integer_buttons_text is ros_calc_memory_buttons_text:
    color "#0000ff"
    xpos 15
style ros_calc_sqrt_text is ros_calc_integer_buttons_text:
    xpos 8
style ros_calc_percent_text is ros_calc_sqrt_text:
    xpos 12
style ros_calc_1x_text is ros_calc_sqrt_text:
    xpos 10
style ros_calc_operations_text is ros_calc_integer_buttons_text:
    color "#ff0000"
style ros_calc_equal_text is ros_calc_operations_text:
    xpos 14
style ros_calc_frame_minimized is empty
style ros_calc_menu_entry:
    idle_background "ros_calc_menu_entry_idle"
    hover_background "ros_calc_menu_entry_hover"
    insensitive_background "ros_calc_menu_entry_idle"
image ros_calc_menu_entry_idle:
    Solid("#d4d0c8")
    xsize 132 ysize 17
image ros_calc_menu_entry_hover:
    Solid("#0a246a")
    xsize 132 ysize 17
style ros_calc_menu_entry_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#fff"
    insensitive_color "#808080"
    insensitive_outlines [(0, "#fff", 1, 1)]
    xpos 15 ypos 1
style ros_calc_menu_entry_text_selected is ros_calc_menu_entry_text:
    xpos -1 ypos -1
style ros_calc_menu_entry_view:
    idle_background "ros_calc_menu_entry_view_idle"
    hover_background "ros_calc_menu_entry_view_hover"
    insensitive_background "ros_calc_menu_entry_view_idle"
image ros_calc_menu_entry_view_idle:
    Solid("#d4d0c8")
    xsize 140 ysize 17
image ros_calc_menu_entry_view_hover:
    Solid("#0a246a")
    xsize 140 ysize 17
style ros_calc_menu_entry_help:
    idle_background "ros_calc_menu_entry_help_idle"
    hover_background "ros_calc_menu_entry_help_hover"
    insensitive_background "ros_calc_menu_entry_help_idle"
image ros_calc_menu_entry_help_idle:
    Solid("#d4d0c8")
    xsize 104 ysize 17
image ros_calc_menu_entry_help_hover:
    Solid("#0a246a")
    xsize 104 ysize 17

# Основные переменные
define calc_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "-1", "-2", "-3", "-4", "-5", "-6", "-7", "-8", "-9"]
default ros_calc_menu_edit_opened = False
default ros_calc_menu_view_opened = False
default ros_calc_menu_help_opened = False
default is_calc_window_opened = True

# Итог
init python:
    def ros_calc_equal(calc_input):
        try:
            calc_input = eval(calc_input)
        except SyntaxError:
            pass
        return str(calc_input)

# Окно
screen ros_calc():
    default calc_input = "0"
    if not is_calc_window_opened:
        frame:
            style "ros_calc_frame_minimized"
    else:
        drag:
            drag_name "ros_calc"
            drag_handle (0, 0, 260, 21)
            xalign 0.5 yalign 0.5
            frame:
                style "ros_calc_frame"
                add "gui/desktop/menu_icons/submenu/calc.png" xpos 3 ypos 0
                text "Калькулятор ReactOS" style "ros_calc_header"
                imagebutton auto "gui/window/common/close_%s.png" action Hide("ros_calc"):
                    xanchor -235 yanchor -1
                imagebutton auto "gui/window/common/expand_%s.png":
                    xanchor -217 yanchor -1
                imagebutton auto "gui/window/common/minimize_%s.png" action SetVariable("is_calc_window_opened", False):
                    xanchor -201 yanchor -1
                hbox:
                    xpos 5 ypos 18
                    spacing 10
                    textbutton "Правка" style "ros_calc_menu_edit" text_style "ros_calc_menu_text" focus_mask "ros_calc_menu_idle" action ToggleVariable("ros_calc_menu_edit_opened", True, False)
                    textbutton "Вид" style "ros_calc_menu_view" text_style "ros_calc_menu_text" focus_mask "ros_calc_menu_idle" action ToggleVariable("ros_calc_menu_view_opened", True, False)
                    textbutton "Справка" style "ros_calc_menu_help" text_style "ros_calc_menu_text" focus_mask "ros_calc_menu_idle" action ToggleVariable("ros_calc_menu_help_opened", True, False)
                frame:
                    # TODO: Сделать вывод цифр справа налево
                    style "ros_calc_input"
                    xpos 7 ypos 40
                    text calc_input style "ros_calc_input_text"
                if calc_input == "0":
                    hbox:
                        xpos 53 ypos 75
                        spacing 40
                        textbutton "Back" style "ros_calc_backspace_button" text_style "ros_calc_backspace_button_text" focus_mask "ros_calc_backspace_button_idle" action NullAction()
                        textbutton "CE" style "ros_calc_ce_button" text_style "ros_calc_ce_button_text" focus_mask "ros_calc_ce_button_idle" xpos -5 action NullAction()
                        textbutton "C" style "ros_calc_ce_button" text_style "ros_calc_c_button_text" focus_mask "ros_calc_ce_button_idle" xpos -1 action NullAction()
                else:
                    python:
                        if calc_input in calc_list:
                            backspace_action = SetScreenVariable("calc_input", "0")
                        else:
                            backspace_action = SetScreenVariable("calc_input", calc_input[:-1])
                    hbox:
                        xpos 53 ypos 75
                        spacing 40
                        textbutton "Back" style "ros_calc_backspace_button" text_style "ros_calc_backspace_button_text" focus_mask "ros_calc_backspace_button_idle" action backspace_action
                        textbutton "CE" style "ros_calc_ce_button" text_style "ros_calc_ce_button_text" focus_mask "ros_calc_ce_button_idle" xpos -5 action SetScreenVariable("calc_input", "0")
                        textbutton "C" style "ros_calc_ce_button" text_style "ros_calc_c_button_text" focus_mask "ros_calc_ce_button_idle" xpos -1 action SetScreenVariable("calc_input", "0")
                frame:
                    style "ros_calc_memory"
                    xpos 11 ypos 77
                vbox:
                    xpos 7 ypos 111
                    spacing 19
                    textbutton "MC" style "ros_calc_memory_buttons" text_style "ros_calc_memory_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action NullAction()
                    textbutton "MR" style "ros_calc_memory_buttons" text_style "ros_calc_memory_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action NullAction()
                    textbutton "MS" style "ros_calc_memory_buttons" text_style "ros_calc_memory_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action NullAction()
                    textbutton "M+" style "ros_calc_memory_buttons" text_style "ros_calc_memory_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action NullAction()
                if calc_input == "0":
                    hbox:
                        xpos 53 ypos 111
                        spacing 33
                        textbutton "7" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", "7")
                        textbutton "8" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", "8")
                        textbutton "9" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", "9")
                        textbutton "/" style "ros_calc_memory_buttons" text_style "ros_calc_operations_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", calc_input+"/")
                        textbutton "Sqrt" style "ros_calc_memory_buttons" text_style "ros_calc_sqrt_text" focus_mask "ros_calc_memory_buttons_idle" xpos 2 action NullAction()
                    hbox:
                        xpos 53 ypos 144
                        spacing 33
                        textbutton "4" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", "4")
                        textbutton "5" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", "5")
                        textbutton "6" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", "6")
                        textbutton "*" style "ros_calc_memory_buttons" text_style "ros_calc_operations_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", calc_input+"*")
                        textbutton "%" style "ros_calc_memory_buttons" text_style "ros_calc_percent_text" focus_mask "ros_calc_memory_buttons_idle" action NullAction()
                    hbox:
                        xpos 53 ypos 177
                        spacing 33
                        textbutton "1" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", "1")
                        textbutton "2" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", "2")
                        textbutton "3" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", "3")
                        textbutton "-" style "ros_calc_memory_buttons" text_style "ros_calc_operations_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", calc_input+"-")
                        textbutton "1/x" style "ros_calc_memory_buttons" text_style "ros_calc_1x_text" focus_mask "ros_calc_memory_buttons_idle" xpos 2 action NullAction()
                    hbox:
                        xpos 53 ypos 210
                        spacing 33
                        textbutton "0" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", "0")
                        textbutton "+/-" style "ros_calc_memory_buttons" text_style "ros_calc_sqrt_text" focus_mask "ros_calc_memory_buttons_idle" action NullAction()
                        textbutton "," style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" xpos -10 action SetScreenVariable("calc_input", calc_input+",")
                        textbutton "+" style "ros_calc_memory_buttons" text_style "ros_calc_operations_text" focus_mask "ros_calc_memory_buttons_idle" xpos -7 action SetScreenVariable("calc_input", calc_input+"+")
                        textbutton "=" style "ros_calc_memory_buttons" text_style "ros_calc_equal_text" focus_mask "ros_calc_memory_buttons_idle" xpos -9 action NullAction()
                else:
                    hbox:
                        xpos 53 ypos 111
                        spacing 33
                        if len(calc_input) < 38:
                            textbutton "7" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", calc_input+"7")
                            textbutton "8" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", calc_input+"8")
                            textbutton "9" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", calc_input+"9")
                        else:
                            textbutton "7" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action NullAction()
                            textbutton "8" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action NullAction()
                            textbutton "9" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action NullAction()
                        textbutton "/" style "ros_calc_memory_buttons" text_style "ros_calc_operations_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", calc_input+"/")
                        textbutton "Sqrt" style "ros_calc_memory_buttons" text_style "ros_calc_sqrt_text" focus_mask "ros_calc_memory_buttons_idle" xpos 2 action NullAction()
                    hbox:
                        xpos 53 ypos 144
                        spacing 33
                        if len(calc_input) < 38:
                            textbutton "4" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", calc_input+"4")
                            textbutton "5" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", calc_input+"5")
                            textbutton "6" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", calc_input+"6")
                        else:
                            textbutton "4" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action NullAction()
                            textbutton "5" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action NullAction()
                            textbutton "6" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action NullAction()
                        textbutton "*" style "ros_calc_memory_buttons" text_style "ros_calc_operations_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", calc_input+"*")
                        textbutton "%" style "ros_calc_memory_buttons" text_style "ros_calc_percent_text" focus_mask "ros_calc_memory_buttons_idle" action NullAction()
                    hbox:
                        xpos 53 ypos 177
                        spacing 33
                        if len(calc_input) < 38:
                            textbutton "1" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", calc_input+"1")
                            textbutton "2" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", calc_input+"2")
                            textbutton "3" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", calc_input+"3")
                        else:
                            textbutton "1" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action NullAction()
                            textbutton "2" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action NullAction()
                            textbutton "3" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action NullAction()
                        textbutton "-" style "ros_calc_memory_buttons" text_style "ros_calc_operations_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", calc_input+"-")
                        textbutton "1/x" style "ros_calc_memory_buttons" text_style "ros_calc_1x_text" focus_mask "ros_calc_memory_buttons_idle" xpos 2 action NullAction()
                    hbox:
                        xpos 53 ypos 210
                        spacing 33
                        if len(calc_input) < 38:
                            textbutton "0" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", calc_input+"0")
                        else:
                            textbutton "0" style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" action NullAction()
                        if not calc_input.startswith("-"):
                            textbutton "+/-" style "ros_calc_memory_buttons" text_style "ros_calc_sqrt_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", "-"+calc_input)
                        else:
                            textbutton "+/-" style "ros_calc_memory_buttons" text_style "ros_calc_sqrt_text" focus_mask "ros_calc_memory_buttons_idle" action SetScreenVariable("calc_input", calc_input[1:])
                        textbutton "," style "ros_calc_memory_buttons" text_style "ros_calc_integer_buttons_text" focus_mask "ros_calc_memory_buttons_idle" xpos -10 action NullAction()
                        textbutton "+" style "ros_calc_memory_buttons" text_style "ros_calc_operations_text" focus_mask "ros_calc_memory_buttons_idle" xpos -7 action SetScreenVariable("calc_input", calc_input+"+")
                        textbutton "=" style "ros_calc_memory_buttons" text_style "ros_calc_equal_text" focus_mask "ros_calc_memory_buttons_idle" xpos -9 action SetScreenVariable("calc_input", ros_calc_equal(calc_input))
                vbox:
                    if ros_calc_menu_edit_opened:
                        use ros_calc_edit
                    elif ros_calc_menu_view_opened:
                        use ros_calc_view
                    elif ros_calc_menu_help_opened:
                        use ros_calc_help

# Контекстные меню
# Правка
screen ros_calc_edit():
    frame:
        style "ros_desktop_context_menu"
        xsize 138 ysize 40
        ypos 36
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Копировать    CTRL-C" style "ros_calc_menu_entry" text_style "ros_calc_menu_entry_text" focus_mask "ros_calc_menu_entry_idle" action NullAction()
            textbutton "Вставить        CTRL-V" style "ros_calc_menu_entry" text_style "ros_calc_menu_entry_text"
# Вид
screen ros_calc_view():
    frame:
        style "ros_desktop_context_menu"
        xsize 147 ysize 83
        xpos 45 ypos 36
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "{font=gui/font/Marlett.ttf}{size=13}a{/font}{/size} Обычный" style "ros_calc_menu_entry_view" text_style "ros_calc_menu_entry_text_selected" focus_mask "ros_calc_menu_entry_view_idle" action NullAction()
            textbutton "Инженерный" style "ros_calc_menu_entry_view" text_style "ros_calc_menu_entry_text" focus_mask "ros_calc_menu_entry_view_idle" action NullAction()
            textbutton "Перевод величин" style "ros_calc_menu_entry_view" text_style "ros_calc_menu_entry_text" focus_mask "ros_calc_menu_entry_view_idle" action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 139 ypos 1
            null height 1
            textbutton "{font=gui/font/Marlett.ttf}{size=13}a{/font}{/size} Группировать цифры" style "ros_calc_menu_entry_view" text_style "ros_calc_menu_entry_text_selected" focus_mask "ros_calc_menu_entry_view_idle" action NullAction()
# Справка
screen ros_calc_help():
    frame:
        style "ros_desktop_context_menu"
        xsize 111 ysize 49
        xpos 74 ypos 36
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Вызов справки" style "ros_calc_menu_entry_help" text_style "ros_calc_menu_entry_text" focus_mask "ros_calc_menu_entry_help_idle" action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 103 ypos 1
            null height 1
            textbutton "О программе" style "ros_calc_menu_entry_help" text_style "ros_calc_menu_entry_text" focus_mask "ros_calc_menu_entry_help_idle" action [
                SetVariable("ros_calc_menu_help_opened", False),
                Show(screen="ros_about", name="calc")]
