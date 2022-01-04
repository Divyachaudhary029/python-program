def delete(connection):
    connection.execute('''DELETE FROM STUDENT WHERE marks=33''')
    print("total no of raws deleted:",connection.total_changes)
    i=connection.execute('''SELECT * FROM STUDENT''')
    for record in i:
        print(record)