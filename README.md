# djangomixin

Is a set of utilities to give you advantage on your django development.
This utilities can help you to manage and upgrade django application.

Is a open source package that works on top django mainly.
Several mixins and snippets is to make django more handy in case of development.
Have class based view snippet, date snippet, mail sending snippet, permission snippet and so on.


# Installation
The latest version of djangomixin can be installed from PyPI:

    pip install djangomixin


# Quick use
After install djangomixin you can test some awesome snippet, best example:


## filename
    from djangomixin import filename

    # filename is a simple function to give you actual filename of a source file
    my_file_name = filename("C://path/this is file.jpg")


## random_string
random_string is a function to give you a lengthy random_string, such as
when we need to generate a slug filed over a model we can simply use
random_string to generate lengthy random_string

    from djangomixin import random_string

    slug = models.CharField(max_length=20, default=random_string)

    # string length is by default 10, but we can change the length by passing a value in it
    slug = models.CharField(max_length=20, default=lambda: random_string(20))


## bootstrap_visible_fields
bootstrap_visible_fields is for generating bootstrap field for your form and model form
all you need to do just go to your form class then call this function and pass the specific object to it

    from django import forms
    from djangomixin import bootstrap_visible_fields


    class MyModelForm(forms.ModelForm):
      def __init__(self, *args, **kwargs):
          super(MyModelForm, self).__init__(*args, **kwargs)
          bootstrap_visible_fields(self.visible_fields)


## RequestAttachMixin
RequestAttachMixin is a class snippet which can be inherit by any class based view.
By default class based view have not request object in it.
So, when we need to get or verify request we have some problem in the class based view
This snippet will attach request object in that class object
You can get this request from any of method, we are using get_context_data for example

    from djangomixin.class_mixin import RequestAttachMixin


    class TestView(RequestAttachMixin):
      template_name = 'home.html'

      def get_context_data(self, *args, **kwargs):
        data = dict(self.request.GET)
        print(data)
        return super(TestView, self).get_context_data(*args, **kwargs)


## NextUrlMixin
NextUrlMixin is a class snippet which can be inherit by any class based view.
By default class based view have not support next url which declined in the browser path like /?next=/admin/
This snippet will attach get_next_url method to your class object
djangomixin will verify the validity of next url, if it secure then it will give you next url path

    from djangomixin.class_mixin import NextUrlMixin


    class TestView(NextUrlMixin):
      template_name = 'home.html'

      def get_context_data(self, *args, **kwargs):
        next_url = self.get_next_url()
        print(next_url)
        return super(TestView, self).get_context_data(*args, **kwargs)


## send_mail
send_mail snippet is to give you nice and pretty good solution for sending mail.
You can verify the mail sending for any server including s3 preferable.
To send mail we must set some flag to our settings file and call this function with appropriate values

    # In your settings, let's add this lines for server configuration

    DEFAULT_FROM_EMAIL = "Your default email who will be the sender"
    DEFAULT_FROM_SENDER = "Your default name who will be the sender"
    USERNAME_SMTP = "Mail server user name"
    PASSWORD_SMTP = "Mail server password"
    HOST_SMTP = "Mail server host address"
    PORT_SMTP = "Mail server host port"

    # After adding this lines to your settings, now you can send email

    from djangomixin.mail_mixin import send_mail

    # send_mail accept at most six parameter, which is your info and body of mailing

    send_mail(
      sender="email@example.com",
      sender_name="Test User",
      recipient=None,
      subject='Message From Django Server',
      body_tex='',
      body_html=''
    )


## last_month_start_end
last_month_start_end is to provide last month start and end day before today
To check this snippet work you can just pass datetime for today into it

    form djangomixin.date_mixin import last_month_start_end
    import datetime

    start_end = last_month_start_end(datetime.datetime.now())
    print(start_end)


## month_data_range
month_data_range is to provide comprehensive month data with all of info
Check the output of month_data_range to get and check how this value can help you rustically

    from djangomixin.date_mixin import month_data_range

    json_data = month_data_range()

    # month_data_range have two exceptional parameter which can be more handy for you

    # months_ago is by default 4
    # include_this_month is by default False

    json_data = month_data_range(months_ago=4, include_this_month=True)



## allowed_roles
allowed_roles is a fancy function to verify and block access to a view function.
Works as decorator in a view function as like other decorator.
It usage django permission management for this work.
you can pass allowed permission for a user as defined in django documentation for permission verification.

    from djangomixin.permission_mixin import allowed_roles

    # django permission verification 'module.model_action'
    # here action can be view, change, add, delete

    @allowed_roles(['store.book_view'])
    def book_view(request):
      ....


# Author
djangomixin is a open source libraries for Python, Initially developed by Nj Nafir.


# Contribute
- Issue Tracker: [djangomixin issues](https://github.com/njNafir/djangomixin/issues)
- Source Code: [djangomixin sources](https://github.com/njNafir/djangomixin)


# Support

If you are having issues, please let us know.
We have a mailing list located at: njnafir@gmail.com


# License
The project is licensed under the MIT license.
