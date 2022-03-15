programa
{
	
	funcao inicio()
	{
		inteiro numFuncionarios,i
		real salario,mediaSalario,maiorSalario,menorSalario

		faca {
			escreva("Digite a quantidade de funcionários da empresa:\n")
			leia(numFuncionarios)
			limpa()
		} enquanto(numFuncionarios<1)
		
		i=numFuncionarios
		maiorSalario=0
		menorSalario=1000000000
		mediaSalario=0
		
		enquanto(i>0) {
			faca {
				escreva("Digite o salário do funcionário:\n")
				leia(salario)
			} enquanto(salario<0)
			
			se(salario>maiorSalario) {
				maiorSalario=salario
			}
			se(salario<menorSalario) {
				menorSalario=salario
			}
			mediaSalario=mediaSalario+salario
			i--
			limpa()
		}
		mediaSalario=mediaSalario/numFuncionarios
		escreva("A média salarial da empresa é R$",mediaSalario,"\n")
		escreva("O maior salário é R$",maiorSalario," e o menor salário é R$",menorSalario)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 472; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */