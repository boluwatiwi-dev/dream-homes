from django.contrib import admin
from .models import Property, PropertyImage, Favorite, Inquiry


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 3


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "location",
        "latitude",
        "longitude",
        "price",
        "featured",
        "owner",
    )

    list_filter = (
        "featured",
        "property_type",
    )

    inlines = [PropertyImageInline]


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "property",
        "created_at",
    )


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "property",
        "owner",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "property__title",
    )