import cassandra.cluster as cluster

cluster = cluster.Cluster()
connection = cluster.connect('people')
result = connection.execute("SELECT * FROM employees")
for row in result:
    print(row.salary, row.city, row.name)