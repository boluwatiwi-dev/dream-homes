from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            "title",
            "location",
            "latitude",
            "longitude",
            "price",
            "description",
            "bedrooms",
            "bathrooms",
            "property_type",
            "image",
            "featured",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={"rows": 5}
            ),
        }