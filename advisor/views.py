from rest_framework.response import Response
from .serializers import AdvisorSerializer,BookingSerializer
from .models import advisor,booking
from rest_framework import viewsets
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View, ListView,DetailView,CreateView,UpdateView, DeleteView


class advisor_list(viewsets.ModelViewSet):
    queryset = advisor.objects.all()
    serializer_class = AdvisorSerializer
    def list(self, request):
        queryset = self.get_queryset()
        serializer = AdvisorSerializer(queryset, many=True)
        return Response(serializer.data)


class booking_list(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = BookingSerializer
    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = BookingSerializer(queryset)
    #     return Response(serializer.data)

    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = BookingSerializer(queryset, many=True)
    #     return Response(serializer.data)
    # def create(self, request,user_id,advisor_id):
    #     serializer = BookingSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response({'msg':'Data Created'}, status=status.HTTP_400_BAD_REQUEST)      


# This class base view is optional 
class advisor_book(viewsets.ViewSet):
    queryset = booking.objects.all()
    def create(self, request,user_id,advisor_id):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'msg':'Data Created'}, status=status.HTTP_400_BAD_REQUEST)    

class base(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'advisor/base.html'


class ProfileDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_detail.html'

    def get(self, request, pk):
        profile = booking.objects.all()
        serializer = BookingSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk,email):
        profile = get_object_or_404(booking, pk=pk)
        serializer = BookingSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return render(request, 'advisor/base.html')


# Create your views here.
class AdvisorBookView(ListView):
    model = booking
    template_name = "advisor/booked_list.html"

class AdvisorCreateView(CreateView):
    model = booking
    fields = ['user','advisor']
    template_name = "advisor/adv_booking.html"  

    def form_valid(self, form,*args, **kwargs):
        form.instance.user = self.request.user
        return super().form_valid(form)  

class AdvisorView(ListView):
    model = advisor
    template_name = "advisor/adv_list.html"    
