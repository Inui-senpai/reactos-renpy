# Оформление
style ros_this_pc_frame:
    background Frame("gui/window/this_pc/window.png")
    xsize 600 ysize 429
style ros_this_pc_menu:
    idle_background "ros_this_pc_menu_idle"
    hover_background "ros_this_pc_menu_idle"
    insensitive_background "ros_this_pc_menu_idle"
    selected_background "ros_this_pc_menu_selected"
image ros_this_pc_menu_idle:
    Solid("#d4d0c8")
    xsize 38 ysize 18
image ros_this_pc_menu_selected:
    "gui/window/notepad/menu_button_selected.png"
    xsize 38 ysize 18
    xpos -6
style ros_this_pc_menu_edit is ros_this_pc_menu:
    selected_background "ros_this_pc_menu_edit_selected"
image ros_this_pc_menu_edit_selected:
    "gui/window/notepad/menu_button_selected.png"
    xsize 42 ysize 18
    xpos -4
style ros_this_pc_menu_view is ros_this_pc_menu:
    selected_background "ros_this_pc_menu_view_selected"
image ros_this_pc_menu_view_selected:
    "gui/window/notepad/menu_button_selected.png"
    xsize 26 ysize 18
    xpos -4
style ros_this_pc_menu_favorites is ros_this_pc_menu:
    selected_background "ros_this_pc_menu_favorites_selected"
image ros_this_pc_menu_favorites_selected:
    "gui/window/notepad/menu_button_selected.png"
    xsize 60 ysize 18
    xpos -4
style ros_this_pc_menu_help is ros_this_pc_menu:
    selected_background "ros_this_pc_menu_help_selected"
image ros_this_pc_menu_help_selected:
    "gui/window/notepad/menu_button_selected.png"
    xsize 49 ysize 18
    xpos -4
style ros_this_pc_menu_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    insensitive_color "#808080"
    insensitive_outlines [(0, "#fff", 1, 1)]
    ypos 2
style ros_this_pc_window_title:
    font "gui/font/tahomabd.ttf"
    size 11
    color "#fff"
    xpos 22 ypos 5
style ros_this_pc_viewport:
    background Frame("gui/window/this_pc/viewport.png")
    xsize 592 ysize 300
    xpos 0 ypos 100
style ros_this_pc_viewport_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    text_align 0.5
    xalign 0.5 yalign 0.9
style ros_this_pc_counter_bar:
    background Frame("gui/window/this_pc/counter_bar.png")
    xsize 592 ysize 18
    ypos 403
style ros_this_pc_counter_bar_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    xpos 2 ypos 2
style ros_this_pc_back_button:
    insensitive_background "gui/window/this_pc/buttons/back_insensitive.png"
    idle_background "gui/window/this_pc/buttons/back_idle.png"
    hover_background "gui/window/this_pc/buttons/back_hover.png"
    selected_background "gui/window/this_pc/buttons/back_selected.png"
style ros_this_pc_back_button_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    insensitive_color "#808080"
    insensitive_outlines [(0, "#fff", 1, 1)]
    xpos 28 ypos 12
style ros_this_pc_search_button:
    idle_background "gui/window/this_pc/buttons/search_idle.png"
    hover_background "gui/window/this_pc/buttons/search_hover.png"
    selected_background "gui/window/this_pc/buttons/search_selected.png"
style ros_this_pc_search_button_text is ros_this_pc_back_button_text
style ros_this_pc_folders_button:
    idle_background "gui/window/this_pc/buttons/folders_idle.png"
    hover_background "gui/window/this_pc/buttons/folders_hover.png"
    selected_background "gui/window/this_pc/buttons/folders_selected.png"
style ros_this_pc_folders_button_text is ros_this_pc_back_button_text
style ros_this_pc_address_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    ypos 4
style ros_this_pc_address:
    idle_background "gui/window/this_pc/address_bar.png"
    hover_background "gui/window/this_pc/address_bar.png"
style ros_this_pc_address_bar_text is ros_this_pc_address_text:
    xpos 22 ypos 0
style ros_this_pc_go:
    idle_background "gui/window/this_pc/buttons/go_idle.png"
    hover_background "gui/window/this_pc/buttons/go_hover.png"
style ros_this_pc_go_text is ros_this_pc_address_text:
    xpos 28
style ros_this_pc_menu_entry:
    idle_background "ros_this_pc_menu_entry_idle"
    hover_background "ros_this_pc_menu_entry_hover"
    insensitive_background "ros_this_pc_menu_entry_idle"
image ros_this_pc_menu_entry_idle:
    Solid("#d4d0c8")
    xsize 136 ysize 17
image ros_this_pc_menu_entry_hover:
    Solid("#0a246a")
    xsize 136 ysize 17
style ros_this_pc_menu_file_view_entry:
    idle_background "ros_this_pc_menu_file_view_entry_idle"
    hover_background "ros_this_pc_menu_file_view_entry_hover"
    insensitive_background "ros_this_pc_menu_file_view_entry_idle"
image ros_this_pc_menu_file_view_entry_idle:
    Solid("#d4d0c8")
    xsize 112 ysize 17
image ros_this_pc_menu_file_view_entry_hover:
    Solid("#0a246a")
    xsize 112 ysize 17
style ros_this_pc_menu_file_sort_entry:
    idle_background "ros_this_pc_menu_file_sort_entry_idle"
    hover_background "ros_this_pc_menu_file_sort_entry_hover"
    insensitive_background "ros_this_pc_menu_file_sort_entry_idle"
image ros_this_pc_menu_file_sort_entry_idle:
    Solid("#d4d0c8")
    xsize 170 ysize 17
image ros_this_pc_menu_file_sort_entry_hover:
    Solid("#0a246a")
    xsize 170 ysize 17
style ros_this_pc_menu_edit_entry:
    idle_background "ros_this_pc_menu_edit_entry_idle"
    hover_background "ros_this_pc_menu_edit_entry_hover"
    insensitive_background "ros_this_pc_menu_edit_entry_idle"
image ros_this_pc_menu_edit_entry_idle:
    Solid("#d4d0c8")
    xsize 182 ysize 17
image ros_this_pc_menu_edit_entry_hover:
    Solid("#0a246a")
    xsize 182 ysize 17
style ros_this_pc_menu_view_entry:
    idle_background "ros_this_pc_menu_view_entry_idle"
    hover_background "ros_this_pc_menu_view_entry_hover"
    insensitive_background "ros_this_pc_menu_view_entry_idle"
image ros_this_pc_menu_view_entry_idle:
    Solid("#d4d0c8")
    xsize 142 ysize 17
image ros_this_pc_menu_view_entry_hover:
    Solid("#0a246a")
    xsize 142 ysize 17
style ros_this_pc_menu_view_toolbars_entry:
    idle_background "ros_this_pc_menu_view_toolbars_entry_idle"
    hover_background "ros_this_pc_menu_view_toolbars_entry_hover"
    insensitive_background "ros_this_pc_menu_view_toolbars_entry_idle"
image ros_this_pc_menu_view_toolbars_entry_idle:
    Solid("#d4d0c8")
    xsize 197 ysize 17
image ros_this_pc_menu_view_toolbars_entry_hover:
    Solid("#0a246a")
    xsize 197 ysize 17
style ros_this_pc_menu_view_browser_panels_entry:
    idle_background "ros_this_pc_menu_view_browser_panels_entry_idle"
    hover_background "ros_this_pc_menu_view_browser_panels_entry_hover"
    insensitive_background "ros_this_pc_menu_view_browser_panels_entry_idle"
image ros_this_pc_menu_view_browser_panels_entry_idle:
    Solid("#d4d0c8")
    xsize 123 ysize 17
image ros_this_pc_menu_view_browser_panels_entry_hover:
    Solid("#0a246a")
    xsize 123 ysize 17
style ros_this_pc_menu_view_sort_entry:
    idle_background "ros_this_pc_menu_view_sort_entry_idle"
    hover_background "ros_this_pc_menu_view_sort_entry_hover"
    insensitive_background "ros_this_pc_menu_view_sort_entry_idle"
image ros_this_pc_menu_view_sort_entry_idle:
    Solid("#d4d0c8")
    xsize 170 ysize 17
image ros_this_pc_menu_view_sort_entry_hover:
    Solid("#0a246a")
    xsize 170 ysize 17
style ros_this_pc_menu_view_go_entry:
    idle_background "ros_this_pc_menu_view_go_entry_idle"
    hover_background "ros_this_pc_menu_view_go_entry_hover"
    insensitive_background "ros_this_pc_menu_view_go_entry_idle"
image ros_this_pc_menu_view_go_entry_idle:
    Solid("#d4d0c8")
    xsize 258 ysize 17
image ros_this_pc_menu_view_go_entry_hover:
    Solid("#0a246a")
    xsize 258 ysize 17
style ros_this_pc_menu_favorites_entry:
    idle_background "ros_this_pc_menu_favorites_entry_idle"
    hover_background "ros_this_pc_menu_favorites_entry_hover"
    insensitive_background "ros_this_pc_menu_favorites_entry_idle"
image ros_this_pc_menu_favorites_entry_idle:
    Solid("#d4d0c8")
    xsize 176 ysize 17
image ros_this_pc_menu_favorites_entry_hover:
    Solid("#0a246a")
    xsize 176 ysize 17
style ros_this_pc_menu_services_entry:
    idle_background "ros_this_pc_menu_services_entry_idle"
    hover_background "ros_this_pc_menu_services_entry_hover"
    insensitive_background "ros_this_pc_menu_services_entry_idle"
image ros_this_pc_menu_services_entry_idle:
    Solid("#d4d0c8")
    xsize 170 ysize 17
image ros_this_pc_menu_services_entry_hover:
    Solid("#0a246a")
    xsize 170 ysize 17
style ros_this_pc_menu_help_entry:
    idle_background "ros_this_pc_menu_help_entry_idle"
    hover_background "ros_this_pc_menu_help_entry_hover"
    insensitive_background "ros_this_pc_menu_help_entry_idle"
image ros_this_pc_menu_help_entry_idle:
    Solid("#d4d0c8")
    xsize 83 ysize 17
image ros_this_pc_menu_help_entry_hover:
    Solid("#0a246a")
    xsize 83 ysize 17
style ros_this_pc_menu_entry_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#fff"
    insensitive_color "#808080"
    insensitive_outlines [(0, "#fff", 1, 1)]
    xpos 20
style ros_this_pc_frame_minimized is empty

# Основные переменные
default ros_explorer_menu_file_opened = False
default ros_explorer_menu_edit_opened = False
default ros_explorer_menu_file_view_opened = False
default ros_explorer_menu_file_sort_opened = False
default ros_explorer_menu_view_opened = False
default ros_explorer_menu_view_toolbars_opened = False
default ros_explorer_menu_view_browser_panels_opened = False
default ros_explorer_menu_view_sort_opened = False
default ros_explorer_menu_view_go_opened = False
default ros_explorer_menu_favorites_opened = False
default ros_explorer_menu_services_opened = False
default ros_explorer_menu_help_opened = False
default ros_explorer_title = "Мой компьютер"
default ros_explorer_title_icon = "device_manager"
default is_explorer_window_opened = True

# Окно
screen ros_explorer(folder=None):
    python:
        if folder == "recycle_bin":
            ros_explorer_title_icon = "recycle_bin"
            ros_explorer_title = "Корзина"
        elif folder == "docs":
            ros_explorer_title_icon = "documents"
            ros_explorer_title = "Мои документы"
        elif folder == "network":
            ros_explorer_title_icon = "network2"
            ros_explorer_title = "Сетевое окружение"
        elif folder == "pictures":
            ros_explorer_title_icon = "pictures"
            ros_explorer_title = "Мои рисунки"
        elif folder == "control_panel":
            ros_explorer_title_icon = "control_panel"
            ros_explorer_title = "Панель управления"
        else:
            ros_explorer_title_icon = "device_manager"
            ros_explorer_title = "Мой компьютер"
    if not is_explorer_window_opened:
        frame:
            style "ros_this_pc_frame_minimized"
    else:
        drag:
            drag_name "ros_explorer"
            drag_handle (0, 0, 600, 23)
            xalign 0.5 yalign 0.5
            frame:
                style "ros_this_pc_frame"
                add "gui/desktop/menu_icons/submenu/[ros_explorer_title_icon].png" xpos 3 ypos 1
                text "[ros_explorer_title]" style "ros_notepad_window_title"
                python:
                    if folder == "control_panel":
                        this_pc_up_arrow_action = Show(screen="ros_explorer")
                    else:
                        this_pc_up_arrow_action = NullAction()
                imagebutton auto "gui/window/common/close_%s.png" action [
                    Hide("ros_explorer"),
                    SetVariable("ros_explorer_menu_file_opened", False),
                    SetVariable("ros_explorer_menu_edit_opened", False),
                    SetVariable("ros_explorer_menu_view_opened", False),
                    SetVariable("ros_explorer_menu_favorites_opened", False),
                    SetVariable("ros_explorer_menu_services_opened", False),
                    SetVariable("ros_explorer_menu_help_opened", False),
                    SetVariable("ros_explorer_menu_file_sort_opened", False),
                    SetVariable("ros_explorer_menu_file_view_opened", False),
                    SetVariable("ros_explorer_menu_view_browser_panels_opened", False),
                    SetVariable("ros_explorer_menu_view_sort_opened", False),
                    SetVariable("ros_explorer_menu_view_go_opened", False),
                    SetVariable("ros_explorer_menu_view_toolbars_opened", False)
                    ]:
                    xanchor -574 yanchor -2
                imagebutton auto "gui/window/common/expand_%s.png" action NullAction():
                    xanchor -556 yanchor -2
                imagebutton auto "gui/window/common/minimize_%s.png" action SetVariable("is_explorer_window_opened", False):
                    xanchor -540 yanchor -2
                hbox:
                    xpos 20 ypos 22
                    spacing 10
                    textbutton "Файл" style "ros_this_pc_menu" text_style "ros_this_pc_menu_text" focus_mask "ros_this_pc_menu_idle" action [
                        ToggleVariable("ros_explorer_menu_file_opened", True, False),
                        SensitiveIf(ros_explorer_menu_edit_opened == ros_explorer_menu_view_opened == ros_explorer_menu_favorites_opened == ros_explorer_menu_services_opened == ros_explorer_menu_help_opened == False)
                        ]
                    textbutton "Правка" style "ros_this_pc_menu_edit" text_style "ros_this_pc_menu_text" focus_mask "ros_this_pc_menu_edit_selected" action [
                        ToggleVariable("ros_explorer_menu_edit_opened", True, False),
                        SensitiveIf(ros_explorer_menu_file_opened == ros_explorer_menu_view_opened == ros_explorer_menu_favorites_opened == ros_explorer_menu_services_opened == ros_explorer_menu_help_opened == False)
                        ]
                    textbutton "Вид" style "ros_this_pc_menu_view" text_style "ros_this_pc_menu_text" focus_mask "ros_this_pc_menu_view_selected" action [
                        ToggleVariable("ros_explorer_menu_view_opened", True, False),
                        SensitiveIf(ros_explorer_menu_file_opened == ros_explorer_menu_edit_opened == ros_explorer_menu_favorites_opened == ros_explorer_menu_services_opened == ros_explorer_menu_help_opened == False)
                        ]
                    textbutton "Избранное" style "ros_this_pc_menu_favorites" text_style "ros_this_pc_menu_text" focus_mask "ros_this_pc_menu_favorites_selected" action [
                        ToggleVariable("ros_explorer_menu_favorites_opened", True, False),
                        SensitiveIf(ros_explorer_menu_file_opened == ros_explorer_menu_edit_opened == ros_explorer_menu_view_opened == ros_explorer_menu_services_opened == ros_explorer_menu_help_opened == False)
                        ]
                    textbutton "Сервис" style "ros_this_pc_menu_edit" text_style "ros_this_pc_menu_text" focus_mask "ros_this_pc_menu_edit_selected" action [
                        ToggleVariable("ros_explorer_menu_services_opened", True, False),
                        SensitiveIf(ros_explorer_menu_file_opened == ros_explorer_menu_edit_opened == ros_explorer_menu_view_opened == ros_explorer_menu_favorites_opened == ros_explorer_menu_help_opened == False)
                        ]
                    textbutton "Справка" style "ros_this_pc_menu_help" text_style "ros_this_pc_menu_text" focus_mask "ros_this_pc_menu_help_selected" action [
                        ToggleVariable("ros_explorer_menu_help_opened", True, False),
                        SensitiveIf(ros_explorer_menu_file_opened == ros_explorer_menu_edit_opened == ros_explorer_menu_view_opened == ros_explorer_menu_favorites_opened == ros_explorer_menu_services_opened == False)
                        ]
                hbox:
                    xpos 11 ypos 42
                    textbutton "Назад" style "ros_this_pc_back_button" text_style "ros_this_pc_back_button_text" focus_mask "gui/window/this_pc/buttons/back_idle.png"
                    imagebutton auto "gui/window/this_pc/buttons/forward_%s.png" focus_mask True xpos 42
                    imagebutton auto "gui/window/this_pc/buttons/up_%s.png" focus_mask True xpos 43 action this_pc_up_arrow_action
                    add "gui/window/this_pc/buttons/separator.png" xpos 43
                    textbutton "Поиск" style "ros_this_pc_search_button" text_style "ros_this_pc_search_button_text" focus_mask "gui/window/this_pc/buttons/search_idle.png" xpos 43 action NullAction()
                    textbutton "Папки" style "ros_this_pc_folders_button" text_style "ros_this_pc_folders_button_text" focus_mask "gui/window/this_pc/buttons/folders_idle.png" xpos 74 action NullAction()
                    add "gui/window/this_pc/buttons/separator.png" xpos 105
                    imagebutton auto "gui/window/this_pc/buttons/move_%s.png" focus_mask True xpos 105 action NullAction()
                    imagebutton auto "gui/window/this_pc/buttons/copy_%s.png" focus_mask True xpos 105 action NullAction()
                    imagebutton auto "gui/window/this_pc/buttons/delete_%s.png" focus_mask True xpos 105 action NullAction()
                    imagebutton auto "gui/window/this_pc/buttons/undo_%s.png" focus_mask True xpos 105 action NullAction()
                    add "gui/window/this_pc/buttons/separator.png" xpos 105
                    imagebutton auto "gui/window/this_pc/buttons/folder_view_%s.png" focus_mask True xpos 105 action NullAction()
                hbox:
                    xpos 15 ypos 74
                    text "Адрес" style "ros_this_pc_address_text"
                    frame:
                        style "ros_this_pc_address"
                        xpos 7
                        add "gui/desktop/menu_icons/submenu/[ros_explorer_title_icon].png" xpos 4 ypos 3
                        textbutton "[ros_explorer_title]" text_style "ros_this_pc_address_bar_text" focus_mask "gui/window/this_pc/address_bar.png" action NullAction()
                    textbutton "Переход" style "ros_this_pc_go" text_style "ros_this_pc_go_text" focus_mask "gui/window/this_pc/buttons/go_idle.png" xpos -100 action NullAction()
                frame:
                    style "ros_this_pc_viewport"
                    viewport:
                        yinitial 0.0
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        side_yfill True
                        vbox:
                            hbox:
                                xpos 11 ypos 6
                                spacing 10
                                if folder in ["recycle_bin", "network", "pictures"]:
                                    vbox:
                                        transclude
                                elif folder == "docs":
                                    vbox:
                                        imagebutton auto "this_pc_videos_%s" xalign 0.5 mouse "link" action NullAction()
                                        text "Мои\nвидеозаписи" style "ros_this_pc_viewport_text"
                                    vbox:
                                        imagebutton auto "this_pc_pictures_%s" xalign 0.5 mouse "link" action NullAction()
                                        text "Мои рисунки" style "ros_this_pc_viewport_text"
                                    vbox:
                                        imagebutton auto "this_pc_music_%s" xalign 0.5 mouse "link" action NullAction()
                                        text "Моя музыка" style "ros_this_pc_viewport_text"
                                elif folder == "control_panel":
                                    vbox:
                                        spacing 10
                                        hbox:
                                            spacing 13
                                            vbox:
                                                imagebutton auto "cp_administrative_tools_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Администрир..." style "ros_this_pc_viewport_text"
                                            vbox:
                                                xpos 2
                                                imagebutton auto "cp_timedate_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Дата и\nвремя" style "ros_this_pc_viewport_text"
                                            vbox:
                                                xpos 5
                                                imagebutton auto "cp_sounds_and_audio_devices_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Звуки и\nаудиоустрой..." style "ros_this_pc_viewport_text"
                                            vbox:
                                                imagebutton auto "cp_game_controllers_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Игровые\nустройства" style "ros_this_pc_viewport_text"
                                            vbox:
                                                imagebutton auto "cp_keyboard_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Клавиатура" style "ros_this_pc_viewport_text"
                                            vbox:
                                                imagebutton auto "cp_command_prompt_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Командная\nстрока" style "ros_this_pc_viewport_text"
                                            vbox:
                                                xpos 10
                                                imagebutton auto "cp_mouse_%s" xalign 0.5 mouse "link" action Show(screen="ros_properties_mouse")
                                                text "Мышь" style "ros_this_pc_viewport_text"
                                        hbox:
                                            spacing 13
                                            xpos 10
                                            vbox:
                                                imagebutton auto "cp_opengl_settings_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Настройки\nOpenGL" style "ros_this_pc_viewport_text"
                                            vbox:
                                                xpos 1
                                                imagebutton auto "cp_wined3dcfg_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Параметры\nWineD3D" style "ros_this_pc_viewport_text"
                                            vbox:
                                                xpos 2
                                                imagebutton auto "cp_printers_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Принтеры" style "ros_this_pc_viewport_text"
                                            vbox:
                                                xpos 2
                                                imagebutton auto "cp_iexplore_settings_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Свойства\nобозревателя" style "ros_this_pc_viewport_text"
                                            vbox:
                                                xpos 2
                                                imagebutton auto "cp_folder_options_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Свойства\nпапки" style "ros_this_pc_viewport_text"
                                            vbox:
                                                imagebutton auto "cp_netshell_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Сетевые\nподключения" style "ros_this_pc_viewport_text"
                                            vbox:
                                                imagebutton auto "cp_system_%s" xalign 0.5 mouse "link" action Show(screen="ros_properties_system")
                                                text "Система" style "ros_this_pc_viewport_text"
                                        hbox:
                                            spacing 13
                                            xpos 2
                                            vbox:
                                                imagebutton auto "cp_ease_of_access_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Специальные\nвозможности" style "ros_this_pc_viewport_text"
                                            vbox:
                                                xpos -4
                                                imagebutton auto "cp_phone_and_modem_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Телефон и\nмодем" style "ros_this_pc_viewport_text"
                                            vbox:
                                                xpos -8
                                                imagebutton auto "cp_setup_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Установка и\nудаление..." style "ros_this_pc_viewport_text"
                                            vbox:
                                                xpos -14
                                                imagebutton auto "cp_hardware_setup_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Установка\nоборудования" style "ros_this_pc_viewport_text"
                                            vbox:
                                                xpos -14
                                                imagebutton auto "cp_users_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Учётные\nзаписи..." style "ros_this_pc_viewport_text"
                                            vbox:
                                                xpos -2
                                                imagebutton auto "cp_fonts_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Шрифты" style "ros_this_pc_viewport_text"
                                            vbox:
                                                xpos 13
                                                imagebutton auto "cp_screen_settings_%s" xalign 0.5 mouse "link" action Show(screen="ros_properties_screen")
                                                text "Экран" style "ros_this_pc_viewport_text"
                                        hbox:
                                            spacing 2
                                            xpos 1
                                            vbox:
                                                imagebutton auto "cp_power_options_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Электропита..." style "ros_this_pc_viewport_text"
                                            vbox:
                                                imagebutton auto "cp_language_and_regional_standards_%s" xalign 0.5 mouse "link" action NullAction()
                                                text "Язык и\nрегиональн..." style "ros_this_pc_viewport_text"
                                else:
                                    vbox:
                                        imagebutton auto "this_pc_disk_drive_%s" xalign 0.5 mouse "link" action NullAction()
                                        text "Локальный\nдиск (C:)" style "ros_this_pc_viewport_text"
                                    vbox:
                                        imagebutton auto "this_pc_cd_drive_%s" xalign 0.5 mouse "link" action NullAction()
                                        text "CD-дисковод\n(D:)" style "ros_this_pc_viewport_text"
                                    vbox:
                                        imagebutton auto "this_pc_control_panel_%s" xalign 0.5 mouse "link" action Show(screen="ros_explorer", folder="control_panel")
                                        text "Панель\nуправления" style "ros_this_pc_viewport_text"
                                    vbox:
                                        imagebutton auto "this_pc_namespaces_%s" xalign 0.5 mouse "link" action NullAction()
                                        text "Пространство\nимён объекто..." style "ros_this_pc_viewport_text"
                                    vbox:
                                        imagebutton auto "this_pc_system_registry_%s" xalign 0.5 mouse "link" action NullAction()
                                        text "Системный\nреестр" style "ros_this_pc_viewport_text"
                            transclude
                frame:
                    style "ros_this_pc_counter_bar"
                    if folder in ["recycle_bin", "network", "pictures"]:
                        text "Объектов: 0" style "ros_this_pc_counter_bar_text"
                    elif folder == "docs":
                        text "Объектов: 3" style "ros_this_pc_counter_bar_text"
                    elif folder == "control_panel":
                        text "Объектов: 23" style "ros_this_pc_counter_bar_text"
                    else:
                        text "Объектов: 5" style "ros_this_pc_counter_bar_text"
                vbox:
                    if ros_explorer_menu_file_opened:
                        use ros_explorer_menu_file
                    elif ros_explorer_menu_edit_opened:
                        use ros_explorer_menu_edit
                    elif ros_explorer_menu_view_opened:
                        use ros_explorer_menu_view
                    elif ros_explorer_menu_favorites_opened:
                        use ros_explorer_menu_favorites
                    elif ros_explorer_menu_services_opened:
                        use ros_explorer_menu_services
                    elif ros_explorer_menu_help_opened:
                        use ros_explorer_menu_help

# Контекстные меню
# Файл
screen ros_explorer_menu_file():
    frame:
        style "ros_desktop_context_menu"
        xsize 142 ysize 161
        xpos 13 ypos 40
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Вид                             {font=gui/font/arial.ttf}►{/font}" style "ros_this_pc_menu_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_entry_idle" hovered [
                SetVariable("ros_explorer_menu_file_sort_opened", False),
                SetVariable("ros_explorer_menu_file_view_opened", True)] action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 134 ypos 1
            null height 1
            textbutton "Упорядочить значки {font=gui/font/arial.ttf}►{/font}" style "ros_this_pc_menu_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_entry_idle" hovered [
                SetVariable("ros_explorer_menu_file_view_opened", False),
                SetVariable("ros_explorer_menu_file_sort_opened", True)] action NullAction()
            textbutton "Обновить" style "ros_this_pc_menu_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_entry_idle" hovered [
                SetVariable("ros_explorer_menu_file_sort_opened", False),
                SetVariable("ros_explorer_menu_file_view_opened", False)] action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 134 ypos 1
            null height 1
            textbutton "Вставить" style "ros_this_pc_menu_entry" text_style "ros_this_pc_menu_entry_text"
            textbutton "Вставить ярлык" style "ros_this_pc_menu_entry" text_style "ros_this_pc_menu_entry_text"
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 134 ypos 1
            null height 1
            textbutton "Свойства" style "ros_this_pc_menu_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_entry_idle" hovered [
                SetVariable("ros_explorer_menu_file_sort_opened", False),
                SetVariable("ros_explorer_menu_file_view_opened", False)] action [SetVariable("ros_explorer_menu_file_opened", False), Show(screen="ros_properties_system")]
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 134 ypos 1
            null height 1
            textbutton "Закрыть" style "ros_this_pc_menu_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_entry_idle" hovered [
                SetVariable("ros_explorer_menu_file_sort_opened", False),
                SetVariable("ros_explorer_menu_file_view_opened", False)] action [SetVariable("ros_explorer_menu_file_opened", False), Hide(screen="ros_explorer")]
        vbox:
            if ros_explorer_menu_file_view_opened:
                use ros_explorer_menu_file_view
            elif ros_explorer_menu_file_sort_opened:
                use ros_explorer_menu_file_sort
# Файл - Вид
screen ros_explorer_menu_file_view():
    frame:
        style "ros_desktop_context_menu"
        xsize 118 ysize 71
        xpos 141 ypos 0
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Крупные значки" style "ros_this_pc_menu_file_view_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_file_view_entry_idle" action NullAction()
            textbutton "Мелкие значки" style "ros_this_pc_menu_file_view_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_file_view_entry_idle" action NullAction()
            textbutton "Список" style "ros_this_pc_menu_file_view_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_file_view_entry_idle" action NullAction()
            textbutton "Таблица" style "ros_this_pc_menu_file_view_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_file_view_entry_idle" action NullAction()
# Файл - Упорядочить значки
screen ros_explorer_menu_file_sort():
    frame:
        style "ros_desktop_context_menu"
        xsize 176 ysize 40
        xpos 141 ypos 28
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Автоматически" style "ros_this_pc_menu_file_sort_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_file_sort_entry_idle" action NullAction()
            textbutton "Выровнять значки по сетке" style "ros_this_pc_menu_file_sort_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_file_sort_entry_idle" action NullAction()

# Правка
screen ros_explorer_menu_edit():
    frame:
        style "ros_desktop_context_menu"
        xsize 188 ysize 182
        xpos 51 ypos 40
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Отменить                      Ctrl+Z" style "ros_this_pc_menu_edit_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_edit_entry_idle" action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 180 ypos 1
            null height 1
            textbutton "Вырезать                      Ctrl+X" style "ros_this_pc_menu_edit_entry" text_style "ros_this_pc_menu_entry_text"
            textbutton "Копировать                  Ctrl+C" style "ros_this_pc_menu_edit_entry" text_style "ros_this_pc_menu_entry_text"
            textbutton "Вставить                       Ctrl+V" style "ros_this_pc_menu_edit_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_edit_entry_idle" action NullAction()
            textbutton "Вставить ярлык" style "ros_this_pc_menu_edit_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_edit_entry_idle" action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 180 ypos 1
            null height 1
            textbutton "Копировать в папку..." style "ros_this_pc_menu_edit_entry" text_style "ros_this_pc_menu_entry_text"
            textbutton "Переместить в папку..." style "ros_this_pc_menu_edit_entry" text_style "ros_this_pc_menu_entry_text"
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 180 ypos 1
            null height 1
            textbutton "Выделить всё               Ctrl+A" style "ros_this_pc_menu_edit_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_edit_entry_idle" action NullAction()
            textbutton "Обратить выделение" style "ros_this_pc_menu_edit_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_edit_entry_idle" action NullAction()
# Вид
screen ros_explorer_menu_view():
    frame:
        style "ros_desktop_context_menu"
        xsize 148 ysize 198
        xpos 97 ypos 40
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Панели инструментов {font=gui/font/arial.ttf}►{/font}" style "ros_this_pc_menu_view_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_entry_idle" hovered [
                SetVariable("ros_explorer_menu_view_browser_panels_opened", False),
                SetVariable("ros_explorer_menu_view_sort_opened", False),
                SetVariable("ros_explorer_menu_view_go_opened", False),
                SetVariable("ros_explorer_menu_view_toolbars_opened", True)] action NullAction()
            textbutton "Строка состояния" style "ros_this_pc_menu_view_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_entry_idle" hovered [
                SetVariable("ros_explorer_menu_view_browser_panels_opened", False),
                SetVariable("ros_explorer_menu_view_sort_opened", False),
                SetVariable("ros_explorer_menu_view_go_opened", False),
                SetVariable("ros_explorer_menu_view_toolbars_opened", False)] action NullAction()
            textbutton "Панели обозревателя {font=gui/font/arial.ttf}►{/font}" style "ros_this_pc_menu_view_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_entry_idle" hovered [
                SetVariable("ros_explorer_menu_view_toolbars_opened", False),
                SetVariable("ros_explorer_menu_view_sort_opened", False),
                SetVariable("ros_explorer_menu_view_go_opened", False),
                SetVariable("ros_explorer_menu_view_browser_panels_opened", True)] action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 140 ypos 1
            null height 1
            textbutton "Крупные значки" style "ros_this_pc_menu_view_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_entry_idle" hovered [
                SetVariable("ros_explorer_menu_view_browser_panels_opened", False),
                SetVariable("ros_explorer_menu_view_sort_opened", False),
                SetVariable("ros_explorer_menu_view_go_opened", False),
                SetVariable("ros_explorer_menu_view_toolbars_opened", False)] action NullAction()
            textbutton "Мелкие значки" style "ros_this_pc_menu_view_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_entry_idle" hovered [
                SetVariable("ros_explorer_menu_view_browser_panels_opened", False),
                SetVariable("ros_explorer_menu_view_sort_opened", False),
                SetVariable("ros_explorer_menu_view_go_opened", False),
                SetVariable("ros_explorer_menu_view_toolbars_opened", False)] action NullAction()
            textbutton "Список" style "ros_this_pc_menu_view_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_entry_idle" hovered [
                SetVariable("ros_explorer_menu_view_browser_panels_opened", False),
                SetVariable("ros_explorer_menu_view_sort_opened", False),
                SetVariable("ros_explorer_menu_view_go_opened", False),
                SetVariable("ros_explorer_menu_view_toolbars_opened", False)] action NullAction()
            textbutton "Таблица" style "ros_this_pc_menu_view_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_entry_idle" hovered [
                SetVariable("ros_explorer_menu_view_browser_panels_opened", False),
                SetVariable("ros_explorer_menu_view_sort_opened", False),
                SetVariable("ros_explorer_menu_view_go_opened", False),
                SetVariable("ros_explorer_menu_view_toolbars_opened", False)] action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 140 ypos 1
            null height 1
            textbutton "Упорядочить значки {font=gui/font/arial.ttf}►{/font}" style "ros_this_pc_menu_view_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_entry_idle" hovered [
                SetVariable("ros_explorer_menu_view_browser_panels_opened", False),
                SetVariable("ros_explorer_menu_view_toolbars_opened", False),
                SetVariable("ros_explorer_menu_view_go_opened", False),
                SetVariable("ros_explorer_menu_view_sort_opened", True)] action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 140 ypos 1
            null height 1
            textbutton "Переход                      {font=gui/font/arial.ttf}►{/font}" style "ros_this_pc_menu_view_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_entry_idle" hovered [
                SetVariable("ros_explorer_menu_view_browser_panels_opened", False),
                SetVariable("ros_explorer_menu_view_toolbars_opened", False),
                SetVariable("ros_explorer_menu_view_sort_opened", False),
                SetVariable("ros_explorer_menu_view_go_opened", True)] action NullAction()
            textbutton "Обновить" style "ros_this_pc_menu_view_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_entry_idle" hovered [
                SetVariable("ros_explorer_menu_view_browser_panels_opened", False),
                SetVariable("ros_explorer_menu_view_sort_opened", False),
                SetVariable("ros_explorer_menu_view_go_opened", False),
                SetVariable("ros_explorer_menu_view_toolbars_opened", False)] action NullAction()
        vbox:
            if ros_explorer_menu_view_toolbars_opened:
                use ros_explorer_menu_view_toolbars
            elif ros_explorer_menu_view_browser_panels_opened:
                use ros_explorer_menu_view_browser_panels
            elif ros_explorer_menu_view_sort_opened:
                use ros_explorer_menu_view_sort
            elif ros_explorer_menu_view_go_opened:
                use ros_explorer_menu_view_go
# Вид - Панели инструментов
screen ros_explorer_menu_view_toolbars():
    frame:
        style "ros_desktop_context_menu"
        xsize 203 ysize 81
        xpos 147 ypos 0
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Обычные кнопки" style "ros_this_pc_menu_view_toolbars_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_toolbars_entry_idle" action NullAction()
            textbutton "Адресная строка" style "ros_this_pc_menu_view_toolbars_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_toolbars_entry_idle" action NullAction()
            textbutton "Ссылки" style "ros_this_pc_menu_view_toolbars_entry" text_style "ros_this_pc_menu_entry_text"
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 195 ypos 1
            null height 1
            textbutton "Закрепить панели инструментов" style "ros_this_pc_menu_view_toolbars_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_toolbars_entry_idle" action NullAction()
# Вид - Панели обозревателя
screen ros_explorer_menu_view_browser_panels():
    frame:
        style "ros_desktop_context_menu"
        xsize 129 ysize 71
        xpos 147 ypos 34
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Поиск             Ctrl+E" style "ros_this_pc_menu_view_browser_panels_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_browser_panels_entry_idle" action NullAction()
            textbutton "Избранное     Ctrl+I" style "ros_this_pc_menu_view_browser_panels_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_browser_panels_entry_idle" action NullAction()
            textbutton "Журнал         Ctrl+H" style "ros_this_pc_menu_view_browser_panels_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_browser_panels_entry_idle" action NullAction()
            textbutton "Папки" style "ros_this_pc_menu_view_browser_panels_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_browser_panels_entry_idle" action NullAction()
# Вид - Упорядочить значки
screen ros_explorer_menu_view_sort():
    frame:
        style "ros_desktop_context_menu"
        xsize 176 ysize 130
        xpos 147 ypos 133
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Название" style "ros_this_pc_menu_view_sort_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_sort_entry_idle" action NullAction()
            textbutton "Комментарии" style "ros_this_pc_menu_view_sort_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_sort_entry_idle" action NullAction()
            textbutton "Тип" style "ros_this_pc_menu_view_sort_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_sort_entry_idle" action NullAction()
            textbutton "Полный объём" style "ros_this_pc_menu_view_sort_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_sort_entry_idle" action NullAction()
            textbutton "Свободно" style "ros_this_pc_menu_view_sort_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_sort_entry_idle" action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 168 ypos 1
            null height 1
            textbutton "Автоматически" style "ros_this_pc_menu_view_sort_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_sort_entry_idle" action NullAction()
            textbutton "Выровнять значки по сетке" style "ros_this_pc_menu_view_sort_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_sort_entry_idle" action NullAction()
# Вид - Переход
screen ros_explorer_menu_view_go():
    frame:
        style "ros_desktop_context_menu"
        xsize 264 ysize 109
        xpos 147 ypos 158
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Назад                               Alt+Стрелка влево" style "ros_this_pc_menu_view_go_entry" text_style "ros_this_pc_menu_entry_text"
            textbutton "Вперёд                             Alt+Стрелка вправо" style "ros_this_pc_menu_view_go_entry" text_style "ros_this_pc_menu_entry_text"
            textbutton "На один уровень вверх" style "ros_this_pc_menu_view_go_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_go_entry_idle" action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 256 ypos 1
            null height 1
            textbutton "Домашняя страница       Alt+Home" style "ros_this_pc_menu_view_go_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_go_entry_idle" action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 256 ypos 1
            null height 1
            textbutton "Мой компьютер" style "ros_this_pc_menu_view_go_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_view_go_entry_idle" action NullAction()
# Избранное
screen ros_explorer_menu_favorites():
    frame:
        style "ros_desktop_context_menu"
        xsize 182 ysize 68
        xpos 126 ypos 40
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Добавить в избранное..." style "ros_this_pc_menu_favorites_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_favorites_entry_idle" action NullAction()
            textbutton "Упорядочить избранное..." style "ros_this_pc_menu_favorites_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_favorites_entry_idle" action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 168 ypos 1
            null height 1
            textbutton "(пусто)" style "ros_this_pc_menu_favorites_entry" text_style "ros_this_pc_menu_entry_text"
# Сервис
screen ros_explorer_menu_services():
    frame:
        style "ros_desktop_context_menu"
        xsize 176 ysize 81
        xpos 190 ypos 40
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Подключить сетевой диск..." style "ros_this_pc_menu_services_entry" text_style "ros_this_pc_menu_entry_text"
            textbutton "Отключить сетевой диск..." style "ros_this_pc_menu_services_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_services_entry_idle" action NullAction()
            textbutton "Синхронизировать..." style "ros_this_pc_menu_services_entry" text_style "ros_this_pc_menu_entry_text"
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 168 ypos 1
            null height 1
            textbutton "Свойства папки..." style "ros_this_pc_menu_services_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_services_entry_idle" action NullAction()
# Справка
screen ros_explorer_menu_help():
    frame:
        style "ros_desktop_context_menu"
        xsize 89 ysize 23
        xpos 235 ypos 40
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "О ReactOS" style "ros_this_pc_menu_help_entry" text_style "ros_this_pc_menu_entry_text" focus_mask "ros_this_pc_menu_help_entry_idle" action [
                SetVariable("ros_explorer_menu_help_opened", False),
                Show(screen="ros_about", name="reactos")]
