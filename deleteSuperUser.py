from django.contrib.auth.models import User
User.objects.get(username="joebloggs", is_superuser=True).delete()
