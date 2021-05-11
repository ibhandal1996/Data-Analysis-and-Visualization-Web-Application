from MockData.models import MockData

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

import requests

from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(View):
    def get(self, request, *args, **kwargs):
        callMockData = requests.get('http://127.0.0.1:8000/api/chart/data/')
        result = callMockData.json()
        r1= result['MockData']
        x = request.GET.get("xaxis")
        y = request.GET.get("yaxis")
        request.session['x'] = x
        request.session['y'] = y
        return render(request, 'charts.html', {'MockData': r1})


def get_data(request, *args, **kwargs):
    return JsonResponse() # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs = MockData.objects.all()
        labels = []
        default_items = []
        xAxis = request.session.get('x')
        yAxis = request.session.get('y')

        if not xAxis or not yAxis:
            title = "Biomarker_T_0 vs Biomarker_L_0"
            for item in qs:
                labels.append(item.PID)
                default_items.append({"x": item.Biomarker_T_0, "y": item.Biomarker_L_0})
        else:
            title = str(xAxis) + " vs " + str(yAxis)
            if xAxis == "PID":
                for index, item in enumerate(qs):
                    labels.append(item.PID)
                    default_items.append({"x": index , "y": getattr(item, yAxis)})
            elif yAxis =="PID":
                for index, item in enumerate(qs):
                    labels.append(item.PID)
                    default_items.append({"x": getattr(item, xAxis) , "y": index})
            else:
                for item in qs:
                    labels.append(item.PID)
                    default_items.append({"x": getattr(item, xAxis), "y": getattr(item, yAxis)})
        mk1 = MockData()
        results = [field.name for field in mk1._meta.get_fields()]
        mockData = results[1:]


        data = {
                "MockData": mockData,
                "labels": labels,
                "default": default_items,
                "title": title
        }
        return Response(data)


class DifferenceView(View):
    def get(self, request, *args, **kwargs):
        callMockData = requests.get('http://127.0.0.1:8000/api/diffchart/data/')
        result = callMockData.json()
        r1= result['MockData']
        x = request.GET.get("xaxis")
        y = request.GET.get("yaxis")
        request.session['x'] = x
        request.session['y'] = y
        return render(request, 'charts1.html', {'MockData': r1})

class DifferenceChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs = MockData.objects.all()
        labels = []
        default_items = []
        xAxis = request.session.get('x')
        yAxis = request.session.get('y')

        if not xAxis or not yAxis:
            title = "Biomarker_T vs Biomarker_L"
            for item in qs:
                labels.append(item.PID)
                default_items.append({"x": (item.Biomarker_T_0 - item.Biomarker_T_12), "y": (item.Biomarker_L_0 - item.Biomarker_L_12)})
        else:
            title = str(xAxis) + " vs " + str(yAxis)
            if xAxis == "PID":
                for index, item in enumerate(qs):
                    labels.append(item.PID)
                    default_items.append({"x": index , "y": ((getattr(item, yAxis + "_0")) - (getattr(item, yAxis + "_12")))})
            elif yAxis =="PID":
                for index, item in enumerate(qs):
                    labels.append(item.PID)
                    default_items.append({"x": ((getattr(item, xAxis + "_0")) - (getattr(item, xAxis + "_12"))) , "y": index})
            else:
                for item in qs:
                    labels.append(item.PID)
                    default_items.append({"x": ((getattr(item, xAxis + "_0")) - (getattr(item, xAxis + "_12"))), "y": ((getattr(item, yAxis + "_0")) - (getattr(item, yAxis + "_12")))})
        mockData = ['PID', 'Histology_A', 'Histology_B', 'Histology_C', 'Biomarker_M', 'Biomarker_H', 'Biomarker_T', 'Biomarker_L', 'Biomarker_A']


        data = {
                "MockData": mockData,
                "labels": labels,
                "default": default_items,
                "title": title
        }
        return Response(data)


