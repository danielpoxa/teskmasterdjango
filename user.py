from django.contrib.auth.models import User
user = user.objects.create_user(
    username = 'usuario_teste',
    email = 'teste@example.com',
    password = 'senha123'

) 
print("Usuario criado com sucesso:", User)
