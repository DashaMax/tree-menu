from django.views.generic import TemplateView

from menu.models import Menu


class MenuView(TemplateView):
    template_name = 'menu/index.html'


class MenuPageView(TemplateView):
    template_name = 'menu/menupage.html'

    def get_context_data(self, **kwargs):
        context = super(MenuPageView, self).get_context_data(**kwargs)
        menu = Menu.objects.get(slug=kwargs['menu'])
        context['name_menu'] = context['title'] = menu

        if 'item' in kwargs:
            item = Menu.objects.get(slug=kwargs['item'])
            context['title'] = item

        return context
