import csv, io
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import MockData

from .forms import MockDataForm


def mockdata(request):
    template = "mockdata.html"

    if request.method == "POST":
        form = MockDataForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = MockDataForm()

    context = {
        'form': form,
    }

    return  render(request, template, context)

def MockData_update_view(request, id):

    form = MockDataForm(instance=MockData.objects.get(PID=id))
    if request.method == "POST":
        form = MockDataForm(request.POST, instance=MockData.objects.get(PID=id))

        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, "mockdata.html", context)

def MockData_delete_view(request, id):
    form = id
    template = "mockdata_delete.html"
    if request.method == "POST":

        MockData.objects.filter(PID=id).delete()
        print("hi2")
        return redirect('/')

    context = {
        "object": form
    }

    return render(request, template, context)

def MockData_deleteall_view(request):
    template = "mockdata_delete.html"
    if request.method == "POST":

        MockData.objects.all().delete()
        print("hi2")
        return redirect('/')

    context = {
        "object": "the whole database"
    }

    return render(request, template, context)


@permission_required("admin.can_add_log_entry")
def mockData_Upload(request):
    template = "MockData_Upload.html"

    prompt = {
        'order': 'Order of CSV should be ID, Hist...'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_files = request.FILES['file']

    if not csv_files.name.endswith('.csv'):
        messages.error(request, 'This is not a CSV file')

    data_set = csv_files.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=','):
        _, created = MockData.objects.update_or_create(
            PID=column[0],
            Histology_A_0=column[1],
            Histology_B_0=column[2],
            Histology_C_0=column[3],
            Biomarker_M_0=column[4],
            Biomarker_H_0=column[5],
            Biomarker_T_0=column[6],
            Biomarker_L_0=column[7],
            Biomarker_A_0=column[8],
            Histology_A_12=column[9],
            Histology_B_12=column[10],
            Histology_C_12=column[11],
            Biomarker_M_12=column[12],
            Biomarker_H_12=column[13],
            Biomarker_T_12=column[14],
            Biomarker_L_12=column[15],
            Biomarker_A_12=column[16]
        )
    comtext = {}
    return render(request, template, comtext)


@permission_required("admin.can_add_log_entry")
def mockData_Download(request):

    items = MockData.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mockdata.csv"'

    writer = csv.writer(response, delimiter=',')

    writer.writerow(['PID',
            'Histology_A_0',
            'Histology_B_0',
            'Histology_C_0',
            'Biomarker_M_0',
            'Biomarker_H_0',
            'Biomarker_T_0',
            'Biomarker_L_0',
            'Biomarker_A_0',
            'Histology_A_12',
            'Histology_B_12',
            'Histology_C_12',
            'Biomarker_M_12',
            'Biomarker_H_12',
            'Biomarker_T_12',
            'Biomarker_L_12',
            'Biomarker_A_12'])

    for obj in items:
        writer.writerow([obj.PID,
            obj.Histology_A_0,
            obj.Histology_B_0,
            obj.Histology_C_0,
            obj.Biomarker_M_0,
            obj.Biomarker_H_0,
            obj.Biomarker_T_0,
            obj.Biomarker_L_0,
            obj.Biomarker_A_0,
            obj.Histology_A_12,
            obj.Histology_B_12,
            obj.Histology_C_12,
            obj.Biomarker_M_12,
            obj.Biomarker_H_12,
            obj.Biomarker_T_12,
            obj.Biomarker_L_12,
            obj.Biomarker_A_12])

    return response

