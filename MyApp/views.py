from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings

def generate_qr(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name=form.cleaned_data['restaurant_name']
            url=form.cleaned_data['url']

            #Generate QR
            qr=qrcode.make(url)
            file_name=res_name.replace(" ", "_").lower() + '_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)#../media/rname.png
            qr.save(file_path)

             #Create image url
            qr_url = os.path.join(settings.MEDIA_URL, file_name)


            context={
                'res_name' : res_name,
                'qr_url' : qr_url,
                'file_name' : file_name,
            }

            return render(request, 'qr_result.html', context)
    else:
        form=QRCodeForm()
        context={
            'form': form,
        }
        return render(request, 'generate_qr.html', context)