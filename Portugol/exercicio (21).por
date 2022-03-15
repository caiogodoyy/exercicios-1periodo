programa
{
	
	funcao inicio()
	{
		real saldo,percentual
		escreva("Fale o saldo de certa aplicação: ")
		leia(saldo)
		escreva("Agora diga o percentual de reajuste: ")
		leia(percentual)
		percentual=percentual/100
		escreva("\nO saldo atual é ",saldo*(1+percentual))
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 229; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */