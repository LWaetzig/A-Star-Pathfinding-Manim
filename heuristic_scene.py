from manim import *


class HeuristicScene(MovingCameraScene):
    def construct(self):
        Text.set_default(font="Arial")

        # Create Graph
        point_s = Dot(color=GREEN, radius=0.5).move_to(5 * LEFT)
        point_x = Dot(color=BLUE, radius=0.5)
        point_e = Dot(color=RED, radius=0.5).move_to(5 * RIGHT)
        letter_s = Text("Start", font_size=25).move_to(point_s.get_center())
        letter_x = MathTex("x", font_size=60).move_to(point_x.get_center())
        letter_e = Text("End", font_size=25).move_to(point_e.get_center())
        line1 = Line(point_s.get_center(), point_x.get_center(), buff=0.5)
        line2 = Line(point_x.get_center(), point_e.get_center(), buff=0.5)
        linegx = Line(point_s.get_center(), point_x.get_center(), buff=0.5, color=GREEN)
        linehx = Line(point_x.get_center(), point_e.get_center(), buff=0.5, color=RED)

        graph = VGroup(
            point_s, point_x, point_e, letter_s, letter_x, letter_e, line1, line2
        )

        # Create Graph for admisibility
        ad_point_s = Dot(color=GREEN, radius=0.5).move_to(5 * LEFT)
        ad_point_x = Dot(color=BLUE, radius=0.5)
        ad_point_e = Dot(color=RED, radius=0.5).move_to(5 * RIGHT)
        ad_letter_s = Text("Start", font_size=25).move_to(ad_point_s.get_center())
        ad_letter_x = MathTex("x", font_size=60).move_to(ad_point_x.get_center())
        ad_letter_e = Text("End", font_size=25).move_to(ad_point_e.get_center())
        ad_line1 = Line(ad_point_s.get_center(), ad_point_x.get_center(), buff=0.5)
        ad_line2 = Line(ad_point_x.get_center(), ad_point_e.get_center(), buff=0.5)
        ad_weight1 = Text("3", font_size=25).move_to(ad_line1.get_center() + 0.5 * DOWN)
        ad_weight2 = Text("2", font_size=25).move_to(ad_line2.get_center() + 0.5 * DOWN)
        ad_heur_s = Text("4", font_size=25).move_to(ad_point_s.get_center() + 1 * DOWN)
        ad_heur_x = Text("1", font_size=25).move_to(ad_point_x.get_center() + 1 * DOWN)
        ad_heur_e = Text("0", font_size=25).move_to(ad_point_e.get_center() + 1 * DOWN)

        ad_graph = VGroup(
            ad_point_s,
            ad_point_x,
            ad_point_e,
            ad_letter_s,
            ad_letter_x,
            ad_letter_e,
            ad_line1,
            ad_line2,
        )

        # Create Graph for non-admisibility
        nonad_point_s = Dot(color=GREEN, radius=0.5).move_to(5 * LEFT)
        nonad_point_x = Dot(color=BLUE, radius=0.5)
        nonad_point_e = Dot(color=RED, radius=0.5).move_to(5 * RIGHT)
        nonad_letter_s = Text("Start", font_size=25).move_to(nonad_point_s.get_center())
        nonad_letter_x = MathTex("x", font_size=60).move_to(nonad_point_x.get_center())
        nonad_letter_e = Text("End", font_size=25).move_to(nonad_point_e.get_center())
        nonad_line1 = Line(
            nonad_point_s.get_center(), nonad_point_x.get_center(), buff=0.5
        )
        nonad_line2 = Line(
            nonad_point_x.get_center(), nonad_point_e.get_center(), buff=0.5
        )
        nonad_weight1 = Text("3", font_size=25).move_to(
            nonad_line1.get_center() + 0.5 * DOWN
        )
        nonad_weight2 = Text("2", font_size=25).move_to(
            nonad_line2.get_center() + 0.5 * DOWN
        )
        nonad_heur_s = Text("6", font_size=25).move_to(
            nonad_point_s.get_center() + 1 * DOWN
        )
        nonad_heur_x = Text("3", font_size=25).move_to(
            nonad_point_x.get_center() + 1 * DOWN
        )
        nonad_heur_e = Text("0", font_size=25).move_to(
            nonad_point_e.get_center() + 1 * DOWN
        )

        nonad_graph = VGroup(
            nonad_point_s,
            nonad_point_x,
            nonad_point_e,
            nonad_letter_s,
            nonad_letter_x,
            nonad_letter_e,
            nonad_line1,
            nonad_line2,
        )

        # Create Texts
        title = Text("Heuristic", font_size=70)

        formula = MathTex("f(x) = g(x) + h(x)", font_size=90)

        g_x = MathTex("g(x)", color=GREEN, font_size=45).move_to(
            line1.get_center() + 0.75 * DOWN
        )
        h_x = MathTex("h(x)", color=RED, font_size=45).move_to(
            line2.get_center() + 0.75 * DOWN
        )

        directtxt = Text("used to direct towards the goal", font_size=30).move_to(
            0.8333 * UP
        )
        priotxt = Text(
            "A* prioritizes nodes leading towards the goal", font_size=30
        ).move_to(0.8334 * DOWN)
        reducetxt = Text(
            "reduces unnecessary examination of the rest of the graph", font_size=30
        ).move_to(2.5 * DOWN)

        admissibletitle = Text("Admissible", font_size=30).to_edge(LEFT).shift(2 * UP)

        notadmissibletitle = (
            Text("Not Admissible", font_size=30).to_edge(LEFT).shift(0.5 * DOWN)
        )

        admissibleexplain = Text(
            "Admissible heuristic = never overestimates the costs (optimistic)",
            font_size=30,
        )

        guaranteetxt = Text(
            "A* guarantees finding the optimal path", font_size=30
        ).move_to(1 * DOWN)

        efficiencytxt = Text("A* can be very efficient", font_size=30).move_to(1 * UP)

        dependendtxt = Text(
            "Dependent on the quality of the heuristic and structure of the graph",
            font_size=30,
        ).move_to(1 * DOWN)

        # Create other stuff
        arrow1 = Arrow(2.4 * UP, 0.8333 * UP, buff=0.35)
        arrow2 = Arrow(0.8333 * UP, 0.8334 * DOWN, buff=0.35)
        arrow3 = Arrow(0.8334 * DOWN, 2.5 * DOWN, buff=0.35)

        arrline = Line(5 * LEFT + 0.3 * DOWN, 5 * LEFT + 1 * DOWN)
        arrow4 = Arrow(5.25 * LEFT + 1 * DOWN, 3.5 * LEFT + 1 * DOWN)
        anglearrow = VGroup(arrline, arrow4)

        arrow5 = Arrow(1 * UP, 1 * DOWN, buff=0.35)

        ###############################
        # Start with the video timeline
        ###############################

        self.play(title.animate.scale(0.5).to_corner(UL), run_time=1)
        self.wait(2)
        # 3
        self.play(Write(formula), run_time=2)
        self.wait(1)
        # 6
        self.play(formula.animate.scale(0.7).move_to(2 * UP), run_time=1)
        self.wait(1)
        self.play(Create(graph), run_time=2)
        self.wait(1)
        # 11
        self.play(Write(g_x), run_time=1)
        self.play(Create(linegx), run_time=3)
        self.wait(1.5)
        # 16.5
        self.play(Write(h_x), run_time=1)
        self.play(Create(linehx), run_time=3)
        self.wait(1.5)
        # 22
        self.play(
            FadeOut(g_x, shift=DOWN),
            FadeOut(linegx, shift=DOWN),
            FadeOut(linehx, shift=DOWN),
            FadeOut(formula, shift=DOWN),
            FadeOut(graph, shift=DOWN),
            h_x.animate.scale(1.5).move_to(2.5 * UP),
            run_time=1,
        )
        self.wait(1)
        # 24
        self.play(Create(arrow1), run_time=1)
        self.play(Write(directtxt), run_time=1)
        self.wait(3)
        # 29
        self.play(Create(arrow2), run_time=1)
        self.play(Write(priotxt), run_time=1)
        self.play(Create(arrow3), run_time=1)
        self.play(Write(reducetxt), run_time=1)
        self.wait(5)
        # 38
        self.play(
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(arrow3),
            FadeOut(directtxt),
            FadeOut(priotxt),
            FadeOut(reducetxt),
            FadeOut(h_x),
            run_time=1,
        )
        self.wait(1)
        # 40

        self.play(Write(admissibleexplain), run_time=4)
        self.wait(2)
        # 46
        self.play(FadeIn(anglearrow), run_time=1)
        self.play(Write(guaranteetxt), run_time=1)
        self.wait(2)
        # 50
        self.play(FadeOut(anglearrow), FadeOut(guaranteetxt), run_time=1)
        self.wait(1)
        # 52
        self.play(admissibleexplain.animate.scale(0.7).to_edge(DOWN), run_time=1)
        self.play(FadeIn(ad_graph), FadeIn(nonad_graph), run_time=1)
        self.play(
            ad_graph.animate.move_to(1 * UP),
            nonad_graph.animate.move_to(1.5 * DOWN),
            run_time=2,
        )
        self.wait(1)
        # 57
        self.play(FadeIn(admissibletitle), FadeIn(notadmissibletitle), run_time=1)
        self.play(
            FadeIn(ad_weight1.move_to(ad_line1.get_center() + 0.5 * DOWN)),
            FadeIn(ad_weight2.move_to(ad_line2.get_center() + 0.5 * DOWN)),
            FadeIn(nonad_weight1.move_to(nonad_line1.get_center() + 0.5 * DOWN)),
            FadeIn(nonad_weight2.move_to(nonad_line2.get_center() + 0.5 * DOWN)),
            run_time=1,
        )
        self.wait(10)
        # 1:09

        self.play(
            FadeIn(ad_heur_s.move_to(ad_point_s.get_center() + 1 * DOWN)),
            run_time=1,
        )
        # 1:10
        self.wait(4)
        self.play(
            FadeIn(ad_heur_x.move_to(ad_point_x.get_center() + 1 * DOWN)),
            run_time=1,
        )
        # 1:15
        self.wait(4)
        self.play(
            FadeIn(ad_heur_e.move_to(ad_point_e.get_center() + 1 * DOWN)),
            run_time=1,
        )
        self.wait(4.5)
        # 1:24.5

        self.play(
            FadeIn(nonad_heur_s.move_to(nonad_point_s.get_center() + 1 * DOWN)),
            run_time=1,
        )

        # 1:25.5
        self.wait(1)
        self.play(
            FadeIn(nonad_heur_x.move_to(nonad_point_x.get_center() + 1 * DOWN)),
            run_time=1,
        )

        # 1:27.5
        self.wait(1)
        self.play(
            FadeIn(nonad_heur_e.move_to(nonad_point_e.get_center() + 1 * DOWN)),
            run_time=1,
        )
        self.wait(7.5)
        self.play(
            FadeOut(ad_graph),
            FadeOut(nonad_graph),
            FadeOut(admissibletitle),
            FadeOut(notadmissibletitle),
            FadeOut(ad_weight1),
            FadeOut(ad_weight2),
            FadeOut(nonad_weight1),
            FadeOut(nonad_weight2),
            FadeOut(ad_heur_s),
            FadeOut(ad_heur_x),
            FadeOut(ad_heur_e),
            FadeOut(nonad_heur_s),
            FadeOut(nonad_heur_x),
            FadeOut(nonad_heur_e),
            FadeOut(admissibleexplain),
            run_time=1,
        )
        self.wait(1)
        # 1:39
        self.play(Write(efficiencytxt), run_time=1)
        self.wait(1)
        # 1:41
        self.play(Create(arrow5), run_time=1)
        self.play(Write(dependendtxt), run_time=1)
        self.wait(6)
        # 1:49
        self.play(
            FadeOut(title),
            FadeOut(efficiencytxt),
            FadeOut(arrow5),
            FadeOut(dependendtxt),
            run_time=1,
        )
