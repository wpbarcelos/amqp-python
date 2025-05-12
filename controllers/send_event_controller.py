import os
import json
import base64
from azure.eventhub import EventData
from azure.eventhub import EventHubProducerClient
# from azure.identity import DefaultAzureCredential

def send_event(id, texto_original):
  
    try:
        EVENT_HUB_FULLY_QUALIFIED_NAMESPACE=  os.getenv("SENDER_ENDPOINT")
        EVENT_HUB_NAME= os.getenv("SENDER_HUB_NAME")

        producer = EventHubProducerClient.from_connection_string(
            conn_str=EVENT_HUB_FULLY_QUALIFIED_NAMESPACE,
            eventhub_name=EVENT_HUB_NAME,
        )
        
        texto_base64 = base64.b64encode(texto_original.encode('utf-8')).decode('utf-8')

        data = {
            "id": id,
            "texto":texto_base64
        }
        event_data_batch = producer.create_batch()
        event_data_batch.add(EventData(json.dumps(data)))
        producer.send_batch(event_data_batch)
        
        print("Evento enviado com sucesso!")

    except Exception as e:
        
        print(f"Erro ao enviar evento: {e}")
        raise
