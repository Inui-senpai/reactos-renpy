# Оформление
style ros_boot_caret:
    font "gui/font/FSEX302.ttf"
    color "#c3c3c3"
image ros_boot_caret:
    Text("_", style="ros_boot_caret")
    subpixel True
    block:
        alpha 1
        0.55
        alpha 0
        0.55
        repeat

label ros_boot:
    python:
        quick_menu = mouse_visible = False
    scene black
    show ros_boot_text "Загрузка FreeLoader...":
        xalign 0 yalign 0
    show ros_boot_caret:
        ypos 10
    $ renpy.pause(0.2, hard=True)
    hide ros_boot_caret
    hide ros_boot_text
    show ros_boot_text "Загрузка системного куста..."
    show boot_progressbar
    $ renpy.pause(0.3, hard=True)
    show ros_boot_text "Обнаружение оборудования..."
    show boot_progressbar:
        xsize 134
    $ renpy.pause(0.2, hard=True)
    show ros_boot_text "Загрузка ntoskrnl.exe..."
    show boot_progressbar:
        xsize 198
    $ renpy.pause(0.2, hard=True)
    show ros_boot_text "Загрузка hal.dll..."
    show boot_progressbar:
        xsize 305
    $ renpy.pause(0.2, hard=True)
    show ros_boot_text "Загрузка загрузочных драйверов..."
    show boot_progressbar:
        xsize 683
    $ renpy.pause(0.5, hard=True)
    hide ros_boot_text
    hide boot_progressbar
    if not persistent.installed:
        jump ros_install
    $ renpy.pause(0.2, hard=True)
    jump graphic_boot

label graphic_boot:
    show graphic_boot_logo
    show graphic_boot_progressbar
    show graphic_boot_progress
    show graphic_boot_loading_bar_back
    show graphic_boot_loading_bar
    show graphic_boot_text "React{color=#b3cbd5}OS{/color}"
    show copyright_text "Авторское право © 1996-2022\nКоманда ReactOS и вкладчики"
    with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    hide graphic_boot_loading_bar
    show graphic_boot_loading_bar_animated
    $ renpy.pause(1.5, hard=True)
    show graphic_boot_progress:
        xsize 40
    $ renpy.pause(0.5, hard=True)
    show graphic_boot_progress:
        xsize 80
    $ renpy.pause(1.5, hard=True)
    show graphic_boot_progress:
        xsize 122
    $ renpy.pause(0.2, hard=True)
    if not persistent.provisioned:
        jump ros_postinstall
    else:
        jump ros_desktop
