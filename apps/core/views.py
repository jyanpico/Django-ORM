from django.shortcuts import render
from .models import DashboardPanel
import requests
import pygal

# Two example views. Change or delete as necessary.


def view_panels(request):
    dboard_panels = DashboardPanel.objects.all()
    context = {
        "dboard_panels": dboard_panels,
    }
    return render(request, "pages/panels.html", context)

def panel_details(request, panel_id):
    panel = DashboardPanel.objects.get(id=panel_id)
    chart = pygal.Pie()

    #unsure how to deal with API data here
    response = requests.get('https://api.github.com/users/kickstartcoding/repos')
    repos = response.json()

    for repo_dict in repos:
        value = repo_dict["size"]
        label = repo_dict["name"]
        chart.add(label, value)
    chart_svg_as_datauri = chart.render_data_uri()
    context = {
        "panel": panel,
        "rendered_chart_svg": chart_svg_as_datauri,
    }
    return render(request, "pages/panel_details.html", context)


