import os

class Usuario:
    def __init__(self, id, nombre, apellido, correo, telefono):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f"{self.id},{self.nombre},{self.apellido},{self.correo},{self.telefono}"

class GestorUsuarios:
    def __init__(self, archivo='usuarios.txt'):
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'w') as f:
                pass

    def registrar_usuario(self, nombre, apellido, correo, telefono):
        id = self._generar_id()
        usuario = Usuario(id, nombre, apellido, correo, telefono)
        with open(self.archivo, 'a') as f:
            f.write(str(usuario) + "\n")
        print(f"Usuario {nombre} registrado con ID {id}.")

    def eliminar_usuario(self, id):
        usuarios = self._cargar_usuarios()
        usuarios_filtrados = [usuario for usuario in usuarios if usuario.id != id]
        if len(usuarios) == len(usuarios_filtrados):
            print(f"No se encontró un usuario con el ID {id}.")
            return
        self._guardar_usuarios(usuarios_filtrados)
        print(f"Usuario con ID {id} eliminado.")

    def actualizar_usuario(self, id, nombre=None, apellido=None, correo=None, telefono=None):
        usuarios = self._cargar_usuarios()
        for usuario in usuarios:
            if usuario.id == id:
                if nombre:
                    usuario.nombre = nombre
                if apellido:
                    usuario.apellido = apellido
                if correo:
                    usuario.correo = correo
                if telefono:
                    usuario.telefono = telefono
                self._guardar_usuarios(usuarios)
                print(f"Usuario con ID {id} actualizado.")
                return
        print(f"No se encontró un usuario con el ID {id}.")

    def ver_usuarios(self):
        usuarios = self._cargar_usuarios()
        if not usuarios:
            print("No hay usuarios registrados.")
        for usuario in usuarios:
            print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Apellido: {usuario.apellido}, Correo: {usuario.correo}, Teléfono: {usuario.telefono}")

    def _cargar_usuarios(self):
        usuarios = []
        with open(self.archivo, 'r') as f:
            for linea in f:
                id, nombre, apellido, correo, telefono = linea.strip().split(',')
                usuarios.append(Usuario(id, nombre, apellido, correo, telefono))
        return usuarios

    def _guardar_usuarios(self, usuarios):
        with open(self.archivo, 'w') as f:
            for usuario in usuarios:
                f.write(str(usuario) + "\n")

    def _generar_id(self):
        usuarios = self._cargar_usuarios()
        if not usuarios:
            return "1"
        return str(int(usuarios[-1].id) + 1)

def menu():
    gestor = GestorUsuarios()
    while True:
        print("\n--- Menú ---")
        print("1. Registrar usuario")
        print("2. Eliminar usuario por ID")
        print("3. Actualizar usuario por ID")
        print("4. Ver usuarios")
        print("5. Salir")
        
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if opcion == 1:
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            telefono = input("Teléfono: ")
            gestor.registrar_usuario(nombre, apellido, correo, telefono)
        elif opcion == 2:
            id = input("Ingresa el ID del usuario a eliminar: ")
            gestor.eliminar_usuario(id)
        elif opcion == 3:
            id = input("Ingresa el ID del usuario a actualizar: ")
            nombre = input("Nuevo nombre (deja en blanco para mantener): ")
            apellido = input("Nuevo apellido (deja en blanco para mantener): ")
            correo = input("Nuevo correo (deja en blanco para mantener): ")
            telefono = input("Nuevo teléfono (deja en blanco para mantener): ")
            gestor.actualizar_usuario(id, nombre or None, apellido or None, correo or None, telefono or None)
        elif opcion == 4:
            gestor.ver_usuarios()
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
