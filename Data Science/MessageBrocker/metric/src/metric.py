import pika
import ___1___
 
# Создаём подключение к серверу на локальном хосте
connection = ___2___(pika.ConnectionParameters(host='localhost'))
channel = connection.___3___
 
# Объявляем очередь y_true
channel.queue_declare(queue='y_true')
# Объявляем очередь y_pred
channel.queue_declare(queue='___4___')
 
# Создаём функцию callback для обработки данных из очереди
def callback(ch, method, properties, body):
    print(f'Из очереди {method.routing_key} получено значение {json.___5___(body)}')
 
# Извлекаем сообщение из очереди y_true
channel.basic_consume(
    queue='y_true',
    on_message_callback=___6___,
    auto_ack=True
)
# Извлекаем сообщение из очереди y_pred
channel.basic_consume(
    queue='y_pred',
    on_message_callback=___7___,
    auto_ack=True
)
 
# Запускаем режим ожидания прихода сообщений
print('...Ожидание сообщений, для выхода нажмите CTRL+C')
channel.___8___()