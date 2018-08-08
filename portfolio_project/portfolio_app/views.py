from django.shortcuts import render
from portfolio_app.models import PersonalData,SocialMedia,PersonalDescription

# Create your views here.
def index(request):
    user_data = PersonalData.objects.get(name__icontains='melo')

    social_link = SocialMedia.objects.order_by('order')

    user_desc = PersonalDescription.objects.order_by('order')

    personal_dict = {'user_data':user_data,
                     'social_link':social_link,
                     'user_desc':user_desc}

    return render(request,'portfolio_app/programming.html',context=personal_dict)
