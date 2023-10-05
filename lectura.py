import xml.etree.ElementTree as ET
from listaDobleEnlazada import *
from niveles import *
from drones import *
from sistema_drones import *
from dronesPrin import *

listaPrincipal = ListaDoblementeEnlazada()
listaSistema = ListaDoblementeEnlazada()
listaDrones = ListaDoblementeEnlazada()
listaNiveles = ListaDoblementeEnlazada()
import graphviz


class lecXml:
    def lectura(ruta):
        
        global listaPrincipal
        global listaSistema
        global listaDrones
        global listaNiveles
        global tamanos
        global dot
        
        
        tree = ET.parse(ruta)
        root = tree.getroot()
        for dron in root.findall(".//listaDrones/dron"):
            a = dron.text
            b = dronesPrincipales(a)
            listaPrincipal.agregar_al_final(b)
        listaPrincipal.ordenamiento_seleccion()
        
        for sistema in  root.findall(".//listaSistemasDrones/sistemaDrones"):
            nombre = sistema.get("nombre")
            altura_max = sistema.find("alturaMaxima")
            cantidad = sistema.find("cantidadDrones")
            if altura_max is not None :
                alturaMaxima = altura_max.text
            else:
                alturaMaxima = None
            if cantidad is not None:
                cantidadDrones = cantidad.text
            else:
                cantidadDrones = None
            '''print(nombre)
            print(alturaMaxima)
            print(cantidadDrones)'''
            for contenido in sistema.findall("contenido"):
                dron = contenido.find("dron").text
                alturas = contenido.find("alturas")
                #print(dron)
                for altura in alturas.findall("altura"):
                    valor = altura.get("valor")
                    letras = altura.text
                    x1 = Niveles(valor,letras)
                    listaNiveles.agregar_al_final(x1)
                y1 = Drones(dron, listaNiveles)
                listaDrones.agregar_al_final(y1)
                
                listaNiveles = ListaDoblementeEnlazada()
            x2 = Sistema_drones(nombre, alturaMaxima, cantidadDrones, listaDrones)
            listaSistema.agregar_al_final(x2)
            listaDrones.ordenamiento_seleccion()
            listaDrones = ListaDoblementeEnlazada()
            
    def dronesPrincipales():
        pass

    def grafica_sistemas():
        sistemas_en = listaSistema.inicio
        longitud = listaSistema.size
        dot = graphviz.Digraph('html_table', node_attr={
            'shape': 'plaintext', 'width': '-4'})
        dot.attr(bgcolor='#FFFFFF',  # White background
                    label='sistemas de drones', fontcolor='#2C3E50', fontname='Arial')  # Dark blue font
        while sistemas_en:
            for i in range(longitud):
                dot.node(
                    f'{i+1}', fontname='Arial', fontcolor='#2C3E50', label='<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" BGCOLOR="#EAECEE">'  # Light gray table background
                    '<TR>'
                    f'<TD>sistema {i+1}</TD>'
                    '</TR>'
                    '<TR>'
                    f'<TD>{sistemas_en.dato.nombre}</TD>'
                    '</TR>'
                    '</TABLE>>')
                sistemas_en = sistemas_en.siguiente
        dot.render(outfile=f'files/sistemas.png').replace('\\', '/')




