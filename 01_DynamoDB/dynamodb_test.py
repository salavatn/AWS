import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Music')                     # Обращаемся к таблице Music
'''
print("\n\n")
print(f"Table Name: {table.table_name}")            # Выводим имя таблицы
print(f"Table Item count: {table.item_count}")      # Выводим количество записей в таблице
print(f"Table status: {table.table_status}")        # Выводим статус таблицы
print(f"Table creation date: {table.creation_date_time}") # Выводим дату создания таблицы
print(f"Table size: {table.table_size_bytes}")      # Выводим размер таблицы в байтах
print(f"Table read capacity: {table.provisioned_throughput['ReadCapacityUnits']}") # Выводим емкость чтения таблицы
print(f"Table write capacity: {table.provisioned_throughput['WriteCapacityUnits']}") # Выводим емкость записи таблицы
print(f"Table global secondary indexes: {table.global_secondary_indexes}") # Выводим глобальные индексы таблицы
print(f"Table local secondary indexes: {table.local_secondary_indexes}") # Выводим локальные индексы таблицы
print(f"Table attribute definitions: {table.attribute_definitions}") # Выводим атрибуты таблицы
print(f"Table key schema: {table.key_schema}")      # Выводим схему ключей таблицы
print(f"Table arn: {table.table_arn}")              # Выводим arn таблицы
print(f"Table stream arn: {table.latest_stream_arn}") # Выводим arn потока таблицы
print(f"Table stream label: {table.latest_stream_label}") # Выводим метку потока таблицы
print(f"Table restore summary: {table.restore_summary}") # Выводим информацию о восстановлении таблицы
print(f"Table sse description: {table.sse_description}") # Выводим информацию о шифровании таблицы
# print(f"Table tags: {table.tags}")                  # Выводим теги таблицы
# print(f"Table time to live description: {table.time_to_live_description}") # Выводим информацию о времени жизни таблицы
print(f"Table billing mode: {table.billing_mode_summary}") # Выводим информацию о режиме оплаты таблицы
print(f"Table global table version: {table.global_table_version}") # Выводим версию глобальной таблицы
# print(f"Table replica description: {table.replica_description}") # Выводим описание реплики таблицы
# print(f"Table auto scaling description: {table.auto_scaling_description}") # Выводим описание автоматического масштабирования таблицы
'''

