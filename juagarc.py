#!/usr/bin/env python
# -*- coding: utf-8 -*-
#	Juan Príncipe Ovelleiro
#	Juan José García Fonsecaç
#
#  juagarc.py

import pygtk
pygtk.require("2.0")
import gtk

class juego:
	
   	def __init__(self):
		filas = 10
		columnas = 10
		#para el marco
		filas+=4
		columnas+=4
		
		self.ventana = gtk.Window(gtk.WINDOW_TOPLEVEL)                  #crea ventana y la pone por encima
		self.ventana.set_border_width(0)								#determina el tamaño de la ventana
		
		
		self.h_colocacion= gtk.HBox(gtk.TRUE, 0)
		self.puntos = gtk.Label('puntos')
		self.h_colocacion.pack_start(self.puntos, gtk.TRUE, gtk.TRUE,0)
		self.puntos.show()
		
		self.deshacer = gtk.Button('deshacer')	
		self.h_colocacion.pack_start(self.deshacer, gtk.TRUE, gtk.TRUE,0)
		self.deshacer.show()
		
		self.v_colocacion= gtk.VBox(gtk.FALSE, 0)
		self.v_colocacion.pack_start(self.h_colocacion,gtk.TRUE,gtk.TRUE,0)		#meto la caja horizontal en la vertical
		self.h_colocacion.show()
		
		self.crearTablero(filas,columnas)
		self.v_colocacion.pack_start(self.tablero, gtk.TRUE, gtk.TRUE,0)
		self.tablero.show()
		
		
		
		self.ventana.add(self.v_colocacion)
		
		self.ventana.set_title("juego de práctica")
		self.ventana.show_all()
		
		    
	def crearTablero(self,filas,columnas):
		#creo una lista a la que añado botones.
		boton=[]
		for i in range(filas):
			boton.append([])
			for j in range(columnas):
				boton[i].append(gtk.Button("."))
		#utilizo una tabla para 
		self.tablero = gtk.Table(filas,columnas, homogeneous=True)
		
		for x in range(2,filas-2):
			for y in range(2,columnas-2):
				self.tablero.attach(boton[x][y], x, x+1, y, y+1,xpadding=1,ypadding=1)

	
	#def golpe():
		
	
		
	def main(self):
		gtk.main()

			
if __name__ == '__main__':
	prueba = juego()
	prueba.main()
