import kuzu

# Initialize the Kùzu database in on-disk mode, storing data in the "my_kuzu_db" folder
db = kuzu.Database("my_kuzu_db")

# Create a connection object to execute queries against the database
conn = kuzu.Connection(db)

# ---------------------------
# SCHEMA DEFINITION
# ---------------------------

# Safely create schema if not exists
try:
    conn.execute("CREATE NODE TABLE IF NOT EXISTS Person(name STRING, age INT64, PRIMARY KEY(name))")
except Exception as e:
    print(f"Skipped creating Person table: {e}")

try:
    conn.execute("CREATE NODE TABLE IF NOT EXISTS City(name STRING, population INT64, PRIMARY KEY(name))")
except Exception as e:
    print(f"Skipped creating City table: {e}")

try:
    conn.execute("CREATE REL TABLE IF NOT EXISTS LivesIn(FROM Person TO City)")
except Exception as e:
    print(f"Skipped creating LivesIn relation: {e}")

try:
    conn.execute("CREATE REL TABLE IF NOT EXISTS Knows(FROM Person TO Person, since INT64)")
except Exception as e:
    print(f"Skipped creating Knows relation: {e}")

# ---------------------------
# DATA INSERTION (Safe)
# ---------------------------

# Insert Person nodes if not exist
conn.execute("MERGE (:Person {name: 'Alice', age: 30})")
conn.execute("MERGE (:Person {name: 'Bob', age: 25})")
conn.execute("MERGE (:Person {name: 'Carol', age: 28})")
conn.execute("MERGE (:Person {name: 'David', age: 35})")
conn.execute("MERGE (:Person {name: 'Eva', age: 22})")

# Insert City nodes if not exist
conn.execute("MERGE (:City {name: 'Nairobi', population: 4397000})")
conn.execute("MERGE (:City {name: 'Mombasa', population: 1200000})")
conn.execute("MERGE (:City {name: 'Kisumu', population: 600000})")

# Create LivesIn relationships only if not already present
conn.execute(
    "MATCH (p:Person), (c:City) WHERE p.name = 'Alice' AND c.name = 'Nairobi' "
    "MERGE (p)-[:LivesIn]->(c)"
)
conn.execute(
    "MATCH (p:Person), (c:City) WHERE p.name = 'Bob' AND c.name = 'Mombasa' "
    "MERGE (p)-[:LivesIn]->(c)"
)
conn.execute(
    "MATCH (p:Person), (c:City) WHERE p.name = 'Carol' AND c.name = 'Nairobi' "
    "MERGE (p)-[:LivesIn]->(c)"
)
conn.execute(
    "MATCH (p:Person), (c:City) WHERE p.name = 'David' AND c.name = 'Kisumu' "
    "MERGE (p)-[:LivesIn]->(c)"
)
conn.execute(
    "MATCH (p:Person), (c:City) WHERE p.name = 'Eva' AND c.name = 'Mombasa' "
    "MERGE (p)-[:LivesIn]->(c)"
)

# Create Knows relationships only if not already present
conn.execute(
    "MATCH (p1:Person), (p2:Person) WHERE p1.name = 'Alice' AND p2.name = 'Bob' "
    "MERGE (p1)-[:Knows {since: 2020}]->(p2)"
)
conn.execute(
    "MATCH (p1:Person), (p2:Person) WHERE p1.name = 'Bob' AND p2.name = 'Carol' "
    "MERGE (p1)-[:Knows {since: 2021}]->(p2)"
)
conn.execute(
    "MATCH (p1:Person), (p2:Person) WHERE p1.name = 'Carol' AND p2.name = 'David' "
    "MERGE (p1)-[:Knows {since: 2019}]->(p2)"
)
conn.execute(
    "MATCH (p1:Person), (p2:Person) WHERE p1.name = 'David' AND p2.name = 'Eva' "
    "MERGE (p1)-[:Knows {since: 2022}]->(p2)"
)