from OperacoesAritimeticas import OperacoesAritmeticas

class CalculadoraBasica(OperacoesAritmeticas):
 
	def somar(self, n1, n2):   
		return n1 + n2
 
	def subtrair(self, n1, n2):   
		return n1 - n2
 
	def multiplicar(self, n1, n2):   
		return n1 * n2

	def dividir(self, n1, n2):   
		return n1 / n2

calcula = CalculadoraBasica()
x = calcula.somar(5, 3)
print(x)

