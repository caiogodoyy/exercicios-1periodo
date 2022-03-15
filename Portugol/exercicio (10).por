programa
{
	
	funcao inicio()
	{
		inteiro trys
		cadeia senha
		senha="x"

		trys=0
		enquanto(senha!="2020") {
			escreva("Digite a senha: ")
			leia(senha)
			limpa()

			se(senha=="2020") {
				escreva("Acesso permitido")
			}
			senao {
				escreva("Senha incorreta\n")
				trys++
				se(trys>1) {
					escreva(trys," tentativas.\n")
				}
				senao {
					escreva(trys," tentativa.\n")
				}
			}
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 146; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */