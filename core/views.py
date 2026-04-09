from django.shortcuts import render
from .forms import ImageUploadForm

def home(request):
    return render(request, 'core/home.html')

def upload_image(request):
    if request.method=='POST':
        form = ImageUploadForm( request.POST, request.FILES)
        
        if form.is_valid():
            from django.shortcuts import render
from .forms import ImageUploadForm

def upload_image(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)

            # attach user (important)
            instance.user = request.user if request.user.is_authenticated else None

            instance.save()

            return render(request, "result.html", {"data": instance})

    else:
        form = ImageUploadForm()

    return render(request, "core/upload.html", {"form": form})


