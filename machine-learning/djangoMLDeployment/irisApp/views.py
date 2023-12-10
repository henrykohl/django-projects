from django.shortcuts import render # default

from joblib import load
model = load('./savedModels/model.joblib')

# Create your views here.
# 方法一
def predictor(request):
  return render(request, 'main.html')

# 方法二
def predictor(request):
  if request.method == 'POST':
    sepal_length = request.POST['sepal_length']
    sepal_width = request.POST['sepal_width']
    petal_length = request.POST['petal_length']
    petal_width = request.POST['petal_width']
    y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    print(y_pred)
    if y_pred[0] == 0:
      y_pred = 'Setosa'
    elif y_pred[0] == 1:
      y_pred = 'Verscicolor'
    else:
      y_pred = 'Virginica'
    return render(request, 'main.html', {'result': y_pred})
  return render(request, 'main.html')

def formInfo(request):
  # sepal_length = request.GET['sepal_length']
  # sepal_width = request.GET['sepal_width']
  # petal_length = request.GET['petal_length']
  # petal_width = request.GET['petal_width']
  # y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
  # print(y_pred)
  # if y_pred[0] == 0:
  #   y_pred = 'Setosa'
  # elif y_pred[0] == 1:
  #   y_pred = 'Verscicolor'
  # else:
  #   y_pred = 'Virginica'
  # return render(request, 'result.html', {'result': y_pred})
  pass
