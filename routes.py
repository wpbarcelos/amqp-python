from app import app
from flask import jsonify, request
from controllers import cache_controller, send_event_controller


@app.route('/')
def index():
    return jsonify({ 'message' :'Eventhub EPROC' }), 200


@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()

    if not data or not 'id' in data or not 'texto' in data:
        return jsonify({ 'error': 'JSON deve ter id e texto'}), 400

    try:
        send_event_controller.send_event(data['id'], data['texto'])
        response = {
            'status': 'Evento enviado com sucesso!',
            'error': None,
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({ 'error': str(e), 'status': "Ocorreu um erro ao enviar mensagem."}), 500


@app.route('/documento/<contexto>/<doc_id>', methods=['GET'])
def get_document(contexto, doc_id):
    try:
        document = cache_controller.get_document_by_id(doc_id + "#" + contexto)
        if document is None:
            return jsonify({'error': 'Documento não encontrado'}), 404
        
        return jsonify(document), 200
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'Erro ao buscar documento'}), 500


