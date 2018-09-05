from django.shortcuts import render
from itertools import chain
from django.http import Http404, HttpResponse

import datetime

from .models import Paper, Quality, Project, Researcher, Journal, JournalPaper, ConferencePaper, Media, Author, Participate
from .filters import PaperFilter, Calidad, ProjectFilter, Participantes

def search(request):
    paper_list = Paper.objects.all()
    
    #Papers que son conferencias
    paper_list_conference = paper_list.filter(journalpaper__journal__isnull=True)
    #Papers que son Jornadas
    paper_list_journal = paper_list.filter(journalpaper__journal__isnull=False)

    paper_filter = PaperFilter(request.GET, queryset=paper_list)
    qs=paper_filter.qs
    #Calidad seleccionada
    qs_calidad = Calidad(request.GET, queryset=Quality.objects.all())
    
    #Papers filtrados por calidad
    if len(qs_calidad.qs)!=22:
        #Evitar null pointer y mostrar no data
        if len(qs_calidad.qs)==0:
            papers = paper_list.filter(paperquality__quality="not")
            qs= PaperFilter(request.GET, queryset=papers)
            qs=qs.qs
        else:
            papers = paper_list.filter(paperquality__quality=qs_calidad.qs[0].id)
            qs= PaperFilter(request.GET, queryset=papers)
            qs=qs.qs

    participantes = Participantes(request.GET, queryset=Researcher.objects.all())
    if len(participantes.qs)==1:
        qs=qs.filter(author__researcher=participantes.qs[0].login)

    media = Media.objects.all().filter(paper__in = qs.values_list('num', flat=True))

    #Obtener Journals y Conferences de los papers filtrados
    qs_j = JournalPaper.objects.all().filter(num__in=qs.values_list('num', flat=True))
    qs_c = ConferencePaper.objects.all().filter(paper__in=qs.values_list('num', flat=True))
       
    return render(request, 'querys/paper_list.html',{   'filter':paper_filter, 
                                                        'filter2':qs_calidad,
                                                        'filter3':participantes, 
                                                        'qs':qs, 
                                                        'journal':qs_j, 
                                                        'conference':qs_c,
                                                        'media':media
                                                    })


def searchProject(request):
    project_list = Project.objects.all()
    project_filter = ProjectFilter(request.GET, queryset=project_list)

    participantes = Participantes(request.GET, queryset=Researcher.objects.all())

    if len(participantes.qs)==1:
        res = Project.objects.all().filter(participate__researcher=participantes.qs[0].login)
        project_filter = ProjectFilter(request.GET, queryset=res)

    return render(request, 'querys/project_list.html',{'filter':project_filter, 'filter2':participantes})


def paperPublic(request):
    paper_list = Paper.objects.all()
    
    #Papers que son conferencias
    paper_list_conference = paper_list.filter(journalpaper__journal__isnull=True)
    #Papers que son Jornadas
    paper_list_journal = paper_list.filter(journalpaper__journal__isnull=False)

    paper_filter = PaperFilter(request.GET, queryset=paper_list)
    qs=paper_filter.qs

    #Obtener Journals y Conferences de los papers filtrados
    qs_j = JournalPaper.objects.all().filter(num__in=qs.values_list('num', flat=True))
    qs_c = ConferencePaper.objects.all().filter(paper__in=qs.values_list('num', flat=True))
   
    return render(request, 'querys/paper_public.html',{ 'filter':paper_filter, 
                                                        'qs':qs, 
                                                        'journal':qs_j, 
                                                        'conference':qs_c
                                                      })

def personalPages(request,offset):
    r = Researcher.objects.all().filter(login=offset)

    if(len(r)==0):
        #Si el nombre no se encuentra entr los researchers fuerzo un error 404
        try:
            int(offset)
        except ValueError:
            raise Http404()

    print(len(r))
    r=r[0]

    aux=""
    paper=Author.objects.all().filter(researcher=offset)
    for p in paper:
        aux = aux + "- "+ p.paper.title + """.<p style= "text-indent:38px;">"""

    aux2=""
    project = Participate.objects.all().filter(researcher=offset)
    for pro in project:
        aux2=aux2 + "· " + pro.project.title + """.<p style="text-indent:38px;">"""
    
    if r.roll ==0:
        descripcion = "encargado del grupo de investigación"
    elif r.roll==1:
        descripcion = "uno de los integrantes del grupo de investigación"
    else:
        descripcion = "colaborador del grupo o forma parte como becario"

    html="""<html>
            <title> Página personal de %s %s</title>
            <style>
            body
            {
                margin-top: 15px;
                margin-bottom: 80px;
                font-family: Georgia, "Times New Roman", Times, serif;
                color: #000000;
                background: #C8FFFD;
            }
            </style>
            <body>
                <button id="back"><</button>
                <h2> Página persona del %s %s </h2>
                <img src="/home/alsanchez/trabajo/trabajo/static/perfil.jpg"></img> 
                <p> %s %s es %s.</p>
                <p><strong> Correco electrónico:</strong> %s</p>

                <p>Es autor en los siguientes <strong>publicaciones</strong>: </p> <p style= "text-indent:38px;" %s </p>

                <br><br><br> <p> Ha participado en los siguientes <strong>proyectos</strong>: </p> <p style="text-indent:38px;" %s </p>

            </body>
            <script>
                document.getElementById("back").onclick = function(){location.href="http://localhost:8000/es/grupo"}
            </script>
            </html>""" %(r.name, r.surnames, r.name, r.surnames, r.name, r.surnames, descripcion, r.email, aux, aux2)

    return HttpResponse(html)

