# Getting Started with Kùzu in a Python Virtual Environment

This guide walks you through setting up your first Kùzu graph database in a Python virtual environment.

---

## 🧰 Step 1: Set Up a Python Virtual Environment

Using a virtual environment ensures that your project's dependencies are isolated from your system-wide Python packages.

```bash
# Create project directory
mkdir kuzu_project && cd kuzu_project

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

---

## 📦 Step 2: Install the Kùzu Python Package

With the virtual environment activated, install the Kùzu package:

```bash
pip install kuzu
```

This installs the Kùzu Python bindings for interacting with the database.

---

## 🗂️ Step 3: Create Your First Kùzu Graph

Create a Python script (e.g., `first_graph.py`) and add:

```python
import kuzu

# Initialize the database (on-disk mode)
db = kuzu.Database("my_kuzu_db")
conn = kuzu.Connection(db)

# Create node tables
conn.execute("CREATE NODE TABLE Person(name STRING, age INT64, PRIMARY KEY(name))")
conn.execute("CREATE NODE TABLE City(name STRING, population INT64, PRIMARY KEY(name))")

# Create relationship tables
conn.execute("CREATE REL TABLE LivesIn(FROM Person TO City)")
conn.execute("CREATE REL TABLE Knows(FROM Person TO Person, since INT64)")

# Insert sample data
conn.execute("CREATE (:Person {name: 'Alice', age: 30})")
conn.execute("CREATE (:Person {name: 'Bob', age: 25})")
conn.execute("CREATE (:City {name: 'Nairobi', population: 4397000})")
conn.execute("MATCH (p:Person), (c:City) WHERE p.name = 'Alice' AND c.name = 'Nairobi' CREATE (p)-[:LivesIn]->(c)")
conn.execute("MATCH (p1:Person), (p2:Person) WHERE p1.name = 'Alice' AND p2.name = 'Bob' CREATE (p1)-[:Knows {since: 2020}]->(p2)")
```

Run the script:

```bash
python first_graph.py
```

---

## 🔍 Step 4: Query the Graph

You can query the graph using Cypher queries:

```python
import kuzu

db = kuzu.Database("my_kuzu_db")
conn = kuzu.Connection(db)

result = conn.execute("MATCH (p:Person)-[r:Knows]->(friend:Person) RETURN p.name, friend.name, r.since")

while result.has_next():
    print(result.get_next())
```

---

## 📊 Optional: Visualize the Graph with Kùzu Explorer

To visualize your graph, you can use Kùzu Explorer:

1. **Install Docker**: [https://www.docker.com/get-started](https://www.docker.com/get-started)
2. **Run Kùzu Explorer**:

```bash
docker run -p 8000:8000 \
    -v $(pwd)/my_kuzu_db:/database \
    --rm kuzudb/explorer:latest
```

3. **Access Explorer**: Open your browser at [http://localhost:8000](http://localhost:8000)

---

With these steps, you've successfully set up Kùzu in a Python environment, created your first graph, and optionally visualized it!
