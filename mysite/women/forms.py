from django import forms
from .models import Category, Husband, Women


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Women
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'col': 50, 'rows': 5})
        }

    # title = forms.CharField(max_length=255, label='Title')
    # slug = forms.SlugField(max_length=255, label='Slug')
    # content = forms.CharField(widget=forms.Textarea, label='Content')
    # is_published = forms.BooleanField(label='Published')
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Not selected', label='Category')
    # husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label='Single', label='Husband')
