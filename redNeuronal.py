import numpy as np
import matplotlib.pyplot as plt
# red neuronal perceptron con compuertas logicas XOR
class perceptron:
    def __init__(self, n):
        self.pesos = np.random.randn(n)
        self.n = n
    
    def propagacion(self, entradas):
        
        self.salida = 1 * (self.pesos.dot(entradas) > 0)
        self.entradas = entradas

    def actualizacion(self, alfa, salida):

        for i in range(0, self.n):
            self.pesos[i] = self.pesos[i] + alfa * (salida - self.salida)* self.entradas[i]


perceptron_and = perceptron(3)
ejemplos = np.array([[0, 0, 0, 0],[0, 0, 1, 1],[0, 1, 0, 1],[0, 1, 1, 0],[1, 0, 0, 1],[1, 0, 1, 0],[1, 1, 0, 0],[1, 1, 1, 1]])

grad_pesos = [perceptron_and.pesos]
for epoca in range(0, 100):
    for i in range(0, 4):
        perceptron_and.propagacion(ejemplos[i,0:3])
        perceptron_and.actualizacion(0.5, ejemplos[i,3])
        grad_pesos = np.concatenate((grad_pesos, [perceptron_and.pesos]), axis = 0)

plt.plot(grad_pesos[:,0],'k')
plt.plot(grad_pesos[:,1],'r')
plt.plot(grad_pesos[:,2],'b')

plt.show()

print('Hola Mundo')