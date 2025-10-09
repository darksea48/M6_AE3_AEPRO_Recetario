from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from recetario.models import EventosCulinarios

admin_group, created = Group.objects.get_or_create(name='Administradores')
org_group, created = Group.objects.get_or_create(name='Organizadores de eventos')
asist_group, created = Group.objects.get_or_create(name='Asistentes')
print("Grupos listos.")

content_type = ContentType.objects.get_for_model(EventosCulinarios)
add_event_perm = Permission.objects.get(codename='add_eventosculinarios', content_type=content_type)
change_event_perm = Permission.objects.get(codename='change_eventosculinarios', content_type=content_type)
delete_event_perm = Permission.objects.get(codename='delete_eventosculinarios', content_type=content_type)
view_event_perm = Permission.objects.get(codename='view_eventosculinarios', content_type=content_type)

org_group.permissions.add(add_event_perm, change_event_perm, view_event_perm)
admin_group.permissions.add(add_event_perm, change_event_perm, delete_event_perm, view_event_perm)
print("Grupo de permisos asignados.")

# Contraseña para todos los usuarios de prueba
password = "testpassword123"

# Usuario Organizador
if not User.objects.filter(username='user1').exists():
    organizador_user = User.objects.create_user('user1', 'organizador@example.com', password)
    org_group.user_set.add(organizador_user) # Asignar al grupo
    print(f"Usuario '{organizador_user.username}' creado y asignado al grupo 'Organizadores'.")
else:
    print("Usuario 'user1' ya existe.")

# Usuario Cliente
if not User.objects.filter(username='user2').exists():
    asistente_user = User.objects.create_user('user2', 'cliente@example.com', password)
    asist_group.user_set.add(asistente_user) # Asignar al grupo
    print(f"Usuario '{asistente_user.username}' creado y asignado al grupo 'Clientes'.")
else:
    print("Usuario 'user2' ya existe.")

# para salir del shell
exit()