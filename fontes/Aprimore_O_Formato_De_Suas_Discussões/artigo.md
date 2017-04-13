# Escrita, leitura e organização

\DECORAR{O}{} principal ponto da escrita é trazer ideias, informações ou conhecimento para o leitor. Este irá entender o texto melhor se estas ideias estiverem bem estruturadas, e irá ver e sentir esta estrutura muito melhor se a forma tipográfica refletir a estrutura lógica e semântica do contexto.[^1]


[^1]: Ver capítulo 2 [daqui](https://www.ime.usp.br/~reverbel/mac212"-02/material/lshortBR.pdf).

O parágrafo é uma básica e importante unidade do texto que deve ser constituído por um pensamento coerente ou uma ideia. Suas quebras e continuações podem auxiliar o leitor a compreender o texto, uma vez que indicam uma alteração ou extensão de uma linha de pensamento. Desta forma, o leitor também lida com cadeias de pensamentos distintos e suas relações internas.
Você também deveria estruturar seus parágrafos em um nível mais alto, colocando os mesmos em capítulos, seções, subseções... para ajudar o leitor a encontrar"-se em seu trabalho.

Uma estruturação ainda superior existe na relação entre textos distintos. Todos podemos nos beneficiar com a possibilidade da categorização, correlação (incluindo a ramificação) e do _feedback/and"-forth_, pois a especialização e nível crítico sobre um assunto é facilitada.

## Uma alternativa ao Facebook e aos blogs

O _Facebook_ é muito popular e facilita a disseminação de textos curtos e médios. Porém suas discussões são limitadas em tipografia, espaço e estrutura. Como resultado, textos médios e longos exigem um maior esforço do leitor.
Nesta plataforma, exceto aqueles mantidos por uma página, não é prático de se organizar e correlacionar textos distintos, até mesmo para serem usados como referência. Existe uma necessidade de ser ativamente respondido, caso contrário, a tendência é que seja abandonado.
Esta é a filosofia da plataforma: não se ater muito aos textos antigos e ter um assunto que flui e é disperso em várias e incessantes mensagens.

Nos blogs há uma grande fonte de textos que seriam simplesmente inviáveis se armazenados pelo e expostos no _Facebook_. Possibilitam uma referência consistente e a correlação facilitada entre os textos, apesar de terem um sistema de _Feedback_ menos dinâmico do que o _Facebook_ pois os textos estão dispersos em vários lugares. Isso não é uma desvantagem, é uma característica que é exigida pela total liberdade estrutural que o escritor tem em sua disposição.

Este site (ancap.ch) faz uso da plataforma _[discourse](https://www.discourse.org/)_ para a exposição e discussão em texto, que pode ser considerado um meio"-termo entre _Facebook_ e blogs próprios. A plataforma _discourse_ recomenda a escrita no formato _Markdown_[^2], que resulta em uma apresentação de forma tão abrangente quanto a dos blogs. Além disto, facilita o _feedback_ entre os usuários pela praticidade de criação de conteúdo e também pela organização de conteúdo através de classificação e correlação.

[^2]: _Markdown_ é uma linguagem de marcação (_markup language_) que consiste em regras de fácil escrita, leitura e manutenção, no qual alguns símbolos são meta"-informações sobre o formato que o leitor verá. É parecido com as mensagens textuais dos emails.

## PDF

As plataformas discutidas até o momento são visualizadas pelo navegador (a partir de seu _HTML_) e, portanto, estão presas aos seus rápidos porém simples algoritmos de tipografia e formatação de texto. A exibição contínua do conteúdo exige uma atenção contínua do leitor. Não é fácil retornar ao último parágrafo depois que sua aba foi fechada, principalmente se alguns dias se passaram. Outra desvantagem desta visualização é a falta de praticidade para a leitura de notações de rodapé, que são normalmente utilizadas em artigos e livros, tornando"-se, na prática, um conteúdo ignorado e perdido. Desta forma, o leitor, já sabendo de tais fatos, tende a penalizar, de maneira antecipada, a leitura de textos maiores.

Os arquivos em PDF não sofrem disto, podem ser lidos _offline_ e quando o leitor desejar. Felizmente, podem ser produzidos e expostos de uma maneira prática.

O programa \LaTeX[^3], através do formatador \TeX[^4] e do texto com marcações em _Markdown_, pode produzir arquivos em PDF com uma formatação de tipografia confortável e consistente, dado as configurações apropriadas. A intuitividade do _Markdown_ limita o potencial de formatação do \LaTeX, mas considero que este arranjo complementa de forma simples e suficiente a visualização do conteúdo deste site.


[^3]: Pronunciado como "LÊiték", foi criado por Leslie Lamport e pode usar o formatador TeX para produzir documentos de alta qualidade tipográfica.


[^4]: Pronunciado "Ték", é um programa criado por Donald E. Knuth e lançado em 1982.

# Editores

No computador, escreve"-se por um editor de texto. Os mais populares são o _MS Word_ e o Bloco de Notas (que estou utilizando agora). Uma grande diferença entre ambos é a incapacidade deste de mudar a forma do texto visto pelo escritor (exceto uma mudança geral da fonte e seu tamanho). Um texto em _Markdown_ conta exatamente com tal incapacidade: conta apenas com algumas marcações textuais que indicam tais formas (como texto em negrito ou sublinhado). Algumas pessoas preferem esta forma de texto (o Bloco de Notas é popular, lembra?) pois não há grandes preocupações nem distrações estéticas no momento em que se produz conteúdo; é como preferir se concentrar em um local mais silencioso ou numa temperatura mais confortável.
Você pode encontrar informações de como utilizar os marcadores em _Markdown_ [aqui](https://br.ancap.ch/t/26). Não se preocupe, é bem óbvio.

![ed1](\fontes/\caminho/editor1.PNG "\\\)Editor padrão da plataforma discourse.")

O editor da figura~\ref{fig:ed1} já vem embutido em toda distribuição padrão do [sistema de discussão](https://www.discourse.org/) utilizado por este site. Tal editor conta com a opção de pré"-visualizar a forma que seu texto terá para o leitor e suporta _boa parte_ das marcações da linguagem _Markdown_. Até 2018 é esperado que o sistema seja atualizado para um mais simples e com mais funcionalidades.
Como cada site pode mostrar um resultado diferente pro leitor a partir do mesmo arquivo _Markdown_, é aconselhável que você confira tal resultado ao publicar seu texto no site. Também é recomendável copiar o conteúdo do texto antes de postá"-lo pois você pode ter perdido conexão e dificilmente recuperará uma versão atualizada de seu texto (já aconteceu comigo).

![ed2](\fontes/\caminho/editor2.PNG "\\\)Editor HackMD.")

O editor da figura~\ref{fig:ed2} é o [HackMD](https://hackmd.io/) e também funciona pelo navegador. Ele suporta o modo de digitação _Emacs_ e _Vim_,[^5] que podem agilizar a escrita caso já se tenha experiência com estas tecnologias - são conhecimentos particularmente úteis para ajustar a formatação na publicação do texto. O editor também tem a opção de mostrar a pré"-visualização, além de poder ser escrito em colaboração com outras pessoas em tempo real, como um _Google Docs_ (mas bem mais "leve"). Vale lembrar que é sempre recomendável ter uma cópia salva dos arquivos _.md_ localmente em seu computador, uma maneira simples de evitar grandes frustações.

[^5]: _Emacs_ e _Vim_ são editores de texto que têm muitas combinações de teclas para ações no texto, como "mover o cursor para o começo da linha" ou "deletar a palavra sob o cursor". Recomendo que procure sobre eles no Google.

# Publicação

## Online

Um navegador desenha na tela de acordo com as instruções no _HTML_ do site. Um texto escrito com notações em _Markdown_ é automaticamente transformado em _HTML_ por este site. Porém tal transformatação possui algumas limitações.

É incapaz de criar notas de rodapé com o direcionamento automático do usuário para o conteúdo da nota. Além disto, você deverá alterar seu texto para deixá"-lo nos conformes seguindo o modelo abaixo, escapando os colchetes:

    Aqui temos um texto que fará uso de uma nota de rodapé[1].
    E no final do texto temos as nossas definições de notas de rodapé:
    \[1\]: A nota de rodapé encontra"-se aqui.


## PDF

Existem conversores de textos em _Markdown_ para documentos em PDF. É recomendado uma produção pelo intermédio do \LaTeX para ter uma alta qualidade tipográfica. Para tal, existem conversores automáticos de textos em _Markdown_ para \LaTeX, porém tais conversores não serão tratados.

### Overleaf

O modelo usado oficialmente por este site pode ser encontrado [aqui](https://br.ancap.ch/t/modelos"-latex"-para"-artigos/36). Para utilizá"-lo, basta seguir suas instruções. Você também pode utilizar como modelo a fonte \LaTeX [deste próprio artigo](https://www.overleaf.com/read/ssjjnsyqwsxt).

### Dicas

É recomendável o aprendizado em \LaTeX caso queira utilizar fórmulas matemáticas e outros _features_ próprio do \LaTeX. Também é recomendável para saber corrigir erros de compilação, que serão **comuns** e serão corrigidos de acordo com a familiaridade com a ferramenta. No entanto, tentarei listar algumas dicas que anotei enquanto produzia alguns PDF's:

* Notas de rodapé:
    * Não funcionam em cabeçalhos;
    * Não podem conter links. Para usá"-los, você deve escrever como no exemplo:

        `<http://link.com>`
    * Devem estar separadas entre si por uma linha em branco.
    * São escritas desta maneira:
      Usando uma nota de rodapé[^1].
      [^1]: Definindo uma nota de rodapé.
* Escapamentos:
    * Os % indicam comentário no \LaTeX. Tome cuidado para escapá"-los para não perder conteúdo;
    * Você deve escapar os símbolos %, & e # com \textbackslash %, \textbackslash & e \textbackslash # respectivamente.
        * Estes símbolos em URL não podem ser escapados. Prefira usar o [encurtador do Google](https://goo.gl/) para substituir tais links. De qualquer forma, a URL fica mais fácil de ser digitada caso seja lida de um documento impresso;
* Imagens:
    * Fonte por URL não funcionam. Devem ser enviadas para a pasta do projeto;
    * Legenda pode ser adicionada seguindo este modelo:
  
      `![referencia](imagem.jpg "Legenda")`;
  
        * E ter seu índice -- que é automaticamente criado -- referenciado, assim: `\ref{fig:referencia}`;
        * E a página onde a figura se encontra, assim: `\pageref{fig:referencia}`;
    * Podem não aparecer no local que você deseja. Você pode querer mudá"-las de posição ou então utilizar o comando `\clearpage` para ter uma página em branco preenchida com figuras que estão "na fila" para serem desenhadas.
* Sempre que for adicionar alguma URL em seu texto deste site (br.ancap.ch), você pode ignorar o título que aparece antes do final da URL, apenas o número do tópico (27, para este tópico) já basta.

Algumas destas dicas podem ser observadas [neste video](https://youtu.be/O"-64IRaZlFs) de demonstração deste processo de geração de PDF.
