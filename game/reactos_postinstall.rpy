# Приветствие установщика
screen setup_step1():
    drag:
        drag_name "ros_setup1"
        drag_handle (0, 0, 503, 22)
        xalign 0.5 yalign 0.5
        frame:
            style_prefix "ros_setup1"
            xsize 503 ysize 389
            text "Установка ReactOS" style "ros_setup_header_text"
            add "gui/window/postinstall/install_badge.png":
                xalign -0.15 yalign 2.6
            text "Добро пожаловать в мастер\nустановки ReactOS." style "ros_setup_page_bold_text"
            text "Этот мастер поможет ввести сведения для правильной\nустановки ReactOS и установит её на ваш компьютер." style "ros_setup_page_text"
            text "Нажмите \"Далее\" для продолжения установки." style "ros_setup_page_lower_text"
            hbox:
                pos(195,310)
                textbutton "< Назад" style "ros_setup_button" text_style "ros_setup_button_text"
                null width 33
                textbutton "Далее >" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_2")

# Второй и последующие шаги установщика
screen setup_step2():
    drag:
        drag_name "ros_setup2"
        drag_handle (0, 0, 503, 22)
        xalign 0.5 yalign 0.5
        frame:
            style_prefix "ros_setup2"
            xsize 503 ysize 389
            text "Установка ReactOS" style "ros_setup_header_text"
            add "gui/window/postinstall/ros_logo_large.png":
                xpos 407 ypos -13
            text "Тип продукта" style "ros_setup_description_title"
            text "Вы можете выбрать тип продукта, который изменяет поведение системы." style "ros_setup_description"
            add "gui/window/postinstall/ros_logo_small.png":
                xpos -19 ypos 68
            text "Пожалуйста, укажите тип продукта:" style "ros_setup_description":
                xpos 19 ypos 68
            text "Тип продукта:" style "ros_setup_description":
                xpos -19 ypos 110
            textbutton "Рабочая станция ReactOS" style "ros_setup_dropdown_list" text_style "ros_setup_dropdown_list_text" focus_mask "gui/window/postinstall/dropdown_box_idle.png":
                xpos 120 ypos 106
            add "gui/window/postinstall/frame.png":
                xpos -19 ypos 140
            text "Информация о продукте" style "ros_setup_description":
                xpos -11 ypos 133
            add "gui/window/postinstall/description_box.png":
                xpos 120 ypos 160
            text "Описание:" style "ros_setup_description":
                xpos 1 ypos 159
            text "Система будет распознаваться как рабочая станция.\nПриватные папки \"Мои изображения\", \"Мои\nвидеозаписи\" и \"Моя музыка\" будут находиться в\nпапке \"Мои документы\"." style "ros_setup_description":
                xpos 124 ypos 162
            hbox:
                pos(195,310)
                textbutton "< Назад" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_1_5")
                null width 33
                textbutton "Далее >" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_3")

screen setup_step3():
    drag:
        drag_name "ros_setup2"
        drag_handle (0, 0, 503, 22)
        xalign 0.5 yalign 0.5
        frame:
            style_prefix "ros_setup2"
            xsize 503 ysize 389
            text "Установка ReactOS" style "ros_setup_header_text"
            add "gui/window/postinstall/ros_logo_large.png":
                xpos 407 ypos -13
            text "Подтверждение лицензии" style "ros_setup_description_title"
            text "Информация о разработчиках ReactOS и лицензионное соглашение." style "ros_setup_description"
            text "Разработчики ReactOS и Open Source-проекты, благодаря которым была создана\nReactOS:" style "ros_setup_description":
                xpos -9 ypos 60
            frame:
                style "ros_setup_developers_box"
                viewport:
                    yinitial 0.0
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    side_yfill True
                    vbox:
                        text "Wine - http://www.winehq.org" style "ros_setup_developers_description"
                        text "FreeType - http://www.freetype.org" style "ros_setup_developers_description"
                        text "SYSLINUX - http://syslinux.zytor.com" style "ros_setup_developers_description"
                        text "MinGW - http://www.mingw.org" style "ros_setup_developers_description"
                        text "Bochs - http://bochs.sourceforge.net" style "ros_setup_developers_description"
                        text "QEMU - http://fabrice.bellard.free.fr/qemu" style "ros_setup_developers_description"
                        text "Mesa3D - http://www.mesa3d,org" style "ros_setup_developers_description"
                        text "adns - http://www.gnu.org/software/adns" style "ros_setup_developers_description"
                        text "ICU - http://www.icu-project.org" style "ros_setup_developers_description"
                        text "GraphApp - http://enchantia.com/software/graphapp" style "ros_setup_developers_description"
                        text "Ext2 - http://www.ext2fsd.com" style "ros_setup_developers_description"
                        text "GNU FreeFont - http://savannah.gnu.org/projects/freefont" style "ros_setup_developers_description"
                        text "DejaVu Fonts - http://dejavu.sourceforge.net" style "ros_setup_developers_description"
                        text "Liberation(tm) Fonts - https://fedorahosted.org/liberation-fonts" style "ros_setup_developers_description"
                        text "Btrfs - https://github.com/maharmstone/btrfs" style "ros_setup_developers_description"
                        transclude
            text "ReactOS распространяется под лицензией GPL. Если вы хотите\nиспользовать и распространять её, вы должны соблюдать GPL.\n\nНажмите \"Далее\" для продолжения установки." style "ros_setup_description":
                xpos -9 ypos 232
            textbutton "Лицензия..." style "ros_setup_button" text_style "ros_setup_license_button" focus_mask "gui/window/postinstall/button_idle.png" action Show("ros_setup_license"):
                xpos 338 ypos 232
            hbox:
                pos(195,310)
                textbutton "< Назад" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_2")
                null width 33
                textbutton "Далее >" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_4")

screen ros_setup_license():
    drag:
        drag_name "ros_setup_license"
        drag_handle (0, 0, 506, 21)
        xalign 0.5 yalign 0.5
        frame:
            style_prefix "ros_setup_license"
            xsize 506 ysize 399
            text "Открытое лицензионное соглашение GNU" style "ros_setup_header_text":
                xpos -66
            imagebutton auto "gui/window/common/close_%s.png" action Hide("ros_setup_license"):
                xpos 445 yalign -0.116
            frame:
                style "ros_setup_license_box"
                viewport:
                    yinitial 0.0
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    side_yfill True
                    vbox:
                        text license_text style "ros_setup_developers_description"
                        transclude
            textbutton "ОК" style "ros_setup_button" text_style "ros_setup_license_button_ok" focus_mask "gui/window/postinstall/button_idle.png" action Hide("ros_setup_license"):
                xpos 170 ypos 320

screen setup_step4():
    drag:
        drag_name "ros_setup2"
        drag_handle (0, 0, 503, 22)
        xalign 0.5 yalign 0.5
        frame:
            style_prefix "ros_setup2"
            xsize 503 ysize 389
            text "Установка ReactOS" style "ros_setup_header_text"
            add "gui/window/postinstall/ros_logo_large.png":
                xpos 407 ypos -13
            text "Региональные настройки" style "ros_setup_description_title"
            text "Вы можете настраивать ReactOS для разных регионов и языков." style "ros_setup_description"
            add "gui/window/postinstall/languages_icon.png":
                xpos 4 ypos 66
            text "Язык системы устанавливается и действует во всех приложениях. Можно\nвыбрать систему исчисления, формат чисел и даты.\n\n\n\n\n\nДля изменения языка системы нажмите \"Настроить...\"." style "ros_setup_description":
                xpos 48 ypos 63
            textbutton "Настроить..." style "ros_setup_button" text_style "ros_setup_set_up_button" focus_mask "gui/window/postinstall/button_idle.png" action Show(screen="dialog_placeholder", message="Местозаполнитель: контент появится позже", ok_action=Hide("dialog_placeholder")):
                xpos 347 ypos 155
            text "Выбрав раскладку, вы сможете вводить символы на вашем языке.\n\n\n\nДля изменения раскладки нажмите \"Настроить...\"." style "ros_setup_description":
                xpos 48 ypos 200
            textbutton "Настроить..." style "ros_setup_button" text_style "ros_setup_set_up_button" focus_mask "gui/window/postinstall/button_idle.png" action Show(screen="dialog_placeholder", message="Местозаполнитель: контент появится позже", ok_action=Hide("dialog_placeholder")):
                xpos 347 ypos 251
            hbox:
                pos(195,310)
                textbutton "< Назад" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_3")
                null width 33
                textbutton "Далее >" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_5")

# TODO: Сделать возможность ввода своих данных в соответствующие поля
screen setup_step5():
    drag:
        drag_name "ros_setup2"
        drag_handle (0, 0, 503, 22)
        xalign 0.5 yalign 0.5
        frame:
            style_prefix "ros_setup2"
            xsize 503 ysize 389
            text "Установка ReactOS" style "ros_setup_header_text"
            add "gui/window/postinstall/ros_logo_large.png":
                xpos 407 ypos -13
            text "Персональные данные" style "ros_setup_description_title"
            text "Установка информации о пользователях ReactOS." style "ros_setup_description"
            add "gui/window/postinstall/userinfo_icon.png":
                xpos 4 ypos 66
            text "Введите ваше полное имя и название организации." style "ros_setup_description":
                xpos 48 ypos 63
            text "Имя:" style "ros_setup_description":
                xpos 48 ypos 120
            textbutton "[username]" style "ros_input_field" text_style "ros_input_field_text" focus_mask "gui/window/postinstall/input_field.png":
                xpos 178 ypos 115
            text "Организация:" style "ros_setup_description":
                xpos 48 ypos 150
            textbutton "[organization]" style "ros_input_field" text_style "ros_input_field_text" focus_mask "gui/window/postinstall/input_field.png":
                xpos 178 ypos 145
            hbox:
                pos(195,310)
                textbutton "< Назад" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_4")
                null width 33
                textbutton "Далее >" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_6")

screen setup_step6():
    drag:
        drag_name "ros_setup2"
        drag_handle (0, 0, 503, 22)
        xalign 0.5 yalign 0.5
        frame:
            style_prefix "ros_setup2"
            xsize 503 ysize 389
            text "Установка ReactOS" style "ros_setup_header_text"
            add "gui/window/postinstall/ros_logo_large.png":
                xpos 407 ypos -13
            text "Имя компьютера и пароль администратора" style "ros_setup_description_title"
            text "Вы должны ввести имя и администраторский пароль для вашего\nкомпьютера." style "ros_setup_description"
            add "gui/window/postinstall/home_icon.png":
                xpos 4 ypos 66
            text "Введите имя вашего компьютера (не более 15 символов). Если ваш\nкомпьютер подключён к сети, то его имя должно быть уникальным." style "ros_setup_description":
                xpos 48 ypos 63
            text "Имя компьютера:" style "ros_setup_description":
                xpos 48 ypos 120
            textbutton "[computer_name]" style "ros_input_field" text_style "ros_input_field_text" focus_mask "gui/window/postinstall/input_field.png":
                xpos 196 ypos 115
            add "gui/window/postinstall/users_icon.png":
                xpos 4 ypos 153
            text "При установке будет создан профиль пользователя с именем\nAdministrator. Вы можете использовать этот профиль, если вам нужно\nполучить права администратора.\n\nВведите пароль администратора (не более 127 символов)" style "ros_setup_description":
                xpos 48 ypos 150
            text "Пароль администратора:" style "ros_setup_description":
                xpos 48 ypos 234
            textbutton "[admin_pass]" style "ros_input_field" text_style "ros_input_field_text" focus_mask "gui/window/postinstall/input_field.png":
                xpos 196 ypos 229
            text "Повторите пароль:" style "ros_setup_description":
                xpos 48 ypos 263
            textbutton "[admin_pass2]" style "ros_input_field" text_style "ros_input_field_text" focus_mask "gui/window/postinstall/input_field.png":
                xpos 196 ypos 258
            hbox:
                pos(195,310)
                textbutton "< Назад" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_5")
                null width 33
                textbutton "Далее >" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_7")

# TODO: Сделать дату, время и часовой пояс обновляемыми
screen setup_step7():
    drag:
        drag_name "ros_setup2"
        drag_handle (0, 0, 503, 22)
        xalign 0.5 yalign 0.5
        frame:
            style_prefix "ros_setup2"
            xsize 503 ysize 389
            text "Установка ReactOS" style "ros_setup_header_text"
            add "gui/window/postinstall/ros_logo_large.png":
                xpos 407 ypos -13
            text "Дата и время" style "ros_setup_description_title"
            text "Установите правильные дату и время на вашем компьютере." style "ros_setup_description"
            add "gui/window/postinstall/date_icon.png":
                xpos 4 ypos 66
            text "Дата и время:" style "ros_setup_description":
                xpos 48 ypos 63
            textbutton cur_date + " г." style "ros_setup_date" text_style "ros_setup_date_text" focus_mask "gui/window/postinstall/date_dropdown_box.png":
                xpos 48 ypos 80
            textbutton cur_time style "ros_setup_time" text_style "ros_setup_time_text" focus_mask "gui/window/postinstall/time_adjust_box.png":
                xpos 265 ypos 80
            text "Часовой пояс:" style "ros_setup_description":
                xpos 48 ypos 120
            textbutton cur_tz style "ros_setup_timezone" text_style "ros_setup_timezone_text" focus_mask "gui/window/postinstall/timezone_dropdown_box.png":
                xpos 48 ypos 137
            vbox:
                xpos 48 ypos 265
                xmaximum 1000
                style_prefix "ros_check"
                textbutton "Автоматический переход на летнее время и обратно" action ToggleVariable("daylight_saving_time", True, False)
            hbox:
                pos(195,310)
                textbutton "< Назад" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_6")
                null width 33
                textbutton "Далее >" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_8")

screen setup_step8():
    drag:
        drag_name "ros_setup2"
        drag_handle (0, 0, 503, 22)
        xalign 0.5 yalign 0.5
        frame:
            style_prefix "ros_setup2"
            xsize 503 ysize 389
            text "Установка ReactOS" style "ros_setup_header_text"
            add "gui/window/postinstall/ros_logo_large.png":
                xpos 407 ypos -13
            text "Внешний вид" style "ros_setup_description_title"
            text "Выберите тему, которую вы предпочитаете." style "ros_setup_description"
            frame:
                style "ros_setup_theme_choose_frame"
                xsize 432 ysize 207
                viewport:
                    yinitial 0.0
                    scrollbars "horizontal"
                    mousewheel "horizontal"
                    draggable True
                    side_yfill True
                    hbox:
                        spacing 10
                        vbox:
                            imagebutton idle "gui/window/postinstall/themes_samples/classic.png" action NullAction()
                            text "Классическая" style "ros_setup_theme_choose_text"
                        vbox:
                            imagebutton idle "gui/window/postinstall/themes_samples/lautus.png" action NullAction()
                            text "Тема \"Lautus\"" style "ros_setup_theme_choose_text"
                        vbox:
                            imagebutton idle "gui/window/postinstall/themes_samples/lunar.png" action NullAction()
                            text "Тема \"Lunar\"" style "ros_setup_theme_choose_text"
                        vbox:
                            imagebutton idle "gui/window/postinstall/themes_samples/mizu.png" action NullAction()
                            text "Тема \"Mizu\"" style "ros_setup_theme_choose_text"
                        transclude
            hbox:
                pos(195,310)
                textbutton "< Назад" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_7")
                null width 33
                textbutton "Далее >" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_9")

screen setup_step9():
    drag:
        drag_name "ros_setup2"
        drag_handle (0, 0, 503, 22)
        xalign 0.5 yalign 0.5
        frame:
            style_prefix "ros_setup2"
            xsize 503 ysize 389
            text "Установка ReactOS" style "ros_setup_header_text"
            add "gui/window/postinstall/ros_logo_large.png":
                xpos 407 ypos -13
            text "Настройки сети" style "ros_setup_description_title"
            text "Настройка сетевого программного обеспечения, необходимого для\nсоединения с другими сетями, компьютерами или Интернетом." style "ros_setup_description"
            add "gui/window/postinstall/network_icon.png":
                xpos 4 ypos 66
            text "Выберите режим настройки сети:" style "ros_setup_description":
                xpos 48 ypos 63
            vbox:
                style_prefix "ros_radio"
                xmaximum 1000
                xpos 48 ypos 100
                textbutton "{font=gui/font/tahomabd.ttf}Обычный режим настройки{/font}\nСоздаёт сетевые соединения, используя клиент для сетей ReactOS,\nобщие файлы и принтеры для сетей ReactOS и транспортный\nпротокол TCP/IP с автоматической адресацией." action SetVariable("network_setup_mode", "regular")
                textbutton "{font=gui/font/tahomabd.ttf}Расширенный режим настройки{/font}\nПозволяет вам настроить сетевые компоненты вручную."
            hbox:
                pos(195,310)
                textbutton "< Назад" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_8")
                null width 33
                textbutton "Далее >" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_10")

screen setup_step10():
    drag:
        drag_name "ros_setup2"
        drag_handle (0, 0, 503, 22)
        xalign 0.5 yalign 0.5
        frame:
            style_prefix "ros_setup2"
            xsize 503 ysize 389
            text "Установка ReactOS" style "ros_setup_header_text"
            add "gui/window/postinstall/ros_logo_large.png":
                xpos 407 ypos -13
            text "Рабочая группа или сетевой домен" style "ros_setup_description_title"
            text "Укажите, как будет использоваться компьютер - в составе рабочей группы\nили как часть сетевого домена." style "ros_setup_description"
            text "Вы хотите, чтобы этот компьютер был частью сетевого домена?\n(Вы можете получить необходимую информацию у вашего сетевого\nадминистратора.)" style "ros_setup_description":
                xpos 20 ypos 58
            vbox:
                style_prefix "ros_radio"
                xmaximum 1000
                xpos 20 ypos 118
                textbutton "Нет, этот компьютер находится в рабочей группе." action SetVariable("workgroup", True)
                textbutton "Да, этот компьютер будет частью сетевого домена."
            text "Имя рабочей группы или домена:" style "ros_setup_description":
                xpos 20 ypos 175
            textbutton "[workgroup_name]" style "ros_input_field" text_style "ros_input_field_text" focus_mask "gui/window/postinstall/input_field.png":
                xpos 20 ypos 192
            text "Примечание: Если этот компьютер не надо присоединять к сети, или у вас\nнет прав для присоединения к сетевому домену, или вы не знаете, как к\nнему присоединиться, тогда выберите опцию рабочей группы. Эту опцию\nпотом можно будет изменить." style "ros_setup_description":
                xpos 20 ypos 230
            hbox:
                pos(195,310)
                textbutton "< Назад" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_9")
                null width 33
                textbutton "Далее >" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_11")

screen setup_step11():
    drag:
        drag_name "ros_setup2"
        drag_handle (0, 0, 503, 22)
        xalign 0.5 yalign 0.5
        frame:
            style_prefix "ros_setup2"
            xsize 503 ysize 389
            text "Установка ReactOS" style "ros_setup_header_text"
            add "gui/window/postinstall/ros_logo_large.png":
                xpos 407 ypos -13
            text "Процесс установки" style "ros_setup_description_title"
            text "Установка ReactOS на ваш компьютер." style "ros_setup_description"
            text "Регистрация компонентов..." style "ros_setup_description":
                xpos 20 ypos 58
            text "(мне лень всё перечислять, извините ещё раз...)" style "ros_setup_description":
                xpos 20 ypos 95
            add "gui/window/postinstall/registration_progress.png":
                xpos 20 ypos 170
            add "ros_setup_registration_progress"
            hbox:
                pos(195,310)
                textbutton "< Назад" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png"
                null width 33
                textbutton "Далее >" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png"
    timer 5.0 action Show(screen="setup_step_gecko")

screen setup_step_gecko():
    drag:
        drag_name "ros_setup_gecko"
        drag_handle (0, 0, 396, 22)
        xalign 0.5 yalign 0.5
        frame:
            style "ros_setup_gecko_frame"
            xsize 396 ysize 179
            imagebutton auto "gui/window/common/close_%s.png" action Call("ros_postinstall_12"):
                xpos 336 yalign -0.42
            text "Установщик Wine Gecko" style "ros_setup_header_text":
                xpos -54 ypos -36
            text "ReactOS не может найти пакет Wine Gecko, который необходим для корректной работы приложений с поддержкой HTML. ReactOS может автоматически загрузить и установить его для вас." style "ros_setup_description":
                xpos -24 ypos -6
            hbox:
                pos(171,105)
                textbutton "Отмена" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_12")
                null width 38
                textbutton "Установить" style "ros_setup_button" text_style "ros_setup_button_text_install" focus_mask "gui/window/postinstall/button_idle.png" action [Hide("setup_step_gecko"), Show(screen="setup_step_gecko1")]

screen setup_step_gecko1():
    drag:
        drag_name "ros_setup_gecko"
        drag_handle (0, 0, 396, 22)
        xalign 0.5 yalign 0.5
        frame:
            style "ros_setup_gecko_frame"
            xsize 396 ysize 179
            imagebutton auto "gui/window/common/close_%s.png" action Call("ros_postinstall_12"):
                xpos 336 yalign -0.42
            text "Установщик Wine Gecko" style "ros_setup_header_text":
                xpos -54 ypos -36
            text "Загрузка..." style "ros_setup_description":
                xpos -24 ypos -6
            add "ros_setup_gecko_installing_progress"
            hbox:
                pos(171,105)
                textbutton "Отмена" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_12")
                null width 38
                textbutton "Установить" style "ros_setup_button" text_style "ros_setup_button_text_install" focus_mask "gui/window/postinstall/button_idle.png"
    timer 30.0 action [Hide("setup_step_gecko1"), Show(screen="setup_step_gecko2")]

screen setup_step_gecko2():
    drag:
        drag_name "ros_setup_gecko"
        drag_handle (0, 0, 396, 22)
        xalign 0.5 yalign 0.5
        frame:
            style "ros_setup_gecko_frame"
            xsize 396 ysize 179
            imagebutton auto "gui/window/common/close_%s.png" action Call("ros_postinstall_12"):
                xpos 336 yalign -0.42
            text "Установщик Wine Gecko" style "ros_setup_header_text":
                xpos -54 ypos -36
            text "Установка..." style "ros_setup_description":
                xpos -24 ypos -6
            hbox:
                pos(171,105)
                textbutton "Отмена" style "ros_setup_button" text_style "ros_setup_button_text" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_12")
                null width 38
                textbutton "Установить" style "ros_setup_button" text_style "ros_setup_button_text_install" focus_mask "gui/window/postinstall/button_idle.png"
    timer 5.0 action Call("ros_postinstall_12")

screen setup_step12():
    drag:
        drag_name "ros_setup1"
        drag_handle (0, 0, 503, 22)
        xalign 0.5 yalign 0.5
        frame:
            style_prefix "ros_setup1"
            xsize 503 ysize 389
            text "Завершение установки ReactOS" style "ros_setup_header_text":
                xalign -0.15
            add "gui/window/postinstall/install_badge.png":
                xalign -0.15 yalign 2.6
            text "Завершение мастера установки\nReactOS." style "ros_setup_page_bold_text"
            text "Вы успешно закончили установку ReactOS.\n\nНажмите \"Готово\" для перезагрузки вашего компьютера." style "ros_setup_page_text"
            add "gui/window/postinstall/final_countdown_progress.png":
                xpos 132 ypos 200
            add "ros_setup_final_countdown_progress"
            text "Если CD находится в приводе, нужно извлечь его. Для\nперезагрузки компьютера нажмите \"Готово\"." style "ros_setup_page_lower_text"
            hbox:
                pos(195,310)
                textbutton "< Назад" style "ros_setup_button" text_style "ros_setup_button_text"
                null width 33
                textbutton "Готово" style "ros_setup_button" text_style "ros_setup_button_text_done" focus_mask "gui/window/postinstall/button_idle.png" action Call("ros_postinstall_13")
    timer 16.0 action Call("ros_postinstall_13")

label ros_postinstall:
    $ mouse_visible = True
    scene postinstall
    show corner_text "{font=gui/font/tahomabd.ttf}ReactOS Version [config.version]{/font}\nBuild [ros_build]\nReporting NT 5.2 (Build 3790: Service Pack 2)\nC:\\[ros_install_directory]"
    $ renpy.pause(0.2, hard=True)
    show screen please_wait("Установка оборудования...")
    $ renpy.pause(1.5, hard=True)
    hide screen please_wait
    label ros_postinstall_1_5:
        hide screen setup_step2
        show screen setup_step1
        $ renpy.pause(hard=True)

label ros_postinstall_2:
    hide screen setup_step1
    hide screen setup_step3
    show screen setup_step2
    $ renpy.pause(hard=True)

label ros_postinstall_3:
    hide screen setup_step2
    hide screen setup_step4
    show screen setup_step3
    $ renpy.pause(hard=True)

label ros_postinstall_4:
    hide screen setup_step3
    hide screen setup_step5
    show screen setup_step4
    $ renpy.pause(hard=True)

label ros_postinstall_5:
    hide screen setup_step4
    hide screen setup_step6
    show screen setup_step5
    $ renpy.pause(hard=True)

label ros_postinstall_6:
    hide screen setup_step5
    hide screen setup_step7
    show screen setup_step6
    $ renpy.pause(hard=True)

label ros_postinstall_7:
    hide screen setup_step6
    hide screen setup_step8
    show screen setup_step7
    $ renpy.pause(hard=True)

label ros_postinstall_8:
    hide screen setup_step7
    hide screen setup_step9
    show screen setup_step8
    $ renpy.pause(hard=True)

label ros_postinstall_9:
    hide screen setup_step8
    hide screen setup_step10
    show screen setup_step9
    $ renpy.pause(hard=True)

label ros_postinstall_10:
    if network_setup_mode != "regular":
        show screen dialog_placeholder("Местозаполнитель: контент появится позже", ok_action=Hide("dialog_placeholder"))
    else:
        hide screen setup_step9
        hide screen setup_step11
        show screen setup_step10
        $ renpy.pause(hard=True)

label ros_postinstall_11:
    if not workgroup:
        show screen dialog_placeholder("Местозаполнитель: контент появится позже", ok_action=Hide("dialog_placeholder"))
    else:
        hide screen setup_step10
        show screen setup_step11
        $ renpy.pause(hard=True)

label ros_postinstall_12:
    hide screen setup_step11
    hide screen setup_step_gecko
    hide screen setup_step_gecko1
    hide screen setup_step_gecko2
    show screen setup_step12
    $ renpy.pause(hard=True)

label ros_postinstall_13:
    hide screen setup_step12
    $ renpy.pause(0.2, hard=True)
    show screen please_wait("Перезагрузка...")
    $ renpy.pause(1.5, hard=True)
    scene black
    hide screen please_wait
    $ persistent.provisioned = True
    $ renpy.save_persistent()
    jump ros_boot
