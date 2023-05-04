import networkx as nx
import matplotlib.pyplot as plt

# Example GraphQL schema
schema = """
type Query {
    hero(id: ID!): Character
    human(id: ID!): Human
    droid(id: ID!): Droid
    starship(id: ID!): Starship
}

interface Character {
    id: ID!
    name: String!
    friends: [Character]
    appearsIn: [Episode]!
}

enum Episode {
    NEWHOPE
    EMPIRE
    JEDI
}

type Human implements Character {
    id: ID!
    name: String!
    friends: [Character]
    appearsIn: [Episode]!
    homePlanet: String
}

type Droid implements Character {
    id: ID!
    name: String!
    friends: [Character]
    appearsIn: [Episode]!
    primaryFunction: String
}

type Starship {
    id: ID!
    name: String!
    length(unit: LengthUnit = METER): Float
}

enum LengthUnit {
    METER
    FOOT
}
"""

# Create a NetworkX graph
G = nx.Graph()

# Add nodes to the graph for each type and interface
types = ["Query", "Character", "Human", "Droid", "Starship", "Episode", "LengthUnit"]
interfaces = ["Character"]

G.add_nodes_from(types, bipartite=0)
G.add_nodes_from(interfaces, bipartite=1)

# Add edges to the graph for each field
fields = {
    "Query": ["hero", "human", "droid", "starship"],
    "Character": ["id: ID!", "name: String!", "friends: [Character]", "appearsIn: [Episode]!"],
    "Human": ["homePlanet: String"],
    "Droid": ["primaryFunction: String"],
    "Starship": ["name: String!", "length(unit: LengthUnit = METER): Float"],
    "Episode": ["NEWHOPE", "EMPIRE", "JEDI"],
    "LengthUnit": ["METER", "FOOT"]
}

for src in types:
    for field in fields[src]:
        if ":" in field:
            dest = field.split(":")[0].strip()
        else:
            dest = field.strip()
        G.add_edge(src, dest)

# Set node positions and label nodes
pos = nx.bipartite_layout(G, interfaces)

nx.draw_networkx_nodes(G, pos, nodelist=types, node_color="lightblue", node_size=500)
nx.draw_networkx_nodes(G, pos, nodelist=interfaces, node_color="lightgreen", node_size=500)
nx.draw_networkx_edges(G, pos)

node_labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels)

# Set edge labels
edge_labels = {(src, dest): dest for src, dest in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Show the graph
plt.axis("off")
plt.show()
