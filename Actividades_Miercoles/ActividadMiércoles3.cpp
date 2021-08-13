#include <stdio.h>
#include<stdlib.h>

char A[9][9];
void mostrar();
void cambiar();
int sudoku[9][9] = {{5,3,4,6,7,0,9,1,2},{6,7,0,1,9,5,3,4,8},{1,9,8,0,4,2,5,6,7},{8,5,9,7,6,1,4,2,0},{4,2,6,8,5,0,7,9,1},{7,0,3,9,2,4,8,5,6},{0,6,1,5,3,7,2,8,4},{2,8,7,4,1,9,6,3,0},{3,4,5,0,8,6,1,7,9}};
int main (){
	
	for (int i=0;i<9;i++){
		for (int j=0;j<9;j++){
			printf("\t%d\t| ",sudoku[i][j]);
		}
	printf("\n\n");
	}
	printf("Ingresa un numero en las coordenadas (0,5)");
	printf("\n");
	cambiar();
	printf("Ingresa un numero en las coordenadas (1,2)");
	printf("\n");
	cambiar();
	printf("Ingresa un numero en las coordenadas (2,3)");
	printf("\n");
	cambiar();
	printf("Ingresa un numero en las coordenadas (3,8)");
	printf("\n");
	cambiar();
	printf("Ingresa un numero en las coordenadas (4,5)");
	printf("\n");
	cambiar();
	printf("Ingresa un numero en las coordenadas (5,1)");
	printf("\n");
	cambiar();
	printf("Ingresa un numero en las coordenadas (6,0)");
	printf("\n");
	cambiar();
	printf("Ingresa un numero en las coordenadas (7,8)");
	printf("\n");
	cambiar();
	printf("Ingresa un numero en las coordenadas (8,3)");
	printf("\n");
	cambiar();
	printf("Felicidades, completaste correctamente el sudoku");
	return 0;
}

void mostrar(){
	for(int i=0;i<9;i++){
		for(int j=0;j<9;j++){
			printf("\t %d\t | ",sudoku[i][j]);
		}
	printf("\n\n");	
	}
}

void cambiar(){
	int fila,columna,nuevo;
	printf("Ingrese las coordenadas para poner el numero");
	printf("\n");
	printf("Ingrese la fila:  ");
	scanf("%d",&fila);
	printf("Ingrese la columna:  ");
	scanf("%d",&columna);
	
	printf("Ingresa el nuevo valor:  ");
	scanf("%d",&nuevo);
	
	sudoku[fila][columna] = nuevo;
	printf("\n");
	system("cls");
	mostrar();	
}

