from manim import *


class OutroScene(MovingCameraScene):
    def construct(self):
        # set default font
        Text.set_default(font="Arial")

        # Create Texts
        text_L = Text("L", font="Arial").scale(2).move_to(1 * UP)
        text_A = Text("A", font="Arial").scale(2)
        text_N = Text("N", font="Arial").scale(2).move_to(1 * DOWN)

        lucas = Text("Lucas Wätzig", font="Arial").scale(2).move_to(1 * UP)
        alex = Text("Alexander Paul", font="Arial").scale(2)
        nicho = Text("Nicholas Link", font="Arial").scale(2).move_to(1 * DOWN)

        text_L_black = Text("L", font="Arial", color=BLACK).scale(2).move_to(1 * UP)
        text_A_black = Text("A", font="Arial", color=BLACK).scale(2)
        text_N_black = Text("N", font="Arial", color=BLACK).scale(2).move_to(1 * DOWN)

        # Create Groups
        lucasg = VGroup(text_L, lucas)
        alexg = VGroup(text_A, alex)
        nichog = VGroup(text_N, nicho)

        ###############################
        # Start video timeline
        ###############################

        self.play(Write(text_L), run_time=1)
        self.play(Write(text_A), run_time=1)
        self.play(Write(text_N), run_time=1)

        self.play(Transform(text_L, lucas), run_time=1)
        self.play(Transform(text_A, alex), run_time=1)
        self.play(Transform(text_N, nicho), run_time=1)

        
        self.play(
            Transform(lucasg, text_L_black),
            Transform(alexg, text_A_black),
            Transform(nichog, text_N_black),
            run_time=1,
        )