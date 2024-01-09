from manim import *


class PathfindingScene(MovingCameraScene):
    def construct(self):
        Text.set_default(font="Arial")
        self.camera.frame.save_state()

        self.wait(2)
        # INTRO PATHFINDING
        title = Text("Pathfinding", font_size=70)
        self.play(FadeIn(title, shift=DOWN, scale=0.8))
        self.wait(1)
        self.play(title.animate.scale(0.5).to_corner(UL))
        self.wait(1)
        subtitle = Text("What is Pathfinding?", font_size=50)
        self.play(Write(subtitle))
        self.wait(2)
        text = Paragraph(
            "Algorithmic search for the optimal path",
            "from a starting point to one or more target points",
            font_size=30,
            alignment="center",
        )
        self.play(ReplacementTransform(subtitle, text))
        self.wait(14)
        self.play(FadeOut(text), FadeOut(title))

        # GRAPH THEORIE
        title = Text("Graph Theory", font_size=70)
        self.play(FadeIn(title, shift=DOWN, scale=0.8))
        self.wait(5)
        self.play(title.animate.scale(0.5).to_corner(UL))
        self.wait(2)
        # create graph
        text = Text(
            "Graph G consists of a set of vertices V and edges E",
            font_size=30,
            t2c={"Knoten": RED, "Kanten": GREEN},
            t2w={"Knoten": BOLD, "Kanten": BOLD},
        ).to_edge(DOWN)
        vertices = [
            "A",
            "B",
            "C",
            "D",
        ]
        edges = [("A", "B"), ("A", "C"), ("B", "D")]
        positions = {
            "A": [0, 1.5, 0],
            "B": [-1.5, 0, 0],
            "C": [1.5, 0, 0],
            "D": [0, -1.5, 0],
        }
        vertex_config = {
            "A": {"fill_color": RED},
            "B": {"fill_color": RED},
            "C": {"fill_color": RED},
            "D": {"fill_color": RED},
        }
        edge_config = {
            ("A", "B"): {"stroke_color": BLUE},
            ("A", "C"): {"stroke_color": BLUE},
            ("B", "D"): {"stroke_color": BLUE},
        }
        graph = Graph(
            vertices,
            edges,
            layout=positions,
            labels=True,
            vertex_config=vertex_config,
            edge_config=edge_config,
        )
        self.play(Write(text))
        self.wait(2)
        self.play(
            Create(graph),
            run_time=2,
        )
        self.wait(14)
        self.play(FadeOut(graph), FadeOut(text))

        # PATHFINDING IN GRAPH
        new_title = Text("Pathfinding", font_size=40).to_corner(UL)
        self.play(ReplacementTransform(title, new_title))
        self.wait(3)

        vertices = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
        ]
        edges = [
            ("A", "B"),
            ("A", "C"),
            ("A", "D"),
            ("B", "C"),
            ("B", "G"),
            ("C", "F"),
            ("C", "E"),
            ("D", "H"),
            ("H", "F"),
            ("G", "E"),
            ("F", "E"),
        ]
        positions = {
            "A": [0, 3, 0],
            "B": [-3, 0, 0],
            "C": [-1, 0, 0],
            "D": [3, 0, 0],
            "E": [0, -3, 0],
            "F": [1, -1.5, 0],
            "G": [-2, -1.5, 0],
            "H": [3, -1.5, 0],
        }
        graph = Graph(vertices, edges, layout=positions, labels=True)
        self.play(
            Create(graph),
            run_time=3,
        )
        self.wait(7)

        # change node color
        for node in ["A", "C", "E"]:
            node_to_highlight = graph.get_vertices()[node]
            self.play(node_to_highlight.animate.set_fill(RED))
        self.play(
            graph.animate.add_edges(
                ("A", "C"), ("C", "E"), edge_config={"stroke_color": RED}
            ),
        )

        self.wait(5)

        self.play(FadeOut(graph, shift=UP), FadeOut(new_title))
