programa
{
	
	funcao inicio()
	{
		inteiro dia
		cadeia diaescrito
		escreva("Digite um número do dia da semana (de 1 a 7)\n")
		leia(dia)
		escolha (dia) {
			caso 1:
				diaescrito="Domingo"
				pare
			caso 2:
				diaescrito="Segunda"
				pare
			caso 3:
				diaescrito="Terça"
				pare
			caso 4:
				diaescrito="Quarta"
				pare
			caso 5:
				diaescrito="Quinta"
				pare
			caso 6:
				diaescrito="Sexta"
				pare
			caso 7:
				diaescrito="Sábado"
				pare
			caso contrario:
				diaescrito="INVÁLIDO"
				escreva("Digite de 1 a 7.\n")
		}
		escreva("O dia da semana escolhido foi: ", diaescrito)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 544; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */