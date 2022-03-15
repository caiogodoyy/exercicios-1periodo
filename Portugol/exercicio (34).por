programa
{
	
	funcao inicio()
	{
		inteiro A, B
		escreva("Digite o primeiro número\n")
		leia(A)
		escreva("Digite o segundo número\n")
		leia(B)
		
		se(A==B) {
			escreva("O número ", A," é igual ao número ", B,".\n")
		}
		senao se(A<B) {
			escreva("O número ", A," é menor que o número ", B,".\n")
		}
		senao se(A>B) {
			escreva("O número ", A," é maior que o número ", B,".\n")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 215; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */