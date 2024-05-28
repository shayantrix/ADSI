from django import forms

from .models import ConversationMassage

class ConversationMassageForm(forms.ModelForm):
    class Meta:
        model = ConversationMassage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 rounded-xl border'
            })
        }