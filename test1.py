from manim import *
import os

class Intro(Scene):
    def construct(self):
        # Titeltext
        title = Text("A* Pathfinding Algorithm", font_size=40)
        title.set_color(YELLOW)
        title.next_to(ORIGIN, UP, buff=0.5)

        # Untertiteltext
        subtitle = Text("An Introduction with Manim", font_size=30)
        subtitle.next_to(title, DOWN)

        # Animation
        self.play(Create(title), Write(subtitle))
        self.wait(2) 

        self.play(FadeOut(title), FadeOut(subtitle))
        self.wait(1)

        # Text1
        new_text1 = Text("Let's explore the A* algorithm!", font_size=35)
        self.play(Create(new_text1))
        self.wait(3)

        self.play(FadeOut(new_text1))
        self.wait(1)

        # Text2
        new_text2 = Text("Für Fortnite!", font_size=35)
        new_text2.set_color(RED)
        self.play(FadeIn(new_text2))
        self.wait(2)

        self.play(FadeOut(new_text2))
        self.wait(1)

if __name__ == "__main__":
    #os.system(f"manim -pql {__file__} MainAnim")
    os.system(f"manim -qh {__file__} MainAnim")
"""
# renderring of the video
if __name__ == "__main__":
    module_name = file_name_to_module_name(__file__)
    command_A = f"manim -pql {module_name}.py {Intro.__name__} -o output_file.mp4"
    os.system(command_A)

"""