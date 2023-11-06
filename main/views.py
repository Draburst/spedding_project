
from django.views.generic import TemplateView


class General_stor(TemplateView):

    
    template_name = 'registration/base.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        return contex
    


