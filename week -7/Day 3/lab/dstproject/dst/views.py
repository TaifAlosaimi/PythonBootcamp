from django.core.files.storage import default_storage
from django.shortcuts import render, redirect

from .forms import UploadForm


def upload(request):

    if request.method == "POST":

        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():

            image = form.cleaned_data["image"]

            file_path = default_storage.save(
                f"uploads/{image.name}",
                image
            )

            request.session["uploaded_image"] = file_path

            return redirect("dst:upload")

    else:
        form = UploadForm()

    uploaded_image = request.session.get("uploaded_image")

    if uploaded_image:
        uploaded_image = default_storage.url(uploaded_image)

    context = {
        "form": form,
        "uploaded_image": uploaded_image,
    }

    return render(request, "dst/upload.html", context)