"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Generar una lista con todos los valores múltiplos de 8 comprendidos entre 1 y 500.
"""

multiplos8=[valor for valor in range(0,501) if valor%8==0]
print(multiplos8)