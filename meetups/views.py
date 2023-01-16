from django.shortcuts import render, redirect

from .models import Meetup, Participant
from .forms import RegistrationForm

# Create your views here.
def index(request):
    meetups = Meetup.objects.all()

    return render(request, "meetups/index.html",
                  {'show_meetups': True,
                  'meetups': meetups}
                  )

def meetup_details(request, meetup_slug):
    try:
        meetup_details = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                # participant = registration_form.save()
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                meetup_details.participants.add(participant)
                return redirect("confirm-registration", meetup_slug=meetup_slug)

        return render(request, "meetups/meetup-details.html",  {
                        'meetup_found': True,
                        'meetup': meetup_details,
                        'form': registration_form
                    })
    except Exception as exc:
        print(exc)
        return render(request, "meetups/meetup-details.html",
                      {'meetup_found': False
                      })

def confirm_registration(request, meetup_slug):
    meetup_details = Meetup.objects.get(slug=meetup_slug)
    return render(request, "meetups/registration-success.html",
                  {
                      'organizer_email': meetup_details.organizer_email
                  })
