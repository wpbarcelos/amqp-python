<?php
// URL de destino


$contexto = 'RS';
$documento_id = '881744651236134419971527116861';
$url = "http://172.22.180.8:5000/documento/$contexto/$documento_id";



// Inicializa o cURL
$ch = curl_init();

// Configura a requisição
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
// curl_setopt($ch, CURLOPT_HTTPHEADER, [
//     'Content-Type: application/json',
// ]);

// Executa a requisição e captura a resposta
$response = curl_exec($ch);
echo $url."\n";

// Verifica se houve algum erro na requisição
if(curl_errno($ch)) {
    echo 'Erro cURL: ' . curl_error($ch);
} else {
    // Exibe a resposta da requisição
    echo 'Resposta: ' . $response;
}

// Fecha a conexão cURL
curl_close($ch);
