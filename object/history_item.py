from dataclasses import dataclass

# use h to show from history

@dataclass
class hSearch_Item:
    x: int # 0
    y: int # 0
    w: int # width
    h: int # height
    br: int # border radius
    bg: str # color

    def __post_init__(self):
        # lb_pic
        self.pic_x = 0
        self.pic_y = 0
        self.pic_h = self.h
        self.pic_w = int(0.6 * self.h)

        # lb_q
        self.q_x = self.pic_w
        self.q_y = self.pic_y
        self.q_w = int((self.w - 0.6 * self.h) * 0.7)
        self.q_h = int(self.h * 0.3)

        # lb_search_type
        self.st_x = self.q_x + self.q_w
        self.st_y = self.q_y
        self.st_w = self.w - self.pic_w - self.q_w
        self.st_h = self.q_h

        # lb_year
        self.y_x = self.q_x
        self.y_y = self.q_y + self.q_h
        self.y_w = int((self.w - 0.6 * self.h) * 0.6)
        self.y_h = int(self.h * 0.25)

        # extension_language
        self.l_x = self.y_x + self.y_w
        self.l_y = self.y_y
        self.l_w = self.w - self.pic_w - self.y_w
        self.l_h = self.y_h

        # lb_book nums
        self.bn_x = self.y_x
        self.bn_y = self.y_y + self.y_h
        self.bn_w = self.y_w
        self.bn_h = self.y_h

        # extension_extension
        self.ex_x = self.l_x
        self.ex_y = self.bn_y
        self.ex_w = self.l_w
        self.ex_h = self.l_h

        # search_time
        self.t_x = self.bn_x
        self.t_y = self.bn_y + self.bn_h
        self.t_w = self.bn_w
        self.t_h = self.h - self.q_h - self.y_h - self.bn_h

        # exact matching
        self.em_x = self.ex_x
        self.em_y = self.t_y
        self.em_w = self.ex_w
        self.em_h = self.t_h

@dataclass
class hBook_Item:
    x: int # 0
    y: int # 0
    w: int # width
    h: int # height
    br: int # border radius
    bg: str # color

    def __post_init__(self):
        # lb_pic
        self.pic_x = 0
        self.pic_y = 0
        self.pic_h = self.h
        self.pic_w = int(0.6 * self.h)

        # te_title
        self.t_x = self.pic_x + self.pic_w
        self.t_y = self.pic_y
        self.t_w = self.w - self.pic_w
        self.t_h = int(0.4 * self.h)
        
        # lb_press
        self.p_x = self.t_x
        self.p_y = self.t_y + self.t_h
        self.p_w = self.t_w // 2
        self.p_h = self.t_h // 2

        # lb_author
        self.a_x = self.p_x + self.p_w
        self.a_y = self.p_y
        self.a_w = self.p_w
        self.a_h = self.p_h

        # lb_zlib
        self.z_x = self.p_x
        self.z_y = self.p_y + self.p_h
        self.z_w = self.t_w
        self.z_h = self.p_h

        # lb_language
        self.l_x = self.z_x
        self.l_y = self.z_y + self.z_h
        self.l_w = self.t_w // 3
        self.l_h = self.z_h

        # lb_year
        self.y_x = self.l_x + self.l_w
        self.y_y = self.l_y
        self.y_w = self.l_w
        self.y_h = self.l_h

        # lb_ext_len
        self.el_x = self.y_x + self.y_w
        self.el_y = self.y_y
        self.el_w = self.y_w
        self.el_h = self.y_h
