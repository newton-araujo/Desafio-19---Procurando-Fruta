<h1>Desafio 19 - Adivinhação da Fruta com Loop While</h1>
<p>
Este código tem como propósito criar um jogo simples em que o usuário tenta adivinhar uma fruta específica (neste caso, "Abacate") através de um loop while.
</p>

<ol>
<h2><li>Inicialização da Variável:</li></h2>
<ul>
<li>Inicia a variável fruta com o valor False. Essa variável será utilizada para armazenar a tentativa do usuário.</li>
</ul>

    fruta = False

<h2><li>Loop While de Adivinhação:</li></h2>
<ul>

<li>Utiliza um loop while que continua até que o valor da variável fruta seja igual a "Abacate".</li>
<li>Dentro do loop, solicita ao usuário que digite o nome de uma fruta usando input.</li>
<li>A entrada do usuário é convertida para a forma capitalizada usando capitalize() para garantir consistência.</li>

</ul>

    while fruta != 'Abacate':
        fruta = input('Digite uma fruta: ').capitalize()

<h2><li>Condição de Parada:</li></h2>
<ul>
<li>Dentro do loop, verifica se a fruta digitada pelo usuário é igual a "Abacate".</li>
<li>Se a condição for verdadeira, utiliza o comando break para sair do loop.</li>
</ul>

    if fruta == 'Abacate':
    break

<h2><li>Mensagem de Conclusão:</li></h2>
<ul>
<li>Fornece uma mensagem de parabéns ao usuário após adivinhar corretamente a fruta.
</li>
</ul>

    print("Parabéns, você acertou a fruta!")
</ol>

<h3>Interatividade:</h3>
<p>
O código cria uma experiência interativa em que o usuário continua a adivinhar a fruta até acertar, proporcionando uma resposta de conclusão personalizada.
</p>

<h3>Conclusão:</h3>
<p>Ao executar este código, o usuário terá a oportunidade de testar suas habilidades de adivinhação até acertar a fruta "Abacate". O loop while é utilizado para garantir a repetição até que a resposta correta seja fornecida.






</p>
