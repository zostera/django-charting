from django.views.generic import TemplateView

from .charts import DemoChart


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["chart"] = DemoChart()
        return context
