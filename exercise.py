import random as rd
from math import *

import numpy as np
from colour import Color

from custom_manim_utils.custom_consts import *
from custom_manim_utils.custom_functions import *
from manim import *

config.frame_width = 16
config.frame_height = 9
config.background_color = BLACK

ETH_COIN = create_circle_asset(
    Tex(r"\textbf{ETH}", color=WHITE, font_size=30), fill_color=C_ETH
)
USDT_COIN = create_circle_asset(
    Tex(r"\textbf{USDT}", color=WHITE, font_size=25), fill_color=C_USDT
)
BTC_COIN = create_circle_asset(
    Tex(r"\textbf{BTC}", color=WHITE, font_size=30), fill_color=C_BTC
)


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)


class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        # place the circle two units left from the origin
        circle.move_to(LEFT * 2)
        # place the square to the left of the circle
        square.next_to(circle, L)
        # align the left border of the triangle to the left border of the circle
        triangle.align_to(circle, R)

        self.add(circle, square, triangle)
        self.wait(1)


class MobjectStyling(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.add(circle, square, triangle)
        self.wait(1)


class MobjectZOrder(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.add(triangle, square, circle)
        self.wait(1)


class SomeAnimations(Scene):
    def construct(self):
        square = Square()

        # some animations display mobjects, ...
        self.play(FadeIn(square))

        # ... some move or rotate mobjects around...
        self.play(Rotate(square, PI))

        # some animations remove mobjects from the screen
        self.play(FadeOut(square))

        self.wait(1)


class AnimateExample(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        # animate the change of color
        self.play(square.animate.set_fill(WHITE))

        # animate the change of position and the rotation at the same time
        self.play(square.animate.shift(UP).rotate(PI / 3))
        self.wait(1)


class CountingScene(Scene):
    def construct(self):
        # Create Decimal Number and add it to scene
        number = DecimalNumber().set_color(WHITE).scale(5)
        # Add an updater to keep the DecimalNumber centered as its value changes
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)

        # Play the Count Animation to count from 0 to 100 in 4 seconds
        self.play(Count(number, 0, 100), run_time=2, rate_func=double_smooth)

        self.wait()


class MobjectExample(Scene):
    def construct(self):
        p1 = [-1, -1, 0]
        p2 = [1, -1, 0]
        p3 = [1, 1, 0]
        p4 = [-1, 1, 0]
        a = (
            Line(p1, p2)
            .append_points(Line(p2, p3).points)
            .append_points(Line(p3, p4).points)
        )
        point_start = a.get_start()
        point_end = a.get_end()
        point_center = a.get_center()
        self.add(
            Text(f"a.get_start() = {np.round(point_start,2).tolist()}", font_size=24)
            .to_edge(UR)
            .set_color(YELLOW)
        )
        self.add(
            Text(f"a.get_end() = {np.round(point_end,2).tolist()}", font_size=24)
            .next_to(self.mobjects[-1], DOWN)
            .set_color(RED)
        )
        self.add(
            Text(f"a.get_center() = {np.round(point_center,2).tolist()}", font_size=24)
            .next_to(self.mobjects[-1], DOWN)
            .set_color(BLUE)
        )

        self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        self.add(Dot(a.get_end()).set_color(RED).scale(2))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[Dot(x) for x in a.points])
        self.add(a)


class ExampleRotation(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1a = Square().set_color(RED).shift(LEFT)
        m1b = Circle().set_color(RED).shift(LEFT)
        m2a = Square().set_color(BLUE).shift(RIGHT)
        m2b = Circle().set_color(BLUE).shift(RIGHT)

        points = m2a.points
        points = np.roll(
            points, int(len(points) / 4), axis=0
        )  # 배열을 역순하여 재생 시 거꾸로 돌게 함.
        m2a.points = points

        self.play(Transform(m1a, m1b), Transform(m2a, m2b), run_time=1)


class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"\LaTeX", font_size=144, fill_color=BLACK)
        self.add(tex)


class MathTeXDemo(Scene):
    def construct(self):
        rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96, fill_color=BLACK)
        rtarrow1 = Tex(r"$\xrightarrow{x^6y^8}$", font_size=96, fill_color=BLACK)

        self.add(VGroup(rtarrow0, rtarrow1).arrange(DOWN))


class AMSLaTeX(Scene):
    def construct(self):
        tex = Tex(
            r"$\mathtt{H} \looparrowright$ \LaTeX", font_size=144, fill_color=BLACK
        )
        self.add(tex)


class ColoredLaTeX(Scene):
    def construct(self):
        tex = Tex(r"Hello \LaTeX", color=BLUE, font_size=144)
        self.add(tex)


class AddPackageLatex(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(
            r"$\mathscr{H} \rightarrow \mathbb{H}$}",
            tex_template=myTemplate,
            font_size=144,
            color=BLUE,
        )
        self.add(tex)


class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex("Hello", r"$\bigstar$", r"\LaTeX", font_size=144, color=BLUE)
        tex.set_color_by_tex("bigstar", RED)
        self.add(tex)


class IncorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            color=RED,
        )
        equation.set_color_by_tex("x", BLACK)
        self.add(equation)


class CorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = Tex(r"가나다라마바사", color=RED)
        self.add(equation)


class News(Scene):
    def get_title(self):
        t1 = Tex(r"IMF 국제통화기금", color=BLUE, font_size=50)
        t2 = Tex(r"2022 세계 경제 전망", color=WHITE, font_size=65)

        text = VGroup(t1, t2).arrange(R, buff=0.3)

        underline = Underline(text, buff=0.3)

        return VGroup(text, underline)

    def get_body(self):
        t1 = Tex(r"세계", color=WHITE, font_size=180)
        t2 = Tex(r"-3\%", color=RED, font_size=240)

        return VGroup(t1, t2).arrange(R, buff=0.8)

    def get_subtitle(self):
        rect1 = Rectangle(width=14.5, height=0.4, fill_opacity=1, fill_color=BLUE)
        t1 = Tex(r"쿠오모", color=WHITE, font_size=30)
        t2 = Tex(r"뉴욕주지사", color=WHITE, font_size=25)
        up_text = VGroup(t1, t2).move_to(rect1, L).arrange(R, buff=0.4, center=False)
        rect1.add(up_text)

        rect2 = Rectangle(width=14.5, height=0.8, fill_opacity=1, fill_color=WHITE)
        t3 = Tex(r"세계 경제 전망이 ...,", color=BLUE_E, font_size=30)
        t4 = Tex(r"물품 구매도 각 주가 책임져야...", color=BLUE_E, font_size=30)
        t4.next_to(t3, DOWN, buff=0.1, aligned_edge=L)
        down_text = VGroup(t3, t4).move_to(rect2, L)
        rect2.add(down_text)

        rect2.next_to(rect1, DOWN, buff=0)

        return VGroup(rect1, rect2)

    def construct(self):
        # 1. create objects
        title = self.get_title()
        body = self.get_body()
        subtitle = self.get_subtitle()

        # 2. set the position
        title.move_to(ORIGIN).to_edge(UP, buff=1)
        body.next_to(title, DOWN, buff=1)
        subtitle.to_edge(DOWN, buff=0.5)

        # 3. animation
        self.add(title)
        self.add(body)
        self.add(subtitle)


class ManimCELogo(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)


class BraceAnnotation(Scene):
    def construct(self):
        dot = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal distance")
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        b2text = b2.get_tex("x-x_1")
        b3 = BraceBetweenPoints(Dot([2, -1, 0]).get_center(), dot2.get_center())
        b3text = b3.get_text("Vertical distance")
        self.add(index_labels(b1[0]))
        self.add(line, dot, dot2, b1, b2, b3, b1text, b2text, b3text)


class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text("(0, 0)").next_to(dot, DOWN)
        tip_text = Text("(2, 2)").next_to(arrow.get_end(), RIGHT)
        self.add(numberplane, dot, arrow, origin_text, tip_text)


class GradientImageFromArray(Scene):
    def construct(self):
        n = 256
        imageArray = np.uint8([[i * 256 / n for i in range(0, n)] for _ in range(0, n)])
        image = ImageMobject(imageArray).scale(2)
        image.background_rectangle = SurroundingRectangle(image, GREEN)
        self.add(image, image.background_rectangle)


class BooleanOperations(Scene):
    def construct(self):
        ellipse1 = Ellipse(
            width=4.0, height=5.0, fill_opacity=0.5, color=BLUE, stroke_width=10
        ).move_to(LEFT)
        ellipse2 = ellipse1.copy().set_color(color=RED).move_to(RIGHT)
        bool_ops_text = MarkupText("<u>Boolean Operation</u>").next_to(ellipse1, UP * 3)
        ellipse_group = Group(bool_ops_text, ellipse1, ellipse2).move_to(LEFT * 3)
        self.play(FadeIn(ellipse_group))

        i = Intersection(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)
        self.play(i.animate.scale(0.25).move_to(RIGHT * 5 + UP * 2.5))
        intersection_text = Text("Intersection", font_size=23).next_to(i, UP)
        self.play(FadeIn(intersection_text))

        u = Union(ellipse1, ellipse2, color=ORANGE, fill_opacity=0.5)
        union_text = Text("Union", font_size=23)
        self.play(u.animate.scale(0.3).next_to(i, DOWN, buff=union_text.height * 3))
        union_text.next_to(u, UP)
        self.play(FadeIn(union_text))

        e = Exclusion(ellipse1, ellipse2, color=YELLOW, fill_opacity=0.5)
        exclusion_text = Text("Exclusion", font_size=23)
        self.play(
            e.animate.scale(0.3).next_to(u, DOWN, buff=exclusion_text.height * 3.5)
        )
        exclusion_text.next_to(e, UP)
        self.play(FadeIn(exclusion_text))

        d = Difference(ellipse1, ellipse2, color=PINK, fill_opacity=0.5)
        difference_text = Text("Difference", font_size=23)
        self.play(
            d.animate.scale(0.3).next_to(u, LEFT, buff=difference_text.height * 3.5)
        )
        difference_text.next_to(d, UP)
        self.play(FadeIn(difference_text))
