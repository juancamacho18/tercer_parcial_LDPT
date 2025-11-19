class matriz:
    @staticmethod
    def mostrar_matriz(A):
        for filas in A:
            print(filas)

    @staticmethod
    def multiplicar_escalar(A, k):
        return [[elem*k for elem in fila] for fila in A]
    
    
    @staticmethod
    def multiplicar_matrices(A, B):
        filas_A, columnas_A=len(A), len(A[0])
        filas_B, columnas_B=len(B), len(B[0])

        if columnas_A!=filas_B:
            raise ValueError("columnas de A != filas de B")

        resultado=[[0 for _ in range(columnas_B)] for _ in range(filas_A)]

        for i in range(filas_A):
            for j in range(columnas_B):
                for k in range(columnas_A):
                    resultado[i][j]+=A[i][k]*B[k][j]
        return resultado
