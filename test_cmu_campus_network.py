import networkx as nx
import cmu_campus_network as cmu


def test_graph_exists():
    # The script builds a graph named G at module level
    assert isinstance(cmu.G, nx.Graph)
    assert cmu.G.number_of_nodes() == 5
    assert cmu.G.number_of_edges() >= 5


def test_shortest_path_gates_to_hunt():
    path = cmu.shortest_path
    assert path[0] == "Gates Hillman Center"
    assert path[-1] == "Hunt Library"
    # The known optimal walking time based on the edges
    assert cmu.walking_time == 5


def test_degree_counts():
    degrees = {b: cmu.G.degree(b) for b in cmu.G.nodes()}
    # Basic sanity check: every building has at least one path
    for d in degrees.values():
        assert d >= 1
