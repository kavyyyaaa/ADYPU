from django.shortcuts import render
from clothing.models import dress
from .forms import dressForm

def clothing(request):
    form = dressForm()
    pro_img = dress.objects.all()

    if request.method == "POST":
        form = dressForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request,'clothing/fashion.html',{'pro_img':pro_img, 'form':form})
