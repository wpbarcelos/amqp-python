<?php
// URL de destino
$url = "http://172.22.180.8:5000/send";

// Dados a serem enviados no corpo da requisição
$data = [
    "id" => "881744651236134419971527116861#RS",
    "texto" => "EXMO. SR. DR. JUIZ DE DIREITO DA 2ª VARA DA COMARCA DE ENCANTADO ? RS Distribuição por Dependência ao Processo Nº ORIGINÁRIO EMPRESA, pessoa jurídica de direito privado, sociedade com sede a, bairro Floresta, Caxias do Sul - RS - CEP 95010-660, inscrita no CNPJ nº , representada por sua sócia administradora NOME ADMINISTRADORA, brasileira, casada, residente e domiciliada em Caxias do Sul ? RS, por seus advogados e procuradores, que recebem intimações a, nos autos da AÇÃO INDENIZATÓRIA ? FASE DE CUMPRIMENTO DE SENTENÇA, que lhe move AUTOR, brasileiro, divorciado, aposentado, portador do CPF nº, e do RG nº, residente e domiciliado na Rual, 999, no município de Roca Sales/RS CEP 95735-000, vem respeitosamente, à presença de Vossa Excelência, propor EMBARGOS À EXECUÇÃO, pelas razões de fato e de direito a seguir expostos: SÍNTESE DOS FATOS A embargante nos autos do processo nº, teve penhorado um imóvel, matrícula nº 11.664 do Registro de Imóveis da 1ª Zona da comarca de Caxias do Sul - RS, avaliado em R$1.600.000,00 (hum milhão e seiscentos mil reais), conforme certidão do Sr. Oficial de Justiça. O valor da dívida é de R$22.716,01 (vinte e dois mil, setecentos e dezesseis reais e um centavo). Fica assim, constatado o evidente excesso de penhora. Neste ato indica duas máquinas de solda, conforme notas fiscais inclusas, no valor total de R$21.125,63 (vinte e um mil, cento e vinte cinco reais e sessenta e três centavos), considerando que a embargante é representante das empresas vendedoras, adquiriu a preço de custo, sendo o valor, se aplicado o de mercado, muito superiores aos apresentados em nota fiscal. De acordo com a proporcionalidade da execução se caracterizou o excesso de penhora. É ínsito ressaltar que o auto de penhora lavrado pelo Sr.Oficial de Justiça incorreu em EXCESSO DE PENHORA, isto é, existe uma nítida discrepância entre o valor do débito e o bem penhorado. Assim, o imóvel possui valor extremamente superior ao necessário para a satisfação do crédito, caracterizando um abusivo excesso de penhora. É certo que a satisfação de um crédito pressupõe sacrifício patrimonial, mas deve haver proporcionalidade e equilíbrio de maneira que a execução nunca exceda a ponto de causar prejuízos ao pagador. Dessa maneira, o bem penhorado deve ter valores proporcionais ao débito a ser adimplido. DO DIREITO Mister salientar, que os presentes Embargos à Execução são perfeitamente admissíveis, consoante prescreve o artigo 914 do Código de Processo Civil, vejamos: ? A r t . 9 1 4 . O e x e c u t ado,indep endentementedepenhora,depósitooucaução,poderáopor-s e à execução por meio de embargos.? Ademais, esclarece a embargante que está evidente a configuração de tal excesso. DO PEDIDO: Ante o exposto, requer: A. Seja concedido efeito suspensivo, conforme artigo 919 § 1º do Código de Processo Civil; B. Seja intimado o embargado, na pessoa dos seus advogados para responder, querendo no prazo legal; C. A procedência dos presentes Embargos à Execução com a determinação de V. Exa. no sentido de DESCONSIDERAR A PENHORA realizada sobre o imóvel do Registro de Imóveis da 1ª Zona da comarca de Caxias do Sul ? RS, promovendo o levantamento da constrição; D. Condenação no embargado nas custas processuais, honorários de advogado e demais cominações legais; E. Protesta provar por todos os meios de provas em direito admitidas. Valor da causa R$21.125,63 Pede deferimento. Cidade, 18 de junho de 2021."
];

// Inicializa o cURL
$ch = curl_init();

// Configura a requisição
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Content-Length: ' . strlen(json_encode($data))
]);

// Executa a requisição e captura a resposta
$response = curl_exec($ch);

// Verifica se houve algum erro na requisição
if(curl_errno($ch)) {
    echo 'Erro cURL: ' . curl_error($ch);
} else {
    // Exibe a resposta da requisição
    echo 'Resposta: ' . $response;
}

// Fecha a conexão cURL
curl_close($ch);
