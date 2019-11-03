from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailAuthBackend(ModelBackend):
    user_model = get_user_model()
    """
    Authenticate using email
    """
    def authenticate(self, request, username=None, password=None):
        try:
            user = self.user_model.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except self.user_model.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return self.user_model.objects.get(pk=user_id)
        except self.user_model.DoesNotExist:
            return None
