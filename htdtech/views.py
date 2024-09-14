from django.shortcuts import render
from .models import Session, Course,Prevyearinfo

# from .models import prevyearinfo

# Create your views here.


def home(request):
    return render(request,'home.html')


def contact(request):
    return render(request,'contactinfo.html')


def admissionguidelines(request):
    return render(request,'admissionguidelines.html')

def notification(request):
    return render(request, 'notification.html')

def previousyearinformation(request):

    # for selection - option :
    years = Session.objects.values_list('session_text', flat=True).distinct() 

    # # getting the selection from option:
    selected_year_text = request.POST.get('year', '2023 - 2024')

  

    
    # {..NOTE ---> REMEMBER SATHRIYAN --->:..session table la irunthu years ah eduthunu vaa first, aproma input la vaanguna selection kooda compare pannu .....:}

        ##  suppose kidaikalana empty value ah vitru

    # filtering from the Session table:
    selected_year = Session.objects.filter(session_text=selected_year_text).first()

    # getting all courses:
    courses = Course.objects.all()

    datas=[]
    serialno = 1

    if selected_year:

        for course in courses :

            try:

                # Prevyearinfo---> table la enter panna datas  Session and Course ku match aagutha check pannu:
                                    # match aana eduthunu vaa illana empty ah vitru :



                details = Prevyearinfo.objects.get(Session = selected_year, Course=course)
                prospectus = details.Prospectus.url if details.Prospectus else ''
                meritlist = details.Meritlist.url if details.Meritlist else ''
                schedule = details.Schedule.url if details.Schedule else ''
                allottedlist = details.Allottedlist.url if details.Allottedlist else ''
                amendments = details.Amendments.url if details.Amendments else ''
                cutoff = details.Cutoff.url if details.Cutoff else ''


            except Prevyearinfo.DoesNotExist:
                  prospectus = meritlist = schedule = allottedlist = amendments = cutoff = ''

            
            datas.append({


                'serialno':serialno,
                'session':selected_year.session_text,
                'course':course.course_text,
                'prospectus': prospectus,
                'meritlist': meritlist,
                'schedule': schedule,
                'allotted_list': allottedlist,
                'amendments': amendments,
                'cutoff': cutoff

            })

            serialno = serialno + 1


    return render(request,'previousyearinformation.html',{'selected_year':selected_year_text, 'datas':datas,'years':years})
  
    
    
    




























# def previousyearinformation(request):
#     selected_year = request.GET.get('year', '2023 - 2024')  
#     infos = prevyearinfo.objects.filter(session=selected_year).order_by('sno')
#     return render(request, 'previousyearinformation.html', {
#         'infos': infos,
#         'selected_year': selected_year
#     })


  
# # getting the selection from option:
#     Selectionyearinput = request.GET.get('year','2023 - 2024')  


#     # {..NOTE ---> REMEMBER SATHRIYAN --->:..session table la irunthu years ah eduthunu vaa first, aproma input la vaanguna selection kooda compare pannu .....:}

#         ##  suppose kidaikalana empty value ah vitru

#     # filtering from the Session table:
#     Session_selected = Session.objects.filter(session_text=Selectionyearinput).first()

#     print("Selected Year Input:", Selectionyearinput)

#     # getting all courses:
#     Courses = Course.objects.all()

#     datas = []
#     serialno = 1

    
#     if Session_selected:

#         for course in Courses :

#             try:

#                 # Prevyearinfo---> table la enter panna datas  Session and Course ku match aagutha check pannu:
#                                     # match aana eduthunu vaa illana empty ah vitru :



#                 details = Prevyearinfo.objects.get(Session = Session_selected, Course=course)
#                 prospectus = details.Prospectus.url if details.Prospectus else ''
#                 meritlist = details.Meritlist.url if details.Meritlist else ''
#                 schedule = details.Schedule.url if details.Schedule else ''
#                 allottedlist = details.Allottedlist.url if details.Allottedlist else ''
#                 amendments = details.Amendments.url if details.Amendments else ''
#                 cutoff = details.Cutoff.url if details.Cutoff else ''


#             except Prevyearinfo.DoesNotExist:
#                   prospectus = meritlist = schedule = allottedlist = amendments = cutoff = ''

            
#             datas.append({


#                 'serialno':serialno,
#                 'session':Session_selected.session_text,
#                 'course':course.course_text,
#                 'prospectus': prospectus,
#                 'meritlist': meritlist,
#                 'schedule': schedule,
#                 'allotted_list': allottedlist,
#                 'amendments': amendments,
#                 'cutoff': cutoff

#             })

#             serialno = serialno + 1


#     return render(request,'previousyearinformation.html',{ 'datas' : datas})


