peso = float(input('qual o peso? (kg)*'))
altura= float(input( 'qual e a altura (m)'))
imc= peso / (altura**2)
print('o imc dessa pessoa é de {:.1f}' .format (imc))
if imc < 18.5:
   print(' você esta abaixo do peso normal')
elif 18.5 <= imc <25:
   print('parabens, você esta na faixa de peso normal')
elif 25 <= imc < 30: 
   print('você esta no sobrepeso')
elif 30 <= imc <40:
   print(' você esta com obsidade')
elif imc >= 40:
   print(' voce esta com obesidade morbida, cuidado') 