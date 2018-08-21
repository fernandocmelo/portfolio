from django.shortcuts import render
from django.views.generic import TemplateView
from portfolio_app.models import PersonalData,SocialMedia,PersonalDescription

# Create your views here.
class IndexView(TemplateView):
    template_name = 'portfolio_app/programming.html';

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        context['user_data'] = PersonalData.objects.get(name__icontains='melo')
        context['social_link'] = SocialMedia.objects.order_by('order')
        context['avatar_link'] = SocialMedia.objects.get(social__icontains='Avatar')
        context['user_desc'] = PersonalDescription.objects.order_by('order')

        return context

        # personal_dict = {'user_data':user_data,
        #                  'social_link':social_link,
        #                  'avatar_link':avatar_link,
        #                  'user_desc':user_desc}
        #
        # return render(request,'portfolio_app/programming.html',context=personal_dict)

# def index(request):
#     user_data = PersonalData.objects.get(name__icontains='melo')
#
#     social_link = SocialMedia.objects.order_by('order')
#
#     avatar_link = SocialMedia.objects.get(social__icontains='Avatar')
#
#     user_desc = PersonalDescription.objects.order_by('order')
#
#     personal_dict = {'user_data':user_data,
#                      'social_link':social_link,
#                      'avatar_link':avatar_link,
#                      'user_desc':user_desc}
#
#     return render(request,'portfolio_app/programming.html',context=personal_dict)
