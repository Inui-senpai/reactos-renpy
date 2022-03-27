# Оформление
style ros_mixer_volume_back:
    background Frame("gui/mixer_volume/back.png")
    xysize(81, 136)
style ros_mixer_volume_slider:
    xysize(21, 65)
    bar_vertical True
    base_bar "gui/mixer_volume/base_bar.png"
    thumb "gui/mixer_volume/thumb.png"

# Регулятор громкости на Панели задач
screen ros_mixer_volume():
    frame:
        pos(1120, 557)
        style "ros_mixer_volume_back"
        text "Громкость" style "ros_properties_text":
            align(0.5, 0.1)
        vbar value Preference("sound volume") style "ros_mixer_volume_slider":
            pos(29, 35)
        vbox:
            pos(6, 110)
            style_prefix "ros_check"
            textbutton "Выкл. все" action Preference("all mute", "toggle")
