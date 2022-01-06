from django.shortcuts import render,redirect

from .forms import CustomUserForm
from .models import CustomUser
from django.urls import reverse

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 

# Create your views here.
def create_custom_user(request):
    form = CustomUserForm()
    context = {
        'form':form,
    }

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.instance.id)
            return redirect(reverse('create-pdf', kwargs={'pk': form.instance.id}))     

    return render(request, 'CustomUser/create-user.html', context)


# def create_user_pdf(request, pk):
#     user = CustomUser.objects.get(id=pk)
#     render_pdf_view(request,user)



def render_pdf_view(request,pk):
    user = CustomUser.objects.get(id=pk)
    template_path = 'CustomUser/create-pdf.html'
    context = {'user': user}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Zaids.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response