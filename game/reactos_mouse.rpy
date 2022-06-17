# Здесь будут всевозможные схемы указателей и переключение на них

# ReactOS Default
define ros_mouse_scheme_default = {
    "default":[("gui/mouse/arrow.png", 0, 0)],
    "helpsel":[("gui/mouse/helpsel.png", 0, 0)],
    "working":[("gui/mouse/working.png", 0, 0)],
    "busy":[("gui/mouse/busy.png", 15, 16)],
    "cross":[("gui/mouse/cross.png", 15, 15)],
    "beam":[("gui/mouse/beam.png", 15, 15)],
    "pen":[("gui/mouse/pen.png", 0, 0)],
    "unavail":[("gui/mouse/unavail.png", 16, 16)],
    "ns":[("gui/mouse/ns.png", 15, 15)],
    "ew":[("gui/mouse/ew.png", 15, 15)],
    "nwse":[("gui/mouse/nwse.png", 15, 15)],
    "nesw":[("gui/mouse/nesw.png", 15, 15)],
    "move":[("gui/mouse/move.png", 15, 15)],
    "up":[("gui/mouse/up.png", 15, 7)],
    "link":[("gui/mouse/link.png", 12, 4)]
    }

# Схема по умолчанию и отключение скрытия указателя
define config.mouse = ros_mouse_scheme_default
define config.mouse_hide_time = None
