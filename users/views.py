"""
This module contains views related to user registration.
It includes a FormView subclass for handling the display and submission of the UserCreationForm.
"""

from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .forms import UserRegistrationForm
from .forms import UserLoginForm

class UserRegistrationFormView(FormView):
    """
    A view for user registration form.

    This view displays a user registration form and handles the form submission.
    Upon successful form submission, the user is registered and redirected to the login page.
    If the form submission is invalid, the user is shown the registration form
    again with an error message.

    Attributes:
          template_name (str): The name of the template to be rendered.
          form_class (class): The form class to be used for user registration.
          success_url (str): The URL to redirect to upon successful form submission.
    """

    template_name = "users/user-auth.html"
    form_class = UserRegistrationForm
    success_url = "/login"

    def form_valid(self, form):
        """
        Handle valid form submission.
        This method is called when the form submission is valid.
        It saves the form data and returns the result of the parent class's form_valid method.

        Args:
              form (Form): The valid form instance.

        Returns:
              HttpResponse: The response returned by the parent class's form_valid method.
        """
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Handle invalid form submission.

        This method is called when the form submission is invalid.
        It renders the registration form again with the invalid form instance and an error message.

        Args:
              form (Form): The invalid form instance.

        Returns:
              HttpResponse: The rendered template with the form and error message.
        """
        return render(
            self.request, self.template_name, {"form": form}
        )
