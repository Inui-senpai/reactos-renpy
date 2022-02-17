# Оформление
image logon_background = Composite((1280, 720), (0, 0), "gui/logonui/background.png", (0, 0), "gui/logonui/header.png", (0, 630), "gui/logonui/footer.png")
image logon_ros_logo = "gui/logonui/ros_logo.png"
image logon_separator:
    "gui/logonui/separator.png"
    align(0.5, 0.5)
image logon_userpic_frame_hover = "gui/logonui/userpic_frame.png"
image logon_user_entry_idle:
    "logon_user_entry_hover"
    alpha 0.0
image logon_user_entry_hover = "gui/logonui/user_entry_hover.png"
image logon_user_entry_selected = "gui/logonui/user_entry_selected.png"
image logon_userpic_default_hover = "gui/logonui/userpic_default.png"
image logon_userpic_default_selected = "logon_userpic_default_hover"
image logon_log_in_idle = "gui/logonui/login_idle.png"
image logon_log_in_hover:
    "logon_log_in_idle"
    matrixcolor BrightnessMatrix(0.3)
image logon_help_idle = "gui/logonui/help_idle.png"
image logon_help_hover:
    "logon_help_idle"
    matrixcolor BrightnessMatrix(0.3)
image logon_password_input_field = "gui/logonui/password_field.png"
style logon_ros_logo_text:
    font "gui/font/Evolventa-Regular.ttf"
    size 24
    color "#000"
    text_align 1.0
style logon_ros_text:
    font "gui/font/tahoma.ttf"
    size 22
    color "#000"
    text_align 1.0
style logon_ros_footer_text:
    font "gui/font/tahoma.ttf"
    size 18
    color "#fff"
style logon_ros_footer_text_2 is logon_ros_footer_text:
    size 11
    text_align 1.0
style logon_ros_username_text:
    font "gui/font/tahoma.ttf"
    size 18
    color "#000"
style logon_ros_username_welcome_text is logon_ros_username_text:
    size 11
image logon_ros_username = Text("Администратор", style="logon_ros_username_text")
image logon_ros_username_welcome = Text("Добро пожаловать", style="logon_ros_username_welcome_text")
transform logon_ros_user_entry:
    alpha 0.5
    on idle:
        linear 0.4 alpha 0.5
    on hover:
        linear 0.4 alpha 1.0

# Основные переменные
default is_user_entry_selected = False

# Экран приветствия
screen ros_logonui(locked=False, in_shutdown=False, in_restart=False, in_logoff=False, in_login=False):
    default logon_page = 0
    python:
        if in_shutdown or in_restart or in_logoff:
            if logon_page == 0:
                logon_text = "Сохранение параметров..."
            elif logon_page  == 1:
                logon_text = "Завершение работы..." if in_shutdown else "Завершение сеанса..." if in_logoff else "Перезагрузка..."
        else:
            if logon_page == 0:
                logon_text = "Запуск ReactOS..."
            elif logon_page == 1:
                logon_text = "Добро пожаловать"
            elif logon_page == 2:
                logon_text = "Загружаются персональные настройки..."
    add "logon_background"
    if not in_shutdown and not in_restart and not in_logoff:
        if not locked and not in_login:
            add "logon_ros_logo":
                xalign 0.65 yalign 0.47
            add Text("React{color=#6d80ab}OS{/color}", style="logon_ros_logo_text"):
                xalign 0.638 yalign 0.532
            if logon_page == 0:
                add Text(logon_text, style="logon_ros_text"):
                    xalign 0.614 yalign 0.6
            elif logon_page == 1:
                add Text(logon_text, style="logon_ros_text"):
                    xalign 0.607 yalign 0.6
            elif logon_page == 2:
                add Text(logon_text, style="logon_ros_text"):
                    xalign 0.505 yalign 0.6
        elif in_login:
            add "logon_ros_logo":
                xpos 533 ypos 288
            add Text("React{color=#6d80ab}OS{/color}", style="logon_ros_logo_text"):
                xpos 494 ypos 352
            add Text("Загружаются персональные настройки...", style="logon_ros_text"):
                xpos 175 ypos 392
            add "logon_separator"
            hbox:
                xpos 663 ypos 316
                imagebutton idle Composite((318, 66), (0, 0), "logon_user_entry_selected", (11, 10), "logon_userpic_default_hover", (9, 8), "logon_userpic_frame_hover", (68, 4), "logon_ros_username", (68, 26), "logon_ros_username_welcome")
            add Text("После входа в систему можно добавлять или\nизменять учётные записи.\nДля этого в Панели управления нужно выбрать\n\"Учётные записи пользователей\".", style="logon_ros_footer_text_2"):
                xalign 0.98 yalign 0.972
        else:
            add "logon_ros_logo":
                xpos 533 ypos 288
            add Text("React{color=#6d80ab}OS{/color}", style="logon_ros_logo_text"):
                xpos 494 ypos 352
            add Text("Чтобы начать работу, выберите\nимя пользователя.", style="logon_ros_text"):
                xpos 259 ypos 392
            add "logon_separator"
            hbox:
                xpos 663 ypos 316
                imagebutton at logon_ros_user_entry:
                    idle Composite((318, 66), (0, 0), "logon_user_entry_idle", (11, 10), "logon_userpic_default_hover", (9, 8), "logon_userpic_frame_hover", (68, 4), "logon_ros_username")
                    hover Composite((318, 66), (0, 0), "logon_user_entry_hover", (11, 10), "logon_userpic_default_hover", (9, 8), "logon_userpic_frame_hover", (68, 4), "logon_ros_username")
                    focus_mask "logon_user_entry_hover"
                    mouse "link"
                    action [SetVariable("is_user_entry_selected", True), Jump("ros_desktop")]
            hbox:
                xpos 23 ypos 650
                spacing 5
                imagebutton auto "gui/shutdown/shutdown_%s.png" mouse "link" action Show("ros_shutdown_frame")
                text "Выключить компьютер" style "logon_ros_footer_text" ypos 3
            add Text("После входа в систему можно добавлять или\nизменять учётные записи.\nДля этого в Панели управления нужно выбрать\n\"Учётные записи пользователей\".", style="logon_ros_footer_text_2"):
                xalign 0.98 yalign 0.972
    else:
        add "logon_ros_logo":
            xalign 0.65 yalign 0.47
        add Text("React{color=#6d80ab}OS{/color}", style="logon_ros_logo_text"):
            xalign 0.638 yalign 0.532
        if logon_page == 0:
            add Text(logon_text, style="logon_ros_text"):
                xalign 0.58 yalign 0.6
        elif logon_page == 1 and (in_shutdown or in_logoff):
            add Text(logon_text, style="logon_ros_text"):
                xalign 0.597 yalign 0.6
        elif logon_page == 1 and in_restart:
            add Text(logon_text, style="logon_ros_text"):
                xalign 0.622 yalign 0.6

    timer 0.2 action SetScreenVariable("logon_page", 1)
    if not in_shutdown and not in_restart and not in_logoff:
        timer 0.3 action SetScreenVariable("logon_page", 2)
