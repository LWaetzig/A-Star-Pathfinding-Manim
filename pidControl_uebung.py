from manim import *

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
        title = Text("Herzlich Willkommen", font_size=50, color=RED, line_spacing=0.5)
        title.move_to(ORIGIN)
        self.play(Write(title, run_time=2))

class PIDControl(Scene):
    def construct(self):
        # Texte
        title = Text("PID-Regelung", font_size=40)
        equation = MathTex(
            "u(t) = K_p e(t) + K_i \\int e(t)dt + K_d \\frac{de(t)}{dt}",
            font_size=30
        )
        explanation = Text(
            "Proportional-Integral-Derivative Regelung",
            font_size=25
        )

        # Animationen
        self.play(Write(title), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), run_time=1)
        self.play(Write(equation), run_time=2)
        self.wait(2)
        self.play(Transform(equation, explanation), run_time=2)
        self.wait(2)

class PIDControlGraph(Scene):
    def construct(self):
        # Achsen erstellen
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": BLUE},
        )

        # PID-Funktion definieren
        def pid_function(x):
            return 0.5 * x - 0.1 * x**2 + np.sin(x)

        # FunktionGraph erstellen
        pid_graph = FunctionGraph(
            pid_function,
            x_range=[0, 5],
            color=GREEN,
        )

        # Texte
        title = Text("PID-Regelung", font_size=40)
        equation = MathTex(
            "u(t) = K_p e(t) + K_i \\int e(t)dt + K_d \\frac{de(t)}{dt}",
            font_size=30
        )

        # Animationen
        self.play(Write(title), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), run_time=1)

        self.play(Write(equation), run_time=2)
        self.wait(1)

        self.play(
            Create(axes),
            run_time=2
        )
        self.play(
            Create(pid_graph),
            run_time=3
        )
        self.wait(2)




