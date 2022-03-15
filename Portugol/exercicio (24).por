programa
{
	
	funcao inicio()
	{
		real a1,a2,a3,a4,a5,media,ah,am
		inteiro s1,s2,s3,s4,s5,h,m
		escreva("Digite a sua altura\n")
		leia(a1)
		escreva("Digite a seu sexo, 1 para homem, 2 para mulher.\n")
		leia(s1)
		escreva("Digite a sua altura\n")
		leia(a2)
		escreva("Digite a seu sexo, 1 para homem, 2 para mulher.\n")
		leia(s2)
		escreva("Digite a sua altura\n")
		leia(a3)
		escreva("Digite a seu sexo, 1 para homem, 2 para mulher.\n")
		leia(s3)
		escreva("Digite a sua altura\n")
		leia(a4)
		escreva("Digite a seu sexo, 1 para homem, 2 para mulher.\n")
		leia(s4)
		escreva("Digite a sua altura\n")
		leia(a5)
		escreva("Digite a seu sexo, 1 para homem, 2 para mulher.\n")
		leia(s5)
		limpa()

		se(a1>=a2) {
			se(a1>=a3) {
				se(a1>=a4) {
					se(a1>=a5) {
						escreva("\n",a1," é a maior altura")
					}
				}
			}
		}
		se(a2>a1) {
			se(a2>=a3) {
				se(a2>=a4) {
					se(a2>=a5) {
						escreva("\n",a2," é a maior altura")
					}
				}
			}
		}
		se(a3>a1) {
			se(a3>a2) {
				se(a3>=a4) {
					se(a3>=a5) {
						escreva("\n",a3," é a maior altura")
					}
				}
			}
		}
		se(a4>a1) {
			se(a4>a2) {
				se(a4>a3) {
					se(a4>=a5) {
						escreva("\n",a4," é a maior altura")
					}
				}
			}
		}
		se(a5>a1) {
			se(a5>a2) {
				se(a5>a3) {
					se(a5>a4) {
						escreva("\n",a5," é a maior altura")
					}
				}
			}
		}



		se(a1<=a2) {
			se(a1<=a3) {
				se(a1<=a4) {
					se(a1<=a5) {
						escreva("\n",a1," é a menor altura")
					}
				}
			}
		}
		se(a2<a1) {
			se(a2<=a3) {
				se(a2<=a4) {
					se(a2<=a5) {
						escreva("\n",a2," é a menor altura")
					}
				}
			}
		}
		se(a3<a1) {
			se(a3<a2) {
				se(a3<=a4) {
					se(a3<=a5) {
						escreva("\n",a3," é a maior altura")
					}
				}
			}
		}
		se(a4<a1) {
			se(a4<a2) {
				se(a4<a3) {
					se(a4<=a5) {
						escreva("\n",a4," é a menor altura")
					}
				}
			}
		}
		se(a5<a1) {
			se(a5<a2) {
				se(a5<a3) {
					se(a5<a4) {
						escreva("\n",a5," é a menor altura")
					}
				}
			}
		}

		media=(a1+a2+a3+a4+a5)/5
		escreva("\nA média das alturas é: ",media)
		
		ah=0
		am=0
		se(s1==1) {
			ah=ah+a1
		}
		senao se(s1==2) {
			am=am+a1
		}
		se(s2==1) {
			ah=ah+a2
		}
		senao se(s2==2) {
			am=am+a2
		}
		se(s3==1) {
			ah=ah+a3
		}
		senao se(s3==2) {
			am=am+a3
		}
		se(s4==1) {
			ah=ah+a4
		}
		senao se(s4==2) {
			am=am+a4
		}
		se(s5==1) {
			ah=ah+a5
		}
		senao se(s5==2) {
			am=am+a5
		}

		h=0
		m=0
		se(s1==1) {
			h=h+1
		}
		senao se(s1==2) {
			m=m+1
		}
		se(s2==1) {
			h=h+1
		}
		senao se(s2==2) {
			m=m+1
		}
		se(s3==1) {
			h=h+1
		}
		senao se(s3==2) {
			m=m+1
		}
		se(s4==1) {
			h=h+1
		}
		senao se(s4==2) {
			m=m+1
		}
		se(s5==1) {
			h=h+1
		}
		senao se(s5==2) {
			m=m+1
		}
		escreva("\nA média das alturas dos homens é: ",ah/h)
		escreva("\nA média das alturas das mulheres é: ",am/m)
		escreva("\nO número de homens é ",h," e o número de mulheres é ",m)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1802; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */