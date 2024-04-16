# import random
# import pandas as pd
#
# data_es = pd.read_csv('data/data_es.csv')
# data_es_dict = data_es.to_dict(orient='records')
# cuestionario = random.sample(data_es_dict, 65)
# carta_actual = cuestionario[0]
# opciones = carta_actual['opciones'].split("\r\n")
# respuesta = carta_actual['respuesta'].split("\r\n")
# print(opciones)
# print(respuesta)

opciones = ['A. Mantener la infraestructura de la red.', 'B. Parchear el sistema operativo invitado.', 'C. Configurar un grupo de seguridad en instancias EC2 implementadas.', 'D. Proporcionar seguridad física para el hardware subyacente de las instancias EC2.', 'E. Administrar el hipervisor subyacente.']
respuesta = ['B. Parchear el sistema operativo invitado.', 'C. Configurar un grupo de seguridad en instancias EC2 implementadas.']

if respuesta[0] in opciones and respuesta[1] in opciones:
    print('Sí')
else:
    print('No')