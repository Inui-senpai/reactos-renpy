# Оформление
style ros_notepad_frame:
    background Frame("gui/window/notepad/window.png")
    xsize 570 ysize 427
style ros_notepad_menu:
    idle_background "ros_notepad_menu_idle"
    hover_background "ros_notepad_menu_idle"
    insensitive_background "ros_notepad_menu_idle"
    selected_background "ros_notepad_menu_selected"
image ros_notepad_menu_idle:
    Solid("#d4d0c8")
    xsize 38 ysize 18
image ros_notepad_menu_selected:
    "gui/window/notepad/menu_button_selected.png"
    xsize 38 ysize 18
    xpos -6
style ros_notepad_menu_edit is ros_notepad_menu:
    selected_background "ros_notepad_menu_selected_edit"
image ros_notepad_menu_selected_edit:
    "gui/window/notepad/menu_button_selected.png"
    xsize 45 ysize 18
    xpos -6
style ros_notepad_menu_format is ros_notepad_menu:
    selected_background "ros_notepad_menu_selected_format"
image ros_notepad_menu_selected_format:
    "gui/window/notepad/menu_button_selected.png"
    xsize 48 ysize 18
    xpos -6
style ros_notepad_menu_view is ros_notepad_menu:
    selected_background "ros_notepad_menu_selected_view"
image ros_notepad_menu_selected_view:
    "gui/window/notepad/menu_button_selected.png"
    xsize 30 ysize 18
    xpos -6
style ros_notepad_menu_help is ros_notepad_menu:
    selected_background "ros_notepad_menu_selected_help"
image ros_notepad_menu_selected_help:
    "gui/window/notepad/menu_button_selected.png"
    xsize 52 ysize 18
    xpos -6
style ros_notepad_menu_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    insensitive_color "#808080"
style ros_notepad_menu_entry:
    idle_background "ros_notepad_menu_entry_idle"
    hover_background "ros_notepad_menu_entry_hover"
    insensitive_background "ros_notepad_menu_entry_idle"
image ros_notepad_menu_entry_idle:
    Solid("#d4d0c8")
    xsize 215 ysize 17
image ros_notepad_menu_entry_hover:
    Solid("#0a246a")
    xsize 215 ysize 17
style ros_notepad_menu_entry_edit:
    idle_background "ros_notepad_menu_entry_edit_idle"
    hover_background "ros_notepad_menu_entry_edit_hover"
    insensitive_background "ros_notepad_menu_entry_edit_idle"
image ros_notepad_menu_entry_edit_idle:
    Solid("#d4d0c8")
    xsize 143 ysize 17
image ros_notepad_menu_entry_edit_hover:
    Solid("#0a246a")
    xsize 143 ysize 17
style ros_notepad_menu_entry_format:
    idle_background "ros_notepad_menu_entry_format_idle"
    hover_background "ros_notepad_menu_entry_format_hover"
    insensitive_background "ros_notepad_menu_entry_format_idle"
image ros_notepad_menu_entry_format_idle:
    Solid("#d4d0c8")
    xsize 126 ysize 17
image ros_notepad_menu_entry_format_hover:
    Solid("#0a246a")
    xsize 126 ysize 17
style ros_notepad_menu_entry_view:
    idle_background "ros_notepad_menu_entry_view_idle"
    hover_background "ros_notepad_menu_entry_view_hover"
    insensitive_background "ros_notepad_menu_entry_view_idle"
image ros_notepad_menu_entry_view_idle:
    Solid("#d4d0c8")
    xsize 122 ysize 17
image ros_notepad_menu_entry_view_hover:
    Solid("#0a246a")
    xsize 122 ysize 17
style ros_notepad_menu_entry_help:
    idle_background "ros_notepad_menu_entry_help_idle"
    hover_background "ros_notepad_menu_entry_help_hover"
    insensitive_background "ros_notepad_menu_entry_help_idle"
image ros_notepad_menu_entry_help_idle:
    Solid("#d4d0c8")
    xsize 139 ysize 17
image ros_notepad_menu_entry_help_hover:
    Solid("#0a246a")
    xsize 139 ysize 17
style ros_notepad_menu_entry_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#fff"
    insensitive_color "#808080"
    xpos 20
style ros_notepad_window_title:
    font "gui/font/tahomabd.ttf"
    size 11
    color "#fff"
    xpos 22 ypos 5
style ros_notepad_viewport:
    background Frame("gui/window/notepad/viewport.png")
    xsize 562 ysize 361
    xpos 1 ypos 39
style ros_notepad_viewport_text:
    font "gui/font/lucon.ttf"
    size 14
    color "#000"
    xpos 8 ypos 7
style ros_notepad_counter_bar:
    background Frame("gui/window/notepad/counter_bar.png")
    xsize 562 ysize 18
    xpos 1 ypos 402
style ros_notepad_counter_bar_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    xpos 7

# Основные переменные
default ros_notepad_menu_file_opened = False
default ros_notepad_menu_edit_opened = False
default ros_notepad_menu_format_opened = False
default ros_notepad_menu_view_opened = False
default ros_notepad_menu_help_opened = False

# Окно
screen ros_notepad(file=None):
    drag:
        drag_name "ros_notepad"
        drag_handle (0, 0, 570, 22)
        xalign 0.5 yalign 0.5
        frame:
            style "ros_notepad_frame"
            add "gui/desktop/menu_icons/submenu/notepad.png":
                xpos 3 ypos 1
            if file:
                python:
                    try: file_text = renpy.file(file).read()
                    except: file = None
            if not file:
                text "Безымянный - Блокнот" style "ros_notepad_window_title"
            else:
                text "[file] - Блокнот" style "ros_notepad_window_title"
            imagebutton idle "gui/window/common/close_idle.png" action [
                SetVariable("ros_notepad_menu_file_opened", False),
                SetVariable("ros_notepad_menu_edit_opened", False),
                SetVariable("ros_notepad_menu_format_opened", False),
                SetVariable("ros_notepad_menu_view_opened", False),
                SetVariable("ros_notepad_menu_help_opened", False),
                Hide("ros_notepad")]:
                xanchor -544 yanchor -2
            imagebutton idle "gui/window/common/expand_idle.png" action NullAction():
                xanchor -526 yanchor -2
            imagebutton idle "gui/window/common/minimize_idle.png" action NullAction():
                xanchor -510 yanchor -2
            hbox:
                xpos 10 ypos 22
                spacing 10
                textbutton "Файл" style "ros_notepad_menu" text_style "ros_notepad_menu_text" action ToggleVariable("ros_notepad_menu_file_opened", True, False)
                textbutton "Правка" style "ros_notepad_menu_edit" text_style "ros_notepad_menu_text" action ToggleVariable("ros_notepad_menu_edit_opened", True, False)
                textbutton "Формат" style "ros_notepad_menu_format" text_style "ros_notepad_menu_text" action ToggleVariable("ros_notepad_menu_format_opened", True, False)
                textbutton "Вид" style "ros_notepad_menu_view" text_style "ros_notepad_menu_text" action ToggleVariable("ros_notepad_menu_view_opened", True, False)
                textbutton "Справка" style "ros_notepad_menu_help" text_style "ros_notepad_menu_text" action ToggleVariable("ros_notepad_menu_help_opened", True, False)
            frame:
                style "ros_notepad_viewport"
                viewport:
                    xinitial 0.0 yinitial 0.0
                    scrollbars "both"
                    mousewheel True
                    draggable True
                    side_yfill True
                    vbox:
                        text (file_text if file else "") style "ros_notepad_viewport_text"
                        transclude
            frame:
                style "ros_notepad_counter_bar"
                text "Строка 1, столбец 1" style "ros_notepad_counter_bar_text"
            vbox:
                if ros_notepad_menu_file_opened:
                    use ros_notepad_menu_file
                elif ros_notepad_menu_edit_opened:
                    use ros_notepad_menu_edit
                elif ros_notepad_menu_format_opened:
                    use ros_notepad_menu_format
                elif ros_notepad_menu_view_opened:
                    use ros_notepad_menu_view
                elif ros_notepad_menu_help_opened:
                    use ros_notepad_menu_help

# Контекстные меню
# Файл
screen ros_notepad_menu_file():
    frame:
        style "ros_desktop_context_menu"
        xsize 221 ysize 157
        ypos 40
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Создать                    Ctrl+N" style "ros_notepad_menu_entry" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_idle" action NullAction()
            textbutton "Новое окно               Ctrl+Shift+N" style "ros_notepad_menu_entry" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_idle" action NullAction()
            textbutton "Открыть...                 Ctrl+O" style "ros_notepad_menu_entry" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_idle" action NullAction()
            textbutton "Сохранить                Ctrl+S" style "ros_notepad_menu_entry" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_idle" action NullAction()
            textbutton "Сохранить как..." style "ros_notepad_menu_entry" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_idle" action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 213 ypos 1
            null height 1
            textbutton "Параметры страницы..." style "ros_notepad_menu_entry" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_idle" action NullAction()
            textbutton "Печать...                   Ctrl+P" style "ros_notepad_menu_entry" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_idle" action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 213 ypos 1
            null height 1
            textbutton "Выход" style "ros_notepad_menu_entry" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_idle" action [
                SetVariable("ros_notepad_menu_file_opened", False),
                Hide(screen="ros_notepad")]
# Правка
screen ros_notepad_menu_edit():
    frame:
        style "ros_desktop_context_menu"
        xsize 149 ysize 215
        xpos 40 ypos 40
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Отменить          Ctrl+Z" style "ros_notepad_menu_entry_edit" text_style "ros_notepad_menu_entry_text"
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 141 ypos 1
            null height 1
            textbutton "Вырезать           Ctrl+X" style "ros_notepad_menu_entry_edit" text_style "ros_notepad_menu_entry_text"
            textbutton "Копировать       Ctrl+C" style "ros_notepad_menu_entry_edit" text_style "ros_notepad_menu_entry_text"
            textbutton "Вставить            Ctrl+V" style "ros_notepad_menu_entry_edit" text_style "ros_notepad_menu_entry_text"
            textbutton "Удалить             Del" style "ros_notepad_menu_entry_edit" text_style "ros_notepad_menu_entry_text"
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 141 ypos 1
            null height 1
            if file:
                textbutton "Найти...              Ctrl+F" style "ros_notepad_menu_entry_edit" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_edit_idle" action NullAction()
                textbutton "Найти далее      F3" style "ros_notepad_menu_entry_edit" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_edit_idle" action NullAction()
                textbutton "Заменить...        Ctrl+H" style "ros_notepad_menu_entry_edit" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_edit_idle" action NullAction()
                textbutton "Перейти...          Ctrl+G" style "ros_notepad_menu_entry_edit" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_edit_idle" action NullAction()
            else:
                textbutton "Найти...              Ctrl+F" style "ros_notepad_menu_entry_edit" text_style "ros_notepad_menu_entry_text"
                textbutton "Найти далее      F3" style "ros_notepad_menu_entry_edit" text_style "ros_notepad_menu_entry_text"
                textbutton "Заменить...        Ctrl+H" style "ros_notepad_menu_entry_edit" text_style "ros_notepad_menu_entry_text"
                textbutton "Перейти...          Ctrl+G" style "ros_notepad_menu_entry_edit" text_style "ros_notepad_menu_entry_text"
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 141 ypos 1
            null height 1
            textbutton "Выделить всё    Ctrl+A" style "ros_notepad_menu_entry_edit" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_edit_idle" action NullAction()
            textbutton "Время и дата     F5" style "ros_notepad_menu_entry_edit" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_edit_idle" action NullAction()
# Формат
screen ros_notepad_menu_format():
    frame:
        style "ros_desktop_context_menu"
        xsize 132 ysize 39
        xpos 86 ypos 40
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Перенос по словам" style "ros_notepad_menu_entry_format" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_format_idle" action NullAction()
            textbutton "Шрифт..." style "ros_notepad_menu_entry_format" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_format_idle" action NullAction()
# Вид
screen ros_notepad_menu_view():
    frame:
        style "ros_desktop_context_menu"
        xsize 128 ysize 23
        xpos 133 ypos 40
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Строка состояния" style "ros_notepad_menu_entry_view" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_view_idle" action NullAction()
# Справка
screen ros_notepad_menu_help():
    frame:
        style "ros_desktop_context_menu"
        xsize 145 ysize 49
        xpos 163 ypos 40
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Содержание" style "ros_notepad_menu_entry_help" text_style "ros_notepad_menu_entry_text"
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 137 ypos 1
            null height 1
            textbutton "О программе" style "ros_notepad_menu_entry_help" text_style "ros_notepad_menu_entry_text" focus_mask "ros_notepad_menu_entry_help_idle" action [
                SetVariable("ros_notepad_menu_help_opened", False),
                Show(screen="ros_about", name="notepad")]
