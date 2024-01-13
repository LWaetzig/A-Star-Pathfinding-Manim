import os
from manim import *


class OutroScene(MovingCameraScene):
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
