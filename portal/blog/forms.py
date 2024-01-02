from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "inputPassword",
        })
    )


class MlPromobotInForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(
        attrs={
            "cols": "30",
            "rows": "3",
            "placeholder": "Введите сообщение",
            "required": "required",
            "autofocus": "autofocus"}))
