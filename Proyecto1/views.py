from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request):
    doc_view = open('D:/Programacion/Python/Fundamentos/Proyecto1/views/myview.html')
    view = Template(doc_view.read())
    doc_view.close()
    ctx = Context()
    doc_render = view.render(ctx)
    return HttpResponse(doc_render)

def despedida(request):
    return HttpResponse('Adios mundo')


def getDate(request):
    current_date = datetime.datetime.now()
    component = """
        <html>
            <body>
                <h1>Fecha y hora current</h1>
                <p>%s</p>
        </html>
    """ % current_date
    return HttpResponse(component)


def calculate_age(request, edad,agno):
    print("La petición: ", request)
    currentAge = 18
    period = agno - 2021
    futureAge = currentAge + period
    component = """
            <html>
            <body>
                <h1>Edad current del usuario en el año %s</h1>
                <p>%s años</p>
        </html>
    """ %(agno, futureAge)
    return HttpResponse(component)
