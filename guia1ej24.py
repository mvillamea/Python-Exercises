"""Crear un programa que almacene el diccionario con los créditos de las asignaturas de
un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los
créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos,
donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus
créditos. Al final debe mostrar también el número total de créditos del curso."""

creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

print(list(creditos.keys())[0], "tiene ", list(creditos.values())[0], "créditos.")
print(list(creditos.keys())[1], "tiene ", list(creditos.values())[1], "créditos.")
print(list(creditos.keys())[2], "tiene ", list(creditos.values())[2], "créditos.")
print("La cantidad total de créditos es ", list(creditos.values())[0]+list(creditos.values())[1]+list(creditos.values())[2], ".")