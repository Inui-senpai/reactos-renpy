# Стили
style ros_shutdown:
    background Frame("gui/shutdown/dlg_bg.png")
style ros_shutdown_title:
    font "gui/font/tahoma.ttf"
    size 17
    color "#f4f4f4"
    xalign 0.04 yalign 0.06
style ros_shutdown_buttons_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    text_align 0.5
style ros_shutdown_cancel_button:
    idle_background "gui/shutdown/cancel_idle.png"
    hover_background "gui/shutdown/cancel_hover.png"
style ros_shutdown_cancel_text is ros_shutdown_buttons_text:
    xpos 7
style ros_shutdown_tooltip:
    background Frame("gui/shutdown/tooltip.png")
style ros_shutdown_tooltip_title:
    font "gui/font/tahomabd.ttf"
    size 11
    color "#000"
style ros_shutdown_tooltip_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
style ros_shutdown_legacy_choice:
    background Frame("gui/window/properties/dropdown_menu_shutdown_variant_idle.png")
    xysize(248, 21)
style ros_shutdown_legacy_choice_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    pos(3, 3)
style ros_shutdown_legacy_buttons:
    idle_background Frame("gui/window/properties/mouse_scheme_delete_button_idle.png")
    hover_background Frame("gui/window/properties/mouse_scheme_delete_button_hover.png")
    xysize(75, 23)
style ros_shutdown_legacy_buttons_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    pos(19, 4)
style ros_shutdown_legacy_buttons_text_ok is ros_shutdown_legacy_buttons_text:
    xpos 31
style ros_shutdown_legacy_buttons_text_logoff is ros_shutdown_legacy_buttons_text:
    xpos 21
style ros_shutdown_legacy_dropdown:
    background Frame("gui/window/properties/dropdown_list.png")
    xysize(248, 44)
style ros_shutdown_legacy_dropdown_menu_entry:
    idle_background "ros_shutdown_legacy_dropdown_menu_idle"
    hover_background "ros_shutdown_legacy_dropdown_menu_hover"
image ros_shutdown_legacy_dropdown_menu_idle:
    Solid("#fff")
    xsize 246 ysize 14
image ros_shutdown_legacy_dropdown_menu_hover:
    Solid("#0a246a")
    xsize 246 ysize 14
style ros_shutdown_legacy_dropdown_menu_entry_text:
    font "gui/font/tahoma.ttf"
    size 11
    idle_color "#000"
    hover_color "#fff"
    pos(2, 0)
style ros_logoff_legacy_window:
    background Frame("gui/window/common/window_small.png")
    xysize(288, 123)
transform ros_shutdown_background:
    matrixcolor SaturationMatrix(1.0)
    linear 1.5 matrixcolor SaturationMatrix(0.0)

# Основные переменные
default is_shutdown_variants_menu_opened = False

# Выход из системы / Завершение работы
screen ros_logoff_frame():
    modal True
    on "show" action [Function(SetThumbnailFull), FileTakeScreenshot(), Function(SetThumbnailOriginal)]
    add FileCurrentScreenshot() at ros_shutdown_background
    use expression "ros_logoff_" + persistent.selected_edition
screen ros_shutdown_frame():
    modal True
    on "show" action [Function(SetThumbnailFull), FileTakeScreenshot(), Function(SetThumbnailOriginal)]
    add FileCurrentScreenshot() at ros_shutdown_background
    use expression "ros_shutdown_" + persistent.selected_edition

# Выход из системы (рабочая станция)
screen ros_logoff_workstation():
    frame:
        style "ros_shutdown"
        xsize 312 ysize 198
        xalign 0.5 yalign 0.5
        text "Выход из ReactOS" style "ros_shutdown_title"
        add "gui/shutdown/reactos_flag.png":
            xalign 1.0 yalign 0.01
        vbox:
            xpos 84 ypos 76
            imagebutton auto "gui/shutdown/switch_user_%s.png"
            text "Смена пользователя" style "ros_shutdown_buttons_text":
                xpos -34 ypos 5
        vbox:
            xpos 199 ypos 76
            imagebutton auto "gui/shutdown/log_off_%s.png" hovered Show(screen="ros_shutdown_tooltip_logoff") unhovered Hide(screen="ros_shutdown_tooltip_logoff") mouse "link" action Jump("ros_logout")
            text "Выход" style "ros_shutdown_buttons_text":
                ypos 5
        hbox:
            xpos 244 ypos 168
            textbutton "Отмена" style "ros_shutdown_cancel_button" text_style "ros_shutdown_cancel_text" focus_mask "gui/shutdown/cancel_idle.png" action Hide("ros_logoff_frame")

# Выход из системы (сервер)
screen ros_logoff_server():
    drag:
        drag_name "ros_logoff"
        drag_handle (0, 0, 419, 22)
        xalign 0.5 yalign 0.5
        frame:
            style "ros_logoff_legacy_window"
            text "Выход из ReactOS" style "ros_wait_header_text":
                xpos -14 ypos 1
            imagebutton auto "gui/window/common/close_%s.png" action Hide("ros_logoff_frame"):
                xanchor -267 yanchor -5
            add "gui/desktop/desktop_icons/logoff.png":
                pos(13, 32)
            text "Вы уверены, что хотите выйти из ReactOS?" style "ros_shutdown_tooltip_text":
                pos(50, 37)
            hbox:
                align(0.5, 0.8)
                spacing 5
                textbutton "Выход" style "ros_shutdown_legacy_buttons" text_style "ros_shutdown_legacy_buttons_text_logoff" action Jump("ros_logout")
                textbutton "Отмена" style "ros_shutdown_legacy_buttons" text_style "ros_shutdown_legacy_buttons_text" action Hide("ros_logoff_frame")

# Завершение работы (рабочая станция)
screen ros_shutdown_workstation():
    frame:
        style "ros_shutdown"
        xsize 312 ysize 198
        xalign 0.5 yalign 0.5
        text "Завершение работы ReactOS" style "ros_shutdown_title":
            xalign 0.1
        add "gui/shutdown/reactos_flag.png":
            xalign 1.0 yalign 0.01
        vbox:
            xpos 55 ypos 76
            imagebutton auto "gui/shutdown/sleep_%s.png"
            text "Спящий режим" style "ros_shutdown_buttons_text":
                xpos -20 ypos 5
        vbox:
            xpos 141 ypos 76
            imagebutton auto "gui/shutdown/shutdown_%s.png" hovered Show(screen="ros_shutdown_tooltip_shutdown") unhovered Hide(screen="ros_shutdown_tooltip_shutdown") mouse "link" action Jump("ros_shutdown")
            text "Выключить" style "ros_shutdown_buttons_text":
                xpos -10 ypos 5
        vbox:
            xpos 226 ypos 76
            imagebutton auto "gui/shutdown/restart_%s.png" hovered Show(screen="ros_shutdown_tooltip_restart") unhovered Hide(screen="ros_shutdown_tooltip_restart") mouse "link" action Jump("ros_restart")
            text "Перезапустить" style "ros_shutdown_buttons_text":
                xpos -21 ypos 5
        hbox:
            xpos 244 ypos 168
            textbutton "Отмена" style "ros_shutdown_cancel_button" text_style "ros_shutdown_cancel_text" focus_mask "gui/shutdown/cancel_idle.png" action Hide("ros_shutdown_frame")

# Завершение работы (сервер)
screen ros_shutdown_server():
    python:
        shutdown_legacy_tooltip = {
            "shutdown":"Закрывает все программы, завершает работу ReactOS\nи выключает компьютер.",
            "logout":"Завершает текущий сеанс и позволяет другим\nпользователям войти в систему.",
            "restart":"Завершает текущий сеанс и перезагружает систему."
        }
        shutdown_choice_pretty = {
            "shutdown":"Завершение работы",
            "logout":"Выйти \"Администратор\"",
            "restart":"Перезагрузка"
        }
        shutdown_action = "ros_"+persistent.last_shutdown_choice
    drag:
        drag_name "ros_shutdown"
        drag_handle (0, 0, 419, 22)
        xalign 0.5 yalign 0.5
        frame:
            style "ros_logon_frame_legacy"
            text "Завершение работы ReactOS" style "ros_wait_header_text":
                xpos -24 ypos 1
            add "gui/window/pleasewait/poster.png":
                xalign 0.5 ypos 22
            add "ros_wait_loading_bar":
                yoffset 40
            imagebutton auto "gui/window/common/close_%s.png" action [
                SetVariable("is_shutdown_variants_menu_opened", False),
                Hide("ros_shutdown_frame")
            ]:
                xanchor -398 yanchor -5
            add "gui/desktop/desktop_icons/shutdown.png":
                pos(17, 115)
            vbox:
                pos(61, 116)
                spacing 2
                text "Выберите желаемое действие:" style "ros_shutdown_tooltip_text"
                textbutton shutdown_choice_pretty[persistent.last_shutdown_choice] style "ros_shutdown_legacy_choice" text_style "ros_shutdown_legacy_choice_text" focus_mask "gui/window/properties/dropdown_menu_shutdown_variant_idle.png" action ToggleVariable("is_shutdown_variants_menu_opened", True, False)
                null height 5
                text shutdown_legacy_tooltip[persistent.last_shutdown_choice] style "ros_shutdown_tooltip_text"
            hbox:
                pos(230, 221)
                spacing 10
                textbutton "ОК" style "ros_shutdown_legacy_buttons" text_style "ros_shutdown_legacy_buttons_text_ok" focus_mask "gui/window/properties/mouse_scheme_delete_button_idle.png" action [
                    SetVariable("is_shutdown_variants_menu_opened", False),
                    Jump(shutdown_action)
                ]
                textbutton "Отмена" style "ros_shutdown_legacy_buttons" text_style "ros_shutdown_legacy_buttons_text" focus_mask "gui/window/properties/mouse_scheme_delete_button_idle.png" action [
                    SetVariable("is_shutdown_variants_menu_opened", False),
                    Hide("ros_shutdown_frame")
                ]
            if is_shutdown_variants_menu_opened:
                use ros_shutdown_server_variants
# Варианты выбора желаемого действия
screen ros_shutdown_server_variants():
    frame:
        style "ros_shutdown_legacy_dropdown"
        pos(61, 153)
        vbox:
            pos(1, 1)
            textbutton "Выйти \"Администратор\"" style "ros_shutdown_legacy_dropdown_menu_entry" text_style "ros_shutdown_legacy_dropdown_menu_entry_text" focus_mask "ros_shutdown_legacy_dropdown_menu_idle" action [
                SetVariable("persistent.last_shutdown_choice", "logout"),
                SetVariable("is_shutdown_variants_menu_opened", False)
            ]
            textbutton "Завершение работы" style "ros_shutdown_legacy_dropdown_menu_entry" text_style "ros_shutdown_legacy_dropdown_menu_entry_text" focus_mask "ros_shutdown_legacy_dropdown_menu_idle" action [
                SetVariable("persistent.last_shutdown_choice", "shutdown"),
                SetVariable("is_shutdown_variants_menu_opened", False)
            ]
            textbutton "Перезагрузка" style "ros_shutdown_legacy_dropdown_menu_entry" text_style "ros_shutdown_legacy_dropdown_menu_entry_text" focus_mask "ros_shutdown_legacy_dropdown_menu_idle" action [
                SetVariable("persistent.last_shutdown_choice", "restart"),
                SetVariable("is_shutdown_variants_menu_opened", False)
            ]

# Подсказки в Выходе из системы / Завершении работы
screen ros_shutdown_tooltip_logoff():
    frame:
        style "ros_shutdown_tooltip"
        xsize 246 ysize 80
        xpos 679 ypos 273
        vbox:
            xpos 10 ypos 16
            text "Выход" style "ros_shutdown_tooltip_title"
            text "Закрывает все программы и завершает сеанс ReactOS." style "ros_shutdown_tooltip_text":
                ypos 6
screen ros_shutdown_tooltip_shutdown():
    frame:
        style "ros_shutdown_tooltip"
        xsize 246 ysize 80
        xpos 621 ypos 273
        vbox:
            xpos 10 ypos 16
            text "Завершение работы" style "ros_shutdown_tooltip_title"
            text "Закрывает все программы, завершает работу ReactOS и выключает компьютер." style "ros_shutdown_tooltip_text":
                ypos 6
screen ros_shutdown_tooltip_restart():
    frame:
        style "ros_shutdown_tooltip"
        xsize 246 ysize 80
        xpos 706 ypos 273
        vbox:
            xpos 10 ypos 16
            text "Перезагрузка" style "ros_shutdown_tooltip_title"
            text "Завершает текущий сеанс и перезагружает систему." style "ros_shutdown_tooltip_text":
                ypos 6

# Окно "Добро пожаловать в ReactOS" (сервер)
screen ros_welcome():
    python:
        ros_welcome_keys = "Ctrl-Alt-Пробел" if renpy.windows else "Ctrl-Alt-Del"
    drag:
        drag_name "ros_welcome"
        drag_handle (0, 0, 419, 22)
        xalign 0.5 yalign 0.5
        frame:
            style_prefix "ros_wait"
            xsize 419 ysize 152
            text "Добро пожаловать в ReactOS" style "ros_wait_header_text":
                xoffset -6
            add "gui/window/pleasewait/poster.png":
                xalign 0.5 ypos -18
            add "cp_keyboard_idle":
                xpos -26 ypos 68
            text "Нажмите клавиши [ros_welcome_keys]." style "ros_wait_text":
                xoffset 37 yoffset 3
            add "ros_wait_loading_bar"
    # На Windows нажатие Ctrl+Alt+Delete приведёт к вызову экрана параметров безопасности
    if not renpy.windows:
        key "ctrl_alt_K_DELETE" action [Hide("ros_welcome"), Show("ros_login_screen")]
    else:
        key "ctrl_alt_K_SPACE" action [Hide("ros_welcome"), Show("ros_login_screen")]

# Экран входа в систему (сервер)
style ros_logon_frame_legacy:
    background Frame("gui/logonui_legacy/window.png")
    xysize(419, 264)
style ros_logon_input_frame:
    background Frame("gui/logonui_legacy/input_field.png")
    xysize(233, 23)
style ros_logon_input_listbox_frame:
    background Frame("gui/logonui_legacy/login_to_field.png")
    xysize(233, 23)
style ros_logon_input_frame_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
style ros_logon_input_frames_header:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    ypos 4
style ros_logon_shutdown_button_text is ros_properties_buttons_text:
    xpos 11
screen ros_login_screen():
    drag:
        drag_name "ros_login_legacy"
        drag_handle (0, 0, 419, 22)
        xalign 0.5 yalign 0.5
        frame:
            style "ros_logon_frame_legacy"
            text "Вход в ReactOS" style "ros_wait_header_text":
                xpos -11 ypos 1
            add "gui/window/pleasewait/poster.png":
                xalign 0.5 ypos 22
            add "ros_wait_loading_bar":
                yoffset 40
            vbox:
                xpos 12 ypos 120
                spacing 8
                hbox:
                    spacing 7
                    text "Пользователь:" style "ros_logon_input_frames_header"
                    textbutton "Администратор" text_style "ros_logon_input_frame_text" style "ros_logon_input_frame" mouse "beam" action NullAction()
                hbox:
                    spacing 42
                    text "Пароль:" style "ros_logon_input_frames_header"
                    textbutton "" text_style "ros_logon_input_frame_text" style "ros_logon_input_frame" mouse "beam" action NullAction()
                hbox:
                    spacing 40
                    text "Войти в:" style "ros_logon_input_frames_header"
                    textbutton "[computer_name]" text_style "ros_logon_input_frame_text" style "ros_logon_input_listbox_frame" mouse "beam" action NullAction()
            hbox:
                xpos 144 ypos 220
                textbutton "ОК" style "ros_properties_buttons" text_style "ros_properties_buttons_text_ok" focus_mask "gui/window/postinstall/button_idle.png" action [Hide("ros_login_screen"), Jump("ros_desktop")]
                null width 72
                textbutton "Отмена" style "ros_properties_buttons" text_style "ros_properties_buttons_text_cancel" focus_mask "gui/window/postinstall/button_idle.png" action [Hide("ros_login_screen"), Jump("ros_shutdown")]
                null width 48
                textbutton "Выключение" style "ros_properties_buttons" text_style "ros_logon_shutdown_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Show("ros_shutdown_frame")

# Выход из системы
label ros_logout:
    $ mouse_visible = False
    hide screen ros_desktop_icons
    hide screen ros_taskbar
    hide screen ros_logoff_frame
    hide screen ros_shutdown_tooltip_logoff
    hide screen ros_shutdown_frame
    if persistent.selected_edition == "workstation":
        show screen ros_logonui(in_logoff=True)
        $ renpy.pause(1.0, hard=True)
    else:
        show screen please_wait("Сохранение параметров...")
        $ renpy.pause(0.2, hard=True)
        show screen please_wait("Завершение сеанса...")
        $ renpy.pause(0.5, hard=True)
        hide screen please_wait
        $ renpy.pause(0.1, hard=True)
    jump ros_login
# Вход в систему
label ros_login:
    $ mouse_visible = True
    if persistent.selected_edition == "workstation":
        show screen ros_logonui(locked=True)
        $ renpy.pause(hard=True)
    else:
        scene postinstall
        show corner_text:
            yalign 0.95
        show screen ros_welcome
        $ renpy.pause(hard=True)

# Выключение
label ros_shutdown:
    $ mouse_visible = False
    hide screen ros_desktop_icons
    hide screen ros_taskbar
    hide screen ros_shutdown_frame
    hide screen ros_logoff_frame
    hide screen ros_shutdown_tooltip_logoff
    hide screen ros_shutdown_tooltip_shutdown
    hide screen ros_login_screen
    if persistent.selected_edition == "workstation":
        show screen ros_logonui(in_shutdown=True)
        $ renpy.pause(1.0, hard=True)
        hide screen ros_logonui
    else:
        show screen please_wait("Сохранение параметров...")
        $ renpy.pause(0.2, hard=True)
        show screen please_wait("Завершение работы...")
        $ renpy.pause(1.0, hard=True)
        hide screen please_wait
    scene black
    $ renpy.pause(0.2, hard=True)
    $ renpy.quit()

# Перезагрузка
label ros_restart:
    $ mouse_visible = False
    hide screen ros_desktop_icons
    hide screen ros_taskbar
    hide screen ros_shutdown_frame
    hide screen ros_shutdown_tooltip_restart
    hide screen ros_login_screen
    if persistent.selected_edition == "workstation":
        show screen ros_logonui(in_restart=True)
        $ renpy.pause(1.0, hard=True)
        hide screen ros_logonui
    else:
        show screen please_wait("Сохранение параметров...")
        $ renpy.pause(0.2, hard=True)
        show screen please_wait("Перезагрузка...")
        $ renpy.pause(1.0, hard=True)
        hide screen please_wait
    scene black
    $ renpy.pause(0.5, hard=True)
    $ renpy.full_restart(transition=None, label="ros_boot")
