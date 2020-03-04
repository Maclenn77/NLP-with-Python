#NLTK Book Cheatsheet
#Importa textos en "book" de NLTK
from nltk.book import *

#Esta línea reproduce de qué trata el texto

text1

#Esta línea reproduce el contexto en que ocurre una palabra en determinado texto

text1.concordance('monstrous')

#Esta línea regresa todas las palabras que aparecen en un contexto similar que monstrous

text1.similar('monstrous')

#Esta línea regresa todos los contextos comunes de una palabra y otra

text1.common_contexts(["monstrous", "very"])

#Esta línea regresa la distribución de las palabras en un texto
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

#esta línea genera un texto aleatorio con las palabras del texto

text3.generate()

#Esta línea regresa la longitud del texto, con sus símbolos de puntuación (tokens)

len(text3)

#Si queremos encontrar cuántas palabras distintas se usan en un texto, se debe ordenar en un conjunto
