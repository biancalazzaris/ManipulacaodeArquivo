'''Criar um sistema Orientado a Objeto que Lê o arquivo iris.data.
Gravar em outro arquivo de saida chamado resultado.txt as seguintes informações:
A quantidade de flores de cada tipo;
e qual é o maior  sepal length  de cada classe de flor.'''

class Flores: 


    def __init__(self):
        self.vetor = []
        self.setosa = 0
        self.versicolor = 0
        self.virginica = 0
        self.SL_setosa = 0
        self.SL_versicolor = 0
        self.SL_viriginica = 0

    def abrir(self):
        self.arquivo= open('iris.data', 'rt')   

    def StringforVetor(self):
        for linha in self.arquivo:
            self.vetor.append(linha.replace('\n', '').split(','))

    def count_flores(self):

        qdte = len(self.vetor)
        for x in range(qdte):
            if (self.vetor[x][4] == 'Iris-setosa'):
                self.setosa +=1
            elif (self.vetor[x][4] == 'Iris-versicolor'):
                self.versicolor +=1
            elif (self.vetor[x][4] == 'Iris-virginica'):
                self.virginica += 1

    def stringToFloat(self):
        for indiceLinha, linha in enumerate(self.vetor):
            for indiceColuna, coluna in enumerate(linha):
                if(coluna.replace('.', '', 1).isdigit()):
                    self.vetor[indiceLinha][indiceColuna] = float(coluna)


    def sepalLength(self):
        for i in range(50):
            print
            if (self.vetor[i][0] >= self.SL_setosa):
                self.SL_vetosa = self.vetor[i][0]
        for i in range(50, 100):
            if (self.vetor[i][0] >= self.SL_versicolor):
                self.SL_versicolor = self.vetor[i][0]
        for i in range(100, 150):
            if (self.vetor[i][0] >= self.SL_viriginica):
                self.SL_viriginica = self.vetor[i][0]


    def close(self):
        self.arquivo.close()

    def resultado(self):
        texto = [
            'A quantidade de flores de cada tipo:',
            '\nE qual o maior sepal length  de cada classe de flor.',
            '\nQuantidade de Iris-setosa: ', str(self.setosa),
            '\nQuantidade de Iris-versicolor: ', str(self.versicolor),
            '\nQuantidade de Iris-virginica: ', str(self.virginica ),
            '\nO maior sepal length da Flor Iris-setosa tem: ', str(self.SL_vetosa), 'cm',
            '\nO maior sepal length da Flor Iris-versicolor tem: ', str(self.SL_versicolor), 'cm',
            '\nO maior sepal length da Flor Iris-virginica tem: ', str(self.SL_viriginica), 'cm',
        ]
        self.resultado = open('resultado.txt', 'wt')

        self.resultado.writelines(texto)

objeto = Flores()
objeto.abrir()
objeto.StringforVetor()
objeto.stringToFloat()
objeto.count_flores()
objeto.sepalLength()
objeto.close()
objeto.resultado()
