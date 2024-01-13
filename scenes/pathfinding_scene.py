from manim import *


class PathfindingScene(MovingCameraScene):
    def construct(self):
        # set default font
        Text.set_default(font="Arial")

        ###############################
        # Start video timeline
        ###############################

        self.wait(2)
        # display title and move it to upper left corner
        title = Text("Pathfinding", font_size=70)
        self.play(FadeIn(title, shift=DOWN, scale=0.8))
        self.wait(1)
        self.play(title.animate.scale(0.5).to_corner(UL))
        self.wait(1)
        # explain what pathfinding is
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
        self.wait(10)
        self.play(FadeOut(text), FadeOut(title))

        # graph theorie
        title = Text("Graph Theory", font_size=70)
        self.play(FadeIn(title, shift=DOWN, scale=0.8))
        self.wait(3)
        self.play(title.animate.scale(0.5).to_corner(UL))
        self.wait(1)

        # create graph
        text = Text(
            "Graph G consists of a set of vertices V and edges E", font_size=30
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
        graph = Graph(vertices, edges, layout=positions, labels=True)
        graph_dr = DiGraph(vertices, edges, labels=True, layout=positions).shift(
            RIGHT * 3.5
        )
        graph_subtitle = Text("undirected", font_size=30)
        graph_dr_subtitle = Text("directed", font_size=30)
        self.play(Write(text))
        self.wait(2)
        self.play(
            Create(graph),
            run_time=2,
        )
        self.wait(5)
        self.play(FadeOut(text), graph.animate.shift(LEFT * 3.5))
        self.wait(1)
        self.play(
            Create(graph_dr),
            Write(graph_subtitle.next_to(graph, DOWN)),
            Write(graph_dr_subtitle.next_to(graph_dr, DOWN)),
        )
        self.wait(5)
        self.play(
            FadeOut(graph),
            FadeOut(graph_dr),
            FadeOut(graph_subtitle),
            FadeOut(graph_dr_subtitle),
        )

        # example
        new_title = Text("Pathfinding", font_size=40).to_corner(UL)
        self.play(ReplacementTransform(title, new_title))
        self.wait(2)

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
            run_time=2,
        )
        self.wait(3)
        for node in ["A", "E"]:
            node_to_highlight = graph.get_vertices()[node]
            self.play(node_to_highlight.animate.set_fill(RED))

        self.wait(3)
        node_to_highlight = graph.get_vertices()["C"]
        self.play(node_to_highlight.animate.set_fill(RED))
        self.play(
            graph.animate.add_edges(
                ("A", "C"), ("C", "E"), edge_config={"stroke_color": RED}
            ),
        )

        self.wait(3)
        self.play(FadeOut(graph, shift=UP), FadeOut(new_title, shift=UP))
