# Import the kuzu module, which provides Python bindings to interact with Kùzu database
import kuzu

# Connect to an existing Kùzu database located in the folder "my_kuzu_db"
# This assumes the database was already created and initialized
db = kuzu.Database("my_kuzu_db")

# Create a connection object to interact with the database.
# The connection is used to execute queries.
conn = kuzu.Connection(db)

# Define and execute a Cypher-like query:
# It matches all 'Person' nodes that are connected by a 'Knows' relationship to other 'Person' nodes,
# then returns the name of each person and the name of their friend, along with the year since they’ve known each other.
result = conn.execute(
    "MATCH (p:Person)-[r:Knows]->(friend:Person) RETURN p.name, friend.name, r.since"
)

# Loop through the results using the result cursor
# `has_next()` checks if there are more rows to read.
# `get_next()` fetches the next row in the result set.
while result.has_next():
    print(result.get_next())  # Each row is printed as a tuple (e.g., ('Alice', 'Bob', 2020))

# ---------------------------
# ADDITIONAL QUERY EXAMPLES
# ---------------------------

# 1. Find all people who live in a specific city
result = conn.execute(
    "MATCH (p:Person)-[:LivesIn]->(c:City) WHERE c.name = 'Nairobi' RETURN p.name"
)
print("\nPeople living in Nairobi:")
while result.has_next():
    print(result.get_next())

# 2. Find all people who are over 26 years old
result = conn.execute(
    "MATCH (p:Person) WHERE p.age > 26 RETURN p.name, p.age"
)
print("\nPeople over 26:")
while result.has_next():
    print(result.get_next())

# 3. Find all friendships that started before 2021
result = conn.execute(
    "MATCH (:Person)-[r:Knows]->(:Person) WHERE r.since < 2021 RETURN r.since"
)
print("\nFriendships that started before 2021:")
while result.has_next():
    print(result.get_next())

# 4. Count how many people live in each city
result = conn.execute(
    "MATCH (p:Person)-[:LivesIn]->(c:City) RETURN c.name, COUNT(p)"
)
print("\nNumber of people per city:")
while result.has_next():
    print(result.get_next())

# 5. List all cities and their populations
result = conn.execute(
    "MATCH (c:City) RETURN c.name, c.population"
)
print("\nCities and their populations:")
while result.has_next():
    print(result.get_next())