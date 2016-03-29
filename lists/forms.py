from django import forms

class ContactForm(froms.Form):
	item_text = forms.CharField()
	csrfmiddlewaretoken = forms.CharField(**widget=forms.hidden**)