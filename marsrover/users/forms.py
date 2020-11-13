from django.contrib.auth.forms import UserCreationForm


# A form for creating new user which includes all required fields,
# plus a repeated password
class CustomUserCreationForm(UserCreationForm):
    # meta class sued to indicate which model is used (default user model)
    # and shows which fields are included in the final form
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields
