from django.shortcuts import render, redirect, reverse
from django.views import View
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import datetime
from .models import Appointment

# Create your views here.
class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html',{})
    
    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            subscriber_name = request.POST['subscriber_name'],
            message = request.POST['message'],
            date = datetime.strptime(request.POST['date'], '%Y-%m-%d')
        )

        appointment.save()
        # send_mail(
        #     subject=f'{appointment.subscriber_name}: {appointment.date.strftime("%d.%m.%Y")}',
        #     message=appointment.message,
        #     from_email='akbar.abdullaev82@yandex.ru',
        #     recipient_list=[],
        #     fail_silently=False,
        # )
        # return redirect('appointments:make_appointment.html')
        
        html_content = render_to_string('appointment_created.html',{'appointment':appointment,})
        msg = EmailMultiAlternatives(
            subject=f'{appointment.subscriber_name}: {appointment.date.strftime("%Y.%m.%d")}',
            body=appointment.message,
            from_email='akbar.abdullaev82@yandex.ru',
            to=['abdullaev.akbar@gmail.com',],
            )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        return redirect('appointments:make_appointment')