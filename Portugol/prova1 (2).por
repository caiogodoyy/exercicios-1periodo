programa
{
	
	funcao inicio()
	{
		inteiro veiculosTotal,acidentesTotal,acidentesFTotal,maisAcidentesNum,menosAcidentesNum
		inteiro veiculos[5570],vFatais[5570],vNFatais[5570],vSem[5570],i,acidentes,x
		cadeia nome[5570],maisAcidentes,menosAcidentes
		
		i=5570
		veiculosTotal=0
		acidentesTotal=0
		acidentesFTotal=0
		maisAcidentesNum=0
		menosAcidentesNum=2147483647
		x=0
		maisAcidentes=""
		menosAcidentes=""
		
		enquanto(i>0) {
			escreva("Digite o nome do município: ")
			leia(nome[x])
			escreva("\nDigite a quantidade de veículos: ")
			leia(veiculos[x])
			escreva("\nDigite a quantidade de acidentes com vítimas fatais: ")
			leia(vFatais[x])
			escreva("\nDigite a quantidade de acidentes com vítimas não-fatais: ")
			leia(vNFatais[x])
			escreva("\nDigite a quantidade de acidentes sem vítimas: ")
			leia(vSem[x])

			acidentes=vFatais[x]+vNFatais[x]+vSem[x]
			veiculosTotal=veiculosTotal+veiculos[x]
			acidentesTotal=acidentesTotal+acidentes
			acidentesFTotal=acidentesFTotal+vFatais[x]

			se(acidentes>maisAcidentesNum) {
				maisAcidentes=nome[x]
				maisAcidentesNum=acidentes
			}
			se(acidentes<menosAcidentesNum) {
				menosAcidentes=nome[x]
				menosAcidentesNum=acidentes
			}

			x++
			i--
			limpa()
		}

		escreva("Quantidade de veículos em todo país: ",veiculosTotal)
		escreva("\nQuantidade de acidentes em todo país: ",acidentesTotal)
		escreva("\nQuantidade de acidentes fatais em todo país: ",acidentesFTotal)
		escreva("\nMunicípio com maior número acidentes: ", maisAcidentes)
		escreva("\nMunicípio com menor número acidentes: ", menosAcidentes)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 261; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */