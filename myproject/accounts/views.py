from .models import CustomUser

# CREATE
def create_user():
    CustomUser.objects.create_user(username="ali", password="123")

# READ
def get_users():
    return CustomUser.objects.all()

# UPDATE
def update_user():
    user = CustomUser.objects.get(id=1)
    user.username = "ahmed"
    user.save()

# DELETE
def delete_user():
    user = CustomUser.objects.get(id=1)
    user.delete()