from django.shortcuts import render
from .forms import inputs
from joblib import load



model = load('./savedModels/model.joblib')
scaler = load('./savedModels/scaler.joblib')
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = inputs(request.POST)
        if form.is_valid():
            age = request.POST['age']
            salary = request.POST['salary']
            X = [[age,salary]]
            X = scaler.transform(X)
            
            prediction = model.predict(X)
            pred = prediction[0]
            #print(pred)
            return render(request, 'mainpage/home.HTML',{'title': 'Result', 'form':form, 'pred':pred })
    else:
        form = inputs()
    return render(request, 'mainpage/home.HTML',{'title': 'Home', 'form':form })


def about(request):
    return render(request, 'mainpage/about.HTML',{'title': 'About'})