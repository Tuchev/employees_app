import random

from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect

# def home(request):
#     html = f'<h1>{request.method}: This is home</h1>'
#     # return HttpResponseNotFound()
#     # same as: return HttpResponse(status=404)
#     return HttpResponse(
#         html,
#         content_type='application/xml',
#         headers={
#             'x-doncho-header': 'Django',
#         },
#     )
from django.urls import reverse_lazy

from employees_app.employees.models import Department, Employee


def home(request):
    print(reverse_lazy('index'))
    print(reverse_lazy('go to home'))
    print(reverse_lazy('list departments'))
    print(reverse_lazy('department details', kwargs={
        'id': 7,
    }))

    rand_number = random.randint(0, 1024)
    context = {
        'number': rand_number,
    }
    return render(request, 'index.html', context)


def go_to_home(request):
    return redirect('department details', id=random.randint(1, 1024))


def not_found(request):
    # return HttpResponseNotFound()
    raise Http404()


def department_details(request, id):
    if not isinstance(id, int):
        pass
    return HttpResponse(f'This is department {id}, {type(id)}')


def list_departments(request):
    department = Department(
        name=f'New Department {random.randint(1, 1024)}',
    )
    department.save()

    # Update
    department.pk = random.randint(1024, 2048)
    department.save()

    Department.objects.create(
        name=f'New Department {random.randint(1, 1024)}',

    )

    context={
        # 'departments': Department.objects.filter(name__iendswith='app'),
        'departments': Department.objects.prefetch_related('employees_set').all(),
        'employees': Employee.objects.all(),
    }
    return render(request, 'list_departments.html', context)


def create_department(request):
    return HttpResponse('Created')