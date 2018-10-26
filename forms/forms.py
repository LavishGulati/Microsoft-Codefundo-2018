from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    contact = forms.CharField(label='contact', max_length=100)
    profession = forms.CharField(label='profession', max_length=100)
    location = forms.CharField(label='location', max_length=100)
    message = forms.CharField(label='message', max_length=100)

    # class Meta:
    #     model = Register
    #     fields = ('name', 'contact', 'profession', 'location', 'message')

class RequestForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    contact = forms.CharField(label='contact', max_length=100)
    location = forms.CharField(label='location', max_length=100)
    assistance = forms.CharField(label='assistance', max_length=100)
    special = forms.CharField(label='special', max_length=100)
    housing = forms.CharField(label='housing', max_length=100)
    priority = forms.CharField(label='priority', max_length=100)

