from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):
    PROPERTY_TYPES = [
        ("House", "House"),
        ("Apartment", "Apartment"),
        ("Land", "Land"),
        ("Commercial", "Commercial"),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    title = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    description = models.TextField()

    bedrooms = models.PositiveIntegerField(default=1)

    bathrooms = models.PositiveIntegerField(default=1)

    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPES,
        default="House"
    )

    image = models.ImageField(
        upload_to="properties/",
        blank=True,
        null=True
    )

    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="property_gallery/"
    )

    def __str__(self):
        return f"{self.property.title} Image"


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ("user", "property")

    def __str__(self):
        return f"{self.user.username} ❤️ {self.property.title}"


class Inquiry(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_inquiries"
    )

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.property.title}"