from django import forms
from . models import Message
from django.forms import HiddenInput

class MessageForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(MessageForm, self).__init__(*args,**kwargs)
        self.fields['sender'].widget = HiddenInput()
        self.fields['recipient'].widget = HiddenInput()
        self.fields['room_name'].widget = HiddenInput()
        self.fields['content'].label = ""

    class Meta:
        model = Message
        fields = ('sender','recipient','room_name','content')
