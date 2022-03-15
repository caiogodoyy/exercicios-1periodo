programa
{
	
	funcao inicio()
	{
		const inteiro NUM_LIVROS = 10000
		inteiro quant_antigos,soma_ano,i,ano,quant_emprestados,ano_atual,media_anual
		caracter emprestado

		soma_ano=0
		quant_antigos = 0
		i = 0
		quant_emprestados = 0

		escreva("Qual é o ano de hoje?\n")							//obtendo o valor do ano_atual
		leia(ano_atual)
		limpa()

		enquanto (i < NUM_LIVROS) {
			escreva("Informe o ano de lançamento do livro:\n")
			leia(ano)
			soma_ano=soma_ano + ano								//soma_ano estava sendo somado +1, o certo seria somar com o ano do lançamento do livro

			se (ano <= ano_atual - 10) {							//ano_atual não tinha sido declarado
				quant_antigos=quant_antigos+1
			}

			escreva("Este livro está emprestado? S=Sim N=Não\n")
			leia(emprestado)

			se (emprestado == 'S' ou emprestado == 's') {
				quant_emprestados=quant_emprestados+1
			}
			i++
			limpa()
		}
		media_anual=soma_ano / i
		escreva("A média de data de lançamento de livros é: ",media_anual,".\n")
		escreva("Quantidade de livros emprestados: ",quant_emprestados,".\n")
		escreva("Quantidade de livros antigos: ",quant_antigos,".\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 67; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */