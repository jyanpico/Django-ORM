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
    
    language_url = "https://api.github.com/repos/" + panel.github_username + "/" + panel.repo_name + "/languages"
    response = requests.get(language_url)
    repos = response.json()

    chart = pygal.Pie()
    for repo in repos:
        value = repos[repo]
        label = repo
        chart.add(label, value)
    chart_svg_as_datauri = chart.render_data_uri()
    context = {
        "panel": panel,
        'github_repo': repos,
        "rendered_chart_svg_as_datauri": chart_svg_as_datauri,
    }

    return render(request, "pages/details.html", context)