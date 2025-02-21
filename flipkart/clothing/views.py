from django.shortcuts import render
from clothing.models import dress

def clothing(request):
    pro_img = dress.objects.all()
    return render(request,'clothing/fashion.html',{'pro_img':pro_img})
