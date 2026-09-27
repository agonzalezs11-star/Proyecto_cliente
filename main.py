from models import Cliente

ana = Cliente(1, "  ana  ", "pérez", "ANA@Ejemplo.com", "0987654321", "guayaquil", "Av. 1")

print(ana.nombre)
print(ana.email)
print(ana.nombre_completo)
print(ana.dominio_email)
print(Cliente.total_creados)

ana.ciudad = "quito"
print(ana.ciudad)

print(ana._Cliente__nombre)