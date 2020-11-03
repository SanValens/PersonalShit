#/usr/bin/env python3.8
'''Esta semana la Corte Suprema de Justicia dictó medida de aseguramiento 
en contra del expresidente Uribe. El documento que sustenta la decisión tiene 1554 páginas.
¿Cuántas veces aparece en la numeración de las páginas la cifra 5?'''

respuesta = 0

for i in range(0, 1555):
    for c in str(i):
        if c == '5':
            respuesta += 1
            #print(i, end=', ')

print(f'\n{respuesta}')