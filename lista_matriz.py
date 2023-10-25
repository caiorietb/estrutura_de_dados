class ListaDeMatrizes:
    def __init__(self):
        self.matrizes = []

    def adicionar_matriz(self, matriz):
        self.matrizes.append(matriz)

    def imprimir_matrizes(self):
        if self.matrizes == []:
          print('Não tem matriz')
          print('\n')
        else:
          for i, matriz in enumerate(self.matrizes):
              print(f"Matriz {i + 1}:\n{matriz.data}")

    def remover_matriz(self, matriz):
        if matriz in self.matrizes:
            self.matrizes.remove(matriz)
        else:
            print("A matriz não está na lista.")

    def limpar_lista(self):
        self.matrizes = []

    def salvar_lista(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'w') as file:
                for matriz in self.matrizes:
                    for row in matriz.data:
                        file.write(' '.join(map(str, row)) + '\n')
                    # Adicione uma linha em branco para separar as matrizes
                    file.write('\n')
        except Exception as e:
            print(f"Erro ao salvar a lista de matrizes: {str(e)}")

    def carregar_lista(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as file:
                lines = file.read().split('\n\n')  # Separa as matrizes por linhas em branco
                for matrix_data in lines:
                    matrix_lines = matrix_data.strip().split('\n')
                    data = []
                    for line in matrix_lines:
                        row = list(map(float, line.split()))
                        data.append(row)
                    matriz = Matriz(data)
                    self.matrizes.append(matriz)
        except Exception as e:
            print(f"Erro ao carregar a lista de matrizes do arquivo: {str(e)}")
