from django.shortcuts import render

def main(request):
    return render(request, 'JointTripApp/index.html')