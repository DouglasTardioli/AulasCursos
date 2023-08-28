class Caneta:
    def __init__(self, cor):
        #private or protected
        self._cor = cor #Atributos que começam com _ ou __ não deve ser
                                   #usados fora da Cclass.
    
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor')
        self._cor = valor
        
        
  
caneta = Caneta('Azul')
caneta.cor = 'Pink'
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)