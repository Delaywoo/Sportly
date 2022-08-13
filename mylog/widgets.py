
"""
class ColorWidget(TextInput):

    template_name = "colorfield/color.html"

    class Media:
        if settings.DEBUG:
            js = [
                "colorfield/jscolor/jscolor.js",
                "colorfield/colorfield.js",
            ]
        else:
            js = [
                "colorfield/jscolor/jscolor.min.js",
                "colorfield/colorfield.js",
            ]
"""
"""
class ColorWidget(Input):
    input_type = 'color'
    template_name = 'myapp/forms/widgets/color.html'

    #https://daemotron.github.io/2017/11/08/Colours-in-Django-Models.html
    #{% include "django/forms/widgets/input.html" %}"""