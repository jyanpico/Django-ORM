from doctest import REPORT_CDIFF
from django.db import models
import requests
import pygal
# Create your models here.

class DashboardPanel(models.Model):
    github_username = models.CharField(max_length=127)
    repo_name = models.CharField(max_length=127)
    repo_description = models.CharField(max_length=300)
    repo_url = models.URLField(max_length = 200)
    panel_type = models.CharField(max_length=127, choices=[
        ("piechart", "Pie-chart of languages used"),
        ("barchart", "Bar-chart of languages used"),
        ("linechart", "Line-chart of languages used"),
    ])