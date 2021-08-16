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
transform ros_shutdown_background:
    matrixcolor SaturationMatrix(1.0)
    linear 1.5 matrixcolor SaturationMatrix(0.0)

# Выход из системы / Завершение работы
screen ros_logoff_frame():
    modal True
    on "show" action [Function(SetThumbnailFull), FileTakeScreenshot(), Function(SetThumbnailOriginal)]
    add FileCurrentScreenshot() at ros_shutdown_background
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
            imagebutton auto "gui/shutdown/log_off_%s.png" hovered Show(screen="ros_shutdown_tooltip_logoff") unhovered Hide(screen="ros_shutdown_tooltip_logoff") mouse "link" action Jump("ros_shutdown")
            text "Выход" style "ros_shutdown_buttons_text":
                ypos 5
        hbox:
            xpos 244 ypos 168
            textbutton "Отмена" style "ros_shutdown_cancel_button" text_style "ros_shutdown_cancel_text" focus_mask "gui/shutdown/cancel_idle.png" action Hide("ros_logoff_frame")
screen ros_shutdown_frame():
    modal True
    on "show" action [Function(SetThumbnailFull), FileTakeScreenshot(), Function(SetThumbnailOriginal)]
    add FileCurrentScreenshot() at ros_shutdown_background
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

# Выключение
label ros_shutdown:
    $ mouse_visible = False
    hide screen ros_desktop_icons
    hide screen ros_taskbar
    hide screen ros_shutdown_frame
    hide screen ros_logoff_frame
    hide screen ros_shutdown_tooltip_logoff
    hide screen ros_shutdown_tooltip_shutdown
    show screen please_wait("Завершение работы...")
    $ renpy.pause(1.0, hard=True)
    hide screen please_wait
    scene black
    $ renpy.quit()
# Перезагрузка
label ros_restart:
    $ mouse_visible = False
    hide screen ros_desktop_icons
    hide screen ros_taskbar
    hide screen ros_shutdown_frame
    hide screen ros_shutdown_tooltip_restart
    show screen please_wait("Перезагрузка...")
    $ renpy.pause(1.0, hard=True)
    hide screen please_wait
    scene black
    $ renpy.pause(0.5, hard=True)
    $ renpy.full_restart(transition=None, label="ros_boot")
