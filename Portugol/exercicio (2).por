programa
{
	
	funcao inicio()
	{
		inteiro espectadores, avaliacao, idade, espectadoresTotal
		real per1, per2, per3, avaliacaoMedia, idadeMedia
		escreva("Qual era a quantidade de pessoas nessa sessão?\n")
		leia(espectadores)
		limpa()

		espectadoresTotal=espectadores
		per1=0
		per2=0
		per3=0
		avaliacaoMedia=0
		idadeMedia=0
		enquanto(espectadores>0) {
			escreva("Qual a idade?\n")
			leia(idade)
			escreva("Qual a avaliação do filme? 3=Ótimo 2=Bom 1=Regular\n")
			leia(avaliacao)
			limpa()
			enquanto(avaliacao>3 ou avaliacao<1) {
				escreva("Erro na leitura da avaliação\n")
				escreva("Qual a avaliação do filme? 3=Ótimo 2=Bom 1=Regular\n")
			leia(avaliacao)
			limpa()
			}
			espectadores--
			idadeMedia=idadeMedia+idade
			avaliacaoMedia=avaliacaoMedia+avaliacao

			se (avaliacao==3) {
				per3=per3+1
			}
			se (avaliacao==2) {
				per2=per2+1
			}
			se (avaliacao==1) {
				per1=per1+1
			}
		}

		per3=(per3/espectadoresTotal)*100
		per2=(per2/espectadoresTotal)*100
		per1=(per1/espectadoresTotal)*100
		
		escreva("A quantidade de pessoas que responderam esse questionario foram ",espectadoresTotal,".\n")
		escreva("A média das idades das pessoas era de ",idadeMedia/espectadoresTotal," anos.\n")
		escreva("O percentual de pessoas que acharam o filme ótimo foi de ",per3,"%.\n")
		escreva("O percentual de pessoas que acharam o filme bom foi de ",per2,"%.\n")
		escreva("O percentual de pessoas que acharam o filme regular foi de ",per1,"%.\n")

		avaliacaoMedia=avaliacaoMedia/espectadoresTotal
		se(avaliacaoMedia>=2.5 e avaliacaoMedia<=3) {
			escreva("A avaliação final do filme foi: ÓTIMO.\n")
		}
		senao se(avaliacaoMedia>1.5 e avaliacaoMedia<2.5) {
			escreva("A avaliação final do filme foi: BOM.\n")
		}
		senao se(avaliacaoMedia>=1 e avaliacaoMedia<=1.5) {
			escreva("A avaliação final do filme foi: REGULAR.\n")
		}
		senao {
			escreva("Erro na leitura da avaliação")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 503; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */