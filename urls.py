from two_factor.views.core import ResendEmailVerificationView

urlpatterns = [
    # ... existing patterns ...
    path(
        'resend-email-verification/',
        ResendEmailVerificationView.as_view(),
        name='resend_email_verification',
    ),
]
