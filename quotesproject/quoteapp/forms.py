from django.forms import ModelForm,CharField,ModelChoiceField,Textarea, MultipleChoiceField,SelectMultiple,TextInput,DateField,DateInput,Select
from .models import Quote,Author,Tag
class QuotesForm(ModelForm):
    quote = CharField(
        min_length=10,
        max_length=3000,
        required=True,
        widget=Textarea(attrs={'class':'custom-textarea',}))
    
    author = ModelChoiceField(queryset= Author.objects.all(),widget=Select(attrs={'class':'custom-select'}))
    class Meta:
        model = Quote
        fields = ['quote','author']
        exclude = ['tags']
        
class TagForm(ModelForm):
    tag = CharField(
        min_length=3,
        max_length=50,
        required=True,
        widget=TextInput(attrs={'class':'custom-textinput','authocomplete':'off'})
    )
    class Meta:
        model = Tag
        fields = ['tag']


class AuthorForm(ModelForm):
    name = CharField(
        min_length=5,
        max_length=50,
        required=True,
        widget=TextInput(attrs={'class':'custom-textinput','autocomplete':'off'})
    )
    born_date = CharField(widget=TextInput(attrs={'type':'date','class':'custom-textinput','authocomplete':'off'}))

    born_location = CharField(
        min_length=5,
        max_length=50,
        required=True,
        widget=TextInput(attrs={'class':'custom-textinput','autocomplete':'off'})
    )

    description = CharField(
        min_length=20,
        max_length=3000,    
        required=True,
        widget=Textarea(attrs={'class':'custom-textarea'})
    )
    class Meta:
        model = Author
        fields = ['name','born_date','born_location','description']
       