from importlib.metadata import distribution
import matplotlib.pyplot as plot
import dask.array as daskArray
import dask
import sys

# Clase que genera distribuciones de probabilidad, conjuntos de datos y algunos cálculos estadísticos.
class Calculadora_estadistica:

  def __init__(self):
      self.dask_array = None

  def verificar_dimension(self):
    # Asumir por defecto 10000 como el tamaño
    dimension = 10000
    if (len(sys.argv) > 1):
      try:
        # Si se proporciona otro tamaño por línea de comandos, usar ese.
        dimension = int(sys.argv[1])
      except:
        print("Parámetro no es número.")
    return dimension

# 1) Generación de datos.
  def generar_conjunto_datos(self):
    matrix_size = self.verificar_dimension()
    matrixDimentions = (matrix_size, matrix_size)
    # Rango de los números aleatorios a generar:
    lowerLimit = 0
    upperLimit = 10
    # Generar los datos aleatorios y almacenarlos.
    chunks_size = 1000
    self.dask_array = daskArray.random.randint(lowerLimit, upperLimit, size = matrixDimentions, chunks=(chunks_size, chunks_size))
    printLimit = 10000
    # No imprimir todo el arreglo; sólo una parte.
    print(self.dask_array[:printLimit, :printLimit].compute())
    # Operar sobre arreglo:
    self.dask_array = self.dask_array + 2
    # Imprimir el arreglo con la suma anterior aplicada
    print(self.dask_array[:printLimit, :printLimit].compute()) 
    # Efectuar cálculos sobre las medidas de variabilidad del arreglo de números aleatorios:
    print("El promedio de datos del arreglo es:", self.dask_array.mean().compute())
    print("La varianza de datos del arreglo es: ",self.dask_array.var().compute())
    print("La desviación estándar del arreglo es: ", self.dask_array.std().compute())

  # Hace el llamado a generar tres distribuciones de probabilidad.
  def generar_distribuciones(self):
    self.generar_exponencial()
    self.generar_binomial()
    self.generar_chi_cuadrada()

  # Generar datos que siguen una distribución exponencial.
  def generar_exponencial(self):
    # Parámetros generales de una distribución exponencial:
    # Valor de lambda.
    lambda_value = 0.5
    # Tamaño de la distribución de datos.
    distribution_size = 1000000
    exponential_distribution_array = daskArray.random.exponential(lambda_value, size=distribution_size, chunks=10000)
    exponential_distribution_values = exponential_distribution_array.compute()
    self.graficar_distribucion(exponential_distribution_values, 100, True, 0.75, "g", "Distribución Exponencial")

  # Generar datos que siguen una distribución binomial.
  def generar_binomial(self):
    # Parámetros generales de una distribución binomial:
    # Cantidad de pruebas.
    n_tests = 1000000
    # Probabilidad de éxito.
    p_success = 0.5
    # Tamaño de la distribución de datos
    distributionSize = 1000000
    binomial_distribution_array = daskArray.random.binomial(n_tests, p_success, size=distributionSize, chunks=10000)
    binomial_distribution_values = binomial_distribution_array.compute()
    self.graficar_distribucion(binomial_distribution_values, 100, True, 0.75, "b", "Distribución Binomial")

  # Genera los datos necesarios para generar una distribució Chi-Cuadrado
  def generar_chi_cuadrada(self):
    distribution_size = 1000000
    chi_squared_distribution = daskArray.random.chisquare(df=3, size=distribution_size, chunks=100000)
    chi_squared_distribution_values = chi_squared_distribution.compute()
    self.graficar_distribucion(chi_squared_distribution_values, 100, True, 0.75, "y", "Distribución Chi Cuadrada")

  # Grafica una función según los parámetros recibidos.
  def graficar_distribucion(self, array, bin, dens, alp, col, name):
    plot.hist(array, bins=bin, density=dens, alpha=alp, color=col)
    plot.ylabel('Frecuencia de repetición')
    plot.title(name)
    plot.xlabel('Datos')
    plot.show()

# Crea una instancia de la clase Calculadora_estadística y llama a sus métodos.
def main():
  calc = Calculadora_estadistica()
  calc.generar_conjunto_datos()
  calc.generar_distribuciones()

# Llamado al método main.
if __name__ == "__main__":
  main()