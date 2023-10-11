from dataclasses import dataclass

@dataclass
class Book_Item:
    # x = 0
    # y = 0
    width: int
    height: int
    border_radius: int
    background: str # color

    def __post_init__(self):
        # pic
        self.pic_x = 0
        self.pic_y = 0
        self.pic_width = int(0.6 * self.height)
        self.pic_height = self.height

        # title
        self.title_x = self.pic_x + self.pic_width
        self.title_y = self.pic_y
        self.title_width = self.width - self.pic_width
        self.title_height = int(0.4 * self.height)
            # te_title
        self.te_title_x = 0
        self.te_title_y = 0
        self.te_title_width = self.title_width
        self.te_title_height = self.title_height

        # press
        self.press_x = self.title_x
        self.press_y = self.title_y + self.title_height
        self.press_width = self.title_width
        self.press_height = int(0.2 * self.height)
            # lb_press
        self.lb_press_x = 0
        self.lb_press_y = 0
        self.lb_press_width = self.press_width
        self.lb_press_height = self.press_height

        # author
        self.author_x = self.title_x
        self.author_y = self.press_y + self.press_height
        self.author_width = self.title_width
        self.author_height = int(0.2 * self.height)
            # lb_author
        self.lb_author_x = 0
        self.lb_author_y = 0
        self.lb_author_width = self.author_width
        self.lb_author_height = self.author_height

        # wgt info
        self.info_x = self.title_x
        self.info_y = self.author_y + self.author_height
        self.info_width = self.title_width
        self.info_height = int(0.2 * self.height)
        self.info_padding = 2
            # lb_language
        self.language_x = 0
        self.language_y = 0
        self.language_width = self.info_width // 3 - 4 * self.info_padding
        self.language_height = self.info_height
            # v-line 1
        self.vline1_x = self.language_width + self.info_padding
        self.vline1_y = self.language_height
        self.vline1_width = 2 * self.info_padding
        self.vline1_height = self.info_height
            # lb_year
        self.year_x = self.language_x + self.language_width + 2 * self.info_padding
        self.year_y = self.language_y
        self.year_width = self.language_width
        self.year_height = self.language_height
            # v-line 2
        self.vline2_x = self.year_width + self.info_padding
        self.vline2_y = self.year_height
        self.vline2_width = 2 * self.info_padding
        self.vline2_height = self.info_height
            # lb_ext_len
        self.ext_len_x = self.year_x + self.year_width + 2 * self.info_padding
        self.ext_len_y = self.year_y
        self.ext_len_width = self.year_width
        self.ext_len_height= self.year_height
