from django.shortcuts import render

from g_sheet import data


def main_view(request):
    return render(request, "service/table.html", context={'data':data})