def inverter_string(s):
    return ''.join(s[i] for i in range(len(s) - 1, -1, -1))

inverter_string('Exemplo')

Resultado
'olpmexE'
