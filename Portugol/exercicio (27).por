programa
{
	
	funcao inicio()
	{
		inteiro valor
		escreva("Digite o valor para ser dividido em cédulas:\n")
		leia(valor)
		limpa()

		se (valor>=200) {
			escreva(valor/200," de R$200")
			valor=valor%200
		}
		se (valor>=100) {
			escreva("\n",valor/100," de R$100")
			valor=valor%100
		}
		se (valor>=50) {
			escreva("\n",valor/50," de R$50")
			valor=valor%50
		}
		se (valor>=20) {
			escreva("\n",valor/20," de R$20")
			valor=valor%20
		}
		se (valor>=10) {
			escreva("\n",valor/10," de R$10")
			valor=valor%10
		}
		se (valor>=5) {
			escreva("\n",valor/5," de R$5")
			valor=valor%5
		}
		se (valor>=2) {
			escreva("\n",valor/2," de R$2")
			valor=valor%2
		}
		se (valor>=1) {
			escreva("\n",valor/1," de R$1")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 732; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */