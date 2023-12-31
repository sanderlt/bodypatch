from django import forms

class CanvasImageForm(forms.Form):
    base64_data = forms.CharField(widget=forms.HiddenInput)
    # Render results 
    