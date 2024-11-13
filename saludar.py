import json
import sys


def load_clients():
    try:
        with open('cliente.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_clients():
    with open('cliente.json', 'w') as file:
        json.dump(clients, file, indent=4)


clients = load_clients()

def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
        save_clients()
    else:
        print('El cliente ya ha sido agregado a la lista')

def list_clients():
    print('uid |  nombre  | empresa  | correo electrónico  | puesto ')
    print('*' * 50)
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))

def update_client(client_id, updated_client):
    global clients
    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
        save_clients()
    else:
        print('El cliente no se encuentra')

def delete_client(client_id):
    global clients
    if 0 <= client_id < len(clients):
        del clients[client_id]
        save_clients()
    else:
        print('El cliente no se encuentra')

def search_client(client_name):
    for client in clients:
        if client['name'] == client_name:
            return True
    return False

def _get_client_field(field_name, message='¿Cuál es el {} del cliente?'):
    field = None
    while not field:
        field = input(message.format(field_name))
    return field

def _get_client_from_user():
    client = {
        'name': _get_client_field('nombre'),
        'company': _get_client_field('empresa'),
        'email': _get_client_field('correo electrónico'),
        'position': _get_client_field('puesto'),
    }
    return client

def _print_welcome():
    print('BIENVENIDO A BIGBALD')
    print('-' * 50)
    print('¿QUÉ ES LO QUE DESEAS HACER?')
    print('[C] Crear cliente') 
    print('[U] Actualizar cliente')  
    print('[D] Borrar cliente')  
    print('[S] Buscar cliente')  
    print('[L] Listar clientes')  

if __name__ == '__main__':
    while True:
        _print_welcome()
        command = input().upper()

        if command == 'C':
            client = _get_client_from_user()
            create_client(client)
            list_clients()

        elif command == 'D':
            client_id = int(_get_client_field('ID'))
            delete_client(client_id)
            list_clients()

        elif command == 'L':
            list_clients()

        elif command == 'U':
            client_id = int(_get_client_field('ID'))
            updated_client = _get_client_from_user()
            update_client(client_id, updated_client)
            list_clients()

        elif command == 'S':
            client_name = _get_client_field('nombre')
            found = search_client(client_name)
            if found:
                print('El cliente está en la lista de clientes')
            else:
                print(f'El cliente: {client_name} no se encuentra en nuestra lista de clientes')

        elif command == 'E':
            print("Saliendo del programa...")
            sys.exit()

        else:
            print('Comando inválido')