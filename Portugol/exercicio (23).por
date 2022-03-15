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
		senao se(idade<5) {
			escreva("Categoria sem faixa")
		}
		senao se(idade<=7) {
			se(idade>=5) {
				escreva("Você é do infantil.\n")
			}
		}
		senao se(idade<=10) {
			se(idade>=8) {
				escreva("Você é do juvenil.\n")
			}
		}
		senao se(idade<=15) {
			se(idade>=11) {
				escreva("Você é um adolescente.\n")
			}
		}
		senao se(idade<=30) {
			se(idade>=16) {
				escreva("Você é um adulto.\n")
			}
		}
		senao se(idade>30) {
			escreva("Você é um sênior.\n")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 194; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */