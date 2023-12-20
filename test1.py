from manim import *
import os

class Introduction(Scene):
    def construct(self):
        introduction_text = [
            "Herzlich Willkommen bei AlgorithmAlchemy!",
            "Heute tauchen wir in die faszinierende Welt des A* Algorithmus ein.",
            "A* ist ein intelligenter Suchalgorithmus,",
            "der in vielen Bereichen der künstlichen Intelligenz und Robotik eingesetzt wird.",
            "Es hilft, den effizientesten Weg zwischen zwei Punkten in einem Netzwerk zu finden.",
            "Lass uns gemeinsam entdecken, wie dieser mächtige Algorithmus funktioniert!"
        ]

        # Untertitel anzeigen
        self.show_subtitles(introduction_text)

    def show_subtitles(self, text_lines):
        subtitles = VGroup(*[Text(line, font_size=24, t2c={'A*': YELLOW}).to_edge(DOWN) for line in text_lines])

        for i, subtitle in enumerate(subtitles):
            # Fade out the previous subtitle
            if i > 0:
                self.play(FadeOut(subtitles[i - 1], run_time=1))

                
        
            # Play the current subtitle
            self.wait(0.1)
            self.play(Write(subtitle, run_time=len(subtitle) * 0.05))
            self.wait(0.1)

        # Fade out the last subtitle
        self.play(FadeOut(subtitles[-1], run_time=1))



    

class Animation(Scene):
    def construct(self):
        # Hintergrund
        background = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color="#0c0c0c",  # Dunkle Hintergrundfarbe
            fill_opacity=1
        )
        self.play(FadeIn(background))

        # Texteffekte
        title = Text("Herzlich Willkommen", font_size=50, color=YELLOW, line_spacing=0.5)
        title.move_to(ORIGIN)
        self.play(Write(title, run_time=2))

        # Pfeile und Animationen
        arrow1 = Arrow(LEFT, RIGHT, color="#ffffff")
        arrow1.next_to(title, DOWN)
        self.play(GrowArrow(arrow1))

        arrow2 = Arrow(RIGHT, LEFT, color="#ffffff")
        arrow2.next_to(title, DOWN)
        self.play(GrowArrow(arrow2))

        text = Text("Der A* Algorithmus!", font_size=35, color="#00ff00")
        text.next_to(title, DOWN, buff=0.5)
        self.play(Create(text))
        self.wait(0.5) 
        self.play(FadeOut(text))

        # Schlussanimation
        self.wait(2)
        self.play(FadeOut(title), FadeOut(arrow1), FadeOut(arrow2), FadeOut(text))


class VideoIntro(Scene):
    def construct(self):
       #create logo
        logo=Circle(fill_opacity=5).scale(2.5)
        logo.set_fill()
        logo.set_color(BLUE)
        text = Text("Algorithm\n Alchemy", font_size=40, color=YELLOW, line_spacing=0.5)
        text.next_to(logo, DOWN, buff=0).scale(1.5)

        text.move_to(ORIGIN)
        logo.move_to(ORIGIN)

        self.play(DrawBorderThenFill(logo, run_time=6), Write(text, run_time=6))
        self.wait()

        text.scale(0.2)
        logoSmall=logo.scale(0.2)
        logoSmall.to_corner(DOWN+RIGHT)
        text2=text.next_to(logoSmall,0,buff=0)

        self.play(Write(logoSmall), Write(text2))
        self.wait(1)



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
