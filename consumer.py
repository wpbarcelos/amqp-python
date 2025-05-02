"""Aplicação para consumir a fila"""
from dotenv import load_dotenv
load_dotenv()

import json
import os
import sqlite3
import init_db
from azure.eventhub import EventHubConsumerClient

# Configurar a conexão com o Event Hub
EVENT_HUB_CONNECTION_STR = os.getenv('CONSUMER_ENDPOINT')
EVENT_HUB_NAME = os.getenv('CONSUMER_HUB_NAME', 'classificacao-1g')
CONSUMER_GROUP = '$Default'

DB_FILE = os.getenv("DB_FILE", "/.data/database.sqlite")


def remove_oldest_cache():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        minutes_to_remove =  os.getenv("MINUTES_TO_REMOVE") 
        minutes_to_remove = int(minutes_to_remove) if int(minutes_to_remove) > 0 else 180
        cursor.execute( f"delete from cache where created_at < datetime( 'now', '-{str(minutes_to_remove)}  minutes')")
        conn.commit()
        print(f"\n ! Dados mais antigos que {minutes_to_remove} minutos foram removidos do banco de dados.\n")
    except Exception as e:
        print(f"Error removing oldest cache from database: {e}")
        conn.rollback()
        raise
    finally:
        conn.close()
    
def add_to_cache(cache_id, data):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    context = 'rs' if EVENT_HUB_NAME == 'classificacao-1g'  else 'tjrs' 
    try:
        cursor.execute(
            'INSERT OR REPLACE INTO cache (id, body, context) VALUES (?, ?, ? )',
            (cache_id, json.dumps(data), context)
        )
        conn.commit()
    except Exception as e:
        print(f"Error saving to database: {e}")
        conn.rollback()
        raise
    finally:
        conn.close()

def receive_message_callback(partition_context, event):
    try:
        print(f'\nEvento recebido\n\n{json.loads(event.body_as_str())}')
        data = json.loads(event.body_as_str())
        cache_id = data.get("id")

        add_to_cache(cache_id, data)
        remove_oldest_cache()
    except Exception as e:
        print(f'Erro ao processar mensagem: {e}')
        raise

def main():
    
    init_db.init_db()

    print('Consumidor iniciado\n Pressione "Ctrl + c" para imterromper...')

    consumer = EventHubConsumerClient.from_connection_string(
        EVENT_HUB_CONNECTION_STR, CONSUMER_GROUP, eventhub_name=EVENT_HUB_NAME
    )

    try:
        with consumer:
            consumer.receive(on_event=receive_message_callback, starting_position="-1")

    except KeyboardInterrupt:
        print('\nConsumidor interrompido pelo usuário.')

    except Exception as e:
        print(f'Erro no consumidor: {e}')
        raise

if __name__ == "__main__":
    main()