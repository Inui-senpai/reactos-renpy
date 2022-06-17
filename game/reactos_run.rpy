# Оформление
style ros_run_window:
    background Frame("gui/window/run/window.png")
    xysize(347, 179)
style ros_run_input_field:
    background Frame("gui/window/run/input_field_with_recents_list.png")
    xysize(266, 21)
style ros_run_window_title:
    font "gui/font/tahomabd.ttf"
    size 11
    color "#fff"
    pos(5, 7)
style ros_run_window_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
style ros_run_input_field_text:
    caret "common_caret"
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
image common_caret:
    Solid("#000", xsize=1, ysize=13)
    subpixel True
    block:
        alpha 1
        0.55
        alpha 0
        0.55
        repeat
style ros_run_error_window:
    background Frame("gui/window/run/window_error.png")
    xysize(258, 121)
style ros_run_error_ok_button:
    idle_background "gui/window/properties/mouse_scheme_delete_button_idle.png"
    hover_background "gui/window/properties/mouse_scheme_delete_button_hover.png"
style ros_run_error_ok_button_text is ros_run_window_text:
    xpos 26

# Основные переменные
default program_name = ""

# Обработчик "имён программ, папок, документа и ресурсов Интернета, которые требуется открыть"
init python:
    def ros_run_parse(name=""):
        if not name:
            pass
        elif name.lower() == "cmd":
            renpy.show_screen("ros_command_prompt")
        elif name.lower() == "explorer":
            renpy.show_screen("ros_explorer")
        elif name.lower() == "notepad":
            renpy.show_screen("ros_notepad")
        elif name.lower() == "winver":
            renpy.show_screen("ros_about", name="reactos")
        else:
            renpy.show_screen("ros_run_error")

# Окно
screen ros_run():
    drag:
        drag_name "ros_run"
        drag_handle(0, 0, 347, 21)
        align(0.0, 0.95)
        frame:
            style "ros_run_window"
            text "Выполнить" style "ros_run_window_title"
            imagebutton auto "gui/window/common/close_%s.png" action Hide("ros_run"):
                pos(326, 5)
            vbox:
                pos(15, 41)
                spacing 15
                hbox:
                    spacing 8
                    add "gui/desktop/desktop_icons/run.png"
                    text "Введите имя программы, папки, документа или ресурса\nИнтернета, которые требуется открыть." style "ros_run_window_text"
                hbox:
                    spacing 5
                    text "Открыть:" style "ros_run_window_text"
                    textbutton "" style "ros_run_input_field" ypos -2 mouse "beam" action NullAction()
                hbox:
                    pos(60, 10)
                    if not program_name:
                        textbutton "ОК" style "ros_properties_buttons" text_style "ros_properties_buttons_text_ok"
                    else:
                        textbutton "ОК" style "ros_properties_buttons" text_style "ros_properties_buttons_text_ok" focus_mask "gui/window/postinstall/button_idle.png" action [Function(ros_run_parse, name=program_name), SetVariable("program_name", ""), Hide("ros_run")]
                    null width 72
                    textbutton "Отмена" style "ros_properties_buttons" text_style "ros_properties_buttons_text_cancel" focus_mask "gui/window/postinstall/button_idle.png" action Hide("ros_run")
                    null width 48
                    textbutton "Обзор..." style "ros_properties_buttons" text_style "ros_properties_buttons_text_cancel" focus_mask "gui/window/postinstall/button_idle.png" action NullAction()
            hbox:
                pos(73, 89)
                input default "" value VariableInputValue("program_name", returnable=True) style "ros_run_input_field_text"
    key "K_RETURN" action [Function(ros_run_parse, name=program_name), SetVariable("program_name", ""), Hide("ros_run")]

# Окно ошибки
screen ros_run_error():
    modal True
    drag:
        drag_name "ros_run_err"
        drag_handle(0, 0, 258, 21)
        align(0.5, 0.5)
        frame:
            style "ros_run_error_window"
            text "Ошибка" style "ros_run_window_title"
            imagebutton auto "gui/window/common/close_%s.png" action [Show("ros_run"), Hide("ros_run_error")]:
                pos(237, 5)
            vbox:
                pos(17, 37)
                hbox:
                    spacing 10
                    add "gui/window/common/error.png"
                    text "Не удалось найти указанный файл." ypos 6 style "ros_run_window_text"
                null height 12
                hbox:
                    xpos 76
                    textbutton "ОК" style "ros_run_error_ok_button" text_style "ros_run_error_ok_button_text" focus_mask "gui/window/properties/mouse_scheme_delete_button_idle.png" action [Show("ros_run"), Hide("ros_run_error")]
