# Экран выбора языка
screen install_lang_choice():
    add "install_lang_choice_field"
    add "install_lang_choice_field_2"
    vbox:
        pos(44,268)
        ysize 23
        textbutton "English (United States)" style "lang_choose" text_style "lang_choose_text" hovered SetVariable("install_lang", "english") action NullAction()
        textbutton "Russian" style "lang_choose" text_style "lang_choose_text" hovered SetVariable("install_lang", "russian") unhovered SetVariable("install_lang", "placeholder") action NullAction()
        textbutton "[[Placeholder]" style "lang_choose" text_style "lang_choose_text" hovered SetVariable("install_lang", "placeholder") action NullAction()
    key "K_RETURN" action Call("ros_install_2")
    key "K_F3" action Quit(confirm=False)

# Экран устройств
screen install_devices():
    vbox:
        pos(235,154)
        ysize 23
        text "Компьютер:\nЭкран:\nКлавиатура:\nРаскладка:\n\nПрименить:" style "devices_choose_text_title"
    vbox:
        pos(380,154)
        ysize 23
        textbutton "ACPI x64-based PC" style "devices_choose" text_style "devices_choose_text" hovered SetVariable("apply_settings", False) action NullAction()
        textbutton "SDL Display (1280x720x32)" style "devices_choose" text_style "devices_choose_text" hovered SetVariable("apply_settings", False) action NullAction()
        textbutton "XT-, AT- or extended keyboard (83-105 keys)" style "devices_choose" text_style "devices_choose_text" hovered SetVariable("apply_settings", False) action NullAction()
        textbutton "Russian" style "devices_choose" text_style "devices_choose_text" hovered SetVariable("apply_settings", False) action NullAction()
        null height 23
        textbutton "Применить данные параметры устройств" style "devices_choose" text_style "devices_choose_text" hovered SetVariable("apply_settings", True) unhovered SetVariable("apply_settings", False) action NullAction()
    key "K_RETURN" action Call("ros_install_5")
    key "K_F3" action Quit(confirm=False)

# Экран с информацией о текущих разделах на жёстком диске
screen partitions_list():
    add "partitions_field"
    add "partitions_field_2"
    vbox:
        xalign 0.5 yalign 0.49
        ysize 23
        text "40 ГБ  Жёсткий диск 0  (Порт=0, Шина=0, Id=0) на uniata [[RAW]" style "partitions_field_text"
    vbox:
        pos(100,366)
        textbutton "Неразмеченное пространство                                    40959 МБ" style "partitions_choose" text_style "partitions_choose_text" hovered SetVariable("partition_hovered", True) unhovered SetVariable("partition_hovered", False) action NullAction()
    key "K_RETURN" action Call("ros_install_6")
    key ["p", "e", "l", "d", "P", "E", "L", "D"] action NullAction()
    key "K_F3" action Quit(confirm=False)

# Экран параметров форматирования
screen format_options():
    vbox:
        pos(97,320)
        ysize 23
        textbutton "Форматирование раздела в файловой системе FAT (быстрое)" style "format_choose" text_style "format_choose_text" hovered SetVariable("format_method", "fat_fast") unhovered SetVariable("format_method", None) action NullAction()
        textbutton "Форматирование раздела в файловой системе FAT" style "format_choose" text_style "format_choose_text" hovered SetVariable("format_method", "fat") action NullAction()
        textbutton "Форматирование раздела в файловой системе BTRFS (быстрое)" style "format_choose" text_style "format_choose_text" hovered SetVariable("format_method", "btrfs_fast") action NullAction()
        textbutton "Форматирование раздела в файловой системе BTRFS" style "format_choose" text_style "format_choose_text" hovered SetVariable("format_method", "btrfs") unhovered SetVariable("format_method", None) action NullAction()
    key "K_RETURN" action Call("ros_install_7")
    key "K_ESCAPE" action Call("ros_install_5")
    key "K_F3" action Quit(confirm=False)

# Экран ввода имени каталога для установки
screen directory_name_input():
    add "directory_name_field"
    add "input_caret":
        pos(215,166)
    hbox:
        text "\\ReactOS" style "directory_name_text"
    key "K_RETURN" action Call("ros_install_9")
    key "K_F3" action Quit(confirm=False)

# Экран выбора варианта установки загрузчика
screen loader_install():
    vbox:
        pos(118,172)
        ysize 23
        textbutton "Установить загрузчик на жёсткий диск (MBR и VBR)." style "format_choose" text_style "format_choose_text" hovered SetVariable("set_loader", "mbr_and_vbr") unhovered SetVariable("set_loader", None) action NullAction()
        textbutton "Установить загрузчик на жёсткий диск (только VBR)." style "format_choose" text_style "format_choose_text" hovered SetVariable("set_loader", "vbr") action NullAction()
        textbutton "Установить загрузчик на гибкий диск." style "format_choose" text_style "format_choose_text" hovered SetVariable("set_loader", "floppy") action NullAction()
        textbutton "Не устанавливать загрузчик." style "format_choose" text_style "format_choose_text" hovered SetVariable("set_loader", None) action NullAction()
    key "K_RETURN" action Call("ros_install_12")
    key "K_F3" action Quit(confirm=False)

# "Невидимый" экран с таймером перезагрузки и перехватчик нажатия клавиши Enter
screen reboot_timer():
    timer 16.0 action Jump("ros_install_14")
    key "K_RETURN" action Jump("ros_install_14")

# Перехватчик названия текущего лейбла
init python:
    def label_callback(name, abnormal):
        store.current_label = name

    config.label_callback = label_callback

# Перехватчик событий нажимаемых клавиш
screen install_keys():
    python:
        if store.current_label == "ros_install_2": next_step = "ros_install_3"
        elif store.current_label == "ros_install_3": next_step = "ros_install_4"
        elif store.current_label == "ros_install_4": next_step = "ros_install_5"
        elif store.current_label == "ros_install_7": next_step = "ros_install_8"
    key "K_RETURN" action Call(next_step)
    key ["r", "l", "R", "L"] action NullAction()
    key "K_F3" action Quit(confirm=False)

label ros_install:
    scene setup
    show border:
        pos(0,698)
    show install_text "  Установка ReactOS [config.version]\n=======================================" as install_text_title:
        pos(63,38)
    show install_text_center "Подождите, пока Установщик ReactOS выполняет инициализацию\nи обнаружение ваших устройств..." as install_centertext:
        xalign 0.5 yalign 0.42
    show border_text "Пожалуйста, подождите..."
    $ renpy.pause(2.0, hard=True)
    hide install_centertext
    hide border_text
    $ renpy.pause(0.2, hard=True)
    show install_text "Выбор языка\n  ●  Пожалуйста, выберите язык, используемый при установке.\n     Затем нажмите Enter.\n  ●  Этот язык будет использоваться по умолчанию в установленной системе.":
        pos(97,115)
    show border_text "ENTER = Продолжить    F3 = Выход"
    show screen install_lang_choice
    $ renpy.pause(hard=True)

label ros_install_2:
    if install_lang != "russian":
        call screen dialog("Местозаполнитель: контент появится позже.", ok_action=Hide("dialog"))
    else:
        hide screen install_lang_choice
        hide install_text
        hide border_text
        $ renpy.pause(0.3, hard=True)
        show install_text "{color=#fff}Добро пожаловать в программу установки ReactOS{/color}\n\nНа этой стадии будут скопированы файлы операционной системы ReactOS\nна ваш компьютер и подготовлена вторая стадия установки.\n\n  ●  Нажмите ENTER для установки или обновления ReactOS.\n  ●  Нажмите R для восстановления ReactOS.\n  ●  Нажмите L для просмотра лицензионного соглашения ReactOS.\n  ●  Нажмите F3 для выхода из программы установки ReactOS.\nДля дополнительной информации о ReactOS посетите:\n{color=#fff}http://www.reactos.ru{/color}":
            pos(97,115)
        show border_text "ENTER = Продолжить  R = Восстановление  L = Лиц. соглашение  F3 = Выход":
            xalign 0.1
        show screen install_keys
        $ renpy.pause(hard=True)

label ros_install_3:
    hide install_text
    hide border_text
    hide screen install_keys
    $ renpy.pause(0.1, hard=True)
    show install_text "{color=#fff}Состояние версии ReactOS{/color}\n\nДанная версия ReactOS находится в альфа-стадии разработки,\nмножество функций и возможностей ещё не доведены до готовности,\nи разработка идёт полным ходом. Рекомендуется использовать эту копию\nтолько в целях ознакомления и тестирования, и ни в коем случае как\nОС для повседневного использования.\n\nЕсли вы собираетесь устанавливать ReactOS на физический компьютер,\nобязательно сделайте резервную копию всех ваших данных, либо\nиспользуйте отдельный ПК, выделенный для тестирования.\n\n  ●  Нажмите ENTER для продолжения установки.\n  ●  Нажмите F3 для выхода из установки.":
        pos(97,115)
    show border_text "ENTER = Продолжить    F3 = Выход"
    show screen install_keys
    $ renpy.pause(hard=True)

label ros_install_4:
    hide install_text
    hide border_text
    hide screen install_keys
    $ renpy.pause(0.1, hard=True)
    show install_text "В списке ниже приведены устройства и их параметры." as install_text1:
        pos(97,115)
    show screen install_devices
    show install_text "Вы можете изменить параметры устройств, нажимая клавиши ВВЕРХ и ВНИЗ\nдля выделения элемента, и клавишу ENTER для выбора других вариантов\nпараметров.\n\nКогда все параметры определены, выберите \"Применить данные параметры\nустройств\" и нажмите ENTER." as install_text2:
        pos(97,310)
    show border_text "ENTER = Продолжить    F3 = Выход"
    $ renpy.pause(hard=True)

label ros_install_5:
    if not apply_settings:
        call screen dialog("Местозаполнитель: контент появится позже.", ok_action=Hide("dialog"))
    else:
        hide install_text1
        hide install_text2
        hide screen install_devices
        hide border_text
        $ renpy.pause(0.1, hard=True)
        show install_text "В списке ниже показаны существующие разделы и неиспользуемое\nпространство для нового раздела.\n  ●  Нажмите ВВЕРХ или ВНИЗ для выбора элемента.\n  ●  Нажмите ENTER для установки ReactOS на выделенный раздел.\n  ●  Нажмите P для создания первичного раздела.\n  ●  Нажмите E для создания расширенного раздела.\n  ●  Нажмите L для создания логического раздела.\n  ●  Нажмите D для удаления существующего раздела.":
            pos(97,115)
        show screen partitions_list
        show border_text "ENTER = Установить  P = Первичный раздел  E = Расширенный  F3 = Выход":
            xalign 0.1
        $ renpy.pause(hard=True)

label ros_install_6:
    if not partition_hovered:
        call screen dialog("Да, \"порт\" несовершенен, я знаю, но будь добр, выдели неразмеченное пространство...", ok_action=Hide("dialog"))
    else:
        hide install_text
        hide screen partitions_list
        hide border_text
        $ renpy.pause(0.3, hard=True)
        show install_text "Программа установки создала новый раздел на:\n  Жёсткий диск 0 (39 ГБ), Порт=0, Шина=0, Id=0 (uniata) [[RAW].\nЭтот раздел будет отформатирован далее.\n\nВыберите файловую систему из списка ниже.\n  ●  Нажмите ВВЕРХ или ВНИЗ для выбора файловой системы.\n  ●  Нажмите ENTER для форматирования раздела.\n  ●  Нажмите ESC для выбора другого раздела.":
            pos(97,115)
        show screen format_options
        show border_text "ENTER = Продолжить  ESC = Отмена  F3 = Выход"
        $ renpy.pause(hard=True)

label ros_install_7:
    if format_method != "fat_fast":
        call screen dialog("Местозаполнитель: контент появится позже.", ok_action=Hide("dialog"))
    else:
        hide install_text
        hide screen format_options
        hide border_text
        $ renpy.pause(0.2, hard=True)
        show install_text "Форматирование раздела\nДля установки раздел будет отформатирован. Нажмите ENTER для продолжения.":
            pos(97,115)
        show border_text "ENTER = Продолжить    F3 = Выход"
        show screen install_keys
        $ renpy.pause(hard=True)

label ros_install_8:
    hide install_text
    hide border_text
    hide screen install_keys
    $ renpy.pause(0.2, hard=True)
    show install_text "Форматирование раздела" as install_text1:
        pos(97,115)
    show install_text "Программа установки форматирует ваш диск" as install_text2:
        pos(162,341)
    show border_text "Пожалуйста, подождите..."
    show partitions_field as progress_window1:
        size(1240,150)
        pos(20,462)
    show partitions_field_2 as progress_window2:
        size(1232,144)
        pos(24,465)
    show partitions_field as progress_window3:
        size(1230,142)
        pos(25,466)
    show partitions_field_2 as progress_window4:
        size(1224,136)
        pos(28,469)
    show partitions_field as progress_window5:
        size(1078,45)
        pos(100,538)
    show partitions_field_2 as progress_window6:
        size(1074,41)
        pos(102,540)
    show formatting_text "0   %"
    show formatting_progressbar
    $ renpy.pause(0.2, hard=True)
    show formatting_text "70  %"
    show formatting_progressbar:
        xsize 707
    $ renpy.pause(0.2, hard=True)
    hide install_text1
    hide install_text2
    hide border_text
    hide progress_window1
    hide progress_window2
    hide progress_window3
    hide progress_window4
    hide progress_window5
    hide progress_window6
    hide formatting_text
    hide formatting_progressbar
    hide border
    hide install_text_title
    $ renpy.pause(0.3, hard=True)
    show install_text "  Установка ReactOS [config.version]\n=======================================" as install_text_title:
        pos(63,38)
    show install_text "Установка файлов ReactOS на выбранный раздел. Выберите директорию,\nв которую будет установлена система:" as install_text1:
        pos(97,115)
    show screen directory_name_input
    show install_text "Чтобы изменить выбранную директорию, нажмите BACKSPACE для удаления\nсимволов, а затем наберите новое имя директории для установки ReactOS." as install_text2:
        pos(97,198)
    show border:
        pos(0,698)
    show border_text "ENTER = Продолжить    F3 = Выход"
    $ renpy.pause(hard=True)

label ros_install_9:
    hide install_text_title
    hide install_text1
    hide install_text2
    hide border
    hide border_text
    hide screen directory_name_input
    $ renpy.pause(0.3, hard=True)
    show install_text "  Установка ReactOS [config.version]\n=======================================" as install_text_title:
        pos(63,38)
    show install_text "Подготовка вашего компьютера к копированию файлов ReactOS.":
        pos(97,115)
    show border:
        pos(0,698)
    show border_text "Подготовка списка копируемых файлов..."
    $ renpy.pause(0.3, hard=True)
    jump ros_install_10

label ros_install_10:
    hide install_text_title
    hide install_text
    hide border
    hide border_text
    $ renpy.pause(0.2, hard=True)
    show install_text "  Установка ReactOS [config.version]\n=======================================" as install_text_title:
        pos(63,38)
    show install_text_center "Пожалуйста, подождите, пока программа установки скопирует файлы\nReactOS в установочную директорию.\nЭто может занять несколько минут.":
        xalign 0.5 yalign 0.25
    show border:
        pos(0,698)
    show border_text "Лень всё перечислять, не обессудьте..."
    show partitions_field as progress_window1:
        size(1036,150)
        pos(130,318)
    show partitions_field_2 as progress_window2:
        size(1025,144)
        pos(136,322)
    show partitions_field as progress_window3:
        size(1023,142)
        pos(137,323)
    show partitions_field_2 as progress_window4:
        size(1017,138)
        pos(140,325)
    show partitions_field as progress_window5:
        size(864,45)
        pos(216,395)
    show partitions_field_2 as progress_window6:
        size(858,39)
        pos(219,398)
    show install_text "Программа установки копирует файлы...":
        pos(165,342)
    show formatting_text "0   %":
        yalign 0.53
    show installing_progressbar
    show partitions_field as kernel_pool1:
        size(163,30)
        pos(214,596)
    show partitions_field_2 as kernel_pool2:
        size(159,26)
        pos(216,598)
    show formatting_text "0   %" as kernel_pool_percent:
        xalign 0.22 yalign 0.82
    show formatting_text "Пул ядра" as kernel_pool_text:
        xalign 0.213 yalign 0.91
    show partitions_field as kernel_cache1:
        size(163,30)
        pos(565,596)
    show partitions_field_2 as kernel_cache2:
        size(159,26)
        pos(567,598)
    show formatting_text "2   %" as kernel_cache_percent:
        xalign 0.51 yalign 0.82
    show formatting_text "Кэш ядра" as kernel_cache_text:
        xalign 0.51 yalign 0.91
    show partitions_field as free_memory1:
        size(163,30)
        pos(918,596)
    show partitions_field_2 as free_memory2:
        size(159,26)
        pos(920,598)
    show installing_progressbar as free_memory_indicator:
        size(127,18)
        pos(928,602)
        xanchor 0 yanchor 0
    show formatting_text "91  %" as free_memory_percent:
        xalign 0.8 yalign 0.82
    show formatting_text "Своб. память" as free_memory_text:
        xalign 0.816 yalign 0.91
    $ renpy.pause(5.0, hard=True)
    show formatting_text "100 %"
    show installing_progressbar:
        xsize 846
    show border_text ":P"
    $ renpy.pause(0.1, hard=True)
    jump ros_install_11

label ros_install_11:
    hide install_text_title
    hide install_text_center
    hide border
    hide border_text
    hide progress_window1
    hide progress_window2
    hide progress_window3
    hide progress_window4
    hide progress_window5
    hide progress_window6
    hide install_text
    hide formatting_text
    hide installing_progressbar
    hide kernel_pool1
    hide kernel_pool2
    hide kernel_pool_percent
    hide kernel_pool_text
    hide kernel_cache1
    hide kernel_cache2
    hide kernel_cache_percent
    hide kernel_cache_text
    hide free_memory1
    hide free_memory2
    hide free_memory_indicator
    hide free_memory_percent
    hide free_memory_text
    $ renpy.pause(0.2, hard=True)
    show install_text "  Установка ReactOS [config.version]\n=======================================" as install_text_title:
        pos(63,38)
    show install_text "Программа установки обновляет конфигурацию системы.":
        pos(97,115)
    show border:
        pos(0,698)
    show border_text "Импортирование caroots.inf..."
    $ renpy.pause(0.5, hard=True)
    show border_text "Импортирование registry.inf..."
    $ renpy.pause(1.5, hard=True)
    show border_text "Добавление информации о кодовой странице в реестр..."
    $ renpy.pause(0.2, hard=True)
    hide install_text_title
    hide install_text
    hide border
    hide border_text
    $ renpy.pause(0.3, hard=True)
    show install_text "  Установка ReactOS [config.version]\n=======================================" as install_text_title:
        pos(63,38)
    show install_text "Установка загрузчика ReactOS:":
        pos(97,115)
    show screen loader_install
    show border:
        pos(0,698)
    show border_text "ENTER = Продолжить    F3 = Выход"
    $ renpy.pause(hard=True)

label ros_install_12:
    if set_loader != "mbr_and_vbr":
        call screen dialog("Местозаполнитель: контент появится позже.", ok_action=Hide("dialog"))
    else:
        hide install_text_title
        hide install_text
        hide screen loader_install
        hide border
        hide border_text
        $ renpy.pause(0.3, hard=True)
        show install_text "  Установка ReactOS [config.version]\n=======================================" as install_text_title:
            pos(63,38)
        show border:
            pos(0,698)
        show border_text "Производится установка загрузчика на носитель. Пожалуйста, подождите...":
            xalign 0.1
        $ renpy.pause(1.5, hard=True)
        jump ros_install_13

label ros_install_13:
    hide install_text_title
    hide border
    hide border_text
    $ renpy.pause(0.5, hard=True)
    show install_text "  Установка ReactOS [config.version]\n=======================================" as install_text_title:
        pos(63,38)
    show install_text "Основные компоненты ReactOS были успешно установлены.\n\nИзвлеките гибкий диск из дисковода A: и\nвсе CD-ROM из CD-дисководов.\n\nНажмите ENTER для перезагрузки компьютера.":
        pos(97,115)
    show partitions_field as progress_window1:
        size(1036,150)
        pos(130,318)
    show partitions_field_2 as progress_window2:
        size(1025,144)
        pos(136,322)
    show partitions_field as progress_window3:
        size(1023,142)
        pos(137,323)
    show partitions_field_2 as progress_window4:
        size(1017,138)
        pos(140,325)
    show partitions_field as progress_window5:
        size(864,45)
        pos(216,395)
    show partitions_field_2 as progress_window6:
        size(858,39)
        pos(219,398)
    show formatting_text "Ваш компьютер будет перезагружен через 16 секунд...":
        yalign 0.53
    show reboot_progressbar
    show border:
        pos(0,698)
    show screen reboot_timer
    show border_text "ENTER = Перезагрузка"
    pause 1.0
    show formatting_text "Ваш компьютер будет перезагружен через 15 секунд..."
    pause 1.0
    show formatting_text "Ваш компьютер будет перезагружен через 14 секунд..."
    pause 1.0
    show formatting_text "Ваш компьютер будет перезагружен через 13 секунд..."
    pause 1.0
    show formatting_text "Ваш компьютер будет перезагружен через 12 секунд..."
    pause 1.0
    show formatting_text "Ваш компьютер будет перезагружен через 11 секунд..."
    pause 1.0
    show formatting_text "Ваш компьютер будет перезагружен через 10 секунд..."
    pause 1.0
    show formatting_text "Ваш компьютер будет перезагружен через 9 секунд..."
    pause 1.0
    show formatting_text "Ваш компьютер будет перезагружен через 8 секунд..."
    pause 1.0
    show formatting_text "Ваш компьютер будет перезагружен через 7 секунд..."
    pause 1.0
    show formatting_text "Ваш компьютер будет перезагружен через 6 секунд..."
    pause 1.0
    show formatting_text "Ваш компьютер будет перезагружен через 5 секунд..."
    pause 1.0
    show formatting_text "Ваш компьютер будет перезагружен через 4 секунды..."
    pause 1.0
    show formatting_text "Ваш компьютер будет перезагружен через 3 секунды..."
    pause 1.0
    show formatting_text "Ваш компьютер будет перезагружен через 2 секунды..."
    pause 1.0
    show formatting_text "Ваш компьютер будет перезагружен через 1 секунду..."
    pause 1.0
    show formatting_text "Ваш компьютер будет перезагружен через 0 секунд..."
    $ renpy.pause(hard=True)

label ros_install_14:
    hide install_text_title
    hide install_text
    hide progress_window1
    hide progress_window2
    hide progress_window3
    hide progress_window4
    hide progress_window5
    hide progress_window6
    hide formatting_text
    hide reboot_progressbar
    hide border
    hide border_text
    hide screen reboot_timer
    $ renpy.pause(0.5, hard=True)
    show install_text "  Установка ReactOS [config.version]\n=======================================" as install_text_title:
        pos(63,38)
    show install_text "Система проверяет, все ли данные записаны на диск.\n\nЭто может занять некоторое время.\nПосле завершения компьютер будет автоматически перезагружен.":
        pos(97,115)
    show border:
        pos(0,698)
    show border_text "Очистка кэша..."
    $ renpy.pause(0.5, hard=True)
    hide install_text_title
    hide install_text
    hide border
    hide border_text
    scene black
    $ persistent.installed = True
    $ renpy.save_persistent()
    jump ros_boot
