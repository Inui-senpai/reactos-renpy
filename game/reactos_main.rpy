# Основные переменные
default persistent.provisioned = False
default persistent.installed = False
default install_lang = "english"
define ros_build = "20210819-0.4.15-dev-3072-gc59c185.GNU_8.4.0"
define ros_build_short = ros_build[9:33]
define ros_build_wo_compiler = ros_build[:33]
default ros_install_directory = "ReactOS"
default apply_settings = False
default partition_hovered = False
default format_method = None
default next_step = None
default set_loader = None
default persistent.selected_edition = "workstation"
default admin_pass = ""
default admin_pass2 = ""
default daylight_saving_time = True
default network_setup_mode = "regular"
default workgroup = True
default start_menu_opened = False
default sort_entry = False
default create_entry = False
default toolbars_entry = False
default properties_current_tab = "general"
default persistent.wallpaper = None
default screensaver = None
default ros_theme = "classic"
default dropdown1 = False
default dropdown2 = False
default dropdown3 = False
default ros_properties_show_bottom_buttons = True
default persistent.user_theme = "reactos_classic"
default persistent.user_theme_color_scheme = "reactos_standard"
default selected_theme = "Классическая тема"
default default_color_scheme = "ReactOS стандартная"
default persistent.start_menu_layout = "legacy"
default persistent.taskbar_settings_lock_taskbar = True
default persistent.taskbar_settings_hide_taskbar = False
default persistent.taskbar_settings_keep_taskbar_on_top_of_other_windows = True
default persistent.taskbar_settings_group_similar_taskbar_buttons = False
default persistent.taskbar_settings_show_quick_launch = False
default persistent.taskbar_settings_show_clock = True
default persistent.taskbar_settings_show_seconds = False
default persistent.taskbar_settings_hide_inactive_icons = False

# Запись действия для кнопки "Вверх" в Проводнике
default this_pc_up_arrow_action = NullAction()

# Использование имеющихся шрифтов вместо псевдорежимов
init python:
    config.font_replacement_map["gui/font/tahoma.ttf", True, False] = ("gui/font/tahomabd.ttf", False, False)

# Узнаём техническую информацию реального ПК для пост-установки
init python:
    if renpy.windows:
        import subprocess
        username = os.environ["USERNAME"]
        organization, computer_name, workgroup_name = [
            line.strip()
            for line in subprocess.check_output(
                " && ".join((
                    "wmic os get organization",
                    "wmic computersystem get name",
                    "wmic computersystem get workgroup"
                )),
                universal_newlines=True,
                shell=True
            ).split("\n")
            if line
        ][1::2]
        if computer_name.startswith("DESKTOP") or computer_name.startswith("LAPTOP"): computer_name = computer_name.replace("DESKTOP","REACTOS").replace("LAPTOP","REACTOS")
    elif renpy.linux or renpy.macintosh:
        import pwd
        username = pwd.getpwuid(os.getuid()).pw_gecos.replace(",","")
        # местозаполнители
        organization, workgroup_name = ["", "WORKGROUP"]
        for i in range(7):
            computer_id = str(computer_id) + renpy.random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
        computer_name = "REACTOS-" + computer_id

# Закручивание гаек
define config.developer = False
init python:
    renpy.game.preferences.pad_enabled = False
    config.keymap["game_menu"] = []
    config.keymap["self_voicing"] = []
    config.keymap["clipboard_voicing"] = []
    config.keymap["toggle_skip"] = []
    config.keymap["help"] = []
    config.keymap["skip"] = []
    config.keymap["toggle_skip"] = []
    config.keymap["fast_skip"] = []
    config.keymap["hide_windows"] = []

# Текст лицензии GNU GPL 2.0
init python:
    license_text = renpy.file("gpl-2.0.txt").read()

# Часы на рабочем столе
init python:
    myClock = Clock(False, 0, 0, 46, False, True)
    myClock.runmode("real")

# Указатели мыши
define config.mouse = {"default":[("gui/mouse/arrow.png", 0, 0)], "helpsel":[("gui/mouse/helpsel.png", 0, 0)], "working":[("gui/mouse/working.png", 0, 0)], "busy":[("gui/mouse/busy.png", 15, 16)], "cross":[("gui/mouse/cross.png", 15, 15)], "beam":[("gui/mouse/beam.png", 15, 15)], "pen":[("gui/mouse/pen.png", 0, 0)], "unavail":[("gui/mouse/unavail.png", 16, 16)], "ns":[("gui/mouse/ns.png", 15, 15)], "ew":[("gui/mouse/ew.png", 15, 15)], "nwse":[("gui/mouse/nwse.png", 15, 15)], "nesw":[("gui/mouse/nesw.png", 15, 15)], "move":[("gui/mouse/move.png", 15, 15)], "up":[("gui/mouse/up.png", 15, 7)], "link":[("gui/mouse/link.png", 12, 4)]}

# Заливки сплошным цветом для загрузчика и установщика
image black = Solid("#000")
image setup = Solid("#0000c3")

# Плашка в нижней части установщика
image border:
    Solid("#c3c3c3")
    xsize 1280 ysize 22

# Заливка сплошным цветом для пост-установки
image postinstall = Solid("#3a6ea5")

# Заливки сплошным цветом для разных тем оформления
image blackshade_solid_color = "lautus_solid_color"
image lautus_solid_color = Solid("#494949")
image lunar_solid_color = Solid("#48636c")
image mizu_solid_color = Solid("#21578d")
image modern_solid_color = "lautus_solid_color"

# Текст с отладочной информацией в углу
style corner_text:
    font "gui/font/tahoma.ttf"
    color "#fff"
    size 11
    text_align 1.0
    align(1.0,1.0)

# Надписи в установщике
style install_text:
    font "gui/font/UniVGA16.ttf"
    color "#c3c3c3"
    size 22
style install_text_center is install_text:
    text_align 0.5
    size 25

# Надпись в нижней плашке
style install_border_text:
    font "gui/font/UniVGA16.ttf"
    color "#000"
    size 22
    xalign 0.05 yalign 1.0

# Область с выбором искомой локализации
image install_lang_choice_field:
    Solid("#c3c3c3")
    size(1203,419)
    pos(38,266)
image install_lang_choice_field_2:
    Solid("#0000c3")
    size(1199,415)
    pos(40,268)

# Выборки метода форматирования
style format_choose is devices_choose:
    xsize 800
style format_choose_text is devices_choose_text:
    xpos 12

# Область с разделами жёсткого диска
image partitions_field:
    Solid("#c3c3c3")
    size(1203,346)
    pos(38,338)
image partitions_field_2:
    Solid("#0000c3")
    size(1199,342)
    pos(40,340)
style partitions_field_text is devices_choose_text:
    text_align 0.5
style partitions_choose is devices_choose:
    xsize 1020
style partitions_choose_text is devices_choose_text:
    xpos 120

# Перечень устройств в установщике
style devices_choose:
    background "#0000c3"
    hover_background "#c3c3c3"
    xsize 820
    ysize 23
style devices_choose_text:
    font "gui/font/UniVGA16.ttf"
    color "#c3c3c3"
    hover_color "#000"
    xpos 20
style devices_choose_text_title is devices_choose_text:
    text_align 1.0

# Текстовый указатель директории для установки
image input_caret:
    Text("_", style="input_caret")
    subpixel True
    block:
        alpha 1
        0.55
        alpha 0
        0.55
        repeat
style input_caret:
    font "gui/font/UniVGA16.ttf"
    color "#000"
image directory_name_field:
    Solid("#c3c3c3")
    xsize 816 ysize 23
    pos(128,166)
style directory_name_text:
    font "gui/font/UniVGA16.ttf"
    color "#000"
    pos(128,166)

# Собственно, сам выбор локализации: внешняя и текстовая части
style lang_choose:
    background "#0000c3"
    hover_background "#c3c3c3"
    xsize 1191
    ysize 23
style lang_choose_text:
    font "gui/font/UniVGA16.ttf"
    color "#c3c3c3"
    hover_color "#000"
    xpos 20

# Процент прогресса форматирования
style formatting_text:
    font "gui/font/UniVGA16.ttf"
    color "#c3c3c3"
    text_align 0.5
    xalign 0.5 yalign 0.74

# Прогрессбар в форматировании
image formatting_progressbar:
    Solid("#ffff55")
    xsize 1 ysize 33
    xanchor 534 yanchor 176

# Прогрессбар в установке
image installing_progressbar:
    Solid("#ffff55")
    xsize 1 ysize 33
    xanchor 415 yanchor 319

# Прогрессбар в таймере перезагрузки
image reboot_progressbar:
    Solid("#c30000")
    xsize 1 ysize 33
    xanchor 415 yanchor 319
    linear 16.0 xsize 846

# Текст в загрузчике
style boot_text:
    font "gui/font/FSEX302.ttf"
    color "#c3c3c3"
    text_align 0.5
    size 18
    xalign 0.5 yalign 0.66

# Надписи на графическом экране загрузки
style graphic_boot_text:
    font "gui/font/Evolventa-Regular.ttf"
    color "#f6f8fa"
    text_align 0.5
    size 46
    xalign 0.5 yalign 0.6
style copyright_text:
    font "gui/font/tahoma.ttf"
    color "#f8f8f8"
    size 13
    xalign 0.04 yalign 0.96

# Элементы графического экрана
image graphic_boot_logo:
    "gui/bootscreen/logo.png"
    xalign 0.5 yalign 0.4
image graphic_boot_progressbar:
    "gui/bootscreen/progressbar.png"
    xalign 0.5 yalign 0.66
image graphic_boot_progress:
    Solid("#f5f7f9")
    xsize 1 ysize 13
    xanchor 61 yanchor 254
image graphic_boot_loading_bar:
    "gui/bootscreen/loading_bar.png"
    yalign 1.0
image graphic_boot_loading_bar_animated:
    "gui/bootscreen/loading_bar.png"
    yalign 1.0
    xpos 641
    block:
        linear 1.5 xpos 1800
    block:
        xpos -1800
        linear 3.5 xpos 1800
        repeat
image graphic_boot_loading_bar_back:
    Solid("#0e171a")
    size(1280,9)
    yalign 1.0

# Окно "Пожалуйста, подождите"
screen please_wait(message="Dolor sit amet"):
    drag:
        drag_name "ros_please_wait"
        drag_handle (0, 0, 419, 22)
        xalign 0.5 yalign 0.5
        frame:
            style_prefix "ros_wait"
            xsize 419 ysize 152
            text "Пожалуйста, подождите..." style "ros_wait_header_text"
            add "gui/window/pleasewait/poster.png":
                xalign 0.5 ypos -18
            text message style "ros_wait_text"
            add "ros_wait_loading_bar"

# Стили для окна "Пожалуйста, подождите"
style ros_wait_header_text:
    font "gui/font/tahomabd.ttf"
    size 11
    color "#fff"
    xalign -0.18 yalign -0.55
style ros_wait_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    xpos -20 ypos 75
style ros_wait_frame is confirm_frame:
    background Frame("gui/window/pleasewait/window.png", gui.confirm_frame_borders, tile=gui.frame_tile)
    xalign 0
    yalign 0

# Стиль для надписи в "распространённом" окне
style ros_common_window_text is ros_wait_header_text:
    xpos -39 ypos -39

# Стили для окна установщика
style ros_setup1_frame is ros_wait_frame:
    background Frame("gui/window/postinstall/window.png", gui.confirm_frame_borders, tile=gui.frame_tile)
style ros_setup2_frame is ros_wait_frame:
    background Frame("gui/window/postinstall/window_step2.png", gui.confirm_frame_borders, tile=gui.frame_tile)
style ros_setup_header_text is ros_wait_header_text:
    xalign -0.12 yalign -0.11
style ros_setup_page_bold_text:
    font "gui/font/tahomabd.ttf"
    size 17
    color "#000"
    xpos 132
style ros_setup_page_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    xpos 132 ypos 46
style ros_setup_page_lower_text is ros_setup_page_text:
    yalign 0.9
style ros_setup_button:
    insensitive_background "gui/window/postinstall/button_idle.png"
    idle_background "gui/window/postinstall/button_idle.png"
    hover_background "gui/window/postinstall/button_hover.png"
style ros_setup_button_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    insensitive_color "#808080"
    xpos 15
style ros_setup_description_title:
    font "gui/font/tahomabd.ttf"
    size 11
    color "#000"
    xpos -15 ypos -5
style ros_setup_description:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    ypos 10
style ros_setup_dropdown_list:
    insensitive_background "gui/window/postinstall/dropdown_box_idle.png"
    idle_background "gui/window/postinstall/dropdown_box_idle.png"
    selected_hover_background "gui/window/postinstall/dropdown_box_selected.png"
style ros_setup_dropdown_list_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    insensitive_color "#000"
    hover_color "#000"
    selected_hover_color "#fff"
    xpos 4 ypos 3
style ros_setup_license_button is ros_setup_button_text:
    xpos 8
style ros_setup_developers_box is game_menu_content_frame:
    background Frame("gui/window/postinstall/developers_box.png")
    left_margin 0
    right_margin 0
    top_margin 0
    xsize 429 ysize 122
    xpos -8 ypos 100
style ros_setup_developers_description is ros_setup_description:
    xpos 3 ypos 0
style ros_setup_license_frame is ros_wait_frame:
    background Frame("gui/window/postinstall/license_window.png", gui.confirm_frame_borders, tile=gui.frame_tile)
style ros_setup_license_box is ros_setup_developers_box:
    background Frame("gui/window/postinstall/license_box.png")
    xsize 479 ysize 309
    xpos -25 ypos -10
style ros_setup_license_button_ok is ros_setup_button_text:
    xpos 29
style ros_setup_set_up_button is ros_setup_license_button:
    xpos 6
style ros_input_field:
    insensitive_background "gui/window/postinstall/input_field.png"
    idle_background "gui/window/postinstall/input_field.png"
style ros_input_field_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    xpos 4 ypos 3
style ros_setup_date:
    insensitive_background "gui/window/postinstall/date_dropdown_box.png"
    idle_background "gui/window/postinstall/date_dropdown_box.png"
style ros_setup_date_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    xpos 4 ypos 3
style ros_setup_time:
    insensitive_background "gui/window/postinstall/time_adjust_box.png"
    idle_background "gui/window/postinstall/time_adjust_box.png"
style ros_setup_time_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    xpos 4 ypos 3
style ros_setup_timezone:
    insensitive_background "gui/window/postinstall/timezone_dropdown_box.png"
    idle_background "gui/window/postinstall/timezone_dropdown_box.png"
style ros_setup_timezone_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    xpos 4 ypos 3
style ros_setup_theme_choose_frame:
    background Frame("gui/window/postinstall/theme_choose_frame.png")
    ypos 70
style ros_setup_theme_choose_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    text_align 0.5
    xalign 0.5 yalign 0.9
style ros_setup_gecko_frame is ros_wait_frame:
    background Frame("gui/window/postinstall/gecko_install_window.png")
style ros_setup_button_text_install is ros_setup_button_text:
    xpos 5
style ros_setup_button_text_done is ros_setup_button_text:
    xpos 18

# Прогрессбар регистрации компонентов
image ros_setup_registration_progress:
    Solid("#0b246a")
    xsize 14 ysize 9
    xanchor -22 yanchor -172
    pause 5.0
    xsize 376

# Прогрессбар загрузки и установки Wine Gecko
image ros_setup_gecko_installing_progress:
    Solid("#0b246a")
    xsize 1 ysize 16
    xanchor 20 yanchor -50
    linear 25.0 xsize 355

# Прогрессбар обратного отсчёта на последней странице установщика
image ros_setup_final_countdown_progress:
    Solid("#0b246a")
    xsize 1 ysize 16
    xanchor -134 yanchor -202
    linear 16.0 xsize 278

# Рабочий стол
# Панель задач - Активное окно
style ros_taskbar_window_buttons:
    idle_background "gui/desktop/taskbar_window_idle.png"
    hover_background "gui/desktop/taskbar_window_idle.png"
    selected_background "gui/desktop/taskbar_window_selected.png"
style ros_taskbar_window_buttons_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    selected_color "#000"
    xpos 8 ypos 4
# Кнопка "Пуск"
style ros_start_button:
    idle_background "gui/desktop/start_button.png"
    hover_background "gui/desktop/start_button.png"
    selected_background "gui/desktop/start_button_selected.png"
style ros_start_button_text:
    font "gui/font/tahomabd.ttf"
    color "#000"
    hover_color "#000"
    selected_color "#000"
    size 11
    xpos 20
# Часы
style ros_taskbar_clock_text:
    font "gui/font/tahoma.ttf"
    color "#000"
    size 11
# Названия иконок на рабочем столе
style ros_desktop_icon_text:
    font "gui/font/tahoma.ttf"
    color "#fff"
    size 11
    text_align 0.5
    outlines [(0, "#000", 1, 1)]
# Меню "Пуск"
# Унаследованное ("Классическое")
style ros_start_menu:
    background Frame("gui/desktop/start_menu.png")
style ros_start_menu_entry_text:
    font "gui/font/tahoma.ttf"
    color "#000"
    hover_color "#fff"
    insensitive_color "#808080"
    size 11
    xpos 40 ypos 10
style ros_start_menu_entry:
    idle_background "ros_start_menu_entry_idle"
    hover_background "ros_start_menu_entry_hover"
    insensitive_background "ros_start_menu_entry_idle"
image ros_start_menu_entry_idle:
    Solid("#d4d0c8")
    xsize 232 ysize 35
image ros_start_menu_entry_hover:
    Solid("#0a246a")
    xsize 232 ysize 35
# Новое ("Современное")
style ros_start_menu_new:
    background Frame("gui/desktop/start_menu_new.png")
style ros_start_menu_new_username:
    font "gui/font/tahomabd.ttf"
    color "#fff"
    size 18
    xpos 20 ypos 15
style ros_start_menu_new_entry:
    idle_background "ros_start_menu_new_entry_idle"
    hover_background "ros_start_menu_new_entry_hover"
    insensitive_background "ros_start_menu_new_entry_idle"
image ros_start_menu_new_entry_idle:
    Solid("#d4d0c8")
    xsize 180 ysize 28
image ros_start_menu_new_entry_hover:
    Solid("#0a246a")
    xsize 180 ysize 28
style ros_start_menu_new_entry_text:
    font "gui/font/tahoma.ttf"
    color "#000"
    hover_color "#fff"
    insensitive_color "#808080"
    size 11
    xpos 36 ypos 8
style ros_start_menu_new_entry_title_text is ros_start_menu_new_entry_text:
    font "gui/font/tahomabd.ttf"
style ros_start_menu_new_entry_text_two_rows is ros_start_menu_new_entry_text:
    ypos 0
style ros_start_menu_new_logoff:
    idle_background "ros_start_menu_new_logoff_idle"
    hover_background "ros_start_menu_new_logoff_hover"
image ros_start_menu_new_logoff_idle:
    Solid("#d4d0c8")
    xsize 130 ysize 29
image ros_start_menu_new_logoff_hover:
    Solid("#0a246a")
    xsize 130 ysize 29
style ros_start_menu_new_shutdown:
    idle_background "ros_start_menu_new_shutdown_idle"
    hover_background "ros_start_menu_new_shutdown_hover"
image ros_start_menu_new_shutdown_idle:
    Solid("#d4d0c8")
    xsize 102 ysize 29
image ros_start_menu_new_shutdown_hover:
    Solid("#0a246a")
    xsize 102 ysize 29
style ros_start_menu_new_logoff_text:
    font "gui/font/tahoma.ttf"
    color "#000"
    hover_color "#fff"
    size 11
    xpos 35 ypos 8
style ros_start_menu_new_shutdown_text:
    font "gui/font/tahoma.ttf"
    color "#000"
    hover_color "#fff"
    size 11
    xpos 35 ypos 8

# Захват экрана для дальнейшей работы с ним
init python:
    def SetThumbnailFull():
        config.thumbnail_width = config.screen_width
        config.thumbnail_height = config.screen_height
    def SetThumbnailOriginal():
        config.thumbnail_width = 256
        config.thumbnail_height = 144

# Контекстное меню
style ros_desktop_context_menu:
    background Frame("gui/desktop/context_menu.png")
style ros_context_menu:
    idle_background "ros_context_menu_idle"
    hover_background "ros_context_menu_hover"
    insensitive_background "ros_context_menu_idle"
style ros_context_menu_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#fff"
    insensitive_color "#808080"
    xpos 10 ypos 1
image ros_context_menu_idle:
    Solid("#d4d0c8")
    xsize 132 ysize 17
image ros_context_menu_hover:
    Solid("#0a246a")
    xsize 132 ysize 17
style ros_context_menu_sort_by:
    idle_background "ros_context_menu_sort_by_idle"
    hover_background "ros_context_menu_sort_by_hover"
    insensitive_background "ros_context_menu_sort_by_idle"
image ros_context_menu_sort_by_idle:
    Solid("#d4d0c8")
    xsize 107 ysize 17
image ros_context_menu_sort_by_hover:
    Solid("#0a246a")
    xsize 107 ysize 17
style ros_context_menu_create:
    idle_background "ros_context_menu_create_idle"
    hover_background "ros_context_menu_create_hover"
    insensitive_background "ros_context_menu_create_idle"
image ros_context_menu_create_idle:
    Solid("#d4d0c8")
    xsize 162 ysize 17
image ros_context_menu_create_hover:
    Solid("#0a246a")
    xsize 162 ysize 17
style ros_context_menu_create_text is ros_context_menu_text:
    xpos 22
style ros_context_menu_this_pc:
    idle_background "ros_context_menu_this_pc_idle"
    hover_background "ros_context_menu_this_pc_hover"
    insensitive_background "ros_context_menu_this_pc_idle"
image ros_context_menu_this_pc_idle:
    Solid("#d4d0c8")
    xsize 124 ysize 17
image ros_context_menu_this_pc_hover:
    Solid("#0a246a")
    xsize 124 ysize 17
style ros_context_menu_title is ros_context_menu_text:
    font "gui/font/tahomabd.ttf"
    ypos 2
style ros_context_menu_taskbar:
    idle_background "ros_context_menu_taskbar_idle"
    hover_background "ros_context_menu_taskbar_hover"
    insensitive_background "ros_context_menu_taskbar_idle"
image ros_context_menu_taskbar_idle:
    Solid("#d4d0c8")
    xsize 205 ysize 17
image ros_context_menu_taskbar_hover:
    Solid("#0a246a")
    xsize 205 ysize 17
style ros_context_menu_toolbars:
    idle_background "ros_context_menu_toolbars_idle"
    hover_background "ros_context_menu_toolbars_hover"
    insensitive_background "ros_context_menu_toolbars_idle"
image ros_context_menu_toolbars_idle:
    Solid("#d4d0c8")
    xsize 192 ysize 17
image ros_context_menu_toolbars_hover:
    Solid("#0a246a")
    xsize 192 ysize 17

# Окно раздела меню "Пуск"
style ros_start_menu_frame:
    background Frame("gui/desktop/start_menu_folder_frame.png")
style ros_start_menu_submenu:
    idle_background "ros_start_menu_submenu_idle"
    hover_background "ros_start_menu_submenu_hover"
style ros_start_menu_submenu_text:
    font "gui/font/tahoma.ttf"
    color "#000"
    hover_color "#fff"
    insensitive_color "#808080"
    size 11
    xpos 27 ypos 2
image ros_start_menu_submenu_idle:
    Solid("#d4d0c8")
    xsize 208 ysize 18
image ros_start_menu_submenu_hover:
    Solid("#0a246a")
    xsize 208 ysize 18
style ros_start_menu_submenu_administration:
    idle_background "ros_start_menu_submenu_administration_idle"
    hover_background "ros_start_menu_submenu_administration_hover"
image ros_start_menu_submenu_administration_idle:
    Solid("#d4d0c8")
    xsize 152 ysize 18
image ros_start_menu_submenu_administration_hover:
    Solid("#0a246a")
    xsize 152 ysize 18
style ros_start_menu_submenu_games:
    idle_background "ros_start_menu_submenu_games_idle"
    hover_background "ros_start_menu_submenu_games_hover"
image ros_start_menu_submenu_games_idle:
    Solid("#d4d0c8")
    xsize 130 ysize 18
image ros_start_menu_submenu_games_hover:
    Solid("#0a246a")
    xsize 130 ysize 18
style ros_start_menu_submenu_system_tools:
    idle_background "ros_start_menu_submenu_system_tools_idle"
    hover_background "ros_start_menu_submenu_system_tools_hover"
image ros_start_menu_submenu_system_tools_idle:
    Solid("#d4d0c8")
    xsize 185 ysize 18
image ros_start_menu_submenu_system_tools_hover:
    Solid("#0a246a")
    xsize 185 ysize 18
style ros_start_menu_submenu_entertainment:
    idle_background "ros_start_menu_submenu_entertainment_idle"
    hover_background "ros_start_menu_submenu_entertainment_hover"
image ros_start_menu_submenu_entertainment_idle:
    Solid("#d4d0c8")
    xsize 125 ysize 18
image ros_start_menu_submenu_entertainment_hover:
    Solid("#0a246a")
    xsize 125 ysize 18
style ros_start_menu_submenu_communications:
    idle_background "ros_start_menu_submenu_communications_idle"
    hover_background "ros_start_menu_submenu_communications_hover"
image ros_start_menu_submenu_communications_idle:
    Solid("#d4d0c8")
    xsize 268 ysize 18
image ros_start_menu_submenu_communications_hover:
    Solid("#0a246a")
    xsize 268 ysize 18
style ros_start_menu_submenu_services:
    idle_background "ros_start_menu_submenu_services_idle"
    hover_background "ros_start_menu_submenu_services_hover"
image ros_start_menu_submenu_services_idle:
    Solid("#d4d0c8")
    xsize 244 ysize 18
image ros_start_menu_submenu_services_hover:
    Solid("#0a246a")
    xsize 244 ysize 18
style ros_start_menu_submenu_accessibility:
    idle_background "ros_start_menu_submenu_accessibility_idle"
    hover_background "ros_start_menu_submenu_accessibility_hover"
image ros_start_menu_submenu_accessibility_idle:
    Solid("#d4d0c8")
    xsize 210 ysize 18
image ros_start_menu_submenu_accessibility_hover:
    Solid("#0a246a")
    xsize 210 ysize 18
style ros_start_menu_submenu_documents:
    idle_background "ros_start_menu_submenu_documents_idle"
    hover_background "ros_start_menu_submenu_documents_hover"
image ros_start_menu_submenu_documents_idle:
    Solid("#d4d0c8")
    xsize 124 ysize 18
image ros_start_menu_submenu_documents_hover:
    Solid("#0a246a")
    xsize 124 ysize 18
style ros_start_menu_submenu_settings:
    idle_background "ros_start_menu_submenu_settings_idle"
    hover_background "ros_start_menu_submenu_settings_hover"
image ros_start_menu_submenu_settings_idle:
    Solid("#d4d0c8")
    xsize 187 ysize 18
image ros_start_menu_submenu_settings_hover:
    Solid("#0a246a")
    xsize 187 ysize 18

# Иконки в разделах меню "Пуск"
image app_manager_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/app_manager.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image explorer_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/explorer.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image services_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/services.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image device_manager_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/device_manager.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image system_settings_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/system_settings.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image event_viewer_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/event_viewer.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image solitaire_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/solitaire.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image spider_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/spider.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image minesweeper_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/minesweeper.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image paint_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/paint.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image wordpad_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/wordpad.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image notepad_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/notepad.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image calc_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/calc.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image cmd_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/cmd.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image volume_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/volume.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image recorder_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/recorder.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image media_player_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/media_player.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image rdp_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/rdp.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image clipboard_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/clipboard.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image task_manager_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/task_manager.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image layout_switcher_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/layout_switcher.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image registry_editor_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/regedit.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image rxdiag_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/rxdiag.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image charmap_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/charmap.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image service_manager_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/service_manager.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image osk_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/osk.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image magnify_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/magnify.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")
image iexplore_shortcut = im.Composite((16, 16), (0, 0), "gui/desktop/menu_icons/submenu/iexplore.png", (0, 0), "gui/desktop/menu_icons/submenu/shortcut.png")

# Иконки в обзоре Проводника
image this_pc_disk_drive_idle = "gui/desktop/desktop_icons/disk_drive.png"
image this_pc_disk_drive_hover:
    "this_pc_disk_drive_idle",
    matrixcolor TintMatrix("#808db0")
image this_pc_cd_drive_idle = "gui/desktop/desktop_icons/cd_drive.png"
image this_pc_cd_drive_hover:
    "this_pc_cd_drive_idle",
    matrixcolor TintMatrix("#808db0")
image this_pc_control_panel_idle = "gui/desktop/desktop_icons/control_panel.png"
image this_pc_control_panel_hover:
    "this_pc_control_panel_idle",
    matrixcolor TintMatrix("#808db0")
image this_pc_namespaces_idle = "gui/desktop/desktop_icons/namespaces.png"
image this_pc_namespaces_hover:
    "this_pc_namespaces_idle",
    matrixcolor TintMatrix("#808db0")
image this_pc_system_registry_idle = "gui/desktop/desktop_icons/system_registry.png"
image this_pc_system_registry_hover:
    "this_pc_system_registry_idle",
    matrixcolor TintMatrix("#808db0")
image this_pc_videos_idle = "gui/desktop/desktop_icons/videos.png"
image this_pc_videos_hover:
    "this_pc_videos_idle",
    matrixcolor TintMatrix("#808db0")
image this_pc_pictures_idle = "gui/desktop/desktop_icons/pictures.png"
image this_pc_pictures_hover:
    "this_pc_pictures_idle",
    matrixcolor TintMatrix("#808db0")
image this_pc_music_idle = "gui/desktop/desktop_icons/music.png"
image this_pc_music_hover:
    "this_pc_music_idle",
    matrixcolor TintMatrix("#808db0")

# Иконки в Панели управления
image cp_administrative_tools_idle = "gui/desktop/menu_icons/control_panel/administrative_tools.png"
image cp_administrative_tools_hover:
    "cp_administrative_tools_idle",
    matrixcolor TintMatrix("#808db0")
image cp_timedate_idle = "gui/desktop/menu_icons/control_panel/timedate.png"
image cp_timedate_hover:
    "cp_timedate_idle",
    matrixcolor TintMatrix("#808db0")
image cp_sounds_and_audio_devices_idle = "gui/desktop/menu_icons/control_panel/sounds_and_audio_devices.png"
image cp_sounds_and_audio_devices_hover:
    "cp_sounds_and_audio_devices_idle",
    matrixcolor TintMatrix("#808db0")
image cp_game_controllers_idle = "gui/desktop/menu_icons/control_panel/game_controllers.png"
image cp_game_controllers_hover:
    "cp_game_controllers_idle",
    matrixcolor TintMatrix("#808db0")
image cp_iexplore_settings_idle = "gui/desktop/menu_icons/control_panel/iexplore_settings.png"
image cp_iexplore_settings_hover:
    "cp_iexplore_settings_idle",
    matrixcolor TintMatrix("#808db0")
image cp_keyboard_idle = "gui/desktop/menu_icons/control_panel/keyboard.png"
image cp_keyboard_hover:
    "cp_keyboard_idle",
    matrixcolor TintMatrix("#808db0")
image cp_command_prompt_idle = "gui/desktop/menu_icons/control_panel/command_prompt.png"
image cp_command_prompt_hover:
    "cp_command_prompt_idle",
    matrixcolor TintMatrix("#808db0")
image cp_mouse_idle = "gui/desktop/menu_icons/control_panel/mouse.png"
image cp_mouse_hover:
    "cp_mouse_idle",
    matrixcolor TintMatrix("#808db0")
image cp_opengl_settings_idle = "gui/desktop/menu_icons/control_panel/opengl_settings.png"
image cp_opengl_settings_hover:
    "cp_opengl_settings_idle",
    matrixcolor TintMatrix("#808db0")
image cp_wined3dcfg_idle = "gui/desktop/menu_icons/control_panel/wined3dcfg.png"
image cp_wined3dcfg_hover:
    "cp_wined3dcfg_idle",
    matrixcolor TintMatrix("#808db0")
image cp_printers_idle = "gui/desktop/menu_icons/control_panel/printers.png"
image cp_printers_hover:
    "cp_printers_idle",
    matrixcolor TintMatrix("#808db0")
image cp_folder_options_idle = "gui/desktop/menu_icons/control_panel/folder_options.png"
image cp_folder_options_hover:
    "cp_folder_options_idle",
    matrixcolor TintMatrix("#808db0")
image cp_netshell_idle = "gui/desktop/menu_icons/control_panel/netshell.png"
image cp_netshell_hover:
    "cp_netshell_idle",
    matrixcolor TintMatrix("#808db0")
image cp_system_idle = "gui/desktop/menu_icons/control_panel/system.png"
image cp_system_hover:
    "cp_system_idle",
    matrixcolor TintMatrix("#808db0")
image cp_ease_of_access_idle = "gui/desktop/menu_icons/control_panel/ease_of_access.png"
image cp_ease_of_access_hover:
    "cp_ease_of_access_idle",
    matrixcolor TintMatrix("#808db0")
image cp_phone_and_modem_idle = "gui/desktop/menu_icons/control_panel/phone_and_modem.png"
image cp_phone_and_modem_hover:
    "cp_phone_and_modem_idle",
    matrixcolor TintMatrix("#808db0")
image cp_setup_idle = "gui/desktop/menu_icons/control_panel/setup.png"
image cp_setup_hover:
    "cp_setup_idle",
    matrixcolor TintMatrix("#808db0")
image cp_hardware_setup_idle = "gui/desktop/menu_icons/control_panel/hardware_setup.png"
image cp_hardware_setup_hover:
    "cp_hardware_setup_idle",
    matrixcolor TintMatrix("#808db0")
image cp_users_idle = "gui/desktop/menu_icons/control_panel/users.png"
image cp_users_hover:
    "cp_users_idle",
    matrixcolor TintMatrix("#808db0")
image cp_fonts_idle = "gui/desktop/menu_icons/control_panel/fonts.png"
image cp_fonts_hover:
    "cp_fonts_idle",
    matrixcolor TintMatrix("#808db0")
image cp_screen_settings_idle = "gui/desktop/menu_icons/control_panel/screen_settings.png"
image cp_screen_settings_hover:
    "cp_screen_settings_idle",
    matrixcolor TintMatrix("#808db0")
image cp_power_options_idle = "gui/desktop/menu_icons/control_panel/power_options.png"
image cp_power_options_hover:
    "cp_power_options_idle",
    matrixcolor TintMatrix("#808db0")
image cp_language_and_regional_standards_idle = "gui/desktop/menu_icons/control_panel/language_and_regional_standards.png"
image cp_language_and_regional_standards_hover:
    "cp_language_and_regional_standards_idle",
    matrixcolor TintMatrix("#808db0")

# Ярлыки на Рабочем столе
image desk_recycle_bin_idle = "gui/desktop/desktop_icons/recycle_bin.png"
image desk_recycle_bin_hover:
    "desk_recycle_bin_idle",
    matrixcolor TintMatrix("#808db0")
image desk_documents_idle = "gui/desktop/desktop_icons/documents.png"
image desk_documents_hover:
    "desk_documents_idle",
    matrixcolor TintMatrix("#808db0")
image desk_this_pc_idle = "gui/desktop/desktop_icons/this_pc.png"
image desk_this_pc_hover:
    "desk_this_pc_idle",
    matrixcolor TintMatrix("#808db0")
image desk_network_idle = "gui/desktop/desktop_icons/network.png"
image desk_network_hover:
    "desk_network_idle",
    matrixcolor TintMatrix("#808db0")
image desk_command_prompt_shortcut_idle = im.Composite((32, 32), (0, 0), "gui/desktop/desktop_icons/command_prompt.png", (0, 0), "gui/desktop/desktop_icons/shortcut.png")
image desk_command_prompt_shortcut_hover:
    "desk_command_prompt_shortcut_idle",
    matrixcolor TintMatrix("#808db0")
image desk_app_manager_shortcut_idle = im.Composite((32, 32), (0, 0), "gui/desktop/desktop_icons/app_manager.png", (0, 0), "gui/desktop/desktop_icons/shortcut.png")
image desk_app_manager_shortcut_hover:
    "desk_app_manager_shortcut_idle",
    matrixcolor TintMatrix("#808db0")
image desk_readme_shortcut_idle = im.Composite((32, 32), (0, 0), "gui/desktop/desktop_icons/readme.png", (0, 0), "gui/desktop/desktop_icons/shortcut.png")
image desk_readme_shortcut_hover:
    "desk_readme_shortcut_idle",
    matrixcolor TintMatrix("#808db0")

# Узнаём системные дату и время
init python:
    import datetime
    import time
    now = datetime.datetime.now()
    month = now.month
    months = (None, "января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря")
    cur_date = now.strftime("%d {0} %Y").format(months[month])
    cur_time = now.strftime("%H:%M:%S")
    cur_tz = time.tzname[0][:6]

# Расчёт времени работы системы
init python:
    def ros_uptime_counter(seconds):
        mins, secs = divmod(int(float(seconds)), 60)
        hours, minutes = divmod(mins, 60)
        days = divmod(hours, 24)
        if hours > 23: hours = hours - 24
        ros_days = str(days) if hours > 23 else "0"
        ros_hours = "0" + str(hours) if len(str(hours)) == 1 else str(hours)
        ros_minutes = "0" + str(minutes) if len(str(minutes)) == 1 else str(minutes)
        ros_seconds = "0" + str(secs) if len(str(secs)) == 1 else str(secs)
        return ros_days + " дн., " + ros_hours + ":" + ros_minutes + ":" + ros_seconds

# Расчёт реального количества ОЗУ
init python:
    def get_size(bytes, suffix="Б"):
        factor = 1024
        for unit in ["", "К", "М", "Г", "Т", "П"]:
            if bytes < factor:
                # return f"{bytes:.2f}{unit}{suffix}"
                return "{0} {1}{2}".format(bytes, unit, suffix)
            bytes /= factor

# Узнаём техническую информацию реального ПК для окна Свойств системы
init python:
    if renpy.windows:
        import subprocess
        ros_pc_model, ros_processor_manufacturer, ros_processor_name, ros_processor_frequency, ros_ram_capacity = [
            line.strip()
            for line in subprocess.check_output(
                " && ".join((
                    "wmic computersystem get model",
                    "wmic cpu get manufacturer",
                    "wmic cpu get name",
                    "wmic cpu get currentclockspeed",
                    "wmic memorychip get capacity"
                )),
                universal_newlines=True,
                shell=True
            ).split("\n")
            if line
        ][1::2]
        ros_ram_capacity = get_size(int(ros_ram_capacity))
    elif renpy.linux or renpy.macintosh:
        # местозаполнители
        ros_pc_model, ros_processor_manufacturer, ros_processor_name, ros_processor_frequency, ros_ram_capacity = [
            "", "", "", "", ""
        ]

# Полоса загрузки в окне "Пожалуйста, подождите"
image ros_wait_loading_bar:
    "gui/window/pleasewait/loading_bar.png"
    xalign 0.5 ypos 54
# TODO: Анимировать полосу загрузки в окне (и сделать более грамотное исполнение самих окон)

# Настраиваемые текстовые элементы; чтобы не использовать show expression Text
image corner_text = ParameterizedText(style="corner_text") # "ReactOS Version [config.version]\nBuild [ros_build]\nReporting NT 5.2 (Build 3790: Service Pack 2)\nC:\\[ros_install_directory]"
image ros_boot_text = ParameterizedText(style="boot_text") # "Загрузка системного куста..." / "Loading system hive..."
image border_text = ParameterizedText(style="install_border_text") # Текст в нижней плашке в установке
image install_text = ParameterizedText(style="install_text") # Надписи в установке
image install_text_center = ParameterizedText(style="install_text_center") # Надписи в установке, выровненные по центру
image formatting_text = ParameterizedText(style="formatting_text") # Изначально прогресс форматирования, но впоследствии был применён и для отображения остального текста в установке
image graphic_boot_text = ParameterizedText(style="graphic_boot_text") # Название системы на графическом экране загрузки
image copyright_text = ParameterizedText(style="copyright_text") # Копирайт в углу графического экрана загрузки

# Прогрессбар в загрузчике
image boot_progressbar:
    Solid("#c3c3c3")
    xsize 99 ysize 16
    xanchor 342 yanchor 224
