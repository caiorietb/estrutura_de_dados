class Matriz:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        if isinstance(other, Matriz):
            if len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
                result = [[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
                return Matriz(result)
            else:
                raise ValueError("As dimensões das matrizes não são compatíveis para a adição.")
        else:
            raise TypeError("A adição é suportada apenas entre objetos Matriz.")

    def __sub__(self, other):
        if isinstance(other, Matriz):
            if len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
                result = [[self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
                return Matriz(result)
            else:
                raise ValueError("As dimensões das matrizes não são compatíveis para a subtração.")
        else:
            raise TypeError("A subtração é suportada apenas entre objetos Matriz.")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = [[self.data[i][j] * other for j in range(len(self.data[0]))] for i in range(len(self.data))]
            return Matriz(result)
        elif isinstance(other, Matriz):
            if len(self.data[0]) == len(other.data):
                result = [[sum(self.data[i][k] * other.data[k][j] for k in range(len(self.data[0]))) for j in range(len(other.data[0]))] for i in range(len(self.data))]
                return Matriz(result)
            else:
                raise ValueError("As dimensões das matrizes não são compatíveis para a multiplicação.")
        else:
            raise TypeError("A multiplicação é suportada apenas entre objetos Matriz e escalares.")

    def transpose(self):
        result = [[self.data[j][i] for j in range(len(self.data))] for i in range(len(self.data[0]))]
        return Matriz(result)

    def traco(self):
        if len(self.data) == len(self.data[0]):
            return sum(self.data[i][i] for i in range(len(self.data)))
        else:
            raise ValueError("O traço só pode ser calculado para matrizes quadradas.")

class MatrizQuadrada(Matriz):
    def determinante(self):
        if len(self.data) == len(self.data[0]):
            if len(self.data) == 1:
                return self.data[0][0]
            elif len(self.data) == 2:
                return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
            else:
                determinant = 0
                for j in range(len(self.data[0])):
                    cofactor = self.data[0][j] * self.cofator(0, j)
                    determinant += cofactor
                return determinant
        else:
            raise ValueError("O determinante só pode ser calculado para matrizes quadradas.")

    def cofator(self, i, j):
        submatrix = [[self.data[x][y] for y in range(len(self.data[0])) if y != j] for x in range(1, len(self.data))]
        submatrix = MatrizQuadrada(submatrix)
        return ((-1) ** (i + j)) * submatrix.determinante()

class MatrizDiagonal(Matriz):
    def __add__(self, other):
        if isinstance(other, MatrizDiagonal) and len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
            result = [[self.data[i][j] + other.data[i][j] if i == j else self.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
            return MatrizDiagonal(result)
        else:
            return super().__add__(other)

    def __sub__(self, other):
        if isinstance(other, MatrizDiagonal) and len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
            result = [[self.data[i][j] - other.data[i][j] if i == j else self.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
            return MatrizDiagonal(result)
        else:
            return super().__sub__(other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = [[self.data[i][j] * other if i == j else self.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
            return MatrizDiagonal(result)
        else:
            return super().__mul__(other)

    def determinante(self):
        if len(self.data) == len(self.data[0]):
            determinant = 1
            for i in range(len(self.data)):
                determinant *= self.data[i][i]
            return determinant
        else:
            raise ValueError("O determinante só pode ser calculado para matrizes diagonais.")

class MatrizTriangularSuperior(Matriz):
    def __init__(self, data):
        super().__init__(data)

    def __add__(self, other):
        if isinstance(other, MatrizTriangularSuperior) and len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
            result = [[self.data[i][j] + other.data[i][j] if j >= i else self.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
            return MatrizTriangularSuperior(result)
        else:
            return super().__add__(other)

    def __sub__(self, other):
        if isinstance(other, MatrizTriangularSuperior) and len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
            result = [[self.data[i][j] - other.data[i][j] if j >= i else self.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
            return MatrizTriangularSuperior(result)
        else:
            return super().__sub__(other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = [[self.data[i][j] * other for j in range(len(self.data[0]))] for i in range(len(self.data))]
            return MatrizTriangularSuperior(result)
        else:
            return super().__mul__(other)

class MatrizTriangularInferior(Matriz):
    def __init__(self, data):
        super().__init__(data)

    def __add__(self, other):
        if isinstance(other, MatrizTriangularInferior) and len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
            result = [[self.data[i][j] + other.data[i][j] if j <= i else self.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
            return MatrizTriangularInferior(result)
        else:
            return super().__add__(other)

    def __sub__(self, other):
        if isinstance(other, MatrizTriangularInferior) and len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
            result = [[self.data[i][j] - other.data[i][j] if j <= i else self.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
            return MatrizTriangularInferior(result)
        else:
            return super().__sub__(other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = [[self.data[i][j] * other for j in range(len(self.data[0]))] for i in range(len(self.data))]
            return MatrizTriangularInferior(result)
        else:
            return super().__mul__(other)
