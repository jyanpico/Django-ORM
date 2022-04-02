from django.shortcuts import render
from .models import DashboardPanel
import requests
import pygal

def view_panels(request):
    dboard_panels = DashboardPanel.objects.all()
    response = requests.get('https://api.github.com/users/jyanpico/repos')
    api_data = response.json()
    context = {
        "dboard": dboard_panels,
        "api": api_data
    }
    return render(request, "pages/panels.html", context)

def panel_details(request, panel_id):
    panel = DashboardPanel.objects.get(id=panel_id)

    url = "https://api.github.com/repos/" + panel.github_username + "/" + panel.repo_name + "/languages"
    response = requests.get(url)

    # chart = pygal.Pie()

    # for repo_dict in repos:
    #     value = repo_dict["size"]
    #     label = repo_dict["name"]
    #     chart.add(label, value)
    # chart_svg_as_datauri = chart.render_data_uri()
    # context = {
    #     "panel": panel,
    #     "rendered_chart_svg": chart_svg_as_datauri,
    # }
    
    print('------------------------------------- panel detail testing')
    context = {
        "panel": panel,
        "raw_data": response.json(),
    }
    return render(request, "pages/details.html", context)