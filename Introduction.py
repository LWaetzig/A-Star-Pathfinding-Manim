import os

from manim import *


class Introduction(Scene):
    def construct(self):
        introduction_text = [
            "Herzlich Willkommen bei AlgorithmAlchemy!",
            "Heute tauchen wir in die faszinierende Welt des A* Algorithmus ein.",
            "A* ist ein intelligenter Suchalgorithmus,",
            "der in vielen Bereichen der künstlichen Intelligenz und Robotik eingesetzt wird.",
            "Er hilft, den effizientesten Weg zwischen zwei Punkten in einem Netzwerk zu finden.",
            "Lasst uns gemeinsam entdecken, wie dieser mächtige Algorithmus funktioniert!",
        ]
        satz1 = Text(
            "Herzlich Willkommen bei AlgorithmAlchemy!", font_size=24, font="Arial"
        ).to_edge(DOWN)
        satz2 = Text(
            "Heute tauchen wir in die faszinierende Welt des A* Algorithmus ein.",
            font_size=24,
            font="Arial",
        ).to_edge(DOWN)
        satz3 = Text(
            "A* ist ein intelligenter Suchalgorithmus,", font_size=24, font="Arial"
        ).to_edge(DOWN)
        satz4 = Text(
            "der in vielen Bereichen der künstlichen Intelligenz und Robotik eingesetzt wird.",
            font_size=24,
            font="Arial",
        ).to_edge(DOWN)
        satz5 = Text(
            "Er hilft, den effizientesten Weg zwischen zwei Punkten in einem Netzwerk zu finden.",
            font_size=24,
            font="Arial",
        ).to_edge(DOWN)
        satz6 = Text(
            "Lasst uns gemeinsam entdecken, wie dieser mächtige Algorithmus funktioniert!",
            font_size=24,
            font="Arial",
        ).to_edge(DOWN)
        img = ImageMobject(os.path.join("data", "Logo1.png")).scale_to_fit_width(8)

        # Play the current subtitle
        self.wait(0.1)
        self.play(Write(satz1, run_time=len(satz1) * 0.05), FadeIn(img))
        self.wait(0.1)
        self.play(FadeOut(satz1, run_time=1))
        self.play(Write(satz2, run_time=len(satz2) * 0.05))
        self.wait(0.1)
        self.play(FadeOut(satz2, run_time=1))
        self.play(Write(satz3, run_time=len(satz3) * 0.05))
        self.play(FadeOut(satz3, run_time=0.05))
        self.play(Write(satz4, run_time=len(satz4) * 0.05))
        self.wait(0.1)
        self.play(FadeOut(satz4, run_time=1))
        self.play(Write(satz5, run_time=len(satz5) * 0.05))
        self.wait(0.1)
        self.play(FadeOut(satz5, run_time=1))
        self.play(Write(satz6, run_time=len(satz6) * 0.05))
        self.wait(0.1)
        self.play(FadeOut(satz6, run_time=1), FadeOut(img))


class AStar(Scene):
    def construct(self):
        Text.set_default(font="Arial")
        ##############################
        """
        Text / Inhalt
        Was ist der A Star Pathfinding Algorithmus überhaupt?
        Der A*(star) Algorithmus ist ein intelligenter Suchalgorithmus, welcher es ermöglicht, den effizientesten Weg zwischen zwei Punkten in einem Graphen zu finden.
        Der Algorithmus wurde 1968 von Peter Hart, Nils Nilsson und Bertram Raphael beschrieben und gilt als Verallgemeinerung und Erweiterung des Dijkstra-Algorithmus.
        Das Hauptziel des A* Algorithmus ist es, den Pfad mit der geringsten Kosten zwischen einem Startknoten und einem Zielpunkt zu finden. 
        Die Kosten können verschiedene Kriterien wie Entfernung, Zeit oder Ressourcenverbrauch sein.
        Im Gegensatz zu uninformierten Suchalgorithmen verwendet der A*-Algorithmus eine Schätzfunktion bzw. Heuristik, um zielgerichtet zu suchen und damit die Laufzeit zu verringern.
        
        """
        # erstelle zwei blaue punkte mit weißem rand und abstand zwischen den punkten
        p1 = Dot(color=BLUE, radius=0.4).shift(LEFT * 2)
        p2 = Dot(color=BLUE, radius=0.4).shift(RIGHT * 2)
        # erstelle inen pfeil zwischen den punkten
        arrow = Arrow(p1.get_center(), p2.get_center(), buff=0.1)
        # gruppiere die punkte und den pfeil
        arr_pf = VGroup(p1, p2, arrow)

        # Beschreibung des Algorithmus
        # text_11 = Text("▪️ Berechnung des kürzesten Pfades zwischen \n     zwei Knoten in einem Graphen", font_size=23, font="Arial", line_spacing=1)
        text_1 = Text(
            "▪️ Berechnung des kürzesten Pfades zwischen zwei Knoten in einem Graphen",
            font_size=23,
            font="Arial",
            line_spacing=1,
        )
        text_2 = Text(
            "▪️ wurde das erste Mal 1968 von Peter Hart, Nils J. Nilsson und Bertram Raphael beschrieben",
            font_size=22,
            font="Arial",
            line_spacing=1,
        )
        text_3 = Text(
            "▪️ gilt als Verallgemeinerung und Erweiterung des Dijkstra-Algorithmus",
            font_size=23,
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
        zeit = ImageMobject(os.path.join("data", "Ressourcen.png")).scale(0.8)
        res = ImageMobject(os.path.join("data", "Ressourcen.png")).scale(0.8)
        self.play(FadeIn(entf.next_to(arr_pf, UP).shift(LEFT * 3)), run_time=0.5)
        self.play(FadeIn(zeit.next_to(arr_pf, UP)), run_time=0.5)
        self.play(FadeIn(res.next_to(arr_pf, UP).shift(RIGHT * 3)), run_time=0.5)
        self.wait(10)
        self.play(
            FadeOut(arr_pf), FadeOut(entf), FadeOut(zeit), FadeOut(res), run_time=2
        )
