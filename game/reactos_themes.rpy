# Оформление: BlackShade
style ros_blackshade_inactive_window:
    background Frame("gui/window/properties/theme_samples/blackshade/inactive_window.png")
    xsize 314 ysize 137
style ros_blackshade_inactive_window_viewport:
    background Frame("gui/window/properties/theme_samples/blackshade/inactive_window_viewport.png")
    xsize 308 ysize 109
style ros_blackshade_inactive_window_title:
    font "gui/font/Ubuntu-Medium.ttf"
    size 12
    color "#fff"
style ros_blackshade_active_window:
    background Frame("gui/window/properties/theme_samples/blackshade/active_window.png")
    xsize 322 ysize 135
style ros_blackshade_active_window_viewport:
    background Frame("gui/window/properties/theme_samples/blackshade/active_window_viewport.png")
    xsize 313 ysize 109
style ros_blackshade_active_window_title:
    font "gui/font/Ubuntu-Medium.ttf"
    size 12
    color "#fff"
style ros_blackshade_active_window_text:
    font "gui/font/Ubuntu-Regular.ttf"
    size 11
    color "#000"
style ros_blackshade_message_window:
    background Frame("gui/window/properties/theme_samples/blackshade/message_window.png")
    xsize 150 ysize 100
style ros_blackshade_message_window_viewport:
    background Frame("gui/window/properties/theme_samples/blackshade/message_window_viewport.png")
    xsize 140 ysize 72
style ros_blackshade_message_window_ok_button:
    insensitive_background "gui/window/properties/theme_samples/blackshade/message_window_ok.png"
style ros_blackshade_message_window_ok_button_text:
    font "gui/font/Ubuntu-Regular.ttf"
    size 11
    color "#000"
    hover_color "#000"
    xpos 28 ypos 10
image ros_blackshade_minimize_button_idle = im.Composite((30, 16), (0, 0), "gui/window/themed/blackshade/window_button.png", (10, 8), "gui/window/themed/blackshade/minimize_sign.png")
image ros_blackshade_maximize_button_idle = im.Composite((30, 16), (0, 0), "gui/window/themed/blackshade/window_button.png", (10, 4), "gui/window/themed/blackshade/maximize_sign.png")
image ros_blackshade_close_button_idle = im.Composite((30, 16), (0, 0), "gui/window/themed/blackshade/window_button.png", (10, 4), "gui/window/themed/blackshade/close_sign.png")
image ros_blackshade_minimize_button_hover = im.Composite((30, 16), (0, 0), "gui/window/themed/blackshade/window_button_minimize_hover.png", (10, 8), "gui/window/themed/blackshade/minimize_sign.png")
image ros_blackshade_maximize_button_hover = im.Composite((30, 16), (0, 0), "gui/window/themed/blackshade/window_button_maximize_hover.png", (10, 4), "gui/window/themed/blackshade/maximize_sign.png")
image ros_blackshade_close_button_hover = im.Composite((30, 16), (0, 0), "gui/window/themed/blackshade/window_button_close_hover.png", (10, 4), "gui/window/themed/blackshade/close_sign.png")

# Оформление: Окна для образца темы
# BlackShade
# Неактивное окно
screen ros_properties_screen_appearance_inactive_window_blackshade():
    frame:
        style "ros_blackshade_inactive_window"
        xpos 183 ypos 162
        text "Неактивное окно" style "ros_blackshade_inactive_window_title" xpos 6 ypos 7
        imagebutton idle "ros_blackshade_close_button_idle" xpos 277 ypos 5
        imagebutton idle "ros_blackshade_maximize_button_idle" xpos 246 ypos 5
        imagebutton idle "ros_blackshade_minimize_button_idle" xpos 215 ypos 5
        frame:
            style "ros_blackshade_inactive_window_viewport"
            xpos 3 ypos 23
# Активное окно
screen ros_properties_screen_appearance_active_window_blackshade():
    frame:
        style "ros_blackshade_active_window"
        xpos 195 ypos 45
        text "Активное окно" style "ros_blackshade_active_window_title" xpos 6 ypos 7
        imagebutton idle "ros_blackshade_close_button_idle" xpos 285 ypos 5
        imagebutton idle "ros_blackshade_maximize_button_idle" xpos 254 ypos 5
        imagebutton idle "ros_blackshade_minimize_button_idle" xpos 223 ypos 5
        frame:
            style "ros_blackshade_active_window_viewport"
            add "gui/window/themed/blackshade/viewport_background.png" ysize 107 xpos 294 ypos 1
            add "gui/window/themed/blackshade/viewport_up_idle.png" xpos 295
            add "gui/window/themed/blackshade/viewport_thumb.png" ysize 50 xpos 295 ypos 17
            add "gui/window/themed/blackshade/viewport_down_idle.png" xpos 295 ypos 90
            xpos 4 ypos 22
            viewport:
                yinitial 0.0
                scrollbars None
                mousewheel True
                draggable True
                side_yfill True
                vbox:
                    text "Текст окна" style "ros_blackshade_active_window_text" xpos 4 ypos 2
# Окно сообщения
screen ros_properties_screen_appearance_message_window_blackshade():
    frame:
        style "ros_blackshade_message_window"
        xpos 189 ypos -97
        text "Окно сообщения" style "ros_blackshade_active_window_title" xpos 6 ypos 7
        imagebutton idle "ros_blackshade_close_button_idle" xpos 114 ypos 5
        frame:
            style "ros_blackshade_message_window_viewport"
            xpos 5 ypos 23
            textbutton "ОК" style "ros_blackshade_message_window_ok_button" text_style "ros_blackshade_message_window_ok_button_text" xpos 31 ypos 22
