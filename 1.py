import socket


PORT = 80

host = input('Введите имя хоста: ')
resource = input('Введите идентификатор ресурса: ')
if not resource:
    resource = '/'
elif resource[0] != '/':
    resource = '/' + resource

client = socket.socket()
client.connect((host, PORT))
request = f'GET {resource} HTTP/1.1\r\nHost:{host}\r\n\r\n'
client.send(request.encode())

response = client.recv(8192).decode()
print(response)