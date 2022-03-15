programa
{
	
	funcao inicio()
	{
		real num1,num2,resultado
		inteiro operador
		escreva("-=CALCULADORA=-\n")
		escreva("Digite o primeiro número:\n")
		leia(num1)
		escreva("Digite o segundo número:\n")
		leia(num2)
		limpa()
		escreva("Escolha o operador: 1 para adição, 2 para subtração, 3 para multiplicação e 4 para divisão.\n")
		leia(operador)
		limpa()

		resultado=0
		escolha(operador) {
			caso 1:
				resultado = num1+num2
				pare
			caso 2:
				resultado = num1-num2
				pare
			caso 3:
				resultado = num1*num2
				pare
			caso 4:
				resultado = num1/num2
				pare
		}
		se (operador>4 ou operador<1) {
			escreva("Operação Inválida")	
		}
		senao {
			escreva("O resultado é igual a: ",resultado)
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 365; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */