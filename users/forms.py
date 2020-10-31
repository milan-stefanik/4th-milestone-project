from django import forms
from phonenumber_field.formfields import PhoneNumberField
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm, ResetPasswordKeyForm
from crispy_forms.helper import FormHelper


class MyCustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.label_class = 'bmd-label-floating'
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'placeholder': '',
                'class': 'form-control',
            })
            del field.widget.attrs['placeholder']
        self.fields['login'].label = 'Username or e-mail'
        self.fields['remember'].widget.attrs.update({
            'class': 'form-check-input'
        })


class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.label_class = 'bmd-label-floating'
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'placeholder': '',
                'class': 'form-control',
            })
            del field.widget.attrs['placeholder']


class MyCustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomResetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.label_class = 'bmd-label-floating'
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'placeholder': '',
                'class': 'form-control',
            })
            del field.widget.attrs['placeholder']


class MyCustomResetPasswordKeyForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomResetPasswordKeyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.label_class = 'bmd-label-floating'
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'placeholder': '',
                'class': 'form-control',
            })
            del field.widget.attrs['placeholder']
