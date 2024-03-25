from flask import Flask, jsonify
import boto3
from botocore.exceptions import ClientError
import pymysql
import json

app = Flask(__name__)


@app.route('/api/get-value', methods=['GET'])
def get_backend_value():
    value = get_DB_val()
    return jsonify({"value": value})  # converts the dictionary to a JSON response


@app.route('/api/get-value-default', methods=['GET'])
def get_backend_value_default():
    value = "General Kenobi"
    return jsonify({"value": value})  # converts the dictionary to a JSON response


def get_DB_val():
    # return "General Kenobi"

    # Configuration values
    host = 'hello-there-mydbinstance-n0wjogepbuph.c9mcsieskixg.il-central-1.rds.amazonaws.com'
    port = 3306
    dbname = 'hello-there-mydbinstance-n0wjogepbuph'
    user = 'adminuser'
    password = 'adminuser'
    table_name = 'hello-there-table'  # Replace with your table name

    # The value you want to update
    key_to_update = 'value'
    new_value = '42'

    # Connect to the database
    connection = pymysql.connect(host=host, user=user, port=port, passwd=password, db=dbname)

    try:
        with connection.cursor() as cursor:
            # Check if the table exists
            cursor.execute(f"SHOW TABLES LIKE '{table_name}';")
            result = cursor.fetchone()
            if not result:
                # If the table doesn't exist, create it
                cursor.execute(f"""CREATE TABLE {table_name} (
                                   key_name VARCHAR(255) NOT NULL,
                                   value VARCHAR(255) NOT NULL,
                                   PRIMARY KEY (key_name)
                                   );""")
                print("Table created.")

            # Check if the key exists
            cursor.execute(f"SELECT * FROM {table_name} WHERE key_name = '{key_to_update}';")
            if cursor.fetchone():
                # If the key exists, update the value
                cursor.execute(f"UPDATE {table_name} SET value = '{new_value}' WHERE key_name = '{key_to_update}';")
            else:
                # If the key doesn't exist, insert it
                cursor.execute(f"INSERT INTO {table_name} (key_name, value) VALUES ('{key_to_update}', '{new_value}');")

            # Commit changes
            connection.commit()
    finally:
        connection.close()

    print("Operation completed.")



def get_secret():

    secret_name = "hello-there/MySQL"
    region_name = "il-central-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']
    return json.loads(secret)






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
