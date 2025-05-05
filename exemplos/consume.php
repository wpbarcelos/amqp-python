<?php
// URL de destino

$baseURL = "http://localhost:5001";
$contexto = 'RS';
$documento_id = '881744651236134419971527116990';

echo $url = "$baseURL/documento/$contexto/$documento_id";

// Inicializa o cURL
$ch = curl_init();

// Configura a requisição
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Executa a requisição e captura a resposta
$response = curl_exec($ch);
//echo $url."\n";

// Verifica se houve algum erro na requisição
if(curl_errno($ch)) {
    echo 'Erro cURL: ' . curl_error($ch);
} else {
    echo 'Resposta: ' . $response;
}

curl_close($ch);
