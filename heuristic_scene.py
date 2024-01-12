from manim import *


class HeuristicScene(MovingCameraScene):
    def construct(self):
        # set default font
        Text.set_default(font="Arial")
        self.wait(2)

        # begin scene
        title = Text("Heuristic", font_size=70)
        self.play(FadeIn(title, shift=DOWN, scale=0.8))
        self.wait(1)
        self.play(title.animate.scale(0.5).to_corner(UL))
        self.wait(1)

        formula = MathTex("f(x) = g(x) + h(x)")
        self.play(Write(formula))
        self.wait(2)
        g_x = MathTex("g(x)").scale(1)
        h_x = MathTex("h(x)").scale(1)
        self.play(Transform(formula, g_x))
        self.wait(2)

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
        self.play(Create(graph), run_time=2)
        self.wait(2)
