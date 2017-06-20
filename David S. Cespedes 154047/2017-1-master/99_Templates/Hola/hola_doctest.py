#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: hola.py
# Description: Este modulo responde un saludo según el argumento,
#              incluídas pruebas con DocTest
# Author: Diego Fernando Marin

def saludo():
    """ (string) -> string
    retorna una cadena con saludo adecuado al argumento recibido

    >>> saludo()
    'Hola, Mundo!'
    >>> saludo(None)
    'Hola, Mundo!'
    >>> saludo('')
    'Hola, Mundo!'
    >>> saludo('Juana')
    'Hola, Juana!'
    >>> saludo('Diego')
    'Hola, Diego!'

    """
    return ''

def main():
    """ Programa Principal """
    print(saludo())

# Test
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()

