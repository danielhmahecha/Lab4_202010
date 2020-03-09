"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will b(base) daniel@daniel-Lenovo-IdeaPad-S340-14API:~/Documene useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
from datetime import datetime
from ADT import list as lt
from ADT import orderedmap as map
from DataStructures import listiterator as it



"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos
'''
def newCatalog():
    """
    Inicializa el catálogo y retorna el catalogo inicializado.
    """
    catalog = {'booksTree':None,'booksList':None}
    catalog['booksTree'] = map.newMap ("BST")
    catalog['booksList'] = lt.newList("ARRAY_LIST")
    catalog

    return catalog
'''

def newCatalog():
    '''
    Inicializa catalogo
    '''
    catalog = {'accidentsDateTree':None}
    catalog['accidentsDateTree'] = map.newMap('RBT')
    catalog
    return catalog

def newCatalog_2 ():
    catalog = {'AccidentsTree': None, 'AccidentsList': None}
    catalog['AccidentsTree'] = map.newMap ("RBT")
    catalog['AccidentsList'] = lt.newList("ARRAY_LIST")
    return catalog

def newBook (row):
    """
    Crea una nueva estructura para almacenar un libro 
    """
    book = {"book_id": row['book_id'], "title":row['title'], "average_rating":row['average_rating'], "ratings_count":row['ratings_count']}
    return book

def newAccident (row):
    id = str(row['ID'])
    sub = id[2:]
    subnum = int(sub)
    if (subnum > 999999):
        sub = id[-6:]
        subnum = int (sub)

    string = str(row['Start_Time'])+":"+str(subnum)
    dateAcc = datetime.strptime(string, '%Y-%m-%d %H:%M:%S:%f')
    accident = {'ID' : row['ID'], 'Date_Hour': dateAcc}
    return accident

def addBookList (catalog, row):
    """
    Adiciona libro a la lista
    """
    books = catalog['booksList']
    book = newBook(row)
    lt.addLast(books, book)

def addAccidentList (catalog,row):
    accidents = catalog['AccidentsList']
    accident = newAccident(row)
    lt.addLast(accidents,accident)
    

def addAccidentMap (catalog,row):
    Accident = newAccident(row)
    #dateAcc = datetime.strptime(row['Start_Time'],'%Y-%m-%d %H:%M:%S')
    catalog['AccidentsTree'] = map.put(catalog['AccidentsTree'], Accident['Date_Hour'], Accident, greater)




def addBookMap (catalog, row):
    """
    Adiciona libro al map con key=title
    """
    book = newBook(row)
    #catalog['booksTree'] = map.put(catalog['booksTree'], int(book['book_id']), book, greater)
    catalog['booksTree']  = map.put(catalog['booksTree'] , book['title'], book, greater)
  


# Funciones de consulta


def getBookMap (catalog, bookTitle):
    """
    Retorna el libro desde el mapa a partir del titulo (key)
    """
    return map.get(catalog['booksTree'], bookTitle, greater)

def rankBookMap (catalog, bookTitle):
    """
    Retorna la cantidad de llaves menores (titulos) dentro del arbol
    """
    return map.rank(catalog['booksTree'], bookTitle, greater)

def rankAccidentMap (catalog, DateAccident):
    dateAcc = datetime.strptime(DateAccident, '%Y-%m-%d %H:%M:%S')

    return map.rank(catalog['AccidentsTree'], dateAcc, greater)




# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element['key'] )  

def compareByTitle(bookTitle, element):
    return  (bookTitle == element['title'] )

def greater (key1, key2):
    if ( key1 == key2):
        return 0
    elif (key1 < key2):
        return -1
    else:
        return 1