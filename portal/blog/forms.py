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
    text = forms.CharField(label='', widget=forms.Textarea(attrs={"cols": "30", "rows": "3"}))
    #group = forms.CharField(label='Group', max_length=100)
    #sub = forms.CharField(label='Subject', max_length=100)
    #location = forms.CharField(label='Location', max_length=100)
    #department = forms.CharField(label='Department', max_length=100)
