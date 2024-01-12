import os
from manim import *


class Outro(MovingCameraScene):
    def construct(self):
        # set default font
        Text.set_default(font="Arial")

        image1 = ImageMobject(os.path.join("data", "image1.png")).scale(1.5)
        image2 = ImageMobject(os.path.join("data", "image2.png")).scale(1.5)
        image3 = ImageMobject(os.path.join("data", "image3.png")).scale(1.5)
        text = Text("PRESENTED", font_size=70)

        # set position
        text.shift(DOWN * 2.2)
        image1.to_edge(UL).shift(RIGHT).scale(0.6)
        image2.shift(UP)
        image3.to_edge(UR).shift(LEFT).scale(0.6)

        self.play(
            FadeIn(image2),
            FadeIn(text, shift=UP, scale=0.8),
            FadeIn(image1),
            FadeIn(image3),
            run_time=2,
        )
        self.wait(3)
        self.clear()
        self.wait(2)

        timeline = NumberLine(
            x_range=[0, 100, 1],
            length=100,
            include_numbers=True,
            include_ticks=True,
            color=WHITE,
        ).rotate(PI / 2)
        timeline.move_to(ORIGIN)
        self.play(Create(timeline), run_time=5)
        self.wait(2)

        # vertical_line = Line(
        #     start=ORIGIN, end=[0, -20, 0], color=WHITE, stroke_opacity=0
        # )
        # self.play(Create(vertical_line))
        # self.wait(1)
        # self.play(self.camera.frame.animate.shift(DOWN * 20))
        # self.wait(1)
        # self.play(Write(Text("THANK YOU", font_size=70).next_to(vertical_line, DOWN)))
        # self.wait(2)
