#Programa 1 - TRIANGULO DE SIERPINSKY (Y otros fractales)



#Importamos las librerias
import random
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------

# Helecho

def helecho():
  # Define las funciones de transformación afín
  def f1(x, y):
      return 0, 0.16*y

  def f2(x, y):
      return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6

  def f3(x, y):
      return 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6

  def f4(x, y):
      return -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44

  # Define la función que genera el helecho de Barnsley
  def barnsley_fern(n):
      x, y = 0, 0
      xlist, ylist = [], []
      for i in range(n):
          rand = random.uniform(0, 1)
          if rand < 0.01:
              x, y = f1(x, y)
          elif rand < 0.86:
              x, y = f2(x, y)
          elif rand < 0.93:
              x, y = f3(x, y)
          else:
              x, y = f4(x, y)
          xlist.append(x)
          ylist.append(y)
      return xlist, ylist

  # Genera el helecho de Barnsley
  x, y = barnsley_fern(100000)

  # Visualiza el helecho de Barnsley
  plt.scatter(x, y, s=0.2, c='green')
  plt.axis('off')
  plt.show()

# ------------------------------------------------------------------------------

# Mandelbrot

def Mandelbrot():
  # Define la función que generará el fractal
  def mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, max_iter):
      x, y = np.meshgrid(np.linspace(xmin, xmax, xn), np.linspace(ymin, ymax, yn))
      c = x + y*1j
      z = c
      div_time = max_iter + np.zeros(z.shape, dtype=int)
      for i in range(max_iter):
          z = z**2 + c
          diverge = z*np.conj(z) > 2**2
          div_now = diverge & (div_time==max_iter)
          div_time[div_now] = i
          z[diverge] = 2
      return div_time

  # Define los parámetros del fractal
  xmin, xmax, xn = -2.0, 1.0, 1000
  ymin, ymax, yn = -1.5, 1.5, 1000
  max_iter = 100

  # Genera el fractal
  mandelbrot = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, max_iter)

  # Visualiza el fractal
  plt.imshow(mandelbrot.T, cmap='gray')
  plt.axis('off')
  plt.show()

# ------------------------------------------------------------------------------

# Julia

def Julia():
  # Define la función que generará el fractal
  def julia_set(xmin, xmax, ymin, ymax, xn, yn, c, max_iter):
      x, y = np.meshgrid(np.linspace(xmin, xmax, xn), np.linspace(ymin, ymax, yn))
      z = x + y*1j
      div_time = max_iter + np.zeros(z.shape, dtype=int)
      for i in range(max_iter):
          z = z**2 + c
          diverge = z*np.conj(z) > 2**2
          div_now = diverge & (div_time==max_iter)
          div_time[div_now] = i
          z[diverge] = 2
      return div_time

  # Define los parámetros del fractal
  xmin, xmax, xn = -1.5, 1.5, 1000
  ymin, ymax, yn = -1.5, 1.5, 1000
  max_iter = 100
  c = complex(0.285, 0.01)

  # Genera el fractal
  julia = julia_set(xmin, xmax, ymin, ymax, xn, yn, c, max_iter)

  # Visualiza el fractal
  plt.imshow(julia.T, cmap='hot')
  plt.axis('off')
  plt.show()

# ------------------------------------------------------------------------------

# TRIANGULO DE SIERPINSKY

def Triangulo():
  # Creamos el triangulo
  # Lado Izquierdo
  punto_ladoIzq1 = [500, 750]
  punto_ladoIzq2 = [1500, 2500]

  # Lado Derecho
  punto_ladoDer1 = [2500, 750]

  # Base del Triangulo
  punto_Base1 = [500, 750]
  punto_Base2 = [2500, 750]

  # Unimos los puntos
  x = [punto_Base1[0], punto_Base2[0], punto_ladoIzq1[0], punto_ladoIzq2[0], punto_ladoDer1[0]]
  y = [punto_Base1[1], punto_Base2[1], punto_ladoIzq1[1], punto_ladoIzq2[1], punto_ladoDer1[1]]
  plt.plot(x, y)

  # Eligimos un punto, en este caso, sera el centro del triangulo
  p = [1500, 1500]
  plt.plot(p[0], p[1], marker=".", color="black")

  # Ciclo for que itera n veces en donde va a ir generando los demas triangulos
  for i in range(10000): # Rango Adecuado: 2600 - 10000

      # Elegimos un numero al azar dentro del perimetro del triangulo
      num_Aleatorio = random.randrange(0, 3)

      # Los puntos son de la base (Inicio, Mitad y Final)
      puntosx = [500, 1500, 2500]

      # Los puntos son de la altura (Inicio, Mitad y Final)
      puntosy = [750, 2500, 750]

      # Se calculan los puntos medios de los nuevos triangulos
      # en base al numero que fue obtenido al azar y
      # se le asigna a la base y altura del triangulo
      m = [(p[0]+puntosx[num_Aleatorio])/2,(p[1]+puntosy[num_Aleatorio])/2]

      # Se grafican los puntos
      plt.plot(m[0], m[1], marker=".", color="green")

      # Se guardan los nuevos puntos en base al punto medio
      p = m

  # Se muestra la grafica
  plt.show()

# ------------------------------------------------------------------------------

# MENU INTERACTIVO

def menu_Principal():

  print("¡BIENVENIDO!\nLista de Fractales: ")

  # Opciones a elegir
  print("1. Helecho\n2. Mandelbrot\n3. Julia\n4. Triangulo de Sierpinsky\n5. Salir")

  while True:

    # Ingresa la opcion el usuario
    opciones = int(input("Elige una opcion: "))

    # Si la opcion es = 1, entonces ejecuta la funcion correspondiente
    if opciones == 1:
          print("Fractal - Helecho\n")
          print("Cargando fractal...\n")
          helecho() # Ejecuta la funcion
          print("¡Listo!")

    # Si la opcion es = 2, entonces ejecuta la funcion correspondiente
    elif opciones == 2:
          print("Fractal - Mandelbrot\n")
          print("Cargando fractal...\n")
          Mandelbrot() # Carga la funcion
          print("¡Listo!")

    # Si la opcion es = 3, entonces ejecuta la funcion correspondiente
    elif opciones == 3:
          print("Fractal - Julia\n")
          print("Cargando fractal...\n")
          Julia() # Carga la funcion
          print("¡Listo!")

    # Si la opcion es = 4, entonces ejecuta la funcion correspondiente
    elif opciones == 4:
          print("Fractal - Triangulo de Sierpinsky\n")
          print("Cargando fractal...\n")
          Triangulo() # Carga la funcion
          print("¡Listo!")

    # Si la opcion es = 5, entonces termina el programa
    elif opciones == 5:
          print("¡Hasta Luego!\n")
          return 0

    # Si la opcion es diferente a algunas de las anteriores,
    # entonces le permite al usuario volver a escrirbir alguna opcion
    else:
          print("¡Opcion no valida!\nEliga de nuevo alguna opcion valida: ")

# Ejecuta el menu principal al iniciar el programa
menu_Principal()

# ------------------------------------------------------------------------------