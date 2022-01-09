# Оформление
style ros_about_frame:
    background Frame("gui/window/system_info/about_window.png")
    xsize 419 ysize 347
style ros_about_title:
    font "gui/font/tahomabd.ttf"
    size 11
    xpos 4 ypos 4
    color "#fff"
style ros_about_description:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
style ros_authors_button:
    idle_background "gui/window/system_info/authors_button_idle.png"
    hover_background "gui/window/system_info/authors_button_hover.png"
style ros_authors_button_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    xpos 29
style ros_authors_viewport:
    background Frame("gui/window/system_info/authors_viewport.png")
    xsize 248 ysize 116

# Основные переменные
default ros_authors_opened = False

# Окно
screen ros_about(name=None):
    python:
        friendly_name = name.replace("notepad", "Блокнот").replace("reactos", "ReactOS").replace("calc", "Калькулятор ReactOS")
        authors_button_text = "Авторы" if not ros_authors_opened else "< Назад"
    modal True
    drag:
        drag_name "ros_about"
        drag_handle (0, 0, 419, 21)
        xalign 0.3 yalign 0.3
        frame:
            style "ros_about_frame"
            text "[friendly_name]: сведения" style "ros_about_title"
            imagebutton auto "gui/window/common/close_%s.png" action [
                SetVariable("ros_authors_opened", False),
                Hide("ros_about")]:
                xanchor -394 yanchor -1
            if persistent.selected_edition == "workstation":
                add "gui/window/system_info/reactosworkstation.png" xpos -1 ypos 19
            else:
                add "gui/window/system_info/reactosserver.png" xpos -1 ypos 19
            add "gui/window/system_info/line.png" xpos -1 ypos 90
            add "gui/desktop/desktop_icons/[name].png" xpos 10 ypos 107
            vbox:
                xpos 53 ypos 107
                spacing 2
                text "[friendly_name]" style "ros_about_description"
                text "Версия [config.version] ([ros_build_wo_compiler])" style "ros_about_description"
                text "Авторское право 1998-2021 Команда ReactOS" style "ros_about_description"
            vbox:
                if not ros_authors_opened:
                    if name == "reactos":
                        use ros_about_general_placeholder
                    else:
                        use expression "ros_about_general_" + name
                    use ros_about_general
                else:
                    use ros_about_general_authors
            textbutton authors_button_text style "ros_authors_button" text_style "ros_authors_button_text" focus_mask "gui/window/system_info/authors_button_idle.png" xpos 8 ypos 307 action ToggleVariable("ros_authors_opened", True, False)
            textbutton "ОК" style "ros_properties_buttons" text_style "ros_properties_buttons_text_ok" focus_mask "gui/window/postinstall/button_idle.png" xpos 321 ypos 307 action [
                SetVariable("ros_authors_opened", False),
                Hide(screen="ros_about")]
# Основное
screen ros_about_general_notepad():
    hbox:
        xpos 53 ypos 163
        text "Copyright 1997,98 Marcel Baur, 2000 Mike McCormack,\n2002 Sylvain Petreolle, 2002 Andriy Palamarchuk" style "ros_about_description"
screen ros_about_general_calc():
    hbox:
        xpos 53 ypos 163
        text "Автор: Карло Брамини\n" style "ros_about_description"
screen ros_about_general_placeholder():
    hbox:
        xpos 53 ypos 163
        text "\n" style "ros_about_description"
screen ros_about_general():
    vbox:
        xpos 53 ypos 177
        spacing 2
        text "Данная версия ReactOS зарегистрирована на:" style "ros_about_description"
        text "[username]" style "ros_about_description" xpos 16
        text "[organization]" style "ros_about_description" xpos 16
        add "gui/window/system_info/about_window_separator.png"
    hbox:
        xpos 53 ypos 187
        spacing 50
        text "Доступная физическая память:" style "ros_about_description"
        text "[ros_ram_capacity]" style "ros_about_description"
# Авторы
screen ros_about_general_authors():
    vbox:
        xpos 53 ypos 163
        text "Разработчики ReactOS:" style "ros_about_description"
        frame:
            ypos 2
            style "ros_authors_viewport"
            vbox:
                xpos 3 ypos 2
                text "Copyright 1993-2021 WINE team" style "ros_about_description"
                text "Copyright 1998-2021 ReactOS Team" style "ros_about_description"
                text "Porting to Ren'Py: MtnDewSmoker420, special for RG Smoking Room" style "ros_about_description"