programa
{
	
	funcao inicio()
	{
	inteiro duracao
	inteiro hora
	inteiro minuto
	inteiro segundo
	escreva("Vamos calcular quantas horas, minutos e segundos durou seu exame")
	escreva("\nQuantos segundou durou seu exame? ")
	leia(duracao)
	hora=duracao/3600
	minuto=(duracao%3600)/60
	segundo=(duracao%3600)%60
	escreva("\nA duração do exame foi de ",hora,"h, ",minuto,"min e ",segundo,"s.")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 380; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */