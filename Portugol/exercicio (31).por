programa
{
	
	funcao inicio()
	{
		inteiro num1,num2,num3,num4
		escreva("Digite um número inteiro: ")
		leia(num1)
		escreva("Digite um número inteiro: ")
		leia(num2)
		escreva("Digite um número inteiro: ")
		leia(num3)
		escreva("Digite um número inteiro: ")
		leia(num4)
		
		inteiro soma=0
		se(num1%2!=0) {
			soma=soma+num1
		}
		se(num2%2!=0) {
			soma=soma+num2
		}
		se(num3%2!=0) {
			soma=soma+num3
		}
		se(num4%2!=0) {
			soma=soma+num4
		}
		escreva("A soma dos números impares é: ", soma)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 509; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */