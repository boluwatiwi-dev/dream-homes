from .forms import PropertyForm
from django.shortcuts import get_object_or_404


from django.shortcuts import render, redirect, get_object_or_404
from .models import Property, PropertyImage, Favorite
from .models import Property, PropertyImage, Favorite, Inquiry
from django.contrib.auth.decorators import login_required

from .models import Property
from .forms import PropertyForm

def index(request):
    properties = Property.objects.all()
    featured_properties = Property.objects.filter(featured=True)

    location = request.GET.get("location")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    property_type = request.GET.get("property_type")

    if location:
        properties = properties.filter(location__icontains=location)

    if min_price:
        properties = properties.filter(price__gte=min_price)

    if max_price:
        properties = properties.filter(price__lte=max_price)

    if property_type:
        properties = properties.filter(property_type=property_type)

    return render(request, "myapp/index.html", {
        "properties": properties,
        "featured_properties": featured_properties,
        "location": location,
        "min_price": min_price,
        "max_price": max_price,
        "property_type": property_type,
    })

def property_detail(request, id):
    property = get_object_or_404(Property, id=id)

    return render(request, "myapp/property_detail.html", {
        "property": property,
    })


@login_required
def add_property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)

        if form.is_valid():
            property = form.save(commit=False)
            property.owner = request.user
            property.save()
            return redirect("dashboard")

    else:
        form = PropertyForm()

    return render(request, "myapp/add_property.html", {
        "form": form,
    })


@login_required
def dashboard(request):
    properties = Property.objects.filter(owner=request.user)

    total_properties = properties.count()

    total_value = sum(
        property.price for property in properties
    )

    total_favorites = Favorite.objects.filter(
        user=request.user
    ).count()

    total_inquiries = Inquiry.objects.filter(
        owner=request.user
    ).count()

    return render(request, "myapp/dashboard.html", {
        "properties": properties,
        "total_properties": total_properties,
        "total_value": total_value,
        "total_favorites": total_favorites,
        "total_inquiries": total_inquiries,
    })

@login_required
def edit_property(request, id):
    property = get_object_or_404(
        Property,
        id=id,
        owner=request.user
    )

    if request.method == "POST":
        form = PropertyForm(
            request.POST,
            request.FILES,
            instance=property
        )

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    else:
        form = PropertyForm(instance=property)

    return render(request, "myapp/edit_property.html", {
        "form": form,
    })


@login_required
def delete_property(request, id):
    property = get_object_or_404(
        Property,
        id=id,
        owner=request.user
    )

    property.delete()

    return redirect("dashboard")

@login_required
def toggle_favorite(request, id):
    property = get_object_or_404(Property, id=id)

    favorite, created = Favorite.objects.get_or_create(
        user=request.user,
        property=property
    )

    if not created:
        favorite.delete()

    return redirect("property_detail", id=id)

@login_required
def favorites(request):
    favorites = Favorite.objects.filter(user=request.user)

    return render(request, "myapp/favorites.html", {
        "favorites": favorites,
    })

@login_required
def contact_owner(request, id):
    property = get_object_or_404(Property, id=id)

    if request.method == "POST":
        Inquiry.objects.create(
            property=property,
            owner=property.owner,
            name=request.POST["name"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            message=request.POST["message"],
        )

        return redirect("property_detail", id=property.id)

    return render(request, "myapp/contact_owner.html", {
        "property": property,
    })

@login_required
def my_inquiries(request):
    inquiries = Inquiry.objects.filter(
        owner=request.user
    ).order_by("-created_at")

    return render(request, "myapp/my_inquiries.html", {
        "inquiries": inquiries,
    })

from django.contrib.auth.decorators import login_required


@login_required
def edit_property(request, id):

    property = get_object_or_404(
        Property,
        id=id,
        owner=request.user
    )

    if request.method == "POST":

        form = PropertyForm(
            request.POST,
            request.FILES,
            instance=property
        )

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    else:

        form = PropertyForm(instance=property)

    return render(
        request,
        "myapp/edit_property.html",
        {
            "form": form,
            "property": property,
        },
    )

@login_required
def delete_property(request, id):

    property = get_object_or_404(
        Property,
        id=id,
        owner=request.user
    )

    if request.method == "POST":
        property.delete()
        return redirect("dashboard")

    return render(
        request,
        "myapp/delete_property.html",
        {
            "property": property,
        },
    )