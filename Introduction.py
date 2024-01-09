import os

from manim import *


class AStar(Scene):
    def construct(self):
        Text.set_default(font="Arial")

        """
        Text / Inhalt
        Was ist der A Star Pathfinding Algorithmus überhaupt?
        Der A*(star) Algorithmus ist ein intelligenter Suchalgorithmus, welcher es ermöglicht, den effizientesten Weg zwischen zwei Punkten in einem Graphen zu finden.
        Der Algorithmus wurde 1968 von Peter Hart, Nils Nilsson und Bertram Raphael beschrieben und gilt als Verallgemeinerung und Erweiterung des Dijkstra-Algorithmus.
        Das Hauptziel des A* Algorithmus ist es, den Pfad mit der geringsten Kosten zwischen einem Startknoten und einem Zielpunkt zu finden. 
        Die Kosten können verschiedene Kriterien wie Entfernung, Zeit oder Ressourcenverbrauch sein.
        Im Gegensatz zu uninformierten Suchalgorithmen verwendet der A*-Algorithmus eine Schätzfunktion bzw. Heuristik, um zielgerichtet zu suchen und damit die Laufzeit zu verringern.
        """

        # create two blue dots with white border and distance between the dots
        p1 = Dot(color=BLUE, radius=0.4).shift(LEFT * 2)
        p2 = Dot(color=BLUE, radius=0.4).shift(RIGHT * 2)
        arrow = Arrow(p1.get_center(), p2.get_center(), buff=0.1)
        arr_pf = VGroup(p1, p2, arrow)

        # Beschreibung des Algorithmus
        text_1 = Text(
            "- calculating the shortest path between two nodes in a graph",
            font_size=22,
            font="Arial",
            line_spacing=1,
        )
        text_2 = Text(
            "- first described in 1968 by Peter Hart, Nils J. Nilsson and Bertram Raphael",
            font_size=22,
            font="Arial",
            line_spacing=1,
        )
        text_3 = Text(
            "- is a generalization and extension of Dijkstra's algorithm",
            font_size=22,
            font="Arial",
            line_spacing=1,
        )
        terms_group = VGroup(text_1, text_2, text_3).arrange(DOWN, aligned_edge=LEFT)

        # Arrange terms
        terms_group.to_edge(LEFT).shift(DOWN * 0.1)

        # Wait and animate
        title = Text("A* Pathfinding Algorithm", font_size=70)
        self.play(FadeIn(title, shift=DOWN, scale=0.8))
        self.wait(2)
        self.play(title.animate.scale(0.5).to_corner(UL))
        self.wait(1)
        self.play(Create(p1))
        self.wait(1)
        self.play(Create(p2))
        self.wait(1)
        self.play(Create(arrow))
        self.wait(1)
        self.play(arr_pf.animate.to_corner(UP + RIGHT).shift(DOWN * 1))
        self.wait(1)

        # spiele die gruppe nacheiander ab
        self.play(Write(terms_group[0]), run_time=1)
        self.wait(1)
        self.play(Write(terms_group[1]), run_time=1)
        self.wait(1)
        self.play(Write(terms_group[2]), run_time=1)
        self.wait(1)
        self.play(
            arr_pf.animate.to_edge(DOWN).shift(LEFT * 4, UP * 1.5),
            terms_group.animate.shift(UP * 1.5),
        )
        self.wait(2)
        euro = Text("€↓", font_size=70)
        self.play(FadeIn(euro.to_edge(DOWN).shift(UP * 2.2)))
        self.wait(5)
        self.play(FadeOut(terms_group), FadeOut(euro), run_time=1)
        self.play(arr_pf.animate.shift(UP * 1).scale(1.5))
        self.wait(1)
        entf = ImageMobject(os.path.join("data", "Entfernung.png")).scale(1)
        zeit = ImageMobject(os.path.join("data", "Zeit.png")).scale(0.8)
        res = ImageMobject(os.path.join("data", "Ressourcen.png")).scale(0.8)
        self.play(FadeIn(entf.next_to(arr_pf, UP).shift(LEFT * 3)), run_time=0.5)
        self.play(FadeIn(zeit.next_to(arr_pf, UP)), run_time=0.5)
        self.play(FadeIn(res.next_to(arr_pf, UP).shift(RIGHT * 3)), run_time=0.5)
        self.wait(10)
        self.play(
            FadeOut(arr_pf), FadeOut(entf), FadeOut(zeit), FadeOut(res), run_time=2
        )
