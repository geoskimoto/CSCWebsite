from django.shortcuts import render
from .forms import BunkReservationForm

@login_required
def bunk_reservation(request):
    if request.method == 'POST':
        form = BunkReservationForm(request.POST)
        if form.is_valid():
            # Process form data
            # Save reservation, etc.
            return redirect('reservation_success')  # Redirect to a success page
    else:
        #NEED TO DO SOMETHING HERE...REDIRECT TO LOGIN SCREEN
        form = BunkReservationForm()
        # return redirect("need to login")
    context = {
        'form': form,
    }
    return render(request, 'bunk_reservation.html')