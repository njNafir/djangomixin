import random, string, os

"""
Some handy snippets for django
"""

def bootstrap_visible_fields(visible_fields):
    """
        It's a good snippet to upgrade your django form fields classes for bootstrap
        In your form class defination in the __init__ file let's add this line
        after import it

        from djangomixin import bootstrap_visible_fields

        class MyForm(forms.ModelForm):
            def __init__(self, *args, **kwargs):
                bootstrap_visible_fields(self.visible_fields)
                super(MyForm, self).__init__(*args, **kwargs)

    """
    for visible in visible_fields():
        widget = visible.field.widget
        class_name = widget.__class__.__name__

        if class_name == 'Select':
            widget.attrs['class'] = 'form-select'
        elif class_name == 'CheckboxInput':
            widget.attrs['class'] = 'form-check-input'
        else:
            widget.attrs['class'] = 'form-control'


def random_string(lenght=10):
    """
        Sometimes we need to generate random string for id or slug
        Handy snippet to give a random lengthy string
    """
	chars = string.ascii_lowercase + string.digits
	plus = ''.join(random.choice(chars) for _ in range(lenght))
	dig = range(0,9)
	plus = plus + str(random.randint(0,9))
	return plus


def filename(file):
    """
        Find file actual name by it's path
    """
	return os.path.basename(file)
