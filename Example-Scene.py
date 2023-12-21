from manim import *
import numpy as np

class AstarVideo(MovingCameraScene):
    def adjust_line_to_circle_boundary(self, start_point, end_point):
        line_vector = end_point.get_center() - start_point.get_center()
        normalized_vector = line_vector / np.linalg.norm(line_vector)
        adjusted_start = start_point.get_center() + 0.25 * normalized_vector
        adjusted_end = end_point.get_center() - 0.25 * normalized_vector
        
        return Line(adjusted_start, adjusted_end)
    
    def create_point(self, center, label):
        circle = Circle(radius=0.25, color=BLUE, fill_opacity=0.5)
        letter = Text(label, color=WHITE).scale(0.5)
        circle.move_to(center)
        letter.move_to(circle.get_center())

        return circle, letter
    
    def create_list_element(self, position, label, via_text, went_num, togo_num):
        element = RoundedRectangle(width=4, height=1, corner_radius=0.25, color=BLUE).move_to(position)
        element_label = Text(label).scale(1).move_to(element.get_center() + 1.65 * LEFT)

        separator1 = Line(element.get_edge_center(UP) + 1.3 * LEFT, element.get_edge_center(DOWN) + 1.3 * LEFT, color=BLUE)

        via = Text("via").scale(0.5).move_to(element.get_center() + 0.9 * LEFT + 0.3 * UP)
        via_value = Text(via_text).scale(0.75).move_to(via.get_center() + 0.45 * DOWN)

        separator2 = Line(element.get_edge_center(UP) + 0.45 * LEFT, element.get_edge_center(DOWN) + 0.45 * LEFT, color=BLUE)

        went = Text("went").scale(0.5).move_to(element.get_center() + 0.1 * RIGHT + 0.3 * UP)
        went_value = Text(went_num, color=GREEN).scale(0.75).move_to(went.get_center() + 0.45 * DOWN)

        separator3 = Line(element.get_edge_center(UP) + 0.7 * RIGHT, element.get_edge_center(DOWN) + 0.7 * RIGHT, color=BLUE)

        togo = Text("+ to go").scale(0.5).move_to(element.get_center() + 1.35 * RIGHT + 0.3 * UP)
        togo_value = Text(togo_num, color=RED).scale(0.75).move_to(togo.get_center() + 0.45 * DOWN)

        group = VGroup(element, element_label, separator1, via, via_value, separator2, went, went_value, separator3, togo, togo_value)
        
        return group, via_value, went_value, togo_value
    
    def construct(self):
        Text.set_default(font="Arial")



        # Create texts
        title = Text("Example").scale(1.5)
        
        start_text = Text("Start").scale(1).to_edge(UP)
        end_text = Text("Ende").scale(1).to_edge(DOWN)
        
        

        # Create graph elements
        # Create points
        point_s, letter_s = self.create_point(3.5 * UP, "S")
        point_a, letter_a = self.create_point(6 * LEFT + 2.1 * UP, "A")
        point_b, letter_b = self.create_point(3 * LEFT + 2.1 * UP, "B")
        point_c, letter_c = self.create_point(4.5 * RIGHT + 2.1 * UP, "C")
        point_d, letter_d = self.create_point(6 * LEFT + 0.7 * UP, "D")
        point_f, letter_f = self.create_point(6 * LEFT + 0.7 * DOWN, "F")
        point_g, letter_g = self.create_point(3 * LEFT + 2.1 * DOWN, "G")
        point_h, letter_h = self.create_point(3 * LEFT + 0.7 * UP, "H")
        point_i, letter_i = self.create_point(3 * RIGHT + 0.7 * DOWN, "I")
        point_j, letter_j = self.create_point(6 * RIGHT + 0.7 * DOWN, "J")
        point_k, letter_k = self.create_point(4.5 * RIGHT + 2.1 * DOWN, "K")
        point_l, letter_l = self.create_point(4.5 * RIGHT + 0.7 * UP, "L")
        point_e, letter_e = self.create_point(3.5 * DOWN, "E")

        # Create lines
        line_sa = self.adjust_line_to_circle_boundary(point_s, point_a)
        line_sb = self.adjust_line_to_circle_boundary(point_s, point_b)
        line_sc = self.adjust_line_to_circle_boundary(point_s, point_c)
        line_ab = self.adjust_line_to_circle_boundary(point_a, point_b)
        line_ad = self.adjust_line_to_circle_boundary(point_a, point_d)
        line_bd = self.adjust_line_to_circle_boundary(point_b, point_d)
        line_bh = self.adjust_line_to_circle_boundary(point_b, point_h)
        line_df = self.adjust_line_to_circle_boundary(point_d, point_f)
        line_hf = self.adjust_line_to_circle_boundary(point_h, point_f)
        line_hg = self.adjust_line_to_circle_boundary(point_h, point_g)
        line_ge = self.adjust_line_to_circle_boundary(point_g, point_e)
        line_cl = self.adjust_line_to_circle_boundary(point_c, point_l)
        line_li = self.adjust_line_to_circle_boundary(point_l, point_i)
        line_lj = self.adjust_line_to_circle_boundary(point_l, point_j)
        line_ij = self.adjust_line_to_circle_boundary(point_i, point_j)
        line_ik = self.adjust_line_to_circle_boundary(point_i, point_k)
        line_jk = self.adjust_line_to_circle_boundary(point_j, point_k)
        line_ke = self.adjust_line_to_circle_boundary(point_k, point_e)

        # Create weights
        weight_sa = Text("7", color=GREEN, weight=BOLD).scale(0.5).move_to(line_sa.get_center() + 0.25 * UP)
        weight_sb = Text("2", color=GREEN, weight=BOLD).scale(0.5).move_to(line_sb.get_center() + 0.25 * DOWN)
        weight_ab = Text("3", color=GREEN, weight=BOLD).scale(0.5).move_to(line_ab.get_center() + 0.25 * DOWN)
        weight_sc = Text("3", color=GREEN, weight=BOLD).scale(0.5).move_to(line_sc.get_center() + 0.25 * UP)
        weight_ad = Text("4", color=GREEN, weight=BOLD).scale(0.5).move_to(line_ad.get_center() + 0.25 * LEFT)
        weight_bd = Text("4", color=GREEN, weight=BOLD).scale(0.5).move_to(line_bd.get_center() + 0.25 * DOWN)
        weight_bh = Text("1", color=GREEN, weight=BOLD).scale(0.5).move_to(line_bh.get_center() + 0.25 * RIGHT)
        weight_df = Text("5", color=GREEN, weight=BOLD).scale(0.5).move_to(line_df.get_center() + 0.25 * LEFT)
        weight_hf = Text("3", color=GREEN, weight=BOLD).scale(0.5).move_to(line_hf.get_center() + 0.25 * DOWN)
        weight_hg = Text("2", color=GREEN, weight=BOLD).scale(0.5).move_to(line_hg.get_center() + 0.25 * RIGHT)
        weight_ge = Text("2", color=GREEN, weight=BOLD).scale(0.5).move_to(line_ge.get_center() + 0.25 * UP)
        weight_cl = Text("2", color=GREEN, weight=BOLD).scale(0.5).move_to(line_cl.get_center() + 0.25 * LEFT)
        weight_li = Text("4", color=GREEN, weight=BOLD).scale(0.5).move_to(line_li.get_center() + 0.25 * LEFT + 0.25 * UP)
        weight_lj = Text("4", color=GREEN, weight=BOLD).scale(0.5).move_to(line_lj.get_center() + 0.25 * RIGHT + 0.25 * UP)
        weight_ij = Text("6", color=GREEN, weight=BOLD).scale(0.5).move_to(line_ij.get_center() + 0.25 * DOWN)
        weight_ik = Text("4", color=GREEN, weight=BOLD).scale(0.5).move_to(line_ik.get_center() + 0.25 * LEFT + 0.25 * DOWN)
        weight_jk = Text("4", color=GREEN, weight=BOLD).scale(0.5).move_to(line_jk.get_center() + 0.25 * RIGHT + 0.25 * DOWN)
        weight_ke = Text("5", color=GREEN, weight=BOLD).scale(0.5).move_to(line_ke.get_center() + 0.25 * UP)

        # Create heuristic weights
        heuristic_s = Text("10", color=RED, weight=BOLD).scale(0.5).move_to(point_s.get_center() + 0.5 * DOWN)
        heuristic_a = Text("9", color=RED, weight=BOLD).scale(0.5).move_to(point_a.get_center() + 0.5 * UP)
        heuristic_b = Text("7", color=RED, weight=BOLD).scale(0.5).move_to(point_b.get_center() + 0.25 * DOWN + 0.5 * RIGHT)
        heuristic_c = Text("8", color=RED, weight=BOLD).scale(0.5).move_to(point_c.get_center() + 0.5 * UP)
        heuristic_d = Text("8", color=RED, weight=BOLD).scale(0.5).move_to(point_d.get_center() + 0.5 * LEFT)
        heuristic_f = Text("6", color=RED, weight=BOLD).scale(0.5).move_to(point_f.get_center() + 0.5 * DOWN)
        heuristic_g = Text("3", color=RED, weight=BOLD).scale(0.5).move_to(point_g.get_center() + 0.5 * LEFT)
        heuristic_h = Text("6", color=RED, weight=BOLD).scale(0.5).move_to(point_h.get_center() + 0.5 * RIGHT)
        heuristic_i = Text("4", color=RED, weight=BOLD).scale(0.5).move_to(point_i.get_center() + 0.5 * LEFT)
        heuristic_j = Text("4", color=RED, weight=BOLD).scale(0.5).move_to(point_j.get_center() + 0.5 * RIGHT)
        heuristic_k = Text("3", color=RED, weight=BOLD).scale(0.5).move_to(point_k.get_center() + 0.25 * DOWN + 0.5 * RIGHT)
        heuristic_l = Text("6", color=RED, weight=BOLD).scale(0.5).move_to(point_l.get_center() + 0.25 * UP + 0.5 * RIGHT)
        heuristic_e = Text("0", color=RED, weight=BOLD).scale(0.5).move_to(point_e.get_center() + 0.5 * UP)







        # Create groups
        group_start = VGroup(point_s, letter_s)
        group_end = VGroup(point_e, letter_e)

        group_other_points = VGroup(point_a, point_b, point_c, point_d, point_f, point_g, point_h, point_i, point_j, point_k, point_l)
        group_other_letters = VGroup(letter_a, letter_b, letter_c, letter_d, letter_f, letter_g, letter_h, letter_i, letter_j, letter_k, letter_l)

        group_lines = VGroup(line_sa, line_sb, line_sc, line_ab, line_ad, line_bd, line_bh, line_df, line_hf, line_hg, line_ge, line_cl, line_li, line_lj, line_ij, line_ik, line_jk, line_ke)

        group_explain = VGroup(point_l, point_i, point_j, point_k, point_e)
        group_explain_weights = VGroup(weight_li, weight_lj, weight_ij, weight_ik, weight_jk, weight_ke)
        group_other_weights = VGroup(weight_sa, weight_sb, weight_ab, weight_sc, weight_ad, weight_bd, weight_bh, weight_df, weight_hf, weight_hg, weight_ge, weight_cl)
        group_explain_heuristics = VGroup(heuristic_i, heuristic_j, heuristic_k, heuristic_l, heuristic_e)
        group_other_heuristics = VGroup(heuristic_s, heuristic_a, heuristic_b, heuristic_c, heuristic_d, heuristic_f, heuristic_g, heuristic_h)

        group_sa = VGroup(point_s, point_a)
        group_sb = VGroup(point_s, point_b)
        group_sc = VGroup(point_s, point_c)
        group_sba = VGroup(group_sb, point_a)


        # Create list elements
        list_outline = RoundedRectangle(width=7, height=12, corner_radius=0.25, color=BLUE).move_to(12 * RIGHT + 0.5 * DOWN)
        list_title = Text("Open List").scale(1).move_to(list_outline.get_center() + 6.5 * UP)

        focus_line = DashedLine(start=list_outline.get_edge_center(LEFT) + 4 * UP, end=list_outline.get_edge_center(RIGHT) + 4 * UP, color=BLUE)

        path_list_outline = RoundedRectangle(width=7, height=12, corner_radius=0.25, color=BLUE).move_to(22 * RIGHT + 0.5 * DOWN)
        path_list_title = Text("Done List").scale(1).move_to(path_list_outline.get_center() + 6.5 * UP)

        element_s_group, element_s_via_text, element_s_went_num, element_s_togo_num = self.create_list_element(
            point_s.get_center() + 1.4 * UP + 1 * RIGHT, "S", "-", "-", "-"
        )

        element_a_group, element_a_via_text, element_a_went_num, element_a_togo_num = self.create_list_element(
            point_a.get_center() + 2 * UP + 2 * RIGHT, "A", "-", "-", "-"
        )

        element_b_group, element_b_via_text, element_b_went_num, element_b_togo_num = self.create_list_element(
            group_sb.get_center() + 1.4 * DOWN + 1.5 * RIGHT, "B", "-", "-", "-"
        )

        element_c_group, element_c_via_text, element_c_went_num, element_c_togo_num = self.create_list_element(
            group_sc.get_center() + 2 * UP, "C", "-", "-", "-"
        )

        


        # elements to animate
        animation_group_heur_s = VGroup(element_s_togo_num, heuristic_s.copy())
        element_s_group.add(animation_group_heur_s)

        animation_group_via_as = VGroup(element_a_via_text, letter_s.copy())
        animation_group_went_as = VGroup(element_a_went_num, weight_sa.copy())
        animation_group_heur_a = VGroup(element_a_togo_num, heuristic_a.copy(), weight_sa.copy())
        element_a_group.add(animation_group_via_as, animation_group_went_as, animation_group_heur_a)

        animation_group_via_bs = VGroup(element_b_via_text, letter_s.copy())
        animation_group_went_bs = VGroup(element_b_went_num, weight_sb.copy())
        animation_group_heur_b = VGroup(element_b_togo_num, heuristic_b.copy(), weight_sb.copy())
        element_b_group.add(animation_group_via_bs, animation_group_went_bs, animation_group_heur_b)

        animation_group_via_cs = VGroup(element_c_via_text, letter_s.copy())
        animation_group_went_cs = VGroup(element_c_went_num, weight_sc.copy())
        animation_group_heur_c = VGroup(element_c_togo_num, heuristic_c.copy(), weight_sc.copy())
        element_c_group.add(animation_group_via_cs, animation_group_went_cs, animation_group_heur_c)
   
        





        # Start with the timeline
        
        self.play(Write(title))
        self.play(FadeOut(title, run_time=1.5))
        self.wait(1)

        camera = self.camera.frame.save_state()
        self.play(Write(start_text), Write(end_text))
        self.wait(2)

        self.play(ReplacementTransform(start_text, group_start), ReplacementTransform(end_text, group_end))
        self.play(Create(group_other_points), Write(group_other_letters), run_time=2)
        self.play(Create(group_lines))
        self.wait(2)

        self.play(self.camera.frame.animate.scale(0.8).move_to(group_explain.get_center()), run_time=2)
        self.wait(2)

        self.play(Write(group_explain_weights))
        self.wait(2)
        self.play(Write(group_explain_heuristics))
        self.wait(2)

        self.play(Restore(camera), run_time=2)
        self.wait(2)

        self.play(Write(group_other_weights))
        self.wait(1)
        self.play(Write(group_other_heuristics))
        self.wait(2)

        self.play(self.camera.frame.animate.scale(1.75).move_to(5 * RIGHT), run_time=3)
        camera = self.camera.frame.save_state()
        

        self.play(Write(list_title), Create(list_outline))
        
        self.play(self.camera.frame.animate.scale(0.3).move_to(point_s.get_center() + 1 * RIGHT + 1 * UP), run_time=2)
        self.play(Create(element_s_group), run_time=2)
        element_s_went_num.set_text("0")
        element_s_togo_num.set_text("10")
        self.play(
            ReplacementTransform(element_s_went_num, Text("0", color=GREEN).scale(0.75).move_to(element_s_went_num.get_center())),
            ReplacementTransform(animation_group_heur_s, Text("10", color=RED).scale(0.75).move_to(element_s_togo_num.get_center()))
        )
        
        self.play(Restore(camera), run_time=2)
        self.play(element_s_group.animate.scale(1.5).move_to(list_outline.get_center() + 5 * UP), Create(focus_line), run_time=2)
        self.wait(2)

        self.play(self.camera.frame.animate.scale(0.3).move_to(group_sa.get_center() + 1 * UP), run_time=2)
        self.play(Create(element_a_group), run_time=2)
        element_a_via_text.set_text("S")
        self.play(ReplacementTransform(animation_group_via_as, Text("S").scale(0.75).move_to(element_a_via_text.get_center())), run_time=1.5)
        element_a_went_num.set_text("7")
        self.play(ReplacementTransform(animation_group_went_as, Text("7", color=GREEN).scale(0.75).move_to(element_a_went_num.get_center())), run_time=1.5)
        element_a_togo_num.set_text("16")
        self.play(ReplacementTransform(animation_group_heur_a, Text("16", color=RED).scale(0.75).move_to(element_a_togo_num.get_center())), run_time=2)
        self.wait(2)

        self.play(Restore(camera), run_time=2)
        self.play(element_a_group.animate.scale(1.5).move_to(list_outline.get_center() + 3 * UP), run_time=2)
        self.wait(2)

        self.play(self.camera.frame.animate.scale(0.3).move_to(group_sb.get_center() + 1 * RIGHT), run_time=2)
        self.play(Create(element_b_group), run_time=2)
        element_b_via_text.set_text("S")
        self.play(ReplacementTransform(animation_group_via_bs, Text("S").scale(0.75).move_to(element_b_via_text.get_center())), run_time=1.5)
        element_b_went_num.set_text("2")
        self.play(ReplacementTransform(animation_group_went_bs, Text("2", color=GREEN).scale(0.75).move_to(element_b_went_num.get_center())), run_time=1.5)
        element_b_togo_num.set_text("9")
        self.play(ReplacementTransform(animation_group_heur_b, Text("9", color=RED).scale(0.75).move_to(element_b_togo_num.get_center())), run_time=2)
        self.wait(2)

        self.play(Restore(camera), run_time=2)
        self.play(element_a_group.animate.move_to(list_outline.get_center() + 1.25 * UP), element_b_group.animate.scale(1.5).move_to(list_outline.get_center() + 3 * UP), run_time=2)
        self.wait(2)

        self.play(self.camera.frame.animate.scale(0.3).move_to(group_sc.get_center() + 1 * UP), run_time=2)
        self.play(Create(element_c_group), run_time=2)
        element_c_via_text.set_text("S")
        self.play(ReplacementTransform(animation_group_via_cs, Text("S").scale(0.75).move_to(element_c_via_text.get_center())), run_time=1.5)
        element_c_went_num.set_text("3")
        self.play(ReplacementTransform(animation_group_went_cs, Text("3", color=GREEN).scale(0.75).move_to(element_c_went_num.get_center())), run_time=1.5)
        element_c_togo_num.set_text("11")
        self.play(ReplacementTransform(animation_group_heur_c, Text("11", color=RED).scale(0.75).move_to(element_c_togo_num.get_center())), run_time=2)
        self.wait(2)

        self.play(Restore(camera), run_time=2)
        self.play(element_a_group.animate.move_to(list_outline.get_center() + 0.5 * DOWN), element_c_group.animate.scale(1.5).move_to(list_outline.get_center() + 1.25 * UP), run_time=2)
        self.wait(2)

        self.play(Restore(camera), run_time=2)
        self.play(self.camera.frame.animate.move_to(15 * RIGHT), run_time=2)
        
        self.play(Write(path_list_title), Create(path_list_outline))
        self.wait(2)
        self.play(element_s_group.animate.move_to(path_list_outline.get_center() + 5 * UP), element_b_group.animate.move_to(list_outline.get_center() + 5 * UP), element_c_group.animate.move_to(list_outline.get_center() + 3 * UP), element_a_group.animate.move_to(list_outline.get_center() + 1.25 * UP), run_time=2)
        self.wait(2)

        self.play(Restore(camera), run_time=2)




        self.wait(10)