from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from app01 import models


def graph(request):
    return render(request, 'graph.html')


def graph_data(request):
    series_list = [
        {
            'name': 'LLL',
            'type': 'bar',
            'data': [5, 20, 36, 10, 10, 20]
        },
        {
            'name': 'CCC',
            'type': 'bar',
            'data': [32, 2, 15, 17, 26, 11]
        },
        {
            'name': 'HHH',
            'type': 'bar',
            'data': [17, 15, 16, 29, 16, 53]
        }]
    legend_list = [i['name'] for i in series_list]
    # x_axis = ['1月', '2月', '3月', '4月', '5月', '6月']
    x_axis = [str(i) + '月' for i in range(1, 7)]

    res = {
        'status': True,
        'data':
            {
                'status': True,
                'legend_list': legend_list,
                'x_axis': x_axis,
                'series_list': series_list
            }}

    return JsonResponse(res)
