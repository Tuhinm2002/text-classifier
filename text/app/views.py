from django.shortcuts import render
import pickle

# Create your views here.
def project(request):
    return render(request,'index.html')


def predict(request):
    text_var=request.POST.get("textentry")
    vect=pickle.load(open("Count_vector.pkl","rb"))
    model=pickle.load(open("Model_classifier.pkl","rb"))
    text_trans=vect.transform([text_var]).toarray()
    pred=model.predict(text_trans)
    if pred[0]==1:
        Predictions="Spam"
    elif pred[0]==2:
        Predictions="Sarcastic"
    elif pred[0]==3:
        Predictions="Negative"
    elif pred[0]==4:
        Predictions="Positive"
    else:
        Predictions="Neutral"
    return render(request,'prediction.html',{"Predictions":Predictions})