from django import forms

# Form for inputting YouTube URL
class YTMediaForm(forms.Form):
    youtube_url = forms.CharField(
        max_length=255,
        label= '',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Paste YouTube URL'
            }
        )
    )

    # Custom clean method to validate the YouTube URL format
    def clean_youtube_url(self):
        url = self.cleaned_data.get('youtube_url')
        if not url.startswith('https://www.youtube.com/watch?v='):
            raise forms.ValidationError("Please enter a valid YouTube URL.")
        return url