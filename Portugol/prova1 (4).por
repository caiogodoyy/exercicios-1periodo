programa
{
	
	funcao inicio()
	{
		inteiro sanduiches
		real queijo,presunto,hamburguer
		escreva("Digite a quantidade de sanduíches a fazer: ")
		leia(sanduiches)
		se(sanduiches<0) {
			escreva("Digite a quantidade de sanduíches a fazer: ")
			leia(sanduiches)
		}
		limpa()

		queijo=0.05*sanduiches
		presunto=0.05*sanduiches
		hamburguer=0.1*sanduiches

		escreva("Será preciso ",queijo,"kg de queijo, ",presunto,"kg de presunto e ",hamburguer,"kg de hamburguer.\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 252; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */