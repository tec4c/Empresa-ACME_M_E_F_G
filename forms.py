import peewee
from wtfpeewee.orm import model_form
from models import User


RegistrationForm = model_form(User)
print(RegistrationForm)
