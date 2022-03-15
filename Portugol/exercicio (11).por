programa
{
	
	funcao inicio()
	{
		inteiro questoes,x,i
		caracter respostaG[80],respostaA[80]

		questoes=80
		x=1
		i=0
		escreva("Preencha com o GABARITO (letra maiúscula apenas)\n")
		enquanto (questoes>0) {
			escreva(x,"a questão: ")
			leia(respostaG[i])

			i++
			x++
			questoes--
		}
		limpa()
		
		questoes=80
		x=1
		i=0
		escreva("Preencha com as RESPOSTAS DO ALUNO (letra maiúscula apenas)\n")
		enquanto (questoes>0) {
			escreva(x,"a questão: ")
			leia(respostaA[i])

			i++
			x++
			questoes--
		}
		limpa()
		
		questoes=80	
		x=1
		i=0
		enquanto (questoes>0) {
			se(respostaG[i]==respostaA[i]) {
				escreva(x,"a questão: CERTA\n")
			}
			senao {
				escreva(x,"a questão: ERRADA\n")
			}
			
			i++
			x++
			questoes--
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 550; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = vetor, matriz, funcao;
 */