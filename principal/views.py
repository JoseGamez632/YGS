from django.shortcuts import render


def ventas(request):
    context={
    }
    return render(request, "ventas.html", context)

# def inicial(request):
 #   context={
  #  }
   # return render(request, "index.html", context)