# Оформление
style ros_properties_frame:
    background Frame("gui/window/properties/window.png")
style ros_properties_window_title:
    font "gui/font/tahomabd.ttf"
    size 11
    color "#fff"
    xpos 22 ypos 3
style ros_properties_tabs:
    idle_background "gui/window/properties/tab_idle.png"
    hover_background "gui/window/properties/tab_idle.png"
    selected_background "gui/window/properties/tab_selected.png"
style ros_properties_tabs_large:
    idle_background "ros_properties_tab_large_idle"
    hover_background "ros_properties_tab_large_idle"
    selected_background "ros_properties_tab_large_selected"
image ros_properties_tab_large_idle:
    "gui/window/properties/tab_idle.png"
    xsize 104 subpixel True
image ros_properties_tab_large_selected:
    "gui/window/properties/tab_selected.png"
    xsize 104 subpixel True
style ros_properties_tabs_medium:
    idle_background "ros_properties_tab_medium_idle"
    hover_background "ros_properties_tab_medium_idle"
    selected_background "ros_properties_tab_medium_selected"
image ros_properties_tab_medium_idle:
    "gui/window/properties/tab_idle.png"
    xsize 79 subpixel True
image ros_properties_tab_medium_selected:
    "gui/window/properties/tab_selected.png"
    xsize 79 subpixel True
style ros_properties_tabs_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    text_align 0.5
    xpos 11 ypos 4
style ros_properties_buttons:
    idle_background "gui/window/postinstall/button_idle.png"
    hover_background "gui/window/postinstall/button_hover.png"
    insensitive_background "gui/window/postinstall/button_idle.png"
style ros_properties_buttons_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    insensitive_color "#808080"
    xpos 14 ypos 4
style ros_properties_buttons_text_ok is ros_properties_buttons_text:
    xpos 34
style ros_properties_buttons_text_cancel is ros_properties_buttons_text:
    xpos 22
style ros_properties_viewport:
    background Frame("gui/window/properties/viewport.png")
    xpos 3 ypos 45
style ros_properties_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
style ros_properties_license_button:
    idle_background "gui/window/properties/license_button_idle.png"
    hover_background "gui/window/properties/license_button_hover.png"
style ros_properties_license_button_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    xpos 26
style ros_properties_license_window:
    background Frame("gui/window/properties/license_window.png")
    xsize 407 ysize 283
style ros_properties_license_window_title is ros_properties_window_title:
    xpos 25 ypos 7
style ros_properties_license_window_viewport:
    background Frame("gui/window/properties/license_box.png")
    xsize 383 ysize 213
    xpos 13 ypos 28
style ros_properties_page2_buttons:
    idle_background "gui/window/properties/button_page2_idle.png"
    hover_background "gui/window/properties/button_page2_hover.png"
style ros_properties_page2_buttons_text is ros_properties_buttons_text:
    xpos 10
style ros_properties_page2_buttons_2_text is ros_properties_page2_buttons_text:
    xpos 28
style ros_properties_submenu_frame:
    background Frame("gui/window/properties/submenu_viewport.png")
    xsize 366 ysize 94
style ros_properties_tabs_text_2 is ros_properties_tabs_text:
    xpos 15
style ros_properties_tabs_text_3 is ros_properties_tabs_text:
    xpos 6
style ros_properties_tabs_text_4 is ros_properties_tabs_text:
    xpos 7
style ros_properties_tabs_text_5 is ros_properties_tabs_text:
    xpos 5
style ros_properties_tabs_text_6 is ros_properties_tabs_text:
    xpos 9
style ros_properties_submenu_frame_title:
    insensitive_background Solid("#d4d0c8")
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
style ros_properties_page3_buttons:
    idle_background "gui/window/properties/button_page3_idle.png"
    hover_background "gui/window/properties/button_page3_hover.png"
style ros_properties_page3_buttons_text is ros_properties_buttons_text:
    xpos 16
style ros_properties_page3_buttons_2_text is ros_properties_page3_buttons_text:
    xpos 12
style ros_properties_page4_buttons_text is ros_properties_buttons_text:
    xpos 9
style ros_properties_page4_buttons_settings_text is ros_properties_page4_buttons_text:
    xpos 5
style ros_properties_system_config_window_title is ros_properties_window_title:
    xpos 6 ypos 7
style ros_properties_system_config_window:
    background Frame("gui/window/properties/system_config_window.png")
    xsize 338 ysize 197
style ros_properties_screen_choice_frame:
    background Frame("gui/window/properties/choice_box.png")
    xsize 261 ysize 140
style ros_properties_screen_choice:
    idle_background Solid("#fff")
    hover_background Solid("#fff")
    selected_background Solid("#0a246a")
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    selected_color "#fff"
style ros_properties_screen_choice_fit_mode:
    background Frame("gui/window/properties/dropdown_menu_insensitive.png")
    xsize 83 ysize 21
style ros_properties_screen_choice_fit_mode_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    selected_color "#fff"
    insensitive_color "#808080"
    xpos 4 ypos 4
style ros_properties_screen_screensaver_frame:
    background Frame("gui/window/properties/screensaver_frame.png")
style ros_properties_screen_screensaver_dropdown_menu:
    background Frame("gui/window/properties/dropdown_menu_idle.png")
    xsize 150 ysize 21
style ros_properties_screen_screensaver_dropdown_menu_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    xpos 4 ypos 4    
style ros_properties_screen_screensaver_view is ros_properties_buttons_text:
    xpos 18
style ros_properties_screen_screensaver_adjust_box:
    background Frame("gui/window/properties/adjust_box_insensitive.png")
    xsize 46 ysize 21
style ros_properties_screen_screensaver_adjust_box_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    selected_color "#fff"
    insensitive_color "#808080"
    text_align 1.0
    xpos 14 ypos 4
style ros_classic_inactive_window:
    background Frame("gui/window/properties/inactive_window.png")
    xsize 311 ysize 153
style ros_classic_inactive_window_title:
    font "gui/font/tahomabd.ttf"
    size 11
    color "#d4d0c8"
style ros_classic_active_window_title:
    font "gui/font/tahomabd.ttf"
    size 11
    color "#fff"
style ros_classic_active_window:
    background Frame("gui/window/properties/active_window.png")
    xsize 322 ysize 135
style ros_classic_active_window_menu:
    idle_background Solid("#d4d0c8")
    hover_background Solid("#d4d0c8")
    insensitive_background Solid("#d4d0c8")
style ros_classic_active_window_menu_selected:
    background Frame("gui/window/properties/active_window_menu_selected.png")
    xsize 68 ysize 18
style ros_classic_active_window_menu_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    insensitive_color "#808080"
style ros_classic_active_window_menu_selected_text is ros_classic_active_window_menu_text:
    xpos 6
style ros_classic_active_window_viewport:
    background Frame("gui/window/properties/active_window_viewport.png")
    xsize 314 ysize 90
style ros_classic_message_window:
    background Frame("gui/window/properties/message_window.png")
    xsize 203 ysize 72
style ros_classic_message_window_ok_button:
    insensitive_background "gui/window/properties/message_window_ok.png"
style ros_classic_message_window_ok_button_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    xpos 28 ypos 10
style ros_properties_screen_appearance_choice_frame:
    background Frame("gui/window/properties/dropdown_menu_appearance_idle.png")
    xsize 201 ysize 21
style ros_properties_screen_appearance_buttons:
    idle_background "gui/window/properties/appearance_setting_button_idle.png"
    hover_background "gui/window/properties/appearance_setting_button_hover.png"
style ros_properties_screen_appearance_buttons_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#000"
    xpos 14 ypos 4
style ros_properties_screen_appearance_buttons_text_2 is ros_properties_screen_appearance_buttons_text:
    xpos 25
style ros_properties_screen_appearance_choice_menu_frame:
    background Frame("gui/window/properties/dropdown_list.png")
style ros_properties_screen_appearance_choice_menu_entry:
    idle_background "ros_properties_screen_appearance_choice_menu_idle"
    hover_background "ros_properties_screen_appearance_choice_menu_hover"
image ros_properties_screen_appearance_choice_menu_idle:
    Solid("#fff")
    xsize 199 ysize 13
image ros_properties_screen_appearance_choice_menu_hover:
    Solid("#0a246a")
    xsize 199 ysize 13
style ros_properties_screen_appearance_choice_menu_entry_text:
    font "gui/font/tahoma.ttf"
    size 11
    color "#000"
    hover_color "#fff"
    xpos 2 ypos 1
style ros_properties_screen_settings_monitors_viewport:
    background Frame("gui/window/properties/monitors_viewport.png")
    xsize 360 ysize 133
image monitor = "gui/window/properties/monitor.png"
style ros_properties_submenu_frame_mini:
    background Frame("gui/window/properties/submenu_viewport_mini.png")
    xsize 173 ysize 65
image ros_properties_slider = "gui/window/properties/horizontal_idle_bar.png"
image ros_properties_slider_thumb = "gui/window/properties/horizontal_idle_thumb.png"
image ros_properties_slider_marks = "gui/window/properties/horizontal_idle_bar_marks.png"
style ros_properties_color_quality_frame:
    background Frame("gui/window/properties/color_quality_frame.png")
    xsize 155 ysize 15

# Окно - Свойства: Система
screen ros_properties_system():
    drag:
        drag_name "ros_properties"
        drag_handle (0, 0, 410, 21)
        xalign 0.1 yalign 0.1
        frame:
            style "ros_properties_frame"
            xsize 410 ysize 467
            add "gui/desktop/menu_icons/submenu/system_properties.png" xpos 3
            text "Свойства: Система" style "ros_properties_window_title"
            imagebutton idle "gui/window/common/close_idle.png" action [
                SetVariable("properties_current_tab", "general"),
                Hide("ros_properties_system_general_license"),
                Hide("ros_properties_system_advanced_system_config"),
                Hide("ros_properties_system")]:
                xanchor -385 yanchor -1
            if properties_current_tab == "general":
                use ros_properties_system_general
            elif properties_current_tab == "pc_name":
                use ros_properties_system_pc_name
            elif properties_current_tab == "hardware":
                use ros_properties_system_hardware
            elif properties_current_tab == "advanced":
                use ros_properties_system_advanced
            hbox:
                xpos 3 ypos 26
                textbutton "Общие" style "ros_properties_tabs" text_style "ros_properties_tabs_text" focus_mask "gui/window/properties/tab_idle.png" action SetVariable("properties_current_tab", "general")
                null width 20
                textbutton "Имя компьютера" style "ros_properties_tabs_large" text_style "ros_properties_tabs_text" focus_mask "ros_properties_tab_large_idle" action SetVariable("properties_current_tab", "pc_name")
                null width 18
                textbutton "Оборудование" style "ros_properties_tabs_large" text_style "ros_properties_tabs_text_2" focus_mask "ros_properties_tab_large_idle" action SetVariable("properties_current_tab", "hardware")
                null width 25
                textbutton "Дополнительно" style "ros_properties_tabs_large" text_style "ros_properties_tabs_text" focus_mask "ros_properties_tab_large_idle" action SetVariable("properties_current_tab", "advanced")
            hbox:
                xpos 140 ypos 430
                textbutton "ОК" style "ros_properties_buttons" text_style "ros_properties_buttons_text_ok" focus_mask "gui/window/postinstall/button_idle.png" action [
                SetVariable("properties_current_tab", "general"),
                Hide("ros_properties_system_general_license"),
                Hide("ros_properties_system_advanced_system_config"),
                Hide("ros_properties_system")]
                null width 72
                textbutton "Отмена" style "ros_properties_buttons" text_style "ros_properties_buttons_text_cancel" focus_mask "gui/window/postinstall/button_idle.png" action [
                SetVariable("properties_current_tab", "general"),
                Hide("ros_properties_system_general_license"),
                Hide("ros_properties_system_advanced_system_config"),
                Hide("ros_properties_system")]
                null width 48
                textbutton "Применить" style "ros_properties_buttons" text_style "ros_properties_buttons_text"
# Общие
screen ros_properties_system_general():
    python:
        ros_system_runtime = ros_uptime_counter(renpy.get_game_runtime())
    frame:
        style "ros_properties_viewport"
        xsize 392 ysize 378
        add "gui/window/properties/ReactOS_logo.png" xsize 319 ysize 170 xalign 0.5 yalign 0.1
        vbox:
            xpos 10 ypos 200
            spacing 1
            text "Операционная система:" style "ros_properties_text"
            null height 2
            text "ReactOS Operating System" style "ros_properties_text" xpos 10
            text "Версия [config.version]" style "ros_properties_text" xpos 10
            text "[ros_build_short]" style "ros_properties_text" xpos 10
        vbox:
            xpos 10 ypos 270
            spacing 1
            text "Время работы системы:" style "ros_properties_text"
            null height 2
            text "[ros_system_runtime]" style "ros_properties_text" xpos 10
        vbox:
            xpos 200 ypos 200
            xmaximum 170
            spacing 1
            text "Компьютер:" style "ros_properties_text"
            null height 2
            text "[ros_pc_model]" style "ros_properties_text" xpos 10
            text "[ros_processor_manufacturer]" style "ros_properties_text" xpos 10
            text "[ros_processor_name]" style "ros_properties_text" xpos 10
            text "[ros_processor_frequency] МГц" style "ros_properties_text" xpos 10
            text "[ros_ram_capacity] ОЗУ" style "ros_properties_text" xpos 10
        hbox:
            xpos 20 ypos 335
            text "Посетите" style "ros_properties_text"
            textbutton "{color=#0a246a}домашнюю страницу ReactOS{/color}" text_style "ros_properties_text" xpos -1 ypos -4 mouse "link" action OpenURL("https://reactos.org/")
            textbutton "Лицензия..." style "ros_properties_license_button" text_style "ros_properties_license_button_text" focus_mask "gui/window/properties/license_button_idle.png" xpos 30 ypos -4 action Show(screen="ros_properties_system_general_license")
# Лицензия
screen ros_properties_system_general_license():
    modal True
    drag:
        drag_name "ros_properties_license"
        drag_handle (0, 0, 407, 21)
        xalign 0.2 yalign 0.2
        frame:
            style "ros_properties_license_window"
            add "gui/desktop/menu_icons/submenu/system_properties.png" xpos 5 ypos 4
            text "Лицензионное соглашение" style "ros_properties_license_window_title"
            imagebutton auto "gui/window/common/close_%s.png" action Hide("ros_properties_system_general_license"):
                xanchor -386 yanchor -5
            frame:
                style "ros_properties_license_window_viewport"
                viewport:
                    yinitial 0.0
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    side_yfill True
                    vbox:
                        text license_text style "ros_setup_developers_description"
                        transclude
            textbutton "ОК" style "ros_properties_buttons" text_style "ros_properties_buttons_text_ok" focus_mask "gui/window/postinstall/button_idle.png" action Hide("ros_properties_system_general_license"):
                xpos 160 ypos 250
# Имя компьютера
screen ros_properties_system_pc_name():
    frame:
        style "ros_properties_viewport"
        xsize 392 ysize 378
        hbox:
            xpos 11 ypos 11
            add "gui/desktop/desktop_icons/network.png"
            text "Указанные ниже сведения используются для\nидентификации компьютера в сети." style "ros_properties_text" xpos 10 ypos 2
        hbox:
            xpos 11 ypos 67
            text "Описание:" style "ros_properties_text" ypos 4
            textbutton "" style "ros_input_field" text_style "ros_input_field_text" focus_mask "gui/window/postinstall/input_field.png" xpos 70
        hbox:
            xpos 11 ypos 110
            text "Полное имя:" style "ros_properties_text" ypos 4
            text "[computer_name]" style "ros_properties_text" xpos 61 ypos 4
        hbox:
            xpos 11 ypos 130
            text "Рабочая группа:" style "ros_properties_text" ypos 4
            text "[workgroup_name]" style "ros_properties_text" xpos 39 ypos 4
        hbox:
            xpos 11 ypos 170
            text "Чтобы вызвать мастер сетевой идентификации\nдля присоединения компьютера к домену,\nнажмите кнопку \"Идентификация\"." style "ros_properties_text" ypos 4
            textbutton "Идентификация..." style "ros_properties_page2_buttons" text_style "ros_properties_page2_buttons_text" focus_mask "gui/window/properties/button_page2_idle.png" xpos 16 ypos 4 action NullAction()
        hbox:
            xpos 11 ypos 220
            text "Чтобы изменить имя компьютера или домена,\nнажмите \"Изменить\"." style "ros_properties_text" ypos 4
            textbutton "Изменить..." style "ros_properties_page2_buttons" text_style "ros_properties_page2_buttons_2_text" focus_mask "gui/window/properties/button_page2_idle.png" xpos 29 ypos 4 action NullAction()
# Оборудование
screen ros_properties_system_hardware():
    frame:
        style "ros_properties_viewport"
        xsize 392 ysize 378
        frame:
            style "ros_properties_submenu_frame"
            xpos 14 ypos 19
            textbutton "Диспетчер устройств" style "ros_properties_submenu_frame_title" text_style "ros_properties_submenu_frame_title" xpos 4 ypos -10
            add "gui/window/properties/device_manager.png" xpos 5 ypos 8
            text "Диспетчер устройств приводит список всего\nустановленного оборудования на данном компьютере и\nпозволяет изменить свойства любого устройства." style "ros_properties_text" xpos 50 ypos 8
            textbutton "Диспетчер устройств..." style "ros_properties_page3_buttons" text_style "ros_properties_page3_buttons_text" focus_mask "gui/window/properties/button_page3_idle.png" xpos 203 ypos 58 action NullAction()
        frame:
            style "ros_properties_submenu_frame"
            xpos 14 ypos 136
            textbutton "Мастер оборудования" style "ros_properties_submenu_frame_title" text_style "ros_properties_submenu_frame_title" xpos 4 ypos -10
            add "gui/window/properties/hardware_wizard.png" xpos 5 ypos 8
            text "Мастер оборудования поможет установить, восстановить,\nотключить или извлечь любое устройство, а также\nнастроить его." style "ros_properties_text" xpos 50 ypos 8
            textbutton "Мастер оборудования..." style "ros_properties_page3_buttons" text_style "ros_properties_page3_buttons_text" focus_mask "gui/window/properties/button_page3_idle.png" xpos 203 ypos 58 action NullAction()
        frame:
            style "ros_properties_submenu_frame"
            xpos 14 ypos 253
            textbutton "Профили оборудования" style "ros_properties_submenu_frame_title" text_style "ros_properties_submenu_frame_title" xpos 4 ypos -10
            add "gui/window/properties/hardware_profiles.png" xpos 5 ypos 8
            text "Профили оборудования помогают устанавливать и\nхранить различные конфигурации оборудования." style "ros_properties_text" xpos 50 ypos 8
            textbutton "Профили оборудования..." style "ros_properties_page3_buttons" text_style "ros_properties_page3_buttons_2_text" focus_mask "gui/window/properties/button_page3_idle.png" xpos 203 ypos 58 action NullAction()
# Дополнительно
screen ros_properties_system_advanced():
    frame:
        style "ros_properties_viewport"
        xsize 392 ysize 378
        text "Необходимо иметь права администратора для изменения большинства\nперечисленных параметров." style "ros_properties_text" xpos 10 ypos 10
        frame:
            style "ros_properties_submenu_frame"
            xpos 14 ypos 50
            textbutton "Быстродействие" style "ros_properties_submenu_frame_title" text_style "ros_properties_submenu_frame_title" xpos 4 ypos -10
            text "Визуальные эффекты, использование процессора,\nоперативной и виртуальной памяти" style "ros_properties_text" xpos 11 ypos 8
            textbutton "Параметры..." style "ros_properties_buttons" text_style "ros_properties_page4_buttons_text" focus_mask "gui/window/postinstall/button_idle.png" xpos 270 ypos 58 action NullAction()
        frame:
            style "ros_properties_submenu_frame"
            xpos 14 ypos 150
            textbutton "Профили пользователей" style "ros_properties_submenu_frame_title" text_style "ros_properties_submenu_frame_title" xpos 4 ypos -10
            text "Параметры рабочего стола, относящиеся ко входу в систему" style "ros_properties_text" xpos 11 ypos 8
            textbutton "Параметры..." style "ros_properties_buttons" text_style "ros_properties_page4_buttons_text" focus_mask "gui/window/postinstall/button_idle.png" xpos 270 ypos 58 action NullAction()
        frame:
            style "ros_properties_submenu_frame"
            xpos 14 ypos 250
            textbutton "Загрузка и восстановление" style "ros_properties_submenu_frame_title" text_style "ros_properties_submenu_frame_title" xpos 4 ypos -10
            text "Загрузка и восстановление системы, отладочная\nинформация" style "ros_properties_text" xpos 11 ypos 8
            textbutton "Параметры..." style "ros_properties_buttons" text_style "ros_properties_page4_buttons_text" focus_mask "gui/window/postinstall/button_idle.png" xpos 270 ypos 58 action NullAction()
        hbox:
            xpos 14 ypos 347
            spacing 31
            textbutton "Настройки системы" style "ros_properties_page2_buttons" text_style "ros_properties_page4_buttons_settings_text" focus_mask "gui/window/properties/button_page2_idle.png" action Show(screen="ros_properties_system_advanced_system_config")
            textbutton "Переменные среды" style "ros_properties_page2_buttons" text_style "ros_properties_page4_buttons_settings_text" focus_mask "gui/window/properties/button_page2_idle.png" action NullAction()
            textbutton "Отчёт об ошибках" style "ros_properties_page2_buttons" text_style "ros_properties_page4_buttons_text" focus_mask "gui/window/properties/button_page2_idle.png" action NullAction()
# Настройки системы
screen ros_properties_system_advanced_system_config():
    modal True
    drag:
        drag_name "ros_properties_system_config"
        drag_handle (0, 0, 338, 21)
        xalign 0.2 yalign 0.2
        frame:
            style "ros_properties_system_config_window"
            text "Системные параметры" style "ros_properties_system_config_window_title"
            frame:
                style "ros_properties_submenu_frame"
                xsize 315 ysize 114
                xpos 12 ypos 32
                textbutton "Информация о версии" style "ros_properties_submenu_frame_title" text_style "ros_properties_submenu_frame_title" xpos 4 ypos -10
                text "ReactOS собрана как серверная ОС и сообщает\nприложениям об этом. Установка флажка изменит это\n(только для приложений)." style "ros_properties_text" xpos 11 ypos 8
                hbox:
                    xpos 12 ypos 80
                    style_prefix "ros_check"
                    textbutton "Представляться как рабочая станция" action ToggleVariable("selected_edition", "workstation", "server")
            textbutton "ОК" style "ros_properties_buttons" text_style "ros_properties_buttons_text_ok" focus_mask "gui/window/postinstall/button_idle.png" xpos 244 ypos 157 action Hide("ros_properties_system_advanced_system_config")

# Окно - Свойства: Экран
screen ros_properties_screen():
    drag:
        drag_name "ros_properties"
        drag_handle (0, 0, 395, 21)
        xalign 0.1 yalign 0.1
        frame:
            style "ros_properties_frame"
            xsize 395 ysize 440
            add "gui/desktop/menu_icons/submenu/screen_properties.png" xpos 3
            text "Свойства: Экран" style "ros_properties_window_title"
            imagebutton idle "gui/window/common/close_idle.png" action [
                SetVariable("properties_current_tab", "general"),
                Hide("ros_properties_screen")]:
                xanchor -370 yanchor 0
            if properties_current_tab == "general":
                use ros_properties_screen_desktop
            elif properties_current_tab == "screensaver":
                use ros_properties_screen_screensaver
            elif properties_current_tab == "appearance":
                use ros_properties_screen_appearance
            elif properties_current_tab == "settings":
                use ros_properties_screen_settings
            hbox:
                xpos 3 ypos 26
                textbutton "Рабочий стол" style "ros_properties_tabs_medium" text_style "ros_properties_tabs_text_3" focus_mask "ros_properties_tab_medium_idle" action SetVariable("properties_current_tab", "general")
                null width 10
                textbutton "Заставка" style "ros_properties_tabs_medium" text_style "ros_properties_tabs_text_2" focus_mask "ros_properties_tab_medium_idle" action SetVariable("properties_current_tab", "screensaver")
                null width 32
                textbutton "Оформление" style "ros_properties_tabs_medium" text_style "ros_properties_tabs_text_4" focus_mask "ros_properties_tab_medium_idle" action SetVariable("properties_current_tab", "appearance")
                null width 14
                textbutton "Параметры" style "ros_properties_tabs_medium" text_style "ros_properties_tabs_text" focus_mask "ros_properties_tab_medium_idle" action SetVariable("properties_current_tab", "settings")
            if ros_properties_show_bottom_buttons:
                hbox:
                    xpos 125 ypos 403
                    textbutton "ОК" style "ros_properties_buttons" text_style "ros_properties_buttons_text_ok" focus_mask "gui/window/postinstall/button_idle.png" action [
                    SetVariable("properties_current_tab", "general"),
                    Hide("ros_properties_screen")]
                    null width 72
                    textbutton "Отмена" style "ros_properties_buttons" text_style "ros_properties_buttons_text_cancel" focus_mask "gui/window/postinstall/button_idle.png" action [
                    SetVariable("properties_current_tab", "general"),
                    Hide("ros_properties_screen")]
                    null width 48
                    textbutton "Применить" style "ros_properties_buttons" text_style "ros_properties_buttons_text"
# Рабочий стол
screen ros_properties_screen_desktop():
    python:
        my_wallpapers = [
            fil.replace(".png", "").replace("images/wallpapers/", "") \
            for fil in renpy.list_files() \
            if fil.startswith("images/wallpapers/") and fil.endswith(".png")
        ]
    frame:
        style "ros_properties_viewport"
        xsize 377 ysize 351
        add "gui/window/properties/screen.png" xpos 110 ypos 19
        if persistent.wallpaper:
            add persistent.wallpaper xsize 120 ysize 84 xalign 0.509 yalign 0.102
        else:
            add "postinstall" xsize 120 ysize 84 xalign 0.509 yalign 0.102
        text "Выберите изображение для рабочего стола:" style "ros_properties_text" xpos 16 ypos 157
    frame:
        style "ros_properties_screen_choice_frame"
        xpos 16 ypos 219
        viewport:
            yinitial 0.0
            scrollbars "vertical"
            mousewheel True
            draggable True
            side_yfill True
            vbox:
                hbox:
                    spacing 2
                    add "gui/desktop/menu_icons/submenu/forbidden.png"
                    textbutton "(нет)" style "ros_properties_screen_choice" text_style "ros_properties_screen_choice" action SetVariable("persistent.wallpaper", None)
                for i in my_wallpapers:
                    python:
                        i2 = i.replace("Silhouette/","").replace("Angelus/Bliss/","").replace("Angelus/BlueHorizon/","").replace("Angelus/DeepSea/","").replace("Angelus/Fisherman/","").replace("Angelus/Flower/","").replace("Angelus/Rain/","").replace("Angelus/ReactOS/","").replace("Angelus/ReactOSNewHope/","").replace("Angelus/ReactOSSea/","").replace("Angelus/ReactOSSunset/","").replace("Angelus/Sea/","").replace("Angelus/Sky/","").replace("Angelus/VistaReactOS/","")
                    hbox:
                        add "gui/desktop/menu_icons/submenu/image.png"
                        textbutton i2 style "ros_properties_screen_choice" text_style "ros_properties_screen_choice" xpos 2 action SetVariable("persistent.wallpaper", "wallpapers/"+i+".png")
    vbox:
        xpos 285 ypos 219
        textbutton "Обзор..." style "ros_properties_buttons" text_style "ros_properties_buttons_text_cancel" focus_mask "gui/window/postinstall/button_idle.png" action NullAction()
        null height 24
        text "Расположение:" style "ros_properties_text"
        null height 4
        textbutton "растянуть" style "ros_properties_screen_choice_fit_mode" text_style "ros_properties_screen_choice_fit_mode_text"
        null height 26
        textbutton "Цвет..." style "ros_properties_buttons" text_style "ros_properties_buttons_text_cancel" focus_mask "gui/window/postinstall/button_idle.png" action NullAction()
# Заставка
screen ros_properties_screen_screensaver():
    frame:
        style "ros_properties_viewport"
        xsize 377 ysize 351
        add "gui/window/properties/screensaver_frame.png" xpos 110 ypos 19
    frame:
        style "ros_properties_submenu_frame"
        xsize 345 ysize 80
        xpos 19 ypos 203
        textbutton "Заставка" style "ros_properties_submenu_frame_title" text_style "ros_properties_submenu_frame_title" xpos 4 ypos -10
        textbutton "(нет)" style "ros_properties_screen_screensaver_dropdown_menu" text_style "ros_properties_screen_screensaver_dropdown_menu_text" xpos 5 ypos 8 action NullAction()
        textbutton "Параметры" style "ros_properties_buttons" text_style "ros_properties_buttons_text" xpos 164 ypos 6
        textbutton "Просмотр" style "ros_properties_buttons" text_style "ros_properties_screen_screensaver_view" xpos 250 ypos 6
        if screensaver is None:
            text "{color=#808080}Интервал:{/color}" style "ros_properties_text" xpos 5 ypos 48
        else:
            text "Интервал:" style "ros_properties_text" xpos 5 ypos 48
        textbutton "10" style "ros_properties_screen_screensaver_adjust_box" text_style "ros_properties_screen_screensaver_adjust_box_text" xpos 60 ypos 45
        if screensaver is None:
            text "{color=#808080}мин.{/color}" style "ros_properties_text" xpos 113 ypos 48
        else:
            text "мин." style "ros_properties_text" xpos 113 ypos 48
        hbox:
            xpos 152 ypos 48
            style_prefix "ros_check"
            textbutton "Начинать с экрана приветствия"
    frame:
        style "ros_properties_submenu_frame"
        xsize 345 ysize 62
        xpos 19 ypos 296
        textbutton "Энергосбережение" style "ros_properties_submenu_frame_title" text_style "ros_properties_submenu_frame_title" xpos 4 ypos -10
        text "Для изменения параметров питания\nмонитора нажмите кнопку \"Питание\"." style "ros_properties_text" xpos 11 ypos 8
        textbutton "Питание..." style "ros_properties_buttons" text_style "ros_properties_screen_screensaver_view" focus_mask "gui/window/postinstall/button_idle.png" xpos 244 ypos 16 action NullAction()
# Оформление
screen ros_properties_screen_appearance():
    frame:
        style "ros_properties_viewport"
        xsize 377 ysize 351
        add "gui/window/properties/appearance_frame.png" xpos 15 ypos 14
        if ros_theme == "classic":
            add "postinstall" xsize 344 ysize 191 xpos 17 ypos 16
        elif ros_theme == "blackshade":
            add "blackshade_solid_color" xsize 344 ysize 191 xpos 17 ypos 16
        elif ros_theme == "lautus":
            add "lautus_solid_color" xsize 344 ysize 191 xpos 17 ypos 16
        elif ros_theme == "lunar":
            add "lunar_solid_color" xsize 344 ysize 191 xpos 17 ypos 16
        elif ros_theme == "mizu":
            add "mizu_solid_color" xsize 344 ysize 191 xpos 17 ypos 16
        elif ros_theme == "modern":
            add "modern_solid_color" xsize 344 ysize 191 xpos 17 ypos 16
        vbox:
            if ros_theme == "classic":
                use ros_properties_screen_appearance_inactive_window
                use ros_properties_screen_appearance_active_window
                use ros_properties_screen_appearance_message_window
            elif ros_theme == "blackshade":
                use ros_properties_screen_appearance_inactive_window_blackshade
                use ros_properties_screen_appearance_active_window_blackshade
                use ros_properties_screen_appearance_message_window_blackshade
        vbox:
            python:
                if ros_theme == "classic":
                    selected_theme = "Классическая тема"
                    default_color_scheme = "ReactOS стандартная"
                elif ros_theme == "blackshade":
                    selected_theme = "BlackShade"
                    default_color_scheme = "По умолчанию"
            xpos 16 ypos 217
            spacing 2
            text "Окна и кнопки:" style "ros_properties_text"
            textbutton selected_theme style "ros_properties_screen_appearance_choice_frame" text_style "ros_properties_text" action [
                ToggleVariable("ros_properties_show_bottom_buttons", False, True),
                ToggleVariable("dropdown1", True, False)]
            text "Цветовая схема:" style "ros_properties_text"
            textbutton default_color_scheme style "ros_properties_screen_appearance_choice_frame" text_style "ros_properties_text" action [
                ToggleVariable("ros_properties_show_bottom_buttons", False, True),
                ToggleVariable("dropdown2", True, False)]
            text "Размер шрифта:" style "ros_properties_text"
            textbutton "Обычный" style "ros_properties_screen_appearance_choice_frame" text_style "ros_properties_text" action [
                ToggleVariable("ros_properties_show_bottom_buttons", False, True),
                ToggleVariable("dropdown3", True, False)]
        vbox:
            if dropdown1:
                use ros_properties_screen_appearance_theme_choice_menu
            elif dropdown2:
                use ros_properties_screen_appearance_scheme_choice_menu
            elif dropdown3:
                use ros_properties_screen_appearance_font_size_choice_menu
        vbox:
            xpos 257 ypos 247
            spacing 15
            textbutton "Эффекты..." style "ros_properties_screen_appearance_buttons" text_style "ros_properties_screen_appearance_buttons_text_2" focus_mask "gui/window/properties/appearance_setting_button_idle.png" action NullAction()
            textbutton "Дополнительно" style "ros_properties_screen_appearance_buttons" text_style "ros_properties_screen_appearance_buttons_text" focus_mask "gui/window/properties/appearance_setting_button_idle.png" action NullAction()
# Выборки
# Окна и кнопки
screen ros_properties_screen_appearance_theme_choice_menu():
    frame:
        style "ros_properties_screen_appearance_choice_menu_frame"
        xsize 201 ysize 99
        xpos 16 ypos 254
        vbox:
            xpos -3 ypos -3
            textbutton "BlackShade" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action [
                SetVariable("ros_theme", "blackshade"),
                SetVariable("dropdown1", False),
                SetVariable("ros_properties_show_bottom_buttons", True)]
            textbutton "Lautus" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
            textbutton "Lunar" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
            textbutton "MetaVerse" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
            textbutton "Mizu" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
            textbutton "Modern" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
            textbutton "Классическая тема" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action [
                SetVariable("ros_theme", "classic"),
                SetVariable("dropdown1", False),
                SetVariable("ros_properties_show_bottom_buttons", True)]
# Цветовая схема
screen ros_properties_screen_appearance_scheme_choice_menu():
    frame:
        style "ros_properties_screen_appearance_choice_menu_frame"
        if ros_theme == "classic":
            xsize 201 ysize 323
            xpos 16 ypos 293
            vbox:
                xpos -3 ypos -3
                textbutton "ReactOS классическая" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "ReactOS стандартная" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Баклажан" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Высокая контрастность-1" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Высокая контрастность-2" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Дождливый день" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Зелёная оливка" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Зеленовато-голубая" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Кирпич" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Клён" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Контрастная белая" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Контрастная чёрная" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Красный, белый и синий" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Морская" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Небо" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Песок" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Пшеница" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Роза" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Сирень" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Слива" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Тыква" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Шифер" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
                textbutton "Шторм" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
        elif ros_theme == "blackshade":
            xsize 201 ysize 13
            xpos 16 ypos 293
            vbox:
                xpos -3 ypos -3
                textbutton "По умолчанию" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
# Размер шрифта
screen ros_properties_screen_appearance_font_size_choice_menu():
    frame:
        style "ros_properties_screen_appearance_choice_menu_frame"
        xsize 201 ysize 43
        xpos 16 ypos 332
        vbox:
            xpos -3 ypos -3
            textbutton "Обычный" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
            textbutton "Большой" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
            textbutton "Огромный" style "ros_properties_screen_appearance_choice_menu_entry" text_style "ros_properties_screen_appearance_choice_menu_entry_text" focus_mask "ros_properties_screen_appearance_choice_menu_idle" action NullAction()
# Оформление: Окна для образца темы
# Классическая тема
# Неактивное окно
screen ros_properties_screen_appearance_inactive_window():
    frame:
        style "ros_classic_inactive_window"
        xpos 181 ypos 177
        text "Неактивное окно" style "ros_classic_inactive_window_title" xpos 6 ypos 8
        imagebutton idle "gui/window/common/close_idle.png" xpos 289 ypos 6
        imagebutton idle "gui/window/common/expand_idle.png" xpos 271 ypos 6
        imagebutton idle "gui/window/common/minimize_idle.png" xpos 255 ypos 6
# Активное окно
screen ros_properties_screen_appearance_active_window():
    frame:
        style "ros_classic_active_window"
        xpos 190 ypos 29
        text "Активное окно" style "ros_classic_active_window_title" xpos 6 ypos 8
        imagebutton idle "gui/window/common/close_idle.png" xpos 300 ypos 6
        imagebutton idle "gui/window/common/expand_idle.png" xpos 282 ypos 6
        imagebutton idle "gui/window/common/minimize_idle.png" xpos 266 ypos 6
        hbox:
            xpos 10 ypos 25
            spacing 5
            textbutton "Обычная" style "ros_classic_active_window_menu" text_style "ros_classic_active_window_menu_text" action NullAction()
            textbutton "Отключённая" style "ros_classic_active_window_menu" text_style "ros_classic_active_window_menu_text"
            textbutton "Выбранная" style "ros_classic_active_window_menu_selected" text_style "ros_classic_active_window_menu_selected_text" action NullAction()
        frame:
            style "ros_classic_active_window_viewport" xpos 4 ypos 41
            add "gui/window/properties/active_window_scrollbars.png" xpos 296 ypos 2
            viewport:
                yinitial 0.0
                scrollbars None
                mousewheel True
                draggable True
                side_yfill True
                vbox:
                    text "Текст окна" style "ros_properties_text" xpos 4 ypos 2
# Окно сообщения
screen ros_properties_screen_appearance_message_window():
    frame:
        style "ros_classic_message_window"
        xpos 139 ypos -86
        text "Окно сообщения" style "ros_classic_active_window_title" xpos 6 ypos 8
        imagebutton idle "gui/window/common/close_idle.png" xpos 182 ypos 5
        text "Сообщение" style "ros_properties_text" xpos 8 ypos 25
        textbutton "ОК" style "ros_classic_message_window_ok_button" text_style "ros_classic_message_window_ok_button_text" xpos 62 ypos 40

# Параметры
screen ros_properties_screen_settings():
    frame:
        style "ros_properties_viewport"
        xsize 377 ysize 351
        text "Разместите значки мониторов в соответствии с их расположением." style "ros_properties_text" xpos 10 ypos 10
        frame:
            style "ros_properties_screen_settings_monitors_viewport"
            xpos 9 ypos 40
            add "monitor" xpos 101 ypos 22
        text "Дисплей:" style "ros_properties_text" xpos 10 ypos 187
        text "(Стандартный монитор) на Ren'Py SDL Framework" style "ros_properties_text" xpos 10 ypos 201
        frame:
            style "ros_properties_submenu_frame_mini"
            xpos 10 ypos 225
            textbutton "Разрешение экрана" style "ros_properties_submenu_frame_title" text_style "ros_properties_submenu_frame_title" xpos 8 ypos -6
            text "мен." style "ros_properties_text" xpos 10 ypos 12
            text "бол." style "ros_properties_text" xpos 135 ypos 12
            add "ros_properties_slider" xpos 49 ypos 21
            add "ros_properties_slider_thumb" xpos 109 ypos 14
            add "ros_properties_slider_marks" xpos 54 ypos 37
            text "[config.screen_width]x[config.screen_height] пикселей" style "ros_properties_text" xpos 38 ypos 45
        frame:
            style "ros_properties_submenu_frame_mini"
            xpos 193 ypos 225
            textbutton "Качество цветопередачи" style "ros_properties_submenu_frame_title" text_style "ros_properties_submenu_frame_title" xpos 8 ypos -6
            textbutton "Самое высокое (32 бита)" style "ros_properties_screen_screensaver_dropdown_menu" text_style "ros_properties_screen_screensaver_dropdown_menu_text" xpos 10 ypos 13 action NullAction()
            frame:
                style "ros_properties_color_quality_frame"
                xpos 10 ypos 42
                add "gui/window/properties/32bit_color.png" xpos -3 ypos -3
        textbutton "Дополнительно" style "ros_properties_screen_appearance_buttons" text_style "ros_properties_screen_appearance_buttons_text" focus_mask "gui/window/properties/appearance_setting_button_idle.png" xpos 260 ypos 298 action NullAction()

# Окно - Свойства: Меню "Пуск" и панель задач
screen ros_properties_taskbar():
    drag:
        drag_name "ros_properties"
        drag_handle (0, 0, 395, 21)
        xalign 0 yalign 0.9
        frame:
            style "ros_properties_frame"
            xsize 404 ysize 449
            add "gui/desktop/menu_icons/submenu/start_menu.png" xpos 3
            text "Свойства: Меню \"Пуск\" и панель задач" style "ros_properties_window_title"
            imagebutton idle "gui/window/common/close_idle.png" action [
                SetVariable("properties_current_tab", "general"),
                Hide("ros_properties_taskbar")]:
                xanchor -379 yanchor 0
            if properties_current_tab == "general":
                use ros_properties_taskbar_taskbar_settings
            elif properties_current_tab == "start_menu":
                use ros_properties_taskbar_start_menu_settings
            hbox:
                xpos 3 ypos 26
                textbutton "Панель задач" style "ros_properties_tabs_medium" text_style "ros_properties_tabs_text_5" focus_mask "ros_properties_tab_medium_idle" action SetVariable("properties_current_tab", "general")
                null width 10
                textbutton "Меню \"Пуск\"" style "ros_properties_tabs_medium" text_style "ros_properties_tabs_text_6" focus_mask "ros_properties_tab_medium_idle" action SetVariable("properties_current_tab", "start_menu")
            hbox:
                xpos 134 ypos 410
                textbutton "ОК" style "ros_properties_buttons" text_style "ros_properties_buttons_text_ok" focus_mask "gui/window/postinstall/button_idle.png" action [
                SetVariable("properties_current_tab", "general"),
                Hide("ros_properties_taskbar")]
                null width 72
                textbutton "Отмена" style "ros_properties_buttons" text_style "ros_properties_buttons_text_cancel" focus_mask "gui/window/postinstall/button_idle.png" action [
                SetVariable("properties_current_tab", "general"),
                Hide("ros_properties_taskbar")]
                null width 48
                textbutton "Применить" style "ros_properties_buttons" text_style "ros_properties_buttons_text"
# Панель задач
screen ros_properties_taskbar_taskbar_settings():
    frame:
        style "ros_properties_viewport"
        xsize 386 ysize 360
    frame:
        style "ros_properties_submenu_frame"
        xsize 360 ysize 168
        xpos 14 ypos 62
        textbutton "Оформление панели задач" style "ros_properties_submenu_frame_title" text_style "ros_properties_submenu_frame_title" xpos 6 ypos -10
        add "gui/window/properties/taskbar_settings_thumbnail_frame.png" xpos 5 ypos 10
        if persistent.taskbar_settings_hide_taskbar:
            add "gui/window/properties/start_menu_settings/145.png" xpos 6 ypos 11
        else:
            if persistent.taskbar_settings_lock_taskbar:
                if persistent.taskbar_settings_group_similar_taskbar_buttons and persistent.taskbar_settings_show_quick_launch:
                    add "gui/window/properties/start_menu_settings/146.png" xpos 6 ypos 11
                elif persistent.taskbar_settings_show_quick_launch and not persistent.taskbar_settings_group_similar_taskbar_buttons:
                    add "gui/window/properties/start_menu_settings/148.png" xpos 6 ypos 11
                elif persistent.taskbar_settings_group_similar_taskbar_buttons and not persistent.taskbar_settings_show_quick_launch:
                    add "gui/window/properties/start_menu_settings/150.png" xpos 6 ypos 11
                elif not persistent.taskbar_settings_group_similar_taskbar_buttons and not persistent.taskbar_settings_show_quick_launch:
                    add "gui/window/properties/start_menu_settings/152.png" xpos 6 ypos 11
            elif not persistent.taskbar_settings_lock_taskbar:
                if persistent.taskbar_settings_group_similar_taskbar_buttons and persistent.taskbar_settings_show_quick_launch:
                    add "gui/window/properties/start_menu_settings/147.png" xpos 6 ypos 11
                elif persistent.taskbar_settings_show_quick_launch and not persistent.taskbar_settings_group_similar_taskbar_buttons:
                    add "gui/window/properties/start_menu_settings/149.png" xpos 6 ypos 11
                elif persistent.taskbar_settings_group_similar_taskbar_buttons and not persistent.taskbar_settings_show_quick_launch:
                    add "gui/window/properties/start_menu_settings/151.png" xpos 6 ypos 11
                elif not persistent.taskbar_settings_group_similar_taskbar_buttons and not persistent.taskbar_settings_show_quick_launch:
                    add "gui/window/properties/start_menu_settings/153.png" xpos 6 ypos 11
        vbox:
            style_prefix "ros_check"
            xmaximum 1000
            xpos 5 ypos 55
            textbutton "Закрепить панель задач" action ToggleVariable("persistent.taskbar_settings_lock_taskbar", True, False)
            textbutton "Автоматически скрывать панель задач" action ToggleVariable("persistent.taskbar_settings_hide_taskbar", True, False)
            textbutton "Отображать панель задач поверх других окон" action ToggleVariable("persistent.taskbar_settings_keep_taskbar_on_top_of_other_windows", True, False)
            textbutton "Группировать схожие кнопки панели задач" action ToggleVariable("persistent.taskbar_settings_group_similar_taskbar_buttons", True, False)
            textbutton "Отображать панель быстрого запуска" action ToggleVariable("persistent.taskbar_settings_show_quick_launch", True, False)
    frame:
        style "ros_properties_submenu_frame"
        xsize 360 ysize 154
        xpos 14 ypos 238
        textbutton "Область уведомлений" style "ros_properties_submenu_frame_title" text_style "ros_properties_submenu_frame_title" xpos 6 ypos -10
        add "gui/window/properties/taskbar_settings_thumbnail_frame.png" xpos 5 ypos 10
        if persistent.taskbar_settings_show_clock:
            if not persistent.taskbar_settings_show_seconds and persistent.taskbar_settings_hide_inactive_icons:
                add "gui/window/properties/start_menu_settings/180.png" xpos 6 ypos 11
            elif not persistent.taskbar_settings_show_seconds and not persistent.taskbar_settings_hide_inactive_icons:
                add "gui/window/properties/start_menu_settings/182.png" xpos 6 ypos 11
            elif persistent.taskbar_settings_show_seconds and not persistent.taskbar_settings_hide_inactive_icons:
                add "gui/window/properties/start_menu_settings/184.png" xpos 6 ypos 11
            elif persistent.taskbar_settings_show_seconds and persistent.taskbar_settings_hide_inactive_icons:
                add "gui/window/properties/start_menu_settings/185.png" xpos 6 ypos 11
        else:
            if persistent.taskbar_settings_hide_inactive_icons:
                add "gui/window/properties/start_menu_settings/181.png" xpos 6 ypos 11
            elif not persistent.taskbar_settings_hide_inactive_icons:
                add "gui/window/properties/start_menu_settings/183.png" xpos 6 ypos 11
        vbox:
            style_prefix "ros_check"
            xmaximum 1000
            xpos 5 ypos 55
            hbox:
                spacing 20
                textbutton "Отображать часы" action ToggleVariable("persistent.taskbar_settings_show_clock", True, False)
                if persistent.taskbar_settings_show_clock:
                    textbutton "Отображать секунды" action ToggleVariable("persistent.taskbar_settings_show_seconds", True, False)
                else:
                    textbutton "Отображать секунды"
            text "Можно избежать загромождения области уведомлений, скрывая\nзначки, которые не использовались." style "ros_properties_text"
            null height 10
            hbox:
                textbutton "Скрывать неиспользуемые значки" action ToggleVariable("persistent.taskbar_settings_hide_inactive_icons", True, False)
                if persistent.taskbar_settings_hide_inactive_icons:
                    textbutton "Настроить..." style "ros_properties_buttons" text_style "ros_properties_buttons_text" focus_mask "gui/window/postinstall/button_idle.png" xpos 60 ypos -6 action NullAction()
                else:
                    textbutton "Настроить..." style "ros_properties_buttons" text_style "ros_properties_buttons_text" xpos 60 ypos -6
# Меню "Пуск"
screen ros_properties_taskbar_start_menu_settings():
    frame:
        style "ros_properties_viewport"
        xsize 386 ysize 360
        add "gui/window/properties/appearance_frame.png" xsize 302 ysize 182 xpos 15 ypos 13
        if persistent.start_menu_layout == "modern":
            add "gui/window/properties/start_menu_settings/170.png" xpos 16 ypos 14
        else:
            add "gui/window/properties/start_menu_settings/171.png" xpos 16 ypos 14
        vbox:
            style_prefix "ros_radio"
            xmaximum 1000
            xpos 15 ypos 215
            hbox:
                textbutton "Меню \"Пуск\"" action SetVariable("persistent.start_menu_layout", "modern")
                if persistent.start_menu_layout == "modern":
                    textbutton "Настроить..." style "ros_properties_buttons" text_style "ros_properties_buttons_text" focus_mask "gui/window/postinstall/button_idle.png" xpos 190 ypos 1 action NullAction()
                else:
                    textbutton "Настроить..." style "ros_properties_buttons" text_style "ros_properties_buttons_text" xpos 190 ypos 1
            text "Этот стиль упрощает доступ к Интернету,\nэлектронной почте и часто используемым программам." style "ros_properties_text"
            null height 8
            hbox:
                textbutton "Классическое меню \"Пуск\"" action SetVariable("persistent.start_menu_layout", "legacy")
                if persistent.start_menu_layout == "legacy":
                    textbutton "Настроить..." style "ros_properties_buttons" text_style "ros_properties_buttons_text" focus_mask "gui/window/postinstall/button_idle.png" xpos 121 ypos 1 action NullAction()
                else:
                    textbutton "Настроить..." style "ros_properties_buttons" text_style "ros_properties_buttons_text" xpos 121 ypos 1
            text "Классический стиль отображения меню \"Пуск\"." style "ros_properties_text"