from django import forms
from django.contrib.auth import get_user_model
from .models import Reservation, Bunk


class BunkReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['bunk', 'start_date', 'end_date']
        labels = {
            'bunk': 'Select Bunk',
            'start_date': 'Start Date',
            'end_date': 'End Date',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bunk'].queryset = Bunk.objects.filter(assigned_to=self.current_user)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.member = self.current_user
        if commit:
            instance.save()
        return instance

    @property
    def current_user(self):
        return get_user_model().objects.get(pk=self.request.user.pk)
