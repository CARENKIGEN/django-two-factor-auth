from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class ResendEmailVerificationView(FormView):
    """
    View for resending the email verification code.
    """
    form_class = forms.AuthenticationTokenForm
    template_name = 'two_factor/core/login.html'

    def form_valid(self, form):
        user = self.request.user
        device = user.totpdevice_set.get()
        
        # Generate a new token
        device.generate_challenge()
        
        messages.success(self.request, _('A new verification code has been sent to your email.'))
        return super().form_valid(form)
