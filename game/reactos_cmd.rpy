screen dialog_placeholder(message, ok_action, level=None):
    style_prefix "ros_installed_confirm"
    modal True
    drag:
        drag_name "ros_confirm_window"
        drag_handle (0, 0, 900, 21)
        xalign 0.5
        yalign 0.5
        frame:
            xsize 306 ysize 110
            vbox:

                if level == "info":
                    text "Информация" style "ros_header_text_installed"
                    add "gui/window/common/info.png"
                elif level == "warning":
                    text "Внимание" style "ros_header_text_installed"
                    add "gui/window/common/warning.png"
                elif level == "question":
                    text "Вопрос" style "ros_header_text_installed"
                    add "gui/window/common/question.png"
                elif level == "error":
                    text "Ошибка" style "ros_header_text_installed"
                    add "gui/window/common/error.png"

                imagebutton auto "gui/window/common/close_%s.png" action ok_action:
                    xanchor -245 yanchor 35

                label _(message):
                    style "ros_confirm_prompt_installed"
                    xalign 0.5

                hbox:
                    xalign 0.37
                    spacing 80

                    textbutton _("ОК") style "ros_confirm_button_installed" text_style "ros_confirm_button_installed_text" focus_mask "gui/window/postinstall/button_idle.png" action ok_action

screen ros_command_prompt():
    use dialog_placeholder(message="Местозаполнитель: контент появится позже", ok_action=Hide("ros_command_prompt"))
