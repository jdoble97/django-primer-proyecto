from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request):
    now_date= datetime.datetime.now()
    doc_view = open('D:/Programacion/Python/Fundamentos/Proyecto1/views/myview.html')
    view = Template(doc_view.read())
    p1 = Person('Jorge J.', 'Gonzalez')
    fruits = ['Manzana','Platanos','Pera']
    print('EL TIPO ES',type(len((fruits[1]))))
    doc_view.close()
    ctx = Context({"user_name":p1.get_name(), "now_date": now_date, 'list':fruits})
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

class Person(object):
    def __init__(self, name, last_name):
        self.__name = name
        self.__last_name = last_name
    def get_name(self):
        return self.__name