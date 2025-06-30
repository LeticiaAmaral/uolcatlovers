# 🐱 UOLCatLovers - Extrator de Fatos sobre Gatos

Script Python que coleta fatos sobre gatos da API [Cat Facts](https://catfact.ninja/) e exporta para CSV.

## 📋 Pré-requisitos

- Python 3.8+
- Git (opcional)

## 🛠️ Configuração do Ambiente

1. *Clone o repositório*:
   ```bash
   git clone https://github.com/seu-usuario/uoicatlovers.git
   cd uoicatlovers

2. *Crie e ative um ambiente virtual (recomendado)*:
      python -m venv venv

      **Linux/Mac**:

      source venv/bin/activate

      **Windows**:

      .\venv\Scripts\activate

4. *Instale as dependências*:
pip install -r requirements.txt


## 🚀 Como Usar
Execute o script principal:

python cat_facts.py

Isso irá:
    Coletar fatos de todas as páginas da API
    Gerar um arquivo cat_facts_<data>.csv

# Respostas Teste

Imagine que você é um engenheiro de dados em uma startup de tecnologia pet chamada “UOLCatLovers”. A UOLCatLovers está desenvolvendo um aplicativo móvel que fornece fatos interessantes sobre gatos para seus usuários. Os fatos são extraídos da API Cat Facts. 

Documentação em: https://alexwohlbruck.github.io/cat-facts/docs/ 

As respostas devem constar em um repositório no GitHub e o link do repositório deve ser compartilhado para a avaliação. 

1 - Como a startup foi recém criada, ainda não há uma grande demanda pelos dados, então você precisa desenvolver um script Python simples que extraía os dados de fatos sobre gatos (cat facts) da API e salva em um arquivo CSV local. 

**Como a API do https://cat-fact.herokuapp.com/facts não estava disponível foi utilizada a API https://catfact.ninja/facts**
**O código python (cat_lovers_fact.py) e o arquivo csv(cat_facts.csv) se encontram salvos neste repositório para avaliação**

2 - Com o tempo, o aplicativo ganhou popularidade e o número de fatos sobre gatos cresceu exponencialmente. Agora, a solução local não é mais viável e é necessário transpor a solução para a nuvem. Você precisa projetar uma arquitetura na plataforma Google Cloud que seja capaz de extrair, armazenar e disponibilizar os dados para os times de anaytics. Não é necessário implementar ou codificar, apenas desenhar a arquitetura. 

**Para uma aplicação bem simples conseguimos adicionar um código Python diretamente no Cloud Run Functions e salvar o csv no BigQuery, porém para uma aplicação mais robusta o Diagrama sugerido é o seguinte:**

<img src="https://github.com/LeticiaAmaral/uolcatlovers/blob/main/Diagrama.drawio.png?raw=true" alt="Se a imagem estiver indisponivel, por favor verifique o diagrama no arquivo Diagrama.drawio.png">

3 - Com o tempo, o time de analytics também sentiu necessidade de realizar suas próprias consultas sobre os dados, como a tecnologia mais conhecida por eles é o BigQuery, você precisa especificar o esquema da tabela de dados de fatos sobre gatos (cat facts), inclua os campos, tipos de campos e quaisquer outras considerações necessárias. A especificação pode ser feita por diagrama ou por código. 

Nota: para as questões a seguir, não é necessário criar uma base de dados no BigQuery ou mostrar os resultados das consultas. Basta ter o código SQL escrito. 

**Considerando o que foi descrito na documentação da API e o exemplo disponibilizado do JSON**

	{
		"_id": "591f9894d369931519ce358f",
		"__v": 0,
		"text": "A female cat will be pregnant for approximately 9 weeks - between 62 and 65 days from conception to delivery.",
		"updatedAt": "2018-01-04T01:10:54.673Z",
		"deleted": false,
		"source": "api",
		"sentCount": 5
	},
 

**Podemos utilizar a função CREATE TABLE no Bigquery para adicionar os tipos, descrições das colunas e descrição para a tabela, acredito que está seja a melhor forma de documentar para os usuários, exemplo:**
 
 ***CREATE TABLE `projeto.dataset.cat_facts` (
  id STRING OPTIONS(description="ID do fato"),
  version INT64 OPTIONS(description="Versão do documento"),
  text STRING OPTIONS(description="Fato sobre gatos"),
  updated_at TIMESTAMP OPTIONS(description="Data e hora da última atualização do fato"),
  deleted BOOL OPTIONS(description="Indica se o fato foi marcado como deletado"),
  source STRING OPTIONS(description="Origem do fato"),
  sent_count INT64 OPTIONS(description="Número de vezes que o fato foi enviado")
)
OPTIONS (
  description = "Tabela com fatos sobre gatos."
);***



4 - Apesar dos dados no BigQuery, o time de analytics não está conseguindo realizar as consultas por conta própria e pediu sua ajuda. Crie uma consulta que extraia os fatos que foram atualizados em agosto de 2020 para um estudo de caso demandado por eles. 

**Me baseando na documentação disponibilizado no link https://alexwohlbruck.github.io/cat-facts/docs/endpoints/facts.html, podemos utilizar o seguinte código para verificar os fatos de Agosto de 2020:**

***SELECT fact, FORMAT_TIMESTAMP('%Y-%m', processed_at) AS mes_ano
FROM `cat_facts`
where FORMAT_TIMESTAMP('%Y-%m', processed_at) = '2020-08';***

5 - O time de desenvolvimento soube da sua habilidade com consultas SQL e decidiu se aproveitar da fila de demandas para solicitar uma amostra da base de fatos sobre gatos (cat facts) para popular o ambiente de QA deles. O time solicitou uma consulta SQL que extraia, de forma aleatória, 10% dos registros da base contendo as informações de texto, data de criação e data de atualização. Uma consideração importante feita pelo time de desenvolvimento é que eles precisam da consulta SQL para extrair os dados para um arquivo CSV separado por vírgulas. 

***WITH total_registros AS (
  SELECT COUNT(*) AS total FROM `cat_facts`
),
dados_numerados AS (
  SELECT
    fact,
    processed_at,
    ROW_NUMBER() OVER (ORDER BY RAND()) AS linha
  FROM
    `cat_facts`
)
SELECT
  fact AS texto_fato,
  FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', processed_at) AS data_processamento
FROM
  dados_numerados,
  total_registros
WHERE
  linha <= (SELECT total / 10 FROM total_registros)***
  
**Após rodar o SQL o próprio BigQuery oferece a opção de exportar os resultados como csv, só é necessário entrar na opção "save results" e selecionar como deseja salvar**
