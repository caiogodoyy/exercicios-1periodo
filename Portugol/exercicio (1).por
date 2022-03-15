programa
{
	
	funcao inicio()
	{
		inteiro idade
		escreva("Qual é a sua idade?\n")
		leia(idade)

		se(idade<=0) {
			escreva("ERRO")
		}
		senao se(idade<=12) {
			escreva("Você é uma criança.\n")
		}
		senao se(idade<=20) {
			escreva("Você é um adolescente.\n")
		}
		senao se(idade<=65) {
			escreva("Você é um adulto.\n")
		}
		senao se(idade<=100) {
			escreva("Você é um idoso.\n")
		}
		senao se(idade>100) {
			escreva("Você está fazendo hora extra.\n")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 463; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */