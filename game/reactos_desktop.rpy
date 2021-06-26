# Панель задач
screen ros_taskbar():
    add "gui/desktop/taskbar.png":
        yalign 1.0
    use ros_desktop_context_menu_trigger
    use ros_desktop_taskbar_context_menu_trigger
    textbutton "Пуск" style "ros_start_button" text_style "ros_start_button_text" focus_mask "gui/desktop/start_button.png" action [
        Hide(screen="ros_start_menu_entertainment_frame"),
        Hide(screen="ros_start_menu_communications_frame"),
        Hide(screen="ros_start_menu_services_frame"),
        Hide(screen="ros_start_menu_accessibility_frame"),
        Hide(screen="ros_start_menu_autostart_frame"),
        Hide(screen="ros_start_menu_administration_frame"),
        Hide(screen="ros_start_menu_games_frame"),
        Hide(screen="ros_start_menu_system_tools_frame"),
        Hide(screen="ros_start_menu_programs_frame"),
        Hide(screen="ros_start_menu_documents_frame"),
        Hide(screen="ros_start_menu_settings_frame"),
        Hide(screen="ros_start_menu_new_recent_docs"),
        Hide(screen="ros_start_menu_new_entertainment_frame"),
        Hide(screen="ros_start_menu_new_communications_frame"),
        Hide(screen="ros_start_menu_new_services_frame"),
        Hide(screen="ros_start_menu_new_accessibility_frame"),
        Hide(screen="ros_start_menu_new_autostart_frame"),
        Hide(screen="ros_start_menu_new_administration_frame"),
        Hide(screen="ros_start_menu_new_games_frame"),
        Hide(screen="ros_start_menu_new_system_tools_frame"),
        Hide(screen="ros_start_menu_new_all_programs"),
        ToggleVariable("start_menu_opened", True, False)]:
        xpos 4 ypos 696
    if start_menu_opened:
        if persistent.start_menu_layout == "legacy":
            use ros_start_menu
        else:
            use ros_start_menu_new
    add "gui/desktop/system_tray.png":
        xalign 0.998 yalign 0.998
    add myClock xpos 1234 ypos 700
    imagebutton idle "gui/desktop/systray_icons/network.png" action NullAction():
        xpos 1222 ypos 700
    imagebutton idle "gui/desktop/systray_icons/ac_powerline.png" action NullAction():
        xpos 1208 ypos 700
    imagebutton idle "gui/desktop/systray_icons/safe_remove.png" action NullAction():
        xpos 1189 ypos 700
    imagebutton idle "gui/desktop/systray_icons/volume.png" action NullAction():
        xpos 1171 ypos 700
    key "K_ESCAPE" action [
        Hide(screen="ros_start_menu_entertainment_frame"),
        Hide(screen="ros_start_menu_communications_frame"),
        Hide(screen="ros_start_menu_services_frame"),
        Hide(screen="ros_start_menu_accessibility_frame"),
        Hide(screen="ros_start_menu_autostart_frame"),
        Hide(screen="ros_start_menu_administration_frame"),
        Hide(screen="ros_start_menu_games_frame"),
        Hide(screen="ros_start_menu_system_tools_frame"),
        Hide(screen="ros_start_menu_programs_frame"),
        Hide(screen="ros_start_menu_documents_frame"),
        Hide(screen="ros_start_menu_settings_frame"),
        Hide(screen="ros_start_menu_new_recent_docs"),
        Hide(screen="ros_start_menu_new_entertainment_frame"),
        Hide(screen="ros_start_menu_new_communications_frame"),
        Hide(screen="ros_start_menu_new_services_frame"),
        Hide(screen="ros_start_menu_new_accessibility_frame"),
        Hide(screen="ros_start_menu_new_autostart_frame"),
        Hide(screen="ros_start_menu_new_administration_frame"),
        Hide(screen="ros_start_menu_new_games_frame"),
        Hide(screen="ros_start_menu_new_system_tools_frame"),
        Hide(screen="ros_start_menu_new_all_programs"),
        SetVariable("start_menu_opened", False)]

# Меню "Пуск" (классический вариант)
screen ros_start_menu():
    frame:
        style "ros_start_menu"
        xsize 260 ysize 310
        xpos 4 ypos 387
        vbox:
            xpos 24 ypos 3
            textbutton "(пусто)" style "ros_start_menu_entry" text_style "ros_start_menu_entry_text"
            null height 25
            frame:
                style "ros_start_menu_entry"
                textbutton "Программы                                          {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_entry" text_style "ros_start_menu_entry_text" focus_mask "ros_start_menu_entry_idle" hovered [
                    Hide(screen="ros_start_menu_entertainment_frame"),
                    Hide(screen="ros_start_menu_communications_frame"),
                    Hide(screen="ros_start_menu_services_frame"),
                    Hide(screen="ros_start_menu_accessibility_frame"),
                    Hide(screen="ros_start_menu_autostart_frame"),
                    Hide(screen="ros_start_menu_administration_frame"),
                    Hide(screen="ros_start_menu_games_frame"),
                    Hide(screen="ros_start_menu_system_tools_frame"),
                    Hide(screen="ros_start_menu_documents_frame"),
                    Hide(screen="ros_start_menu_settings_frame"),
                    Show(screen="ros_start_menu_programs_frame")] action NullAction()
                add "gui/desktop/menu_icons/programs.png":
                    xpos 2 ypos 1
                textbutton "Документы                                          {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_entry" text_style "ros_start_menu_entry_text" focus_mask "ros_start_menu_entry_idle" hovered [
                    Hide(screen="ros_start_menu_entertainment_frame"),
                    Hide(screen="ros_start_menu_communications_frame"),
                    Hide(screen="ros_start_menu_services_frame"),
                    Hide(screen="ros_start_menu_accessibility_frame"),
                    Hide(screen="ros_start_menu_autostart_frame"),
                    Hide(screen="ros_start_menu_administration_frame"),
                    Hide(screen="ros_start_menu_games_frame"),
                    Hide(screen="ros_start_menu_system_tools_frame"),
                    Hide(screen="ros_start_menu_programs_frame"),
                    Hide(screen="ros_start_menu_settings_frame"),
                    Show(screen="ros_start_menu_documents_frame")] action NullAction():
                    yalign 0.12
                add "gui/desktop/menu_icons/documents.png":
                    xpos 2 ypos 32
                textbutton "Настройка                                           {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_entry" text_style "ros_start_menu_entry_text" focus_mask "ros_start_menu_entry_idle" hovered [
                    Hide(screen="ros_start_menu_entertainment_frame"),
                    Hide(screen="ros_start_menu_communications_frame"),
                    Hide(screen="ros_start_menu_services_frame"),
                    Hide(screen="ros_start_menu_accessibility_frame"),
                    Hide(screen="ros_start_menu_autostart_frame"),
                    Hide(screen="ros_start_menu_administration_frame"),
                    Hide(screen="ros_start_menu_games_frame"),
                    Hide(screen="ros_start_menu_system_tools_frame"),
                    Hide(screen="ros_start_menu_programs_frame"),
                    Hide(screen="ros_start_menu_documents_frame"),
                    Show(screen="ros_start_menu_settings_frame")] action NullAction():
                    yalign 0.24
                add "gui/desktop/menu_icons/settings.png":
                    xpos 2 ypos 62
                textbutton "Поиск" style "ros_start_menu_entry" text_style "ros_start_menu_entry_text" focus_mask "ros_start_menu_entry_idle" hovered [
                    Hide(screen="ros_start_menu_entertainment_frame"),
                    Hide(screen="ros_start_menu_communications_frame"),
                    Hide(screen="ros_start_menu_services_frame"),
                    Hide(screen="ros_start_menu_accessibility_frame"),
                    Hide(screen="ros_start_menu_autostart_frame"),
                    Hide(screen="ros_start_menu_administration_frame"),
                    Hide(screen="ros_start_menu_games_frame"),
                    Hide(screen="ros_start_menu_system_tools_frame"),
                    Hide(screen="ros_start_menu_programs_frame"),
                    Hide(screen="ros_start_menu_documents_frame"),
                    Hide(screen="ros_start_menu_settings_frame")] action NullAction():
                    yalign 0.37
                add "gui/desktop/menu_icons/search.png":
                    xpos 2 ypos 97
                textbutton "Справка и поддержка" style "ros_start_menu_entry" text_style "ros_start_menu_entry_text" focus_mask "ros_start_menu_entry_idle" hovered [
                    Hide(screen="ros_start_menu_entertainment_frame"),
                    Hide(screen="ros_start_menu_communications_frame"),
                    Hide(screen="ros_start_menu_services_frame"),
                    Hide(screen="ros_start_menu_accessibility_frame"),
                    Hide(screen="ros_start_menu_autostart_frame"),
                    Hide(screen="ros_start_menu_administration_frame"),
                    Hide(screen="ros_start_menu_games_frame"),
                    Hide(screen="ros_start_menu_system_tools_frame"),
                    Hide(screen="ros_start_menu_programs_frame"),
                    Hide(screen="ros_start_menu_documents_frame"),
                    Hide(screen="ros_start_menu_settings_frame")] action NullAction():
                    yalign 0.5
                add "gui/desktop/menu_icons/help.png":
                    xpos 2 ypos 128
                textbutton "Выполнить..." style "ros_start_menu_entry" text_style "ros_start_menu_entry_text" focus_mask "ros_start_menu_entry_idle" hovered [
                    Hide(screen="ros_start_menu_entertainment_frame"),
                    Hide(screen="ros_start_menu_communications_frame"),
                    Hide(screen="ros_start_menu_services_frame"),
                    Hide(screen="ros_start_menu_accessibility_frame"),
                    Hide(screen="ros_start_menu_autostart_frame"),
                    Hide(screen="ros_start_menu_administration_frame"),
                    Hide(screen="ros_start_menu_games_frame"),
                    Hide(screen="ros_start_menu_system_tools_frame"),
                    Hide(screen="ros_start_menu_programs_frame"),
                    Hide(screen="ros_start_menu_documents_frame"),
                    Hide(screen="ros_start_menu_settings_frame")] action NullAction():
                    yalign 0.62
                add "gui/desktop/menu_icons/run.png":
                    xpos 2 ypos 161
                textbutton "Завершение сеанса Administrator..." style "ros_start_menu_entry" text_style "ros_start_menu_entry_text" focus_mask "ros_start_menu_entry_idle" hovered [
                    Hide(screen="ros_start_menu_entertainment_frame"),
                    Hide(screen="ros_start_menu_communications_frame"),
                    Hide(screen="ros_start_menu_services_frame"),
                    Hide(screen="ros_start_menu_accessibility_frame"),
                    Hide(screen="ros_start_menu_autostart_frame"),
                    Hide(screen="ros_start_menu_administration_frame"),
                    Hide(screen="ros_start_menu_games_frame"),
                    Hide(screen="ros_start_menu_system_tools_frame"),
                    Hide(screen="ros_start_menu_programs_frame"),
                    Hide(screen="ros_start_menu_documents_frame"),
                    Hide(screen="ros_start_menu_settings_frame")] action [
                        SetVariable("start_menu_opened", False),
                        Show(screen="ros_logoff_frame")]:
                    yalign 0.78
                add "gui/desktop/menu_icons/logoff.png":
                    xpos 2 ypos 201
                textbutton "Выключить компьютер..." style "ros_start_menu_entry" text_style "ros_start_menu_entry_text" focus_mask "ros_start_menu_entry_idle" hovered [
                    Hide(screen="ros_start_menu_entertainment_frame"),
                    Hide(screen="ros_start_menu_communications_frame"),
                    Hide(screen="ros_start_menu_services_frame"),
                    Hide(screen="ros_start_menu_accessibility_frame"),
                    Hide(screen="ros_start_menu_autostart_frame"),
                    Hide(screen="ros_start_menu_administration_frame"),
                    Hide(screen="ros_start_menu_games_frame"),
                    Hide(screen="ros_start_menu_system_tools_frame"),
                    Hide(screen="ros_start_menu_programs_frame"),
                    Hide(screen="ros_start_menu_documents_frame"),
                    Hide(screen="ros_start_menu_settings_frame")] action [
                        SetVariable("start_menu_opened", False),
                        Show(screen="ros_shutdown_frame")]:
                    yalign 0.9
                add "gui/desktop/menu_icons/shutdown.png":
                    xpos 2 ypos 233
            transclude

# Программы
screen ros_start_menu_programs_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 214 ysize 134
        xpos 264 ypos 427
        vbox:
            xalign -0.01
            textbutton "Автозагрузка                                 {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_submenu" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_idle" hovered [
                Hide(screen="ros_start_menu_entertainment_frame"),
                Hide(screen="ros_start_menu_communications_frame"),
                Hide(screen="ros_start_menu_services_frame"),
                Hide(screen="ros_start_menu_accessibility_frame"),
                Hide(screen="ros_start_menu_games_frame"),
                Hide(screen="ros_start_menu_system_tools_frame"),
                Hide(screen="ros_start_menu_administration_frame"),
                Show(screen="ros_start_menu_autostart_frame")] action NullAction()
            add "gui/desktop/menu_icons/submenu/folder.png":
                xpos 6 ypos -12
            textbutton "Администрирование                      {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_submenu" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_idle" hovered [
                Hide(screen="ros_start_menu_entertainment_frame"),
                Hide(screen="ros_start_menu_communications_frame"),
                Hide(screen="ros_start_menu_services_frame"),
                Hide(screen="ros_start_menu_accessibility_frame"),
                Hide(screen="ros_start_menu_autostart_frame"),
                Hide(screen="ros_start_menu_games_frame"),
                Hide(screen="ros_start_menu_system_tools_frame"),
                Show(screen="ros_start_menu_administration_frame")] action NullAction():
                ypos -12
            add "gui/desktop/menu_icons/submenu/folder.png":
                xpos 6 ypos -24
            textbutton "Игры                                               {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_submenu" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_idle" hovered [
                Hide(screen="ros_start_menu_entertainment_frame"),
                Hide(screen="ros_start_menu_communications_frame"),
                Hide(screen="ros_start_menu_services_frame"),
                Hide(screen="ros_start_menu_accessibility_frame"),
                Hide(screen="ros_start_menu_autostart_frame"),
                Hide(screen="ros_start_menu_administration_frame"),
                Hide(screen="ros_start_menu_system_tools_frame"),
                Show(screen="ros_start_menu_games_frame")] action NullAction():
                ypos -24
            add "gui/desktop/menu_icons/submenu/programs.png":
                xpos 6 ypos -36
            textbutton "Стандартные                                {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_submenu" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_idle" hovered [
                Hide(screen="ros_start_menu_entertainment_frame"),
                Hide(screen="ros_start_menu_communications_frame"),
                Hide(screen="ros_start_menu_services_frame"),
                Hide(screen="ros_start_menu_accessibility_frame"),
                Hide(screen="ros_start_menu_autostart_frame"),
                Hide(screen="ros_start_menu_administration_frame"),
                Hide(screen="ros_start_menu_games_frame"),
                Show(screen="ros_start_menu_system_tools_frame")] action NullAction():
                ypos -36
            add "gui/desktop/menu_icons/submenu/programs.png":
                xpos 6 ypos -48
            textbutton "Wine Internet Explorer" style "ros_start_menu_submenu" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_idle" hovered [
                Hide(screen="ros_start_menu_entertainment_frame"),
                Hide(screen="ros_start_menu_communications_frame"),
                Hide(screen="ros_start_menu_services_frame"),
                Hide(screen="ros_start_menu_accessibility_frame"),
                Hide(screen="ros_start_menu_autostart_frame"),
                Hide(screen="ros_start_menu_administration_frame"),
                Hide(screen="ros_start_menu_games_frame"),
                Hide(screen="ros_start_menu_system_tools_frame")] action NullAction():
                ypos -48
            add "iexplore_shortcut":
                xpos 6 ypos -60
            textbutton "Менеджер приложений ReactOS" style "ros_start_menu_submenu" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_idle" hovered [
                Hide(screen="ros_start_menu_entertainment_frame"),
                Hide(screen="ros_start_menu_communications_frame"),
                Hide(screen="ros_start_menu_services_frame"),
                Hide(screen="ros_start_menu_accessibility_frame"),
                Hide(screen="ros_start_menu_autostart_frame"),
                Hide(screen="ros_start_menu_administration_frame"),
                Hide(screen="ros_start_menu_games_frame"),
                Hide(screen="ros_start_menu_system_tools_frame")] action NullAction():
                ypos -60
            add "app_manager_shortcut":
                xpos 6 ypos -72
            textbutton "Проводник ReactOS" style "ros_start_menu_submenu" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_idle" hovered [
                Hide(screen="ros_start_menu_entertainment_frame"),
                Hide(screen="ros_start_menu_communications_frame"),
                Hide(screen="ros_start_menu_services_frame"),
                Hide(screen="ros_start_menu_accessibility_frame"),
                Hide(screen="ros_start_menu_autostart_frame"),
                Hide(screen="ros_start_menu_administration_frame"),
                Hide(screen="ros_start_menu_games_frame"),
                Hide(screen="ros_start_menu_system_tools_frame")] action [
                    SetVariable("start_menu_opened", False),
                    Hide(screen="ros_start_menu_programs_frame"),
                    Show(screen="ros_explorer")]:
                ypos -72
            add "explorer_shortcut":
                xpos 6 ypos -84
# Программы: Автозагрузка
screen ros_start_menu_autostart_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 88 ysize 24
        xpos 477 ypos 427
        vbox:
            xalign -0.01
            textbutton "(пусто)" style "ros_start_menu_submenu" text_style "ros_start_menu_submenu_text"
# Программы: Администрирование
screen ros_start_menu_administration_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 159 ysize 78
        xpos 477 ypos 447
        vbox:
            xalign -0.01
            textbutton "Диспетчер служб" style "ros_start_menu_submenu_administration" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_administration_idle" action NullAction()
            add "services_shortcut":
                xpos 6 ypos -12
            textbutton "Диспетчер устройств" style "ros_start_menu_submenu_administration" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_administration_idle" action NullAction():
                ypos -12
            add "device_manager_shortcut":
                xpos 6 ypos -24
            textbutton "Параметры системы" style "ros_start_menu_submenu_administration" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_administration_idle" action NullAction():
                ypos -24
            add "system_settings_shortcut":
                xpos 6 ypos -36
            textbutton "Просмотр событий" style "ros_start_menu_submenu_administration" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_administration_idle" action NullAction():
                ypos -36
            add "event_viewer_shortcut":
                xpos 6 ypos -48
# Программы: Игры
screen ros_start_menu_games_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 138 ysize 60
        xpos 477 ypos 465
        vbox:
            xalign -0.01
            textbutton "Пасьянс \"Косынка\"" style "ros_start_menu_submenu_games" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_games_idle" action NullAction()
            add "solitaire_shortcut":
                xpos 6 ypos -12
            textbutton "Пасьянс \"Паук\"" style "ros_start_menu_submenu_games" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_games_idle" action NullAction():
                ypos -12
            add "spider_shortcut":
                xpos 6 ypos -24
            textbutton "Сапёр" style "ros_start_menu_submenu_games" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_games_idle" action NullAction():
                ypos -24
            add "minesweeper_shortcut":
                xpos 6 ypos -36
# Программы: Стандартные
screen ros_start_menu_system_tools_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 190 ysize 168
        xpos 477 ypos 482
        vbox:
            xalign -0.01
            textbutton "Развлечения                          {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_communications_frame"),
                Hide(screen="ros_start_menu_services_frame"),
                Hide(screen="ros_start_menu_accessibility_frame"),
                Show(screen="ros_start_menu_entertainment_frame")] action NullAction()
            add "gui/desktop/menu_icons/submenu/programs.png":
                xpos 6 ypos -12
            textbutton "Связь                                      {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_entertainment_frame"),
                Hide(screen="ros_start_menu_services_frame"),
                Hide(screen="ros_start_menu_accessibility_frame"),
                Show(screen="ros_start_menu_communications_frame")] action NullAction():
                ypos -12
            add "gui/desktop/menu_icons/submenu/programs.png":
                xpos 6 ypos -24
            textbutton "Служебные                             {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_communications_frame"),
                Hide(screen="ros_start_menu_accessibility_frame"),
                Hide(screen="ros_start_menu_entertainment_frame"),
                Show(screen="ros_start_menu_services_frame")] action NullAction():
                ypos -24
            add "gui/desktop/menu_icons/submenu/programs.png":
                xpos 6 ypos -36
            textbutton "Специальные возможности  {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_services_frame"),
                Hide(screen="ros_start_menu_communications_frame"),
                Hide(screen="ros_start_menu_entertainment_frame"),
                Show(screen="ros_start_menu_accessibility_frame")] action NullAction():
                ypos -36
            add "gui/desktop/menu_icons/submenu/programs.png":
                xpos 6 ypos -48
            textbutton "Paint" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_entertainment_frame"),
                Hide(screen="ros_start_menu_communications_frame"),
                Hide(screen="ros_start_menu_services_frame"),
                Hide(screen="ros_start_menu_accessibility_frame")] action NullAction():
                ypos -48
            add "paint_shortcut":
                xpos 6 ypos -60
            textbutton "WordPad" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_entertainment_frame"),
                Hide(screen="ros_start_menu_communications_frame"),
                Hide(screen="ros_start_menu_services_frame"),
                Hide(screen="ros_start_menu_accessibility_frame")] action NullAction():
                ypos -60
            add "wordpad_shortcut":
                xpos 6 ypos -72
            textbutton "Блокнот" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_entertainment_frame"),
                Hide(screen="ros_start_menu_communications_frame"),
                Hide(screen="ros_start_menu_services_frame"),
                Hide(screen="ros_start_menu_accessibility_frame")] action [
                    SetVariable("start_menu_opened", False),
                    Hide(screen="ros_start_menu_system_tools_frame"),
                    Hide(screen="ros_start_menu_programs_frame"),
                    Show(screen="ros_notepad")]:
                ypos -72
            add "notepad_shortcut":
                xpos 6 ypos -84
            textbutton "Калькулятор" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_entertainment_frame"),
                Hide(screen="ros_start_menu_communications_frame"),
                Hide(screen="ros_start_menu_services_frame"),
                Hide(screen="ros_start_menu_accessibility_frame")] action NullAction():
                ypos -84
            add "calc_shortcut":
                xpos 6 ypos -96
            textbutton "Командная строка" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_entertainment_frame"),
                Hide(screen="ros_start_menu_communications_frame"),
                Hide(screen="ros_start_menu_services_frame"),
                Hide(screen="ros_start_menu_accessibility_frame")] action NullAction():
                ypos -96
            add "cmd_shortcut":
                xpos 6 ypos -108
# Программы: Стандартные - Развлечения
screen ros_start_menu_entertainment_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 131 ysize 60
        xpos 666 ypos 482
        vbox:
            xalign -0.01
            textbutton "Громкость" style "ros_start_menu_submenu_entertainment" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_entertainment_idle" action NullAction()
            add "volume_shortcut":
                xpos 6 ypos -12
            textbutton "Звукозапись" style "ros_start_menu_submenu_entertainment" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_entertainment_idle" action NullAction():
                ypos -12
            add "recorder_shortcut":
                xpos 6 ypos -24
            textbutton "Проигрыватель" style "ros_start_menu_submenu_entertainment" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_entertainment_idle" action NullAction():
                ypos -24
            add "media_player_shortcut":
                xpos 6 ypos -36
# Программы: Стандартные - Связь
screen ros_start_menu_communications_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 275 ysize 24
        xpos 666 ypos 502
        vbox:
            xalign -0.01
            textbutton "Подключение к удалённому рабочему столу" style "ros_start_menu_submenu_communications" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_communications_idle" action NullAction()
            add "rdp_shortcut":
                xpos 6 ypos -14
# Программы: Стандартные - Служебные
screen ros_start_menu_services_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 251 ysize 114
        xpos 666 ypos 521
        vbox:
            xalign -0.01
            textbutton "Буфер обмена" style "ros_start_menu_submenu_services" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_services_idle" action NullAction()
            add "clipboard_shortcut":
                xpos 6 ypos -12
            textbutton "Диспетчер задач" style "ros_start_menu_submenu_services" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_services_idle" action NullAction():
                ypos -12
            add "task_manager_shortcut":
                xpos 6 ypos -24
            textbutton "Переключатель раскладки клавиатуры" style "ros_start_menu_submenu_services" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_services_idle" action NullAction():
                ypos -24
            add "layout_switcher_shortcut":
                xpos 6 ypos -36
            textbutton "Редактор реестра" style "ros_start_menu_submenu_services" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_services_idle" action NullAction():
                ypos -36
            add "registry_editor_shortcut":
                xpos 6 ypos -48
            textbutton "Средство диагностики ReactX" style "ros_start_menu_submenu_services" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_services_idle" action NullAction():
                ypos -48
            add "rxdiag_shortcut":
                xpos 6 ypos -60
            textbutton "Таблица символов" style "ros_start_menu_submenu_services" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_services_idle" action NullAction():
                ypos -60
            add "charmap_shortcut":
                xpos 6 ypos -72
# Программы: Стандартные - Специальные возможности
screen ros_start_menu_accessibility_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 217 ysize 60
        xpos 666 ypos 539
        vbox:
            xalign -0.01
            textbutton "Диспетчер служебных программ" style "ros_start_menu_submenu_accessibility" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_accessibility_idle" action NullAction()
            add "service_manager_shortcut":
                xpos 6 ypos -12
            textbutton "Экранная клавиатура" style "ros_start_menu_submenu_accessibility" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_accessibility_idle" action NullAction():
                ypos -12
            add "osk_shortcut":
                xpos 6 ypos -24
            textbutton "Экранная лупа" style "ros_start_menu_submenu_accessibility" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_accessibility_idle" action NullAction():
                ypos -24
            add "magnify_shortcut":
                xpos 6 ypos -36

# Документы
screen ros_start_menu_documents_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 131 ysize 68
        xpos 264 ypos 459
        vbox:
            xalign -0.01
            textbutton "Мои документы" style "ros_start_menu_submenu_documents" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_documents_idle" action [
                SetVariable("start_menu_opened", False),
                Hide(screen="ros_start_menu_documents_frame"),
                Show(screen="ros_explorer", folder="docs")]
            add "gui/desktop/menu_icons/submenu/documents.png":
                xpos 6 ypos -12
            textbutton "Мои рисунки" style "ros_start_menu_submenu_documents" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_documents_idle" action [
                SetVariable("start_menu_opened", False),
                Hide(screen="ros_start_menu_documents_frame"),
                Show(screen="ros_explorer", folder="pictures")]:
                ypos -12
            add "gui/desktop/menu_icons/submenu/pictures.png":
                xpos 6 ypos -24
            add "gui/desktop/start_menu_separator.png":
                xpos 6 ypos -20
            textbutton "(пусто)" style "ros_start_menu_submenu_documents" text_style "ros_start_menu_submenu_text":
                ypos -19

# Настройка
screen ros_start_menu_settings_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 194 ysize 86
        xpos 264 ypos 490
        vbox:
            xalign -0.01
            textbutton "Панель управления" style "ros_start_menu_submenu_settings" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_settings_idle" action NullAction()
            add "gui/desktop/menu_icons/submenu/control_panel.png":
                xpos 6 ypos -12
            add "gui/desktop/start_menu_separator.png":
                xsize 180 xpos 6 ypos -8
            textbutton "Сетевые подключения" style "ros_start_menu_submenu_settings" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_settings_idle" action NullAction():
                ypos -6
            add "gui/desktop/menu_icons/submenu/network.png":
                xpos 6 ypos -19
            textbutton "Принтеры и факсы" style "ros_start_menu_submenu_settings" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_settings_idle" action NullAction():
                ypos -19
            add "gui/desktop/menu_icons/submenu/printers_and_faxes.png":
                xpos 6 ypos -31
            textbutton "Панель задач и меню \"Пуск\"" style "ros_start_menu_submenu_settings" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_settings_idle" action NullAction():
                ypos -31
            add "gui/desktop/menu_icons/submenu/start_menu.png":
                xpos 6 ypos -44

# Меню "Пуск" (современный вариант)
screen ros_start_menu_new():
    frame:
        style "ros_start_menu_new"
        xsize 380 ysize 444
        xpos 4 ypos 253
        vbox:
            text "Administrator" style "ros_start_menu_new_username"
        vbox:
            xpos 9 ypos 44
            textbutton "(пусто)" style "ros_start_menu_new_entry" text_style "ros_start_menu_new_entry_text"
            textbutton "Все программы {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_new_entry" text_style "ros_start_menu_new_entry_text" focus_mask "ros_start_menu_new_entry_idle" hovered [
                Hide(screen="ros_start_menu_new_recent_docs"),
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame"),
                Show(screen="ros_start_menu_new_all_programs")] action NullAction():
                ypos 320
        vbox:
            xpos 195 ypos 44
            textbutton "Мои документы" style "ros_start_menu_new_entry" text_style "ros_start_menu_new_entry_title_text" focus_mask "ros_start_menu_new_entry_idle" hovered [
                Hide(screen="ros_start_menu_new_recent_docs"),
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame"),
                Hide(screen="ros_start_menu_new_all_programs")] action [
                SetVariable("start_menu_opened", False),
                Show(screen="ros_explorer", folder="docs")]
            add "gui/desktop/desktop_icons/documents.png":
                xpos 2 ypos -13
            textbutton "Недавние документы {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_new_entry" text_style "ros_start_menu_new_entry_title_text" focus_mask "ros_start_menu_new_entry_idle" hovered [
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame"),
                Hide(screen="ros_start_menu_new_all_programs"),
                Show("ros_start_menu_new_recent_docs")] action NullAction():
                ypos -14
            add "gui/desktop/desktop_icons/recent_docs.png":
                xpos 2 ypos -29
            textbutton "Мои рисунки" style "ros_start_menu_new_entry" text_style "ros_start_menu_new_entry_title_text" focus_mask "ros_start_menu_new_entry_idle" hovered [
                Hide(screen="ros_start_menu_new_recent_docs"),
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame"),
                Hide(screen="ros_start_menu_new_all_programs")] action [
                SetVariable("start_menu_opened", False),
                Show(screen="ros_explorer", folder="pictures")]:
                ypos -28
            add "gui/desktop/desktop_icons/pictures.png":
                xpos 2 ypos -42
            textbutton "Моя музыка" style "ros_start_menu_new_entry" text_style "ros_start_menu_new_entry_title_text" focus_mask "ros_start_menu_new_entry_idle" hovered [
                Hide(screen="ros_start_menu_new_recent_docs"),
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame"),
                Hide(screen="ros_start_menu_new_all_programs")] action NullAction():
                ypos -41
            add "gui/desktop/desktop_icons/music.png":
                xpos 2 ypos -55
            textbutton "Мой компьютер" style "ros_start_menu_new_entry" text_style "ros_start_menu_new_entry_title_text" focus_mask "ros_start_menu_new_entry_idle" hovered [
                Hide(screen="ros_start_menu_new_recent_docs"),
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame"),
                Hide(screen="ros_start_menu_new_all_programs")] action [
                SetVariable("start_menu_opened", False),
                Show(screen="ros_explorer")]:
                ypos -53
            add "gui/desktop/desktop_icons/this_pc.png":
                xpos 2 ypos -66
            textbutton "Панель управления" style "ros_start_menu_new_entry" text_style "ros_start_menu_new_entry_text" focus_mask "ros_start_menu_new_entry_idle" hovered [
                Hide(screen="ros_start_menu_new_recent_docs"),
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame"),
                Hide(screen="ros_start_menu_new_all_programs")] action [
                SetVariable("start_menu_opened", False),
                Show(screen="ros_explorer", folder="control_panel")]:
                ypos -62
            add "gui/desktop/desktop_icons/control_panel.png":
                xpos 2 ypos -78
            textbutton "Выбор программ по\nумолчанию" style "ros_start_menu_new_entry" text_style "ros_start_menu_new_entry_text_two_rows" focus_mask "ros_start_menu_new_entry_idle" hovered [
                Hide(screen="ros_start_menu_new_recent_docs"),
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame"),
                Hide(screen="ros_start_menu_new_all_programs")] action NullAction():
                ypos -76
            add "gui/desktop/desktop_icons/favorites.png":
                xpos 2 ypos -106
            textbutton "Принтеры и факсы" style "ros_start_menu_new_entry" text_style "ros_start_menu_new_entry_text" focus_mask "ros_start_menu_new_entry_idle" hovered [
                Hide(screen="ros_start_menu_new_recent_docs"),
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame"),
                Hide(screen="ros_start_menu_new_all_programs")] action NullAction():
                ypos -105
            add "gui/desktop/desktop_icons/printers_and_faxes.png":
                xpos 2 ypos -121
            textbutton "Справка и поддержка" style "ros_start_menu_new_entry" text_style "ros_start_menu_new_entry_text" focus_mask "ros_start_menu_new_entry_idle" hovered [
                Hide(screen="ros_start_menu_new_recent_docs"),
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame"),
                Hide(screen="ros_start_menu_new_all_programs")] action NullAction():
                ypos -116
            add "gui/desktop/desktop_icons/help_and_support.png":
                xpos 2 ypos -131
            textbutton "Поиск" style "ros_start_menu_new_entry" text_style "ros_start_menu_new_entry_text" focus_mask "ros_start_menu_new_entry_idle" hovered [
                Hide(screen="ros_start_menu_new_recent_docs"),
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame"),
                Hide(screen="ros_start_menu_new_all_programs")] action NullAction():
                ypos -130
            add "gui/desktop/desktop_icons/search.png":
                xpos 2 ypos -144
            textbutton "Выполнить..." style "ros_start_menu_new_entry" text_style "ros_start_menu_new_entry_text" focus_mask "ros_start_menu_new_entry_idle" hovered [
                Hide(screen="ros_start_menu_new_recent_docs"),
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame"),
                Hide(screen="ros_start_menu_new_all_programs")] action NullAction():
                ypos -145
            add "gui/desktop/desktop_icons/run.png":
                xpos 2 ypos -160
        hbox:
            xpos 138 ypos 410
            spacing 5
            textbutton "Выход из системы" style "ros_start_menu_new_logoff" text_style "ros_start_menu_new_logoff_text" focus_mask "ros_start_menu_new_logoff_idle" hovered [
                Hide(screen="ros_start_menu_new_recent_docs"),
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame"),
                Hide(screen="ros_start_menu_new_all_programs")] action [
                SetVariable("start_menu_opened", False),
                Show(screen="ros_logoff_frame")]
            add "gui/desktop/desktop_icons/logoff.png":
                xpos -97 ypos -1
            textbutton "Выключение" style "ros_start_menu_new_shutdown" text_style "ros_start_menu_new_shutdown_text" focus_mask "ros_start_menu_new_shutdown_idle" hovered [
                Hide(screen="ros_start_menu_new_recent_docs"),
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame"),
                Hide(screen="ros_start_menu_new_all_programs")] action [
                SetVariable("start_menu_opened", False),
                Show(screen="ros_shutdown_frame")]
            add "gui/desktop/desktop_icons/shutdown.png":
                xpos -68 ypos -1
# Все программы
screen ros_start_menu_new_all_programs():
    frame:
        style "ros_start_menu_frame"
        xsize 214 ysize 133
        xpos 188 ypos 528
        vbox:
            xalign -0.01
            textbutton "Автозагрузка                                 {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_submenu" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_idle" hovered [
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Show(screen="ros_start_menu_new_autostart_frame")] action NullAction()
            add "gui/desktop/menu_icons/submenu/folder.png":
                xpos 6 ypos -12
            textbutton "Администрирование                      {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_submenu" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_idle" hovered [
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame"),
                Show(screen="ros_start_menu_new_administration_frame")] action NullAction():
                ypos -12
            add "gui/desktop/menu_icons/submenu/folder.png":
                xpos 6 ypos -24
            textbutton "Игры                                               {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_submenu" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_idle" hovered [
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame"),
                Show(screen="ros_start_menu_new_games_frame")] action NullAction():
                ypos -24
            add "gui/desktop/menu_icons/submenu/programs.png":
                xpos 6 ypos -36
            textbutton "Стандартные                                {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_submenu" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_idle" hovered [
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Show(screen="ros_start_menu_new_system_tools_frame")] action NullAction():
                ypos -36
            add "gui/desktop/menu_icons/submenu/programs.png":
                xpos 6 ypos -48
            textbutton "Wine Internet Explorer" style "ros_start_menu_submenu" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_idle" hovered [
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame")] action NullAction():
                ypos -48
            add "iexplore_shortcut":
                xpos 6 ypos -60
            textbutton "Менеджер приложений ReactOS" style "ros_start_menu_submenu" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_idle" hovered [
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame")] action NullAction():
                ypos -60
            add "app_manager_shortcut":
                xpos 6 ypos -72
            textbutton "Проводник ReactOS" style "ros_start_menu_submenu" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_idle" hovered [
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_autostart_frame"),
                Hide(screen="ros_start_menu_new_administration_frame"),
                Hide(screen="ros_start_menu_new_games_frame"),
                Hide(screen="ros_start_menu_new_system_tools_frame")] action [
                    SetVariable("start_menu_opened", False),
                    Hide(screen="ros_start_menu_new_all_programs"),
                    Show(screen="ros_explorer")]:
                ypos -72
            add "explorer_shortcut":
                xpos 6 ypos -84
# Все программы: Автозагрузка
screen ros_start_menu_new_autostart_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 88 ysize 24
        xpos 401 ypos 528
        vbox:
            xalign -0.01
            textbutton "(пусто)" style "ros_start_menu_submenu" text_style "ros_start_menu_submenu_text"
# Все программы: Администрирование
screen ros_start_menu_new_administration_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 159 ysize 78
        xpos 401 ypos 550
        vbox:
            xalign -0.01
            textbutton "Диспетчер служб" style "ros_start_menu_submenu_administration" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_administration_idle" action NullAction()
            add "services_shortcut":
                xpos 6 ypos -12
            textbutton "Диспетчер устройств" style "ros_start_menu_submenu_administration" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_administration_idle" action NullAction():
                ypos -12
            add "device_manager_shortcut":
                xpos 6 ypos -24
            textbutton "Параметры системы" style "ros_start_menu_submenu_administration" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_administration_idle" action NullAction():
                ypos -24
            add "system_settings_shortcut":
                xpos 6 ypos -36
            textbutton "Просмотр событий" style "ros_start_menu_submenu_administration" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_administration_idle" action NullAction():
                ypos -36
            add "event_viewer_shortcut":
                xpos 6 ypos -48
# Все программы: Игры
screen ros_start_menu_new_games_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 138 ysize 60
        xpos 401 ypos 568
        vbox:
            xalign -0.01
            textbutton "Пасьянс \"Косынка\"" style "ros_start_menu_submenu_games" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_games_idle" action NullAction()
            add "solitaire_shortcut":
                xpos 6 ypos -12
            textbutton "Пасьянс \"Паук\"" style "ros_start_menu_submenu_games" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_games_idle" action NullAction():
                ypos -12
            add "spider_shortcut":
                xpos 6 ypos -24
            textbutton "Сапёр" style "ros_start_menu_submenu_games" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_games_idle" action NullAction():
                ypos -24
            add "minesweeper_shortcut":
                xpos 6 ypos -36
# Все программы: Стандартные
screen ros_start_menu_new_system_tools_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 190 ysize 168
        xpos 401 ypos 436
        vbox:
            xalign -0.01
            textbutton "Развлечения                          {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Show(screen="ros_start_menu_new_entertainment_frame")] action NullAction()
            add "gui/desktop/menu_icons/submenu/programs.png":
                xpos 6 ypos -12
            textbutton "Связь                                      {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Show(screen="ros_start_menu_new_communications_frame")] action NullAction():
                ypos -12
            add "gui/desktop/menu_icons/submenu/programs.png":
                xpos 6 ypos -24
            textbutton "Служебные                             {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame"),
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Show(screen="ros_start_menu_new_services_frame")] action NullAction():
                ypos -24
            add "gui/desktop/menu_icons/submenu/programs.png":
                xpos 6 ypos -36
            textbutton "Специальные возможности  {font=gui/font/arial.ttf}►{/font}" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Show(screen="ros_start_menu_new_accessibility_frame")] action NullAction():
                ypos -36
            add "gui/desktop/menu_icons/submenu/programs.png":
                xpos 6 ypos -48
            textbutton "Paint" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame")] action NullAction():
                ypos -48
            add "paint_shortcut":
                xpos 6 ypos -60
            textbutton "WordPad" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame")] action NullAction():
                ypos -60
            add "wordpad_shortcut":
                xpos 6 ypos -72
            textbutton "Блокнот" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame")] action [
                    SetVariable("start_menu_opened", False),
                    Hide(screen="ros_start_menu_new_all_programs"),
                    Hide(screen="ros_start_menu_new_system_tools_frame"),
                    Show(screen="ros_notepad")]:
                ypos -72
            add "notepad_shortcut":
                xpos 6 ypos -84
            textbutton "Калькулятор" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame")] action NullAction():
                ypos -84
            add "calc_shortcut":
                xpos 6 ypos -96
            textbutton "Командная строка" style "ros_start_menu_submenu_system_tools" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_system_tools_idle" hovered [
                Hide(screen="ros_start_menu_new_entertainment_frame"),
                Hide(screen="ros_start_menu_new_communications_frame"),
                Hide(screen="ros_start_menu_new_services_frame"),
                Hide(screen="ros_start_menu_new_accessibility_frame")] action NullAction():
                ypos -96
            add "cmd_shortcut":
                xpos 6 ypos -108
# Все программы: Стандартные - Развлечения
screen ros_start_menu_new_entertainment_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 131 ysize 60
        xpos 590 ypos 436
        vbox:
            xalign -0.01
            textbutton "Громкость" style "ros_start_menu_submenu_entertainment" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_entertainment_idle" action NullAction()
            add "volume_shortcut":
                xpos 6 ypos -12
            textbutton "Звукозапись" style "ros_start_menu_submenu_entertainment" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_entertainment_idle" action NullAction():
                ypos -12
            add "recorder_shortcut":
                xpos 6 ypos -24
            textbutton "Проигрыватель" style "ros_start_menu_submenu_entertainment" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_entertainment_idle" action NullAction():
                ypos -24
            add "media_player_shortcut":
                xpos 6 ypos -36
# Все программы: Стандартные - Связь
screen ros_start_menu_new_communications_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 275 ysize 24
        xpos 590 ypos 455
        vbox:
            xalign -0.01
            textbutton "Подключение к удалённому рабочему столу" style "ros_start_menu_submenu_communications" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_communications_idle" action NullAction()
            add "rdp_shortcut":
                xpos 6 ypos -14
# Все программы: Стандартные - Служебные
screen ros_start_menu_new_services_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 251 ysize 114
        xpos 590 ypos 476
        vbox:
            xalign -0.01
            textbutton "Буфер обмена" style "ros_start_menu_submenu_services" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_services_idle" action NullAction()
            add "clipboard_shortcut":
                xpos 6 ypos -12
            textbutton "Диспетчер задач" style "ros_start_menu_submenu_services" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_services_idle" action NullAction():
                ypos -12
            add "task_manager_shortcut":
                xpos 6 ypos -24
            textbutton "Переключатель раскладки клавиатуры" style "ros_start_menu_submenu_services" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_services_idle" action NullAction():
                ypos -24
            add "layout_switcher_shortcut":
                xpos 6 ypos -36
            textbutton "Редактор реестра" style "ros_start_menu_submenu_services" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_services_idle" action NullAction():
                ypos -36
            add "registry_editor_shortcut":
                xpos 6 ypos -48
            textbutton "Средство диагностики ReactX" style "ros_start_menu_submenu_services" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_services_idle" action NullAction():
                ypos -48
            add "rxdiag_shortcut":
                xpos 6 ypos -60
            textbutton "Таблица символов" style "ros_start_menu_submenu_services" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_services_idle" action NullAction():
                ypos -60
            add "charmap_shortcut":
                xpos 6 ypos -72
# Все программы: Стандартные - Специальные возможности
screen ros_start_menu_new_accessibility_frame():
    frame:
        style "ros_start_menu_frame"
        xsize 217 ysize 60
        xpos 590 ypos 494
        vbox:
            xalign -0.01
            textbutton "Диспетчер служебных программ" style "ros_start_menu_submenu_accessibility" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_accessibility_idle" action NullAction()
            add "service_manager_shortcut":
                xpos 6 ypos -12
            textbutton "Экранная клавиатура" style "ros_start_menu_submenu_accessibility" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_accessibility_idle" action NullAction():
                ypos -12
            add "osk_shortcut":
                xpos 6 ypos -24
            textbutton "Экранная лупа" style "ros_start_menu_submenu_accessibility" text_style "ros_start_menu_submenu_text" focus_mask "ros_start_menu_submenu_accessibility_idle" action NullAction():
                ypos -24
            add "magnify_shortcut":
                xpos 6 ypos -36
# Недавние документы
screen ros_start_menu_new_recent_docs():
    frame:
        style "ros_start_menu_frame"
        xsize 88 ysize 24
        xpos 380 ypos 329
        vbox:
            xalign -0.01
            textbutton "(пусто)" style "ros_start_menu_submenu" text_style "ros_start_menu_submenu_text"

# Иконки
screen ros_desktop_icons():
    vbox:
        xpos 20 ypos 12
        spacing 20
        vbox:
            imagebutton auto "desk_recycle_bin_%s" mouse "link" action Show(screen="ros_explorer", folder="recycle_bin"):
                xpos 4
            text "Корзина" style "ros_desktop_icon_text"
        vbox:
            imagebutton auto "desk_documents_%s" mouse "link" action Show(screen="ros_explorer", folder="docs"):
                xpos 4
            text "Мои\nдокументы" style "ros_desktop_icon_text":
                xpos -7
        vbox:
            imagebutton auto "desk_this_pc_%s" mouse "link" action Show(screen="ros_explorer") alternate [
                Hide(screen="ros_taskbar_context_menu"),
                Hide(screen="ros_desktop_context_menu"),
                Show(screen="ros_desktop_context_menu_this_pc")]:
                xpos 5
            text "Мой\nкомпьютер" style "ros_desktop_icon_text":
                xpos -7
        vbox:
            imagebutton auto "desk_network_%s" mouse "link" action Show(screen="ros_explorer", folder="network"):
                xpos 4
            text "Сетевое\nокружение" style "ros_desktop_icon_text":
                xpos -7
        vbox:
            imagebutton auto "desk_command_prompt_shortcut_%s" mouse "link" action Show(screen="ros_command_prompt"):
                xpos 4
            text "Командная\nстрока" style "ros_desktop_icon_text":
                xpos -7
        vbox:
            imagebutton auto "desk_app_manager_shortcut_%s" mouse "link" action Show(screen="ros_app_manager"):
                xpos 4
            text "Менеджер\nприложений" style "ros_desktop_icon_text":
                xpos -10
        vbox:
            imagebutton auto "desk_readme_shortcut_%s" mouse "link" action Show(screen="ros_notepad", file="readme.txt"):
                xpos 4
            text "Прочти\nменя" style "ros_desktop_icon_text":
                xpos 2

# Область для триггера контекстного меню Рабочего стола
screen ros_desktop_context_menu_trigger():
    imagebutton idle "gui/desktop/desktop_trigger_frame.png" focus_mask "gui/desktop/desktop_trigger_frame_focus_mask.png" action NullAction() alternate [
        SetVariable("sort_entry", False),
        SetVariable("create_entry", False),
        SetVariable("toolbars_entry", False),
        Hide(screen="ros_taskbar_context_menu"),
        Hide(screen="ros_desktop_context_menu_this_pc"),
        Show(screen="ros_desktop_context_menu")]

# Область для триггера контекстного меню Панели задач
screen ros_desktop_taskbar_context_menu_trigger():
    imagebutton idle "gui/desktop/desktop_trigger_frame.png" focus_mask "gui/desktop/taskbar_trigger_frame_focus_mask.png" action NullAction() alternate [
        SetVariable("sort_entry", False),
        SetVariable("create_entry", False),
        SetVariable("toolbars_entry", False),
        Hide(screen="ros_desktop_context_menu"),
        Hide(screen="ros_desktop_context_menu_this_pc"),
        Show(screen="ros_taskbar_context_menu")]

# Контекстное меню: Рабочий стол
screen ros_desktop_context_menu():
    default c_menu_xpos = renpy.get_mouse_pos()[0]
    default c_menu_ypos = renpy.get_mouse_pos()[1]
    default hovered_button = False
    if not hovered_button:
        key "mouseup_1" action [SetVariable("sort_entry", False), SetVariable("create_entry", False), Hide("ros_desktop_context_menu")]
    frame:
        style "ros_desktop_context_menu"
        xsize 139 ysize 161
        xpos c_menu_xpos ypos c_menu_ypos
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Упорядочить значки {font=gui/font/arial.ttf}►{/font}" style "ros_context_menu" text_style "ros_context_menu_text" hovered [
                SetVariable("sort_entry", True),
                SetVariable("create_entry", False),
                SetVariable("hovered_button", True)] unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_idle" action NullAction()
            textbutton "Выровнять значки" style "ros_context_menu" text_style "ros_context_menu_text" hovered [
                SetVariable("sort_entry", False),
                SetVariable("create_entry", False),
                SetVariable("hovered_button", True)] unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_idle" action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" ypos 2
            null height 1
            textbutton "Обновить" style "ros_context_menu" text_style "ros_context_menu_text" hovered [
                SetVariable("sort_entry", False),
                SetVariable("create_entry", False),
                SetVariable("hovered_button", True)] unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_idle" action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" ypos 2
            null height 1
            textbutton "Вставить" style "ros_context_menu" text_style "ros_context_menu_text" focus_mask "ros_context_menu_idle"
            textbutton "Вставить ярлык" style "ros_context_menu" text_style "ros_context_menu_text" focus_mask "ros_context_menu_idle"
            null height 1
            add "gui/desktop/context_menu_separator.png" ypos 2
            null height 1
            textbutton "Создать                     {font=gui/font/arial.ttf}►{/font}" style "ros_context_menu" text_style "ros_context_menu_text" hovered [
                SetVariable("sort_entry", False),
                SetVariable("create_entry", True),
                SetVariable("hovered_button", True)] unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_idle" action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" ypos 2
            null height 1
            textbutton "Свойства" style "ros_context_menu" text_style "ros_context_menu_text" hovered [
                SetVariable("sort_entry", False),
                SetVariable("create_entry", False),
                SetVariable("hovered_button", True)] unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_idle" action [
                    Hide("ros_desktop_context_menu"),
                    Show(screen="ros_properties_screen")]
        if sort_entry:
            hbox:
                xpos 138
                use ros_desktop_context_menu_sort_by
        elif create_entry:
            hbox:
                xpos 138 ypos 111
                use ros_desktop_context_menu_create
    key "K_ESCAPE" action [SetVariable("sort_entry", False), SetVariable("create_entry", False), Hide("ros_desktop_context_menu")]
screen ros_desktop_context_menu_sort_by():
    frame:
        style "ros_desktop_context_menu"
        xsize 113 ysize 129
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Название" style "ros_context_menu_sort_by" text_style "ros_context_menu_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_sort_by_idle" action NullAction()
            textbutton "Комментарии" style "ros_context_menu_sort_by" text_style "ros_context_menu_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_sort_by_idle" action NullAction()
            textbutton "Тип" style "ros_context_menu_sort_by" text_style "ros_context_menu_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_sort_by_idle" action NullAction()
            textbutton "Размер" style "ros_context_menu_sort_by" text_style "ros_context_menu_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_sort_by_idle" action NullAction()
            textbutton "Изменён" style "ros_context_menu_sort_by" text_style "ros_context_menu_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_sort_by_idle" action NullAction()
            textbutton "Атрибуты" style "ros_context_menu_sort_by" text_style "ros_context_menu_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_sort_by_idle" action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 105 ypos 2
            null height 1
            textbutton "Автоматически" style "ros_context_menu_sort_by" text_style "ros_context_menu_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_sort_by_idle" action NullAction()
screen ros_desktop_context_menu_create():
    frame:
        style "ros_desktop_context_menu"
        xsize 168 ysize 98
        vbox:
            xpos 3 ypos 3
            frame:
                style "ros_context_menu_create"
                textbutton "Папку" style "ros_context_menu_create" text_style "ros_context_menu_create_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_create_idle" action NullAction()
                add "gui/desktop/menu_icons/submenu/folder.png" xpos 2 ypos 1
                textbutton "Ярлык" style "ros_context_menu_create" text_style "ros_context_menu_create_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_create_idle" ypos 17 action NullAction()
                add "gui/desktop/menu_icons/submenu/shortcut.png" xpos 2 ypos 16
                add "gui/desktop/context_menu_separator.png" xsize 158 xpos 2 ypos 36
                textbutton "Точечный рисунок" style "ros_context_menu_create" text_style "ros_context_menu_create_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_create_idle" ypos 40 action NullAction()
                add "gui/desktop/menu_icons/submenu/bitmap.png" xpos 2 ypos 40
                textbutton "Файл RTF" style "ros_context_menu_create" text_style "ros_context_menu_create_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_create_idle" ypos 58 action NullAction()
                add "gui/desktop/menu_icons/submenu/rtf_file.png" xpos 2 ypos 58
                textbutton "Текстовый документ" style "ros_context_menu_create" text_style "ros_context_menu_create_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_create_idle" ypos 75 action NullAction()
                add "gui/desktop/menu_icons/submenu/text.png" xpos 2 ypos 75
# Контекстное меню: Иконка "Мой компьютер"
screen ros_desktop_context_menu_this_pc():
    default hovered_button = False
    if not hovered_button:
        key "mouseup_1" action Hide("ros_desktop_context_menu_this_pc")
    frame:
        style "ros_desktop_context_menu"
        xsize 131 ysize 154
        xpos 40 ypos 180
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Открыть" style "ros_context_menu_this_pc" text_style "ros_context_menu_title" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_this_pc_idle" action [Hide("ros_desktop_context_menu_this_pc"), Show(screen="ros_explorer")]
            textbutton "Поиск" style "ros_context_menu_this_pc" text_style "ros_context_menu_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_this_pc_idle" action NullAction()
            textbutton "Управление" style "ros_context_menu_this_pc" text_style "ros_context_menu_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_this_pc_idle" action NullAction()
            textbutton "Открыть в дереве" style "ros_context_menu_this_pc" text_style "ros_context_menu_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_this_pc_idle" action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 123 ypos 2
            null height 1
            textbutton "Создать ярлык" style "ros_context_menu_this_pc" text_style "ros_context_menu_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_this_pc_idle" action NullAction()
            textbutton "Удалить" style "ros_context_menu_this_pc" text_style "ros_context_menu_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_this_pc_idle" action NullAction()
            textbutton "Переименовать" style "ros_context_menu_this_pc" text_style "ros_context_menu_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_this_pc_idle" action NullAction()
            null height 1
            add "gui/desktop/context_menu_separator.png" xsize 123 ypos 2
            null height 1
            textbutton "Свойства" style "ros_context_menu_this_pc" text_style "ros_context_menu_text" hovered SetVariable("hovered_button", True) unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_this_pc_idle" action [
                Hide("ros_desktop_context_menu_this_pc"),
                Show(screen="ros_properties_system")]
    key "K_ESCAPE" action Hide("ros_desktop_context_menu_this_pc")
# Контекстное меню: Панель задач
screen ros_taskbar_context_menu():
    default c_menu_xpos = renpy.get_mouse_pos()[0]
    default c_menu_ypos = renpy.get_mouse_pos()[1] - 197
    default hovered_button = False
    if not hovered_button:
        key "mouseup_1" action [SetVariable("toolbars_entry", False), Hide("ros_taskbar_context_menu")]
    frame:
        style "ros_desktop_context_menu"
        xsize 212 ysize 197
        xpos c_menu_xpos ypos c_menu_ypos
        vbox:
            xpos 3 ypos 3
            spacing 2
            textbutton "Панели инструментов                        {font=gui/font/arial.ttf}►{/font}" style "ros_context_menu_taskbar" text_style "ros_context_menu_text" hovered [
                SetVariable("toolbars_entry", True),
                SetVariable("hovered_button", True)] unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_taskbar_idle" action NullAction()
            textbutton "Настройка даты и времени" style "ros_context_menu_taskbar" text_style "ros_context_menu_text" hovered [
                SetVariable("toolbars_entry", False),
                SetVariable("hovered_button", True)] unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_taskbar_idle" action NullAction()
            textbutton "Настройка уведомлений..." style "ros_context_menu_taskbar" text_style "ros_context_menu_text" hovered [
                SetVariable("toolbars_entry", False),
                SetVariable("hovered_button", True)] unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_taskbar_idle" action NullAction()
            add "gui/desktop/context_menu_separator.png" xsize 204 ypos 2
            textbutton "Расположить окна каскадом" style "ros_context_menu_taskbar" text_style "ros_context_menu_text"
            textbutton "Расположить окна по горизонтали" style "ros_context_menu_taskbar" text_style "ros_context_menu_text"
            textbutton "Расположить окна по вертикали" style "ros_context_menu_taskbar" text_style "ros_context_menu_text"
            textbutton "Показать рабочий стол" style "ros_context_menu_taskbar" text_style "ros_context_menu_text" hovered [
                SetVariable("toolbars_entry", False),
                SetVariable("hovered_button", True)] unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_taskbar_idle" action NullAction()
            textbutton "Отменить" style "ros_context_menu_taskbar" text_style "ros_context_menu_text" hovered [
                SetVariable("toolbars_entry", False),
                SetVariable("hovered_button", True)] unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_taskbar_idle" action NullAction()
            add "gui/desktop/context_menu_separator.png" xsize 204 ypos 2
            textbutton "Диспетчер задач" style "ros_context_menu_taskbar" text_style "ros_context_menu_text" hovered [
                SetVariable("toolbars_entry", False),
                SetVariable("hovered_button", True)] unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_taskbar_idle" action NullAction()
            add "gui/desktop/context_menu_separator.png" xsize 204 ypos 2
            textbutton "Закрепить панель задач" style "ros_context_menu_taskbar" text_style "ros_context_menu_text" hovered [
                SetVariable("toolbars_entry", False),
                SetVariable("hovered_button", True)] unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_taskbar_idle" action NullAction()
            textbutton "Свойства" style "ros_context_menu_taskbar" text_style "ros_context_menu_text" hovered [
                SetVariable("toolbars_entry", False),
                SetVariable("hovered_button", True)] unhovered SetVariable("hovered_button", False) focus_mask "ros_context_menu_taskbar_idle" action [
                    Hide(screen="ros_taskbar_context_menu"),
                    Show(screen="ros_properties_taskbar")]
        if toolbars_entry:
            hbox:
                xpos 210
                use ros_taskbar_context_menu_toolbars
# Подменю контекстного меню Панели задач
screen ros_taskbar_context_menu_toolbars():
    frame:
        style "ros_desktop_context_menu"
        xsize 199 ysize 72
        vbox:
            xpos 3 ypos 3
            style "ros_context_menu_toolbars"
            textbutton "Адрес" style "ros_context_menu_toolbars" text_style "ros_context_menu_text" focus_mask "ros_context_menu_toolbars_idle" action NullAction()
            textbutton "Рабочий стол" style "ros_context_menu_toolbars" text_style "ros_context_menu_text" focus_mask "ros_context_menu_toolbars_idle" action NullAction()
            textbutton "Быстрый запуск" style "ros_context_menu_toolbars" text_style "ros_context_menu_text" focus_mask "ros_context_menu_toolbars_idle" action NullAction()
            null height 2
            add "gui/desktop/context_menu_separator.png" xsize 191 ypos 2
            null height 2
            textbutton "Создать панель инструментов..." style "ros_context_menu_toolbars" text_style "ros_context_menu_text" focus_mask "ros_context_menu_toolbars_idle" action NullAction()

# Выход из системы / Завершение работы
screen ros_logoff_frame():
    modal True
    on "show" action [Function(SetThumbnailFull), FileTakeScreenshot(), Function(SetThumbnailOriginal)]
    add FileCurrentScreenshot():
        matrixcolor SaturationMatrix(0)
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
    add FileCurrentScreenshot():
        matrixcolor SaturationMatrix(0)
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

label ros_desktop:
    $ mouse_visible = True
    scene postinstall
    show corner_text "{font=gui/font/tahomabd.ttf}ReactOS Version [config.version]{/font}\nBuild [ros_build]\nReporting NT 5.2 (Build 3790: Service Pack 2)\nC:\\[ros_install_directory]"
    show screen please_wait("Загружаются персональные настройки...")
    $ renpy.pause(0.5, hard=True)
    hide screen please_wait
    show screen ros_desktop_icons
    show screen ros_taskbar
    show corner_text "{font=gui/font/tahomabd.ttf}ReactOS Version [config.version]{/font}\nBuild [ros_build]\nReporting NT 5.2 (Build 3790: Service Pack 2)\nC:\\[ros_install_directory]":
        yalign 0.95
    $ renpy.pause(hard=True)

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
    $ renpy.quit()

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
    jump ros_boot
# ...
