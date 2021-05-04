import paramiko

host = '192.168.0.130'
user = 'root'
passwd = 'toor'

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)

while True:
    comando = input(('Comando: '))
    entrada, saida, erros = client.exec_command(comando)

    print(saida.readlines())
    print(erros.readlines())