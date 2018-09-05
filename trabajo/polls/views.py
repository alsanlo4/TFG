from django.http import HttpResponse
from django.template import loader
import sqlite3

def index(request):
    conexion = sqlite3.connect('ELiRF.db')
    cursor = conexion.cursor()
    
    #Obtener persona/s con rol 0
    cursor.execute('SELECT name, surnames, login FROM Researcher WHERE roll=0 ORDER BY surnames')
        
    data = cursor.fetchall()

    aux1=[]
    #Juntar nombre y apellidos
    for row in data:
        var=[]
        var.append(row[2])
        var.append(row[0] + " " +row[1]+" ")
        aux1.append(var)

    #Obtener persona/s con rol 1    
    cursor.execute('SELECT name, surnames,login FROM Researcher WHERE roll=1 ORDER BY surnames')
        
    data = cursor.fetchall()

    aux2=[]
    #Juntar nombre y apellidos
    for row in data:
        var=[]
        var.append(row[2])
        var.append(row[0] + " " +row[1]+" ")
        aux2.append(var)

    #Obtener persona/s con rol > 1
    cursor.execute('SELECT name, surnames, login FROM Researcher WHERE roll>1 OR roll is NULL ORDER BY surnames')
        
    data = cursor.fetchall()
    
    aux3=[]
    #Juntar nombre y apellidos
    for row in data:
        var=[]
        var.append(row[2])
        var.append(row[0] + " " +row[1]+" ")
        aux3.append(var)

    template=loader.get_template('people.html')
    #aux2=zip(*[iter(aux2)]*3)
    #aux3=zip(*[iter(aux3)]*3)
    context={'lider':aux1, 'integrantes': aux2, 'colaboradores':aux3}
    
    return HttpResponse(template.render(context,request))
