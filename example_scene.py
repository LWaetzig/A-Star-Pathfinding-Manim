import numpy as np
from manim import *


class ExampleScene(MovingCameraScene):
    @staticmethod
    def adjust_line_to_circle_boundary(start_point, end_point):
        """Adjust a line to end on the boundary of a circle

        Args:
            start_point (list): Location where the line should start
            end_point (list): Location where the line should end

        Returns:
            Line: Line element adjusted to the boundary of the circle
        """
        line_vector = end_point.get_center() - start_point.get_center()
        normalized_vector = line_vector / np.linalg.norm(line_vector)
        adjusted_start = start_point.get_center() + 0.25 * normalized_vector
        adjusted_end = end_point.get_center() - 0.25 * normalized_vector

        return Line(adjusted_start, adjusted_end)

    @staticmethod
    def create_point(center, label: str):
        """Create node with label

        Args:
            center (list): location of the node
            label (_type_): label displayed in the node

        Returns:
            tuple: _description_
        """
        circle = Circle(radius=0.25, color=BLUE, fill_opacity=0.5)
        letter = Text(label, color=WHITE).scale(0.5)
        circle.move_to(center)
        letter.move_to(circle.get_center())

        return circle, letter

    @staticmethod
    def create_list_element(
        position, label: str, via_text: str, went_num: str, togo_num: str
    ):
        """Create single list element

        Args:
            position (list): Position of the element
            label (str): Label corresponding to a node
            via_text (str): Label of the node from which the current node was reached
            went_num (str): Weight of the path from the start node to the current node
            togo_num (str): Weight of the path from the current node to the end node

        Returns:
            tuple: Element as a group
        """
        element = RoundedRectangle(
            width=4, height=1, corner_radius=0.25, color=BLUE
        ).move_to(position)
        element_label = Text(label).scale(1).move_to(element.get_center() + 1.65 * LEFT)

        separator1 = Line(
            element.get_edge_center(UP) + 1.3 * LEFT,
            element.get_edge_center(DOWN) + 1.3 * LEFT,
            color=BLUE,
        )

        via = (
            Text("via").scale(0.5).move_to(element.get_center() + 0.9 * LEFT + 0.3 * UP)
        )
        via_value = Text(via_text).scale(0.75).move_to(via.get_center() + 0.45 * DOWN)

        separator2 = Line(
            element.get_edge_center(UP) + 0.45 * LEFT,
            element.get_edge_center(DOWN) + 0.45 * LEFT,
            color=BLUE,
        )

        went = (
            Text("went")
            .scale(0.5)
            .move_to(element.get_center() + 0.1 * RIGHT + 0.3 * UP)
        )
        went_value = (
            Text(went_num, color=GREEN)
            .scale(0.75)
            .move_to(went.get_center() + 0.45 * DOWN)
        )

        separator3 = Line(
            element.get_edge_center(UP) + 0.7 * RIGHT,
            element.get_edge_center(DOWN) + 0.7 * RIGHT,
            color=BLUE,
        )

        togo = (
            Text("+ to go")
            .scale(0.5)
            .move_to(element.get_center() + 1.35 * RIGHT + 0.3 * UP)
        )
        togo_value = (
            Text(togo_num, color=RED)
            .scale(0.75)
            .move_to(togo.get_center() + 0.45 * DOWN)
        )

        group = VGroup(
            element,
            element_label,
            separator1,
            via,
            via_value,
            separator2,
            went,
            went_value,
            separator3,
            togo,
            togo_value,
        )

        return group, via_value, went_value, togo_value

    def construct(self):
        Text.set_default(font="Arial")

        # Create texts
        title = Text("Example").scale(1.5)

        start_text = Text("Start").scale(1).to_edge(UP)
        end_text = Text("End").scale(1).to_edge(DOWN)

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

        # Edit the z-index of the lines to Create them in the background of the points
        line_sa.set_z_index(point_s.z_index - 1)
        line_sb.set_z_index(point_s.z_index - 1)
        line_sc.set_z_index(point_s.z_index - 1)
        line_ab.set_z_index(point_s.z_index - 1)
        line_ad.set_z_index(point_s.z_index - 1)
        line_bd.set_z_index(point_s.z_index - 1)
        line_bh.set_z_index(point_s.z_index - 1)
        line_df.set_z_index(point_s.z_index - 1)
        line_hf.set_z_index(point_s.z_index - 1)
        line_hg.set_z_index(point_s.z_index - 1)
        line_ge.set_z_index(point_s.z_index - 1)
        line_cl.set_z_index(point_s.z_index - 1)
        line_li.set_z_index(point_s.z_index - 1)
        line_lj.set_z_index(point_s.z_index - 1)
        line_ij.set_z_index(point_s.z_index - 1)
        line_ik.set_z_index(point_s.z_index - 1)
        line_jk.set_z_index(point_s.z_index - 1)
        line_ke.set_z_index(point_s.z_index - 1)

        # Create weights
        weight_sa = (
            Text("7", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_sa.get_center() + 0.25 * UP)
        )
        weight_sb = (
            Text("2", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_sb.get_center() + 0.25 * DOWN)
        )
        weight_ab = (
            Text("3", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_ab.get_center() + 0.25 * DOWN)
        )
        weight_sc = (
            Text("3", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_sc.get_center() + 0.25 * UP)
        )
        weight_ad = (
            Text("4", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_ad.get_center() + 0.25 * LEFT)
        )
        weight_bd = (
            Text("4", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_bd.get_center() + 0.25 * DOWN)
        )
        weight_bh = (
            Text("1", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_bh.get_center() + 0.25 * RIGHT)
        )
        weight_df = (
            Text("5", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_df.get_center() + 0.25 * LEFT)
        )
        weight_hf = (
            Text("3", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_hf.get_center() + 0.25 * DOWN)
        )
        weight_hg = (
            Text("2", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_hg.get_center() + 0.25 * RIGHT)
        )
        weight_ge = (
            Text("2", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_ge.get_center() + 0.25 * UP)
        )
        weight_cl = (
            Text("2", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_cl.get_center() + 0.25 * LEFT)
        )
        weight_li = (
            Text("4", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_li.get_center() + 0.25 * LEFT + 0.25 * UP)
        )
        weight_lj = (
            Text("4", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_lj.get_center() + 0.25 * RIGHT + 0.25 * UP)
        )
        weight_ij = (
            Text("6", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_ij.get_center() + 0.25 * DOWN)
        )
        weight_ik = (
            Text("4", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_ik.get_center() + 0.25 * LEFT + 0.25 * DOWN)
        )
        weight_jk = (
            Text("4", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_jk.get_center() + 0.25 * RIGHT + 0.25 * DOWN)
        )
        weight_ke = (
            Text("5", color=GREEN, weight=BOLD)
            .scale(0.5)
            .move_to(line_ke.get_center() + 0.25 * UP)
        )

        # Create heuristic weights
        heuristic_s = (
            Text("10", color=RED, weight=BOLD)
            .scale(0.5)
            .move_to(point_s.get_center() + 0.5 * DOWN)
        )
        heuristic_a = (
            Text("9", color=RED, weight=BOLD)
            .scale(0.5)
            .move_to(point_a.get_center() + 0.5 * UP)
        )
        heuristic_b = (
            Text("7", color=RED, weight=BOLD)
            .scale(0.5)
            .move_to(point_b.get_center() + 0.25 * DOWN + 0.5 * RIGHT)
        )
        heuristic_c = (
            Text("8", color=RED, weight=BOLD)
            .scale(0.5)
            .move_to(point_c.get_center() + 0.5 * UP)
        )
        heuristic_d = (
            Text("8", color=RED, weight=BOLD)
            .scale(0.5)
            .move_to(point_d.get_center() + 0.5 * LEFT)
        )
        heuristic_f = (
            Text("6", color=RED, weight=BOLD)
            .scale(0.5)
            .move_to(point_f.get_center() + 0.5 * DOWN)
        )
        heuristic_g = (
            Text("3", color=RED, weight=BOLD)
            .scale(0.5)
            .move_to(point_g.get_center() + 0.5 * LEFT)
        )
        heuristic_h = (
            Text("6", color=RED, weight=BOLD)
            .scale(0.5)
            .move_to(point_h.get_center() + 0.5 * RIGHT)
        )
        heuristic_i = (
            Text("4", color=RED, weight=BOLD)
            .scale(0.5)
            .move_to(point_i.get_center() + 0.5 * LEFT)
        )
        heuristic_j = (
            Text("4", color=RED, weight=BOLD)
            .scale(0.5)
            .move_to(point_j.get_center() + 0.5 * RIGHT)
        )
        heuristic_k = (
            Text("3", color=RED, weight=BOLD)
            .scale(0.5)
            .move_to(point_k.get_center() + 0.25 * DOWN + 0.5 * RIGHT)
        )
        heuristic_l = (
            Text("6", color=RED, weight=BOLD)
            .scale(0.5)
            .move_to(point_l.get_center() + 0.25 * UP + 0.5 * RIGHT)
        )
        heuristic_e = (
            Text("0", color=RED, weight=BOLD)
            .scale(0.5)
            .move_to(point_e.get_center() + 0.5 * UP)
        )

        # Create groups
        group_start = VGroup(point_s, letter_s)
        group_end = VGroup(point_e, letter_e)

        group_other_points = VGroup(
            point_a,
            point_b,
            point_c,
            point_d,
            point_f,
            point_g,
            point_h,
            point_i,
            point_j,
            point_k,
            point_l,
        )
        group_other_letters = VGroup(
            letter_a,
            letter_b,
            letter_c,
            letter_d,
            letter_f,
            letter_g,
            letter_h,
            letter_i,
            letter_j,
            letter_k,
            letter_l,
        )

        group_lines = VGroup(
            line_sa,
            line_sb,
            line_sc,
            line_ab,
            line_ad,
            line_bd,
            line_bh,
            line_df,
            line_hf,
            line_hg,
            line_ge,
            line_cl,
            line_li,
            line_lj,
            line_ij,
            line_ik,
            line_jk,
            line_ke,
        )

        group_explain = VGroup(point_l, point_i, point_j, point_k, point_e)
        group_explain_weights = VGroup(
            weight_li, weight_lj, weight_ij, weight_ik, weight_jk, weight_ke
        )

        group_other_weights = VGroup(
            weight_sa,
            weight_sb,
            weight_ab,
            weight_sc,
            weight_ad,
            weight_bd,
            weight_bh,
            weight_df,
            weight_hf,
            weight_hg,
            weight_ge,
            weight_cl,
        )

        group_not_final_path_weights = VGroup(
            group_explain_weights,
            weight_sa,
            weight_ab,
            weight_sc,
            weight_ad,
            weight_bd,
            weight_df,
            weight_hf,
            weight_cl,
        )

        group_explain_heuristics = VGroup(
            heuristic_i, heuristic_j, heuristic_k, heuristic_l, heuristic_e
        )

        group_other_heuristics = VGroup(
            heuristic_s,
            heuristic_a,
            heuristic_b,
            heuristic_c,
            heuristic_d,
            heuristic_f,
            heuristic_g,
            heuristic_h,
        )

        group_heuristics = VGroup(group_other_heuristics, group_explain_heuristics)

        group_complete_graph = VGroup(
            group_start, group_end, group_other_points, group_other_letters, group_lines
        )

        # Groups for the expanding of the list
        group_sa = VGroup(point_s, point_a)
        group_sb = VGroup(point_s, point_b)
        group_sc = VGroup(point_s, point_c)
        group_sba = VGroup(group_sb, point_a)
        group_sbd = VGroup(group_sb, point_d)
        group_sbh = VGroup(group_sb, point_h)
        group_sbhf = VGroup(group_sbh, point_f)
        group_sbhg = VGroup(group_sbh, point_g)
        group_sbhge = VGroup(group_sbhg, point_e)

        # Create list and necessary elements (Labels, Lines, etc.)
        list_outline = RoundedRectangle(
            width=7, height=12, corner_radius=0.25, color=BLUE
        ).move_to(12 * RIGHT + 0.5 * DOWN)
        list_title = (
            Text("Open List").scale(1).move_to(list_outline.get_center() + 6.5 * UP)
        )

        focus_line = DashedLine(
            start=list_outline.get_edge_center(LEFT) + 4 * UP,
            end=list_outline.get_edge_center(RIGHT) + 4 * UP,
            color=BLUE,
        )

        path_list_outline = RoundedRectangle(
            width=7, height=12, corner_radius=0.25, color=BLUE
        ).move_to(22 * RIGHT + 0.5 * DOWN)
        path_list_title = (
            Text("Done List")
            .scale(1)
            .move_to(path_list_outline.get_center() + 6.5 * UP)
        )

        (
            element_s_group,
            element_s_via_text,
            element_s_went_num,
            element_s_togo_num,
        ) = self.create_list_element(
            point_s.get_center() + 1.4 * UP + 1 * RIGHT, "S", "-", "-", "-"
        )

        (
            element_a_group,
            element_a_via_text,
            element_a_went_num,
            element_a_togo_num,
        ) = self.create_list_element(
            point_a.get_center() + 2 * UP + 2 * RIGHT, "A", "-", "-", "-"
        )

        (
            element_b_group,
            element_b_via_text,
            element_b_went_num,
            element_b_togo_num,
        ) = self.create_list_element(
            group_sb.get_center() + 1.4 * DOWN + 1.5 * RIGHT, "B", "-", "-", "-"
        )

        (
            element_c_group,
            element_c_via_text,
            element_c_went_num,
            element_c_togo_num,
        ) = self.create_list_element(group_sc.get_center() + 2 * UP, "C", "-", "-", "-")

        (
            new_element_a_group,
            new_element_a_via_text,
            new_element_a_went_num,
            new_element_a_togo_num,
        ) = self.create_list_element(
            group_sba.get_center() + 1 * UP, "A", "-", "-", "-"
        )

        (
            element_d_group,
            element_d_via_text,
            element_d_went_num,
            element_d_togo_num,
        ) = self.create_list_element(
            group_sbd.get_center() + 1 * DOWN + 3 * RIGHT, "D", "-", "-", "-"
        )

        (
            element_h_group,
            element_h_via_text,
            element_h_went_num,
            element_h_togo_num,
        ) = self.create_list_element(
            group_sbd.get_center() + 1 * DOWN + 3 * RIGHT, "H", "-", "-", "-"
        )

        (
            element_f_group,
            element_f_via_text,
            element_f_went_num,
            element_f_togo_num,
        ) = self.create_list_element(
            group_sbhf.get_center() + 1 * DOWN + 3 * RIGHT, "F", "-", "-", "-"
        )

        (
            element_g_group,
            element_g_via_text,
            element_g_went_num,
            element_g_togo_num,
        ) = self.create_list_element(
            group_sbhg.get_center() + 1 * DOWN + 1.5 * RIGHT, "G", "-", "-", "-"
        )

        (
            element_e_group,
            element_e_via_text,
            element_e_went_num,
            element_e_togo_num,
        ) = self.create_list_element(
            group_sbhge.get_center() + 1 * DOWN + 1.5 * RIGHT, "E", "-", "-", "-"
        )

        # Create some Groups and Elements for animation purposes
        animation_group_heur_s = VGroup(element_s_togo_num, heuristic_s.copy())
        element_s_group.add(animation_group_heur_s)

        animation_group_via_as = VGroup(element_a_via_text, letter_s.copy())
        animation_group_went_as = VGroup(element_a_went_num, weight_sa.copy())
        animation_group_heur_a = VGroup(
            element_a_togo_num, heuristic_a.copy(), weight_sa.copy()
        )
        element_a_group.add(
            animation_group_via_as, animation_group_went_as, animation_group_heur_a
        )

        animation_group_via_bs = VGroup(element_b_via_text, letter_s.copy())
        animation_group_went_bs = VGroup(element_b_went_num, weight_sb.copy())
        animation_group_heur_b = VGroup(
            element_b_togo_num, heuristic_b.copy(), weight_sb.copy()
        )
        element_b_group.add(
            animation_group_via_bs, animation_group_went_bs, animation_group_heur_b
        )

        animation_group_via_cs = VGroup(element_c_via_text, letter_s.copy())
        animation_group_went_cs = VGroup(element_c_went_num, weight_sc.copy())
        animation_group_heur_c = VGroup(
            element_c_togo_num, heuristic_c.copy(), weight_sc.copy()
        )
        element_c_group.add(
            animation_group_via_cs, animation_group_went_cs, animation_group_heur_c
        )

        animation_group_new_via_abs = VGroup(new_element_a_via_text, letter_b.copy())
        animation_group_new_went_abs = VGroup(
            new_element_a_went_num, weight_sb.copy(), weight_ab.copy()
        )
        animation_group_new_heur_a = VGroup(new_element_a_togo_num, heuristic_a.copy())
        new_element_a_group.add(
            animation_group_new_via_abs,
            animation_group_new_went_abs,
            animation_group_new_heur_a,
        )
        animation_new_went_abs_copy = (
            Text("5", color=GREEN)
            .scale(0.75)
            .move_to(new_element_a_went_num.get_center())
        )

        animation_group_via_db = VGroup(element_d_via_text, letter_b.copy())
        animation_group_went_db = VGroup(
            element_d_went_num, weight_sb.copy(), weight_bd.copy()
        )
        animation_group_heur_d = VGroup(element_d_togo_num, heuristic_d.copy())
        element_d_group.add(
            animation_group_via_db, animation_group_went_db, animation_group_heur_d
        )
        animation_went_dbs_copy = (
            Text("6", color=GREEN).scale(0.75).move_to(element_d_went_num.get_center())
        )

        animation_group_via_hb = VGroup(element_h_via_text, letter_b.copy())
        animation_group_went_hb = VGroup(
            element_h_went_num, weight_sb.copy(), weight_bh.copy()
        )
        animation_group_heur_h = VGroup(element_h_togo_num, heuristic_h.copy())
        element_h_group.add(
            animation_group_via_hb, animation_group_went_hb, animation_group_heur_h
        )
        animation_went_hbs_copy = (
            Text("3", color=GREEN).scale(0.75).move_to(element_h_went_num.get_center())
        )

        animation_group_via_fh = VGroup(element_f_via_text, letter_h.copy())
        animation_group_went_fh = VGroup(
            element_f_went_num, weight_hf.copy(), weight_bh.copy(), weight_sb.copy()
        )
        animation_group_heur_f = VGroup(element_f_togo_num, heuristic_f.copy())
        element_f_group.add(
            animation_group_via_fh, animation_group_went_fh, animation_group_heur_f
        )
        animation_went_fhbs_copy = (
            Text("6", color=GREEN).scale(0.75).move_to(element_f_went_num.get_center())
        )

        animation_group_via_gh = VGroup(element_g_via_text, letter_h.copy())
        animation_group_went_gh = VGroup(
            element_g_went_num, weight_hg.copy(), weight_bh.copy(), weight_sb.copy()
        )
        animation_group_heur_g = VGroup(element_g_togo_num, heuristic_g.copy())
        element_g_group.add(
            animation_group_via_gh, animation_group_went_gh, animation_group_heur_g
        )
        animation_went_ghbs_copy = (
            Text("5", color=GREEN).scale(0.75).move_to(element_g_went_num.get_center())
        )

        animation_group_via_eg = VGroup(element_e_via_text, letter_g.copy())
        animation_group_went_eg = VGroup(
            element_e_went_num,
            weight_ge.copy(),
            weight_hg.copy(),
            weight_bh.copy(),
            weight_sb.copy(),
        )
        animation_group_heur_e = VGroup(element_e_togo_num, heuristic_e.copy())
        element_e_group.add(
            animation_group_via_eg, animation_group_went_eg, animation_group_heur_e
        )
        animation_went_eghbs_copy = (
            Text("7", color=GREEN).scale(0.75).move_to(element_e_went_num.get_center())
        )

        group_final_path_labels = VGroup(
            element_s_group,
            element_b_group,
            element_h_group,
            element_g_group,
            element_e_group,
        )

        ###############################
        # Start with the video timeline
        ###############################

        # Create the title
        self.play(Write(title), run_time=1.5)
        self.play(FadeOut(title, run_time=1.5))
        self.wait(2)

        # Create the text for the start and end point and morph them into the points
        camera = self.camera.frame.save_state()
        self.play(Write(start_text), Write(end_text), run_time=2)
        self.play(
            ReplacementTransform(start_text, group_start),
            ReplacementTransform(end_text, group_end),
            run_time=2,
        )
        self.wait(2)

        # Create the whole graph
        self.play(Create(group_other_points), Write(group_other_letters), run_time=2)
        self.wait(2)
        self.play(Create(group_lines), run_time=2)
        self.wait(2)

        # Zoom to a Group of points to explain the weights and heuristics
        self.play(
            self.camera.frame.animate.scale(0.8).move_to(group_explain.get_center()),
            run_time=3,
        )
        self.wait(3)

        self.play(Write(group_explain_weights), run_time=2)
        self.wait(7)
        self.play(Write(group_explain_heuristics), run_time=2)
        self.wait(8)

        # Zoom out again and show the other weights and heuristics
        self.play(Restore(camera), run_time=2)
        self.wait(1)

        self.play(Write(group_other_weights), run_time=2)
        self.wait(1)
        self.play(Write(group_other_heuristics), run_time=2)
        self.wait(2)

        # Zoom out of the graph and create the open list
        self.play(self.camera.frame.animate.scale(1.75).move_to(5 * RIGHT), run_time=3)
        camera = self.camera.frame.save_state()

        self.play(Write(list_title), Create(list_outline), run_time=2)

        # Create the label of Point S, the first element of the open list and animate it
        self.play(
            self.camera.frame.animate.scale(0.3).move_to(
                point_s.get_center() + 1 * RIGHT + 1 * UP
            ),
            run_time=2,
        )
        self.play(Create(element_s_group), run_time=2)
        self.wait(8)
        element_s_went_num.set_text("0")
        self.wait(5)
        self.play(
            ReplacementTransform(
                element_s_went_num,
                Text("0", color=GREEN)
                .scale(0.75)
                .move_to(element_s_went_num.get_center()),
            ),
            run_time=2,
        )
        self.wait(7)
        element_s_togo_num.set_text("10")
        self.play(
            ReplacementTransform(
                animation_group_heur_s,
                Text("10", color=RED)
                .scale(0.75)
                .move_to(element_s_togo_num.get_center()),
            ),
            run_time=2,
        )

        # Zoom out and add it into the list
        self.play(Restore(camera), run_time=2)
        self.play(
            element_s_group.animate.scale(1.5).move_to(
                list_outline.get_center() + 5 * UP
            ),
            Create(focus_line),
            run_time=2,
        )
        self.wait(8.5)

        # Create the Label of Point A and animate it
        self.play(
            self.camera.frame.animate.scale(0.3).move_to(
                group_sa.get_center() + 1 * UP
            ),
            run_time=2,
        )
        self.play(Create(element_a_group), run_time=2)
        self.wait(2)
        element_a_via_text.set_text("S")
        self.play(
            ReplacementTransform(
                animation_group_via_as,
                Text("S").scale(0.75).move_to(element_a_via_text.get_center()),
            ),
            run_time=1.5,
        )
        self.wait(4)
        element_a_went_num.set_text("7")
        self.play(
            ReplacementTransform(
                animation_group_went_as,
                Text("7", color=GREEN)
                .scale(0.75)
                .move_to(element_a_went_num.get_center()),
            ),
            run_time=2,
        )
        self.wait(16)
        element_a_togo_num.set_text("16")
        self.play(
            ReplacementTransform(
                animation_group_heur_a,
                Text("16", color=RED)
                .scale(0.75)
                .move_to(element_a_togo_num.get_center()),
            ),
            run_time=2,
        )
        self.wait(4)

        # Zoom out and add it into the list
        self.play(Restore(camera), run_time=2)
        self.play(
            element_a_group.animate.scale(1.5).move_to(
                list_outline.get_center() + 3 * UP
            ),
            run_time=2,
        )
        self.wait(5.5)

        # Create the Label of Point B and animate it
        self.play(
            self.camera.frame.animate.scale(0.3).move_to(
                group_sb.get_center() + 1 * RIGHT
            ),
            run_time=2,
        )
        self.wait(2)
        self.play(Create(element_b_group), run_time=2)
        element_b_via_text.set_text("S")
        self.play(
            ReplacementTransform(
                animation_group_via_bs,
                Text("S").scale(0.75).move_to(element_b_via_text.get_center()),
            ),
            run_time=1.5,
        )
        self.wait(2)
        element_b_went_num.set_text("2")
        self.play(
            ReplacementTransform(
                animation_group_went_bs,
                Text("2", color=GREEN)
                .scale(0.75)
                .move_to(element_b_went_num.get_center()),
            ),
            run_time=2,
        )
        self.wait(10)
        element_b_togo_num.set_text("9")
        self.play(
            ReplacementTransform(
                animation_group_heur_b,
                Text("9", color=RED)
                .scale(0.75)
                .move_to(element_b_togo_num.get_center()),
            ),
            run_time=2,
        )
        self.wait(2.5)

        # Zoom out and add it into the list
        self.play(Restore(camera), run_time=2)
        self.wait(7)
        self.play(
            element_a_group.animate.move_to(list_outline.get_center() + 1.25 * UP),
            element_b_group.animate.scale(1.5).move_to(
                list_outline.get_center() + 3 * UP
            ),
            run_time=2,
        )
        self.wait(4.5)

        # Create the Label of Point C and animate it
        self.play(
            self.camera.frame.animate.scale(0.3).move_to(
                group_sc.get_center() + 1 * UP
            ),
            run_time=2,
        )
        self.play(Create(element_c_group), run_time=2)
        element_c_via_text.set_text("S")
        self.play(
            ReplacementTransform(
                animation_group_via_cs,
                Text("S").scale(0.75).move_to(element_c_via_text.get_center()),
            ),
            run_time=1.5,
        )
        element_c_went_num.set_text("3")
        self.play(
            ReplacementTransform(
                animation_group_went_cs,
                Text("3", color=GREEN)
                .scale(0.75)
                .move_to(element_c_went_num.get_center()),
            ),
            run_time=1.5,
        )
        element_c_togo_num.set_text("11")
        self.play(
            ReplacementTransform(
                animation_group_heur_c,
                Text("11", color=RED)
                .scale(0.75)
                .move_to(element_c_togo_num.get_center()),
            ),
            run_time=2,
        )
        self.wait(4)

        # Zoom out and add it into the list
        self.play(Restore(camera), run_time=2)
        self.play(
            element_a_group.animate.move_to(list_outline.get_center() + 0.5 * DOWN),
            element_c_group.animate.scale(1.5).move_to(
                list_outline.get_center() + 1.25 * UP
            ),
            run_time=2,
        )
        self.wait(4)

        # Create the Done List and add Label of Point A and animate the transitions
        self.play(Restore(camera), run_time=2)
        self.play(self.camera.frame.animate.move_to(15 * RIGHT), run_time=2)

        self.play(Write(path_list_title), Create(path_list_outline), run_time=2)
        self.wait(5)
        self.play(
            element_s_group.animate.move_to(path_list_outline.get_center() + 5 * UP),
            element_b_group.animate.move_to(list_outline.get_center() + 5 * UP),
            element_c_group.animate.move_to(list_outline.get_center() + 3 * UP),
            element_a_group.animate.move_to(list_outline.get_center() + 1.25 * UP),
            run_time=2,
        )
        self.wait(4)

        # Create the new Label of Point A and animate the replacement of the old one
        self.play(Restore(camera), run_time=2)
        self.wait(3)

        self.play(
            self.camera.frame.animate.scale(0.3).move_to(
                group_sba.get_center() + 0.9 * UP
            ),
            run_time=2,
        )
        self.wait(4.5)
        self.play(
            element_a_group.animate.scale(1 / 1.5).move_to(
                group_sba.get_center() + 2.3 * UP
            ),
            run_time=2,
        )
        self.wait(1)

        self.play(Create(new_element_a_group), run_time=2)
        self.wait(2)
        new_element_a_via_text.set_text("B")
        self.play(
            ReplacementTransform(
                animation_group_new_via_abs,
                Text("B").scale(0.75).move_to(new_element_a_via_text.get_center()),
            ),
            run_time=2,
        )
        self.wait(5)
        new_element_a_went_num.set_text("5")
        self.play(
            ReplacementTransform(
                animation_group_new_went_abs,
                Text("5", color=GREEN)
                .scale(0.75)
                .move_to(new_element_a_went_num.get_center()),
            ),
            run_time=2,
        )
        self.wait(8)
        animation_group_new_heur_a.add(animation_new_went_abs_copy)
        new_element_a_togo_num.set_text("14")
        self.play(
            ReplacementTransform(
                animation_group_new_heur_a,
                Text("14", color=RED)
                .scale(0.75)
                .move_to(new_element_a_togo_num.get_center()),
            ),
            run_time=2,
        )
        self.wait(5)

        self.play(FadeOut(element_a_group), run_time=2)
        self.play(Restore(camera), run_time=2)
        self.play(
            new_element_a_group.animate.scale(1.5).move_to(
                list_outline.get_center() + 1.25 * UP
            ),
            run_time=2,
        )
        self.wait(2)

        # Create the Label of Point D and animate it
        self.play(
            self.camera.frame.animate.scale(0.4).move_to(
                group_sbd.get_center() + 0.9 * DOWN + 1 * RIGHT
            ),
            run_time=2,
        )

        self.play(Create(element_d_group), run_time=2)
        element_d_via_text.set_text("B")
        self.play(
            ReplacementTransform(
                animation_group_via_db,
                Text("B").scale(0.75).move_to(element_d_via_text.get_center()),
            ),
            run_time=1.5,
        )
        element_d_went_num.set_text("6")
        self.play(
            ReplacementTransform(
                animation_group_went_db,
                Text("6", color=GREEN)
                .scale(0.75)
                .move_to(element_d_went_num.get_center()),
            ),
            run_time=1.5,
        )
        animation_group_heur_d.add(animation_went_dbs_copy)
        element_d_togo_num.set_text("14")
        self.play(
            ReplacementTransform(
                animation_group_heur_d,
                Text("14", color=RED)
                .scale(0.75)
                .move_to(element_d_togo_num.get_center()),
            ),
            run_time=2,
        )
        self.wait(2)

        # Zoom out and add it into the list
        self.play(Restore(camera), run_time=2)
        self.play(
            element_d_group.animate.scale(1.5).move_to(
                list_outline.get_center() + 0.5 * DOWN
            ),
            run_time=2,
        )
        self.wait(2)

        # Create the Label of Point H and animate it
        self.play(
            self.camera.frame.animate.scale(0.4).move_to(
                group_sbh.get_center() + 0.9 * DOWN + 3 * RIGHT
            ),
            run_time=2,
        )

        self.play(Create(element_h_group), run_time=2)
        element_h_via_text.set_text("B")
        self.play(
            ReplacementTransform(
                animation_group_via_hb,
                Text("B").scale(0.75).move_to(element_h_via_text.get_center()),
            ),
            run_time=1.5,
        )
        element_h_went_num.set_text("3")
        self.play(
            ReplacementTransform(
                animation_group_went_hb,
                Text("3", color=GREEN)
                .scale(0.75)
                .move_to(element_h_went_num.get_center()),
            ),
            run_time=1.5,
        )
        animation_group_heur_h.add(animation_went_hbs_copy)
        element_h_togo_num.set_text("9")
        self.play(
            ReplacementTransform(
                animation_group_heur_h,
                Text("9", color=RED)
                .scale(0.75)
                .move_to(element_h_togo_num.get_center()),
            ),
            run_time=2,
        )
        self.wait(2)
        # 5:05:50
        # Zoom out, add it into the list and move Label of Point B to the Done List
        self.play(Restore(camera), run_time=2)
        self.play(
            element_h_group.animate.scale(1.5).move_to(
                list_outline.get_center() + 3 * UP
            ),
            element_c_group.animate.move_to(list_outline.get_center() + 1.25 * UP),
            new_element_a_group.animate.move_to(list_outline.get_center() + 0.5 * DOWN),
            element_d_group.animate.move_to(list_outline.get_center() + 2.25 * DOWN),
            run_time=2,
        )
        self.wait(3.5)
        self.play(self.camera.frame.animate.move_to(15 * RIGHT), run_time=2)
        self.play(
            element_b_group.animate.move_to(path_list_outline.get_center() + 3.25 * UP),
            element_h_group.animate.move_to(list_outline.get_center() + 5 * UP),
            element_c_group.animate.move_to(list_outline.get_center() + 3 * UP),
            new_element_a_group.animate.move_to(list_outline.get_center() + 1.25 * UP),
            element_d_group.animate.move_to(list_outline.get_center() + 0.5 * DOWN),
            run_time=2,
        )
        self.wait(4)

        # Create the Label of Point F and animate it
        self.play(Restore(camera), run_time=2)
        self.play(
            self.camera.frame.animate.scale(0.45).move_to(
                group_sbhf.get_center() + 1 * RIGHT
            ),
            run_time=2,
        )

        self.play(Create(element_f_group), run_time=2)
        element_f_via_text.set_text("H")
        self.play(
            ReplacementTransform(
                animation_group_via_fh,
                Text("H").scale(0.75).move_to(element_f_via_text.get_center()),
            ),
            run_time=1.5,
        )
        element_f_went_num.set_text("6")
        self.play(
            ReplacementTransform(
                animation_group_went_fh,
                Text("6", color=GREEN)
                .scale(0.75)
                .move_to(element_f_went_num.get_center()),
            ),
            run_time=1.5,
        )
        animation_group_heur_f.add(animation_went_fhbs_copy)
        element_f_togo_num.set_text("12")
        self.play(
            ReplacementTransform(
                animation_group_heur_f,
                Text("12", color=RED)
                .scale(0.75)
                .move_to(element_f_togo_num.get_center()),
            ),
            run_time=2,
        )
        self.wait(2)

        # Zoom out and add it into the list
        self.play(Restore(camera), run_time=2)
        self.play(
            element_f_group.animate.scale(1.5).move_to(
                list_outline.get_center() + 1.25 * UP
            ),
            new_element_a_group.animate.move_to(list_outline.get_center() + 0.5 * DOWN),
            element_d_group.animate.move_to(list_outline.get_center() + 2.25 * DOWN),
            run_time=2,
        )
        self.wait(2)

        # Create the Label of Point G and animate it
        self.play(
            self.camera.frame.animate.scale(0.5).move_to(group_sbhg.get_center()),
            run_time=2,
        )

        self.play(Create(element_g_group), run_time=2)
        element_g_via_text.set_text("H")
        self.play(
            ReplacementTransform(
                animation_group_via_gh,
                Text("H").scale(0.75).move_to(element_g_via_text.get_center()),
            ),
            run_time=1.5,
        )
        element_g_went_num.set_text("5")
        self.play(
            ReplacementTransform(
                animation_group_went_gh,
                Text("5", color=GREEN)
                .scale(0.75)
                .move_to(element_g_went_num.get_center()),
            ),
            run_time=1.5,
        )
        animation_group_heur_g.add(animation_went_ghbs_copy)
        element_g_togo_num.set_text("8")
        self.play(
            ReplacementTransform(
                animation_group_heur_g,
                Text("8", color=RED)
                .scale(0.75)
                .move_to(element_g_togo_num.get_center()),
            ),
            run_time=2,
        )
        self.wait(2)

        # Zoom out, add it into the list and move Label of Point H to the Done List
        self.play(Restore(camera), run_time=2)
        self.play(
            element_g_group.animate.scale(1.5).move_to(
                list_outline.get_center() + 3 * UP
            ),
            element_c_group.animate.move_to(list_outline.get_center() + 1.25 * UP),
            element_f_group.animate.move_to(list_outline.get_center() + 0.5 * DOWN),
            new_element_a_group.animate.move_to(
                list_outline.get_center() + 2.25 * DOWN
            ),
            element_d_group.animate.move_to(list_outline.get_center() + 4 * DOWN),
            run_time=2,
        )
        self.wait(2)

        self.play(self.camera.frame.animate.move_to(15 * RIGHT), run_time=2)
        self.play(
            element_h_group.animate.move_to(path_list_outline.get_center() + 1.5 * UP),
            element_g_group.animate.move_to(list_outline.get_center() + 5 * UP),
            element_c_group.animate.move_to(list_outline.get_center() + 3 * UP),
            element_f_group.animate.move_to(list_outline.get_center() + 1.25 * UP),
            new_element_a_group.animate.move_to(list_outline.get_center() + 0.5 * DOWN),
            element_d_group.animate.move_to(list_outline.get_center() + 2.25 * DOWN),
            run_time=2,
        )
        self.wait(2)

        # Create the Label of Point E and animate it
        self.play(Restore(camera), run_time=2)
        self.wait(2)
        self.play(
            self.camera.frame.animate.scale(0.55).move_to(
                group_sbhge.get_center() + 1 * RIGHT
            ),
            run_time=2,
        )

        self.play(Create(element_e_group), run_time=2)
        self.wait(5)
        element_e_via_text.set_text("G")
        self.play(
            ReplacementTransform(
                animation_group_via_eg,
                Text("G").scale(0.75).move_to(element_e_via_text.get_center()),
            ),
            run_time=2,
        )
        element_e_went_num.set_text("7")
        self.play(
            ReplacementTransform(
                animation_group_went_eg,
                Text("7", color=GREEN)
                .scale(0.75)
                .move_to(element_e_went_num.get_center()),
            ),
            run_time=1.5,
        )
        animation_group_heur_e.add(animation_went_eghbs_copy)
        element_e_togo_num.set_text("7")
        self.play(
            ReplacementTransform(
                animation_group_heur_e,
                Text("7", color=RED)
                .scale(0.75)
                .move_to(element_e_togo_num.get_center()),
            ),
            run_time=2,
        )
        self.wait(2)

        # Zoom out, add it into the list and move Label of Point G to the Done List
        self.play(Restore(camera), run_time=2)
        self.play(
            element_e_group.animate.scale(1.5).move_to(
                list_outline.get_center() + 3 * UP
            ),
            element_c_group.animate.move_to(list_outline.get_center() + 1.25 * UP),
            element_f_group.animate.move_to(list_outline.get_center() + 0.5 * DOWN),
            new_element_a_group.animate.move_to(
                list_outline.get_center() + 2.25 * DOWN
            ),
            element_d_group.animate.move_to(list_outline.get_center() + 4 * DOWN),
            run_time=2,
        )
        self.wait(2)

        self.play(self.camera.frame.animate.move_to(15 * RIGHT), run_time=2)
        self.play(
            element_g_group.animate.move_to(
                path_list_outline.get_center() + 0.25 * DOWN
            ),
            element_e_group.animate.move_to(list_outline.get_center() + 5 * UP),
            element_c_group.animate.move_to(list_outline.get_center() + 3 * UP),
            element_f_group.animate.move_to(list_outline.get_center() + 1.25 * UP),
            new_element_a_group.animate.move_to(list_outline.get_center() + 0.5 * DOWN),
            element_d_group.animate.move_to(list_outline.get_center() + 2.25 * DOWN),
            run_time=2,
        )

        # Move Label of Point E to the Done List
        self.play(Restore(camera), run_time=2)
        self.wait(2)
        self.play(self.camera.frame.animate.move_to(15 * RIGHT), run_time=2)
        self.play(
            element_e_group.animate.move_to(path_list_outline.get_center() + 2 * DOWN),
            run_time=2,
        )

        self.wait(3)

        # Let the rest of the open list disappear
        self.play(
            FadeOut(list_outline),
            FadeOut(list_title),
            FadeOut(element_c_group),
            FadeOut(element_f_group),
            FadeOut(new_element_a_group),
            FadeOut(element_d_group),
            FadeOut(focus_line),
            run_time=2,
        )

        # iterate backwards through the done list and create the final path
        self.play(
            element_e_group.animate.move_to(list_outline.get_center() + 5 * UP),
            run_time=2,
        )
        self.play(
            element_g_group.animate.move_to(list_outline.get_center() + 3.25 * UP),
            run_time=2,
        )
        self.play(
            element_h_group.animate.move_to(list_outline.get_center() + 1.5 * UP),
            run_time=2,
        )
        self.play(
            element_b_group.animate.move_to(list_outline.get_center() + 0.25 * DOWN),
            run_time=2,
        )
        self.play(
            element_s_group.animate.move_to(list_outline.get_center() + 2 * DOWN),
            run_time=2,
        )
        self.wait(18.5)

        # switch the elements to the right order
        self.play(
            element_s_group.animate.move_to(list_outline.get_center() + 5 * UP),
            element_b_group.animate.move_to(list_outline.get_center() + 3.25 * UP),
            element_h_group.animate.move_to(list_outline.get_center() + 1.5 * UP),
            element_g_group.animate.move_to(list_outline.get_center() + 0.25 * DOWN),
            element_e_group.animate.move_to(list_outline.get_center() + 2 * DOWN),
            run_time=2,
        )

        self.wait(5)

        # Zoom into the graph and move the final path labels to the center
        self.play(
            self.camera.frame.animate.scale(1 / 1.75).move_to(
                group_complete_graph.get_center()
            ),
            group_final_path_labels.animate.scale(0.5).move_to(
                group_complete_graph.get_center()
            ),
            run_time=2,
        )

        # Highlight the final path
        self.play(
            FadeOut(group_heuristics), FadeOut(group_not_final_path_weights), run_time=2
        )
        self.play(
            point_s.animate.set_color(GREEN),
            letter_s.animate.set_color(GREEN),
            run_time=2,
        )
        self.play(
            point_b.animate.set_color(GREEN),
            letter_b.animate.set_color(GREEN),
            line_sb.animate.set_color(GREEN),
            run_time=2,
        )
        self.play(
            point_h.animate.set_color(GREEN),
            letter_h.animate.set_color(GREEN),
            line_bh.animate.set_color(GREEN),
            run_time=2,
        )
        self.play(
            point_g.animate.set_color(GREEN),
            letter_g.animate.set_color(GREEN),
            line_hg.animate.set_color(GREEN),
            run_time=2,
        )
        self.wait(1)
        self.play(
            point_e.animate.set_color(GREEN),
            letter_e.animate.set_color(GREEN),
            line_ge.animate.set_color(GREEN),
            run_time=2,
        )

        self.wait(8)
