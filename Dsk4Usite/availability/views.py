from django.shortcuts import render

# Create your views here.

from availability.models import Desk, University, DeskInstance, Building

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_desks = Desk.objects.all().count()
    num_instances = DeskInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = DeskInstance.objects.filter(status__exact='a').count()

    context = {
        'num_desks': num_desks,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,

    }

    # Render the HTML template Home_Page.html with the data in the context variable
    return render(request, 'Home_Page.html', context=context)\

def choose_campus(request):
    # links to universities in Database

    universities_list = [i[0] for i in University.objects.values_list('name')]

    context = {
        'universities_list': universities_list
    }

    return render(request, 'Choose_Campus.html', context=context)\

def choose_location(request):
    # links to buildings in Database

    locations_list = [i[0] for i in Building.objects.filter(University=1).values_list('name')]

    context = {
        'locations_list': locations_list
    }

    return render(request, 'Choose_Location.html', context=context)\

def dc_floor_plan(request):
    # links to desks in Database
    num_instances_location = DeskInstance.objects.filter(building= 1 ).count()
    instances_location_status = [i[0] for i in DeskInstance.objects.filter(building=1).values_list('status')]

    desks_list = []

    #red='255,0,0'
    #green='0,255,0'
    #yellow='255,255,0'

    for j in instances_location_status:
        if j == 'a':
            desks_list.append('olivedrab')
        elif j == 'o':
            desks_list.append('firebrick')
        elif j == 'm':
            desks_list.append('gold')


    context = {
        'desks_list': desks_list
    }

    return render(request, 'DC_Floor_Plan.html', context=context)\

def dp_floor_plan(request):
    # links to desks in Database
    num_instances_location = DeskInstance.objects.filter(building= 2 ).count()
    instances_location_status = [i[0] for i in DeskInstance.objects.filter(building=2).values_list('status')]

    desks_list = []

    #red='255,0,0'
    #green='0,255,0'
    #yellow='255,255,0'

    for j in instances_location_status:
        if j == 'a':
            desks_list.append('olivedrab')
        elif j == 'o':
            desks_list.append('firebrick')
        elif j == 'm':
            desks_list.append('gold')


    context = {
        'desks_list': desks_list
    }

    return render(request, 'DP_Floor_Plan.html', context=context)\

def choose_queens(request):
    # links to buildings in Database

    locations_list = [i[0] for i in Building.objects.filter(University=2).values_list('name')]

    context = {
        'locations_list': locations_list
    }

    return render(request, 'Choose_Queens.html', context=context)\

def choose_western(request):
    # links to buildings in Database

    locations_list = [i[0] for i in Building.objects.filter(University=3).values_list('name')]

    context = {
        'locations_list': locations_list
    }

    return render(request, 'Choose_Western.html', context=context)\
