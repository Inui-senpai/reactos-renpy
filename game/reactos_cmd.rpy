# Оформление
style ros_cmd_window:
    background Frame("gui/window/cmd/window.png")
    xysize(668, 431)
style ros_cmd_viewport:
    background Frame("ros_cmd_viewport")
    xysize(660, 404)
    pos(4, 24)
image ros_cmd_viewport = Composite((660, 404), (0, 0), "gui/window/cmd/viewport.png", (2, 2), "ros_cmd_viewport_back")
image ros_cmd_viewport_back:
    Solid("#000")
    xysize(656, 400)
style ros_cmd_text:
    caret "cmd_caret"
    font "gui/font/UniVGA16.ttf"
    size 16
    color "#c0c0c0"
    xpos 2
style ros_cmd_window_title:
    font "gui/font/tahomabd.ttf"
    size 11
    color "#fff"
    xpos 24 ypos 8
image ros_cmd_header:
    Solid("#000080")
    xysize(648, 16)
    pos(2, 2)
style ros_cmd_header_text:
    font "gui/font/UniVGA16.ttf"
    size 16
    color "#fff"
image cmd_caret:
    Text("_", style="ros_cmd_text")
    subpixel True
    block:
        alpha 1
        0.55
        alpha 0
        0.55
        repeat

# Основные переменные
default cmd_history = []
default prompt = "C:\\Documents and Settings\\Administrator>"
default command = ""
default cmd_display = ""

# Обработчик команд
init python:
    def ros_cmd_parse(name=""):
        cmd_history.append(prompt + name)
        if name.lower() == "":
            pass
        # Местозаполнители; эти команды будут реализованы в будущем
        elif name.lower() in [
            "?", "alias", "attrib", "beep", "call", "cd", "chcp", "choice", "cls", "cmd", "color", "copy", "delete", "dir", "erase", "for", "free", "goto", "history", "if", "label", "md", "mkdir", "mklink", "move", "path", "pause",
            "popd", "prompt", "pushd", "rd", "rem", "ren", "rename", "replace", "rmdir", "screen", "set", "shift", "start", "timer", "title", "type", "verify", "vol"
        ]:
            cmd_history.append("Местозаполнитель. Контент будет добавлен позже.")
        elif name.lower() == "control":
            renpy.show_screen("ros_explorer", folder="control_panel")
        elif name.lower() == "date":
            cmd_history.append(now.strftime("{}").format(weekdays[int(now.weekday())]) + " " + now.strftime("%d.%m.%Y"))
        elif name.lower().startswith("echo "):
            cmd_history.append(name[5:])
        elif name.lower() == "exit":
            cmd_history.clear()
            command = ""
            renpy.hide_screen("ros_command_prompt")
        elif name.lower() == "explorer":
            renpy.show_screen("ros_explorer")
        elif name.lower() == "help":
            cmd_history.append("""Список всех доступных команд с коротким описанием

HELP [команда]
команда /?     Выводит подробную информацию о команде.

?        Список всех доступных команд без описания.
ALIAS    Вывод, установка или удаление псевдонимов.
ATTRIB   Отображение и изменение атрибутов файлов.
BEEP     Звуковой сигнал.
CALL     Вызов одного пакетного файла из другого.
CD       Вывод имени или смена текущей папки.
CHCP     Вывод или установка активной кодовой страницы.
CHOICE   Ждёт, пока пользователь не выберет один из указанных в списке символов.
CLS      Очистка экрана.
CMD      Запуск ещё одного интерпретатора командных строк ReactOS.
COLOR    Установка цветов переднего плана и фона, используемых по умолчанию.
COPY     Копирование одного или нескольких файлов в другое место.
DATE     Вывод или установка текущей даты.
DELETE   Удаление одного или нескольких файлов.
DIR      Вывод списка файлов и подпапок из указанной папки.
ECHO     Вывод сообщений и переключение режима отображения команд на экране.
ERASE    Удаление одного или нескольких файлов.
EXIT     Завершение работы программы CMD.EXE (интерпретатора командных строк).
FOR      Запуск указанной команды для каждого из файлов в наборе.
FREE     (Свободное) дисковое пространство.
GOTO     Передача управления в отмеченную строку пакетного файла.
HELP     Выводит справочную информацию о командах ReactOS.
HISTORY  Список запущенных команд.
IF       Оператор условного выполнения команд в пакетном файле.
LABEL    Создание, изменение и удаление меток тома для дисков.
MD       Создание папки.
MKDIR    Создание папки.
MKLINK   Создание символических и жёстких ссылок.
MOVE     Перемещение одного или нескольких файлов из одной папки в другую.
PATH     Отображает или устанавливает путь поиска исполняемых файлов.
PAUSE    Приостанавливает выполнение пакетного файла и выводит сообщение.
POPD     Восстанавливает предыдущее значение активной папки, сохранённое с
         помощью команды PUSHD.
PROMPT   Изменяет приглашение в командной строке ReactOS.
PUSHD    Сохраняет значение активной папки и переходит к другой папке.
RD       Удаляет папку.
REM      Помещает комментарии в пакетные файлы.
REN      Переименовывает файлы или папки.
RENAME   Переименовывает файлы или папки.
REPLACE  Заменяет файлы.
RMDIR    Удаляет папку.
SCREEN   Перемещение курсора и вывод текста.
SET      Показывает, устанавливает и удаляет переменные среды ReactOS.
SHIFT    Изменение положения (сдвиг) подставляемых параметров для пакетного
         файла.
START    Выполнение программы или команды в отдельном окне.
TIME     Вывод и установка системного времени.
TIMER    Секундомер.
TITLE    Назначение заголовка окна для текущего сеанса интерпретатора командных
         строк CMD.EXE.
TYPE     Вывод на экран содержимого текстовых файлов.
VER      Вывод сведений о версии ReactOS.
VERIFY   Установка режима проверки правильности записи файлов на диск.
VOL      Вывод метки и серийного номера тома для диска.
""")
        elif name.lower() == "notepad":
            renpy.show_screen("ros_notepad")
        elif name.lower() == "time":
            cmd_history.append("Текущее время: " + now.strftime("%H:%M:%S,%f")[:11])
        elif name.lower() == "ver":
            cmd_history.append("""
Интерпретатор командной строки ReactOS
Версия {} {}
Запущен на: ReactOS [Версия 5.2.3790] Service Pack 3
""".format(config.version, ros_build_wo_compiler))
        elif name.lower() == "winver":
            renpy.show_screen("ros_about", name="reactos")
        else:
            cmd_history.append("\"" + name + "\" не является внутренней или внешней командой, исполняемой программой или пакетным файлом.")

# Экран для ввода команд
screen cmd_input():
    input default "" prefix prompt value VariableInputValue("command", returnable=True) style "ros_cmd_text"
    key "K_RETURN" action [Function(ros_cmd_parse, name=command), SetVariable("command", "")]

# Окно
screen ros_command_prompt():
    python:
        cmd_display = "\n".join(map(str, cmd_history))
    drag:
        drag_name "ros_cmd"
        drag_handle (0, 0, 668, 23)
        xalign 0.2 yalign 0.2
        frame:
            style "ros_cmd_window"
            add "gui/desktop/menu_icons/submenu/cmd.png" xpos 5 ypos 5
            text "Командная строка" style "ros_cmd_window_title"
            imagebutton auto "gui/window/common/close_%s.png" action [
                SetVariable("command", ""),
                SetVariable("cmd_history", []),
                Hide("ros_command_prompt")]:
                xanchor -646 yanchor -6
            imagebutton auto "gui/window/common/expand_%s.png" action NullAction():
                xanchor -628 yanchor -6
            imagebutton auto "gui/window/common/minimize_%s.png" action NullAction():
                xanchor -612 yanchor -6
            frame:
                style "ros_cmd_viewport"
                viewport:
                    yinitial 0.0
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    side_yfill True
                    vbox:
                        add "ros_cmd_header"
                        hbox:
                            xpos 14 ypos -14
                            text "Командная строка ReactOS" style "ros_cmd_header_text"
                            text "Введите HELP для вывода справки" style "ros_cmd_header_text" xpos 180
                        text "ReactOS [[Версия [config.version] [ros_build_wo_compiler]]\n(C) Авторское право 1998-2022 Команда ReactOS." style "ros_cmd_text" ypos -12
                        if not cmd_history:
                            vbox:
                                use cmd_input
                        else:
                            vbox:
                                text "[cmd_display]" style "ros_cmd_text"
                                use cmd_input
                        transclude
