from django.forms import ModelForm
from django import forms
from .models import Gender, Post

class PostCreateForm(forms.ModelForm):
    gender = forms.ModelChoiceField(
        label='性別',
        queryset=Gender.objects,
        required=False
    )

    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.required = False
            #field.widget.attrs['style'] = 'width:200px;'
            field.widget.attrs['class'] = 'form-control'
            
            if field == 'm_category':
                field.widget = forms.HiddenInput()

    field_order = ('gender', 'm_category', 's_category', 'silhouette', 'design', 'neck', 'coller', 'zip_button', 'length', 'leg', 'effect')
