# traffic/views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import TrafficData
from .forms import TrafficDataForm

def index(request):
    if request.method == "POST":
        form = TrafficDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
    else:
        form = TrafficDataForm()
    traffic_data = TrafficData.objects.all()
    return render(request, 'traffic/index.html', {'form': form, 'traffic_data': traffic_data})

def analyze(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.send)("capture-packets", {"type": "capture.packets"})
    # Process captured data here or redirect to another page
    anomalies = ["Example anomaly 1", "Example anomaly 2"]
    return render(request, 'traffic/analysis.html', {'anomalies': anomalies})
