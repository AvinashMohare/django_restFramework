from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def index(request):
    courses = {
        'course_name' : 'Python',
        'learn' : ['flask', 'Django', 'Tornado'],
        'course_provider' : 'Scaler'
    }

    if(request.method == 'GET'):
        return Response(courses)
    
    elif(request.method == 'POST'):
        print('Post is used')
        return Response(courses)