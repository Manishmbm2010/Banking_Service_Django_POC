DJANGO_DB_NAME="default"
DJANGO_SU_NAME="admin"
DJANGO_SU_EMAIL="admin@gmail.com"
DJANGO_SU_PASSWORD="password123"
#DJANGO_SETTINGS_MODULE="bankingSystem.settings"
import django,os;
#DJANGO_SETTINGS_MODULE='$DJANGO_SETTINGS_MODULE';
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bankingSystem.settings"); 
django.setup(); 
from django.contrib.auth.management.commands.createsuperuser import get_user_model; 
get_user_model()._default_manager.db_manager(DJANGO_DB_NAME).create_superuser(username=DJANGO_SU_NAME, email=DJANGO_SU_EMAIL, password='$DJANGO_SU_PASSWORD')
