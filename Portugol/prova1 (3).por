programa
{
	
	funcao inicio()
	{
		real mediaVeiculos,veiculosTotal,mediaVF,mediaVNF,mediaSV,acidentesFTotal,acidentesNFTotal,acidentesSFTotal
		inteiro veiculos[5570],vFatais[5570],vNFatais[5570],vSem[5570],acidentes,x,IVT,i,y,z
		inteiro maiorIVTnum,menorIVTnum
		cadeia nome[5570],maiorIVT,menorIVT
		caracter logica

		IVT=0
		veiculosTotal=0
		acidentesNFTotal=0
		acidentesSFTotal=0
		acidentesFTotal=0
		mediaVeiculos=0
		mediaVF=0
		mediaVNF=0
		mediaSV=0
		x=0
		i=0
		y=0
		z=0
		logica='S'
		maiorIVTnum=0
		menorIVTnum=2147483647
		maiorIVT=""
		menorIVT=""
		
		enquanto(logica=='S' ou logica=='s') {
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
			acidentesFTotal=acidentesFTotal+vFatais[x]
			acidentesNFTotal=acidentesNFTotal+vNFatais[x]
			acidentesSFTotal=acidentesSFTotal+vSem[x]
			IVT=((5*vFatais[x])+(3*vNFatais[x])+(1*vSem[x]))/veiculos[x]

			se(IVT>maiorIVTnum) {
				maiorIVT=nome[x]
				maiorIVTnum=IVT
				y=x
			}
			se(IVT<menorIVTnum) {
				menorIVT=nome[x]
				menorIVTnum=IVT
				z=x
			}

			escreva("\nDeseja incluir dados de um novo município? S-Sim N-Não ")
			leia(logica)

			x++
			i++
			limpa()
		}

			mediaVeiculos=veiculosTotal/i
			mediaVF=acidentesFTotal/i
			mediaVNF=acidentesNFTotal/i
			mediaSV=acidentesSFTotal/i
			escreva("Média de carros por município: ",mediaVeiculos)
			escreva("\nMédia de acidentes com vítimas fatais: ",mediaVF)
			escreva("\nMédia de acidentes com vítimas não-fatais: ",mediaVNF)
			escreva("\nMédia de acidentes sem vítimas: ",mediaSV)
			se(maiorIVTnum==menorIVTnum) {
				escreva("\nO maior IVT:",maiorIVTnum," de ",maiorIVT)
			}
			senao {
				escreva("\nO maior IVT:",maiorIVTnum," de ",maiorIVT)
				escreva("\nO menor IVT:",menorIVTnum," de ",menorIVT)
			}
			escreva("\n")
			se(maiorIVTnum==menorIVTnum) {
				escreva("\n",maiorIVT,":\nQuantidade de veículos: ",veiculos[y],"\nQuantidade de vítimas fatais: ",vFatais[y],"\nQuantidade de vítimas não-fatais: ",vNFatais[y],"\nQuantidade de acidentes sem vítimas: ",vSem[y])
			}
			senao {
				escreva("\n",maiorIVT,":\nQuantidade de veículos: ",veiculos[y],"\nQuantidade de vítimas fatais: ",vFatais[y],"\nQuantidade de vítimas não-fatais: ",vNFatais[y],"\nQuantidade de acidentes sem vítimas: ",vSem[y])
				escreva("\n",menorIVT,":\nQuantidade de veículos: ",veiculos[z],"\nQuantidade de vítimas fatais: ",vFatais[z],"\nQuantidade de vítimas não-fatais: ",vNFatais[z],"\nQuantidade de acidentes sem vítimas: ",vSem[z])
			}
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 2902; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */