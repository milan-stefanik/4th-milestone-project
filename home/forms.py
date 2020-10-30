from django import forms
from phonenumber_field.formfields import PhoneNumberField
from crispy_forms.helper import FormHelper


class ContactForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput,
        required=True,
    )

    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput,
        required=True,
    )

    email = forms.EmailField(
        label='E-mail',
        widget=forms.TextInput,
        required=True,
    )

    phone = PhoneNumberField(
        label='Phone Number',
        widget=forms.TextInput,
        required=False,
    )

    subject = forms.CharField(
        label='Subject',
        widget=forms.TextInput,
        required=True,
    )

    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'rows': 6}),
        required=True,
    )

    send_copy = forms.BooleanField(
        label='Send me a copy of my message',
        initial=True,
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.label_class = 'bmd-label-floating'
        self.fields['send_copy'].widget.attrs.update({
            'class': 'form-check-input'
        })
