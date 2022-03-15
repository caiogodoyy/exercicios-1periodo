programa
{
	
	funcao inicio()
	{
		inteiro r,g,b
		escreva("Digite o valor de R, entre 0 e 255\n")
		leia(r)
		escreva("Digite o valor de G, entre 0 e 255\n")
		leia(g)
		escreva("Digite o valor de B, entre 0 e 255\n")
		leia(b)

		se(r==0) {
			se(g==0) {
				se(b==0) {
					escreva("\nA cor representada é preto")
				}
			}
		}

		se(r==255) {
			se(g==255) {
				se(b==255) {
					escreva("\nA cor representada é branco")
				}
			}
		}

		se(r>0) {
			se(r<255) {
				se(g==r) {
					se(b==r) {
						escreva("\nA cor representada é cinza")
					}
				}
			}
		}

		se(r>g) {
			se(r>b) {
				escreva("\nA cor representada é vermelho")
			}
		}
		
		se(g>r) {
			se(g>b) {
				escreva("\nA cor representada é verde")
			}
		}

		se(b>g) {
			se(b>r) {
				escreva("\nA cor representada é azul")
			}
		}

		se(r==g) {
			se(r>b) {
				escreva("\nA cor representada é amarelo")
			}
		}

		se(r==b) {
			se(r>g) {
				escreva("\nA cor representada é magenta")
			}
		}

		se(g==b) {
			se(g>r) {
				escreva("\nA cor representada é ciano")
			}
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1047; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */