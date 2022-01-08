import math
import pygame


class ChuckChackChoe:
    def __init__(self):
        pygame.init()
        self.screen_width = 600
        self.screen_height = 600
        self.screen_height_offset = 400
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height + self.screen_height_offset))
        self.font = pygame.font.SysFont("Arial", int(self.screen_width / 12))
        self.cross_color = (0, 0, 255)
        self.circle_color = (255, 127, 0)
        self.lines_color = (150, 150, 150)
        self.black_color = (0, 0, 0)
        self.main_menu_buttons_texts = ["Quit", "Start"]
        self.board_buttons = []
        self.cross_turn = True
        self.list_of_cell_states_of_the_board = ["Free"] * 9

    def get_text_button_sizes(self):
        sizes = []
        for text in self.main_menu_buttons_texts:
            font = pygame.font.SysFont("Arial", int(self.screen_width / 12))
            text_render = font.render(text, True, (255, 0, 0))
            _, _, width, _ = text_render.get_rect()
            sizes.append(width)
        return max(sizes)

    def create_button_box(self, x_coordinate, y_coordinate, button_width, text_height):
        pygame.draw.line(surface=self.screen,
                         color=(150, 150, 150),
                         start_pos=(x_coordinate, y_coordinate),
                         end_pos=(x_coordinate + button_width, y_coordinate),
                         width=5)
        pygame.draw.line(surface=self.screen,
                         color=(150, 150, 150),
                         start_pos=(x_coordinate, y_coordinate - 2),
                         end_pos=(x_coordinate, y_coordinate + text_height),
                         width=5)
        pygame.draw.line(surface=self.screen,
                         color=(50, 50, 50),
                         start_pos=(x_coordinate, y_coordinate + text_height),
                         end_pos=(x_coordinate + button_width, y_coordinate + text_height),
                         width=5)
        pygame.draw.line(surface=self.screen,
                         color=(50, 50, 50),
                         start_pos=(x_coordinate + button_width, y_coordinate + text_height),
                         end_pos=[x_coordinate + button_width, y_coordinate],
                         width=5)

    def create_button(self, button_y_coordinate, button_text, button_width):
        text_render = self.font.render(button_text, True, (255, 0, 0))
        _, _, _, text_height = text_render.get_rect()
        button_x_coordinate = self.screen_width - button_width - self.screen_width * 0.05
        self.create_button_box(button_x_coordinate, button_y_coordinate, button_width, text_height)
        pygame.draw.rect(surface=self.screen,
                         color=(100, 100, 100),
                         rect=(button_x_coordinate, button_y_coordinate, button_width, text_height))
        return self.screen.blit(text_render, (button_x_coordinate, button_y_coordinate))

    def create_invisible_button(self, button_x_coordinate, button_y_coordinate, button_size):
        surface = pygame.Surface((button_size, button_size))
        return self.screen.blit(surface, (button_x_coordinate, button_y_coordinate))

    def draw_board_lines(self):
        pygame.draw.line(surface=self.screen,
                         color=self.lines_color,
                         start_pos=(self.screen_width / 3, self.screen_height_offset / 2),
                         end_pos=(self.screen_width / 3, self.screen_height + self.screen_height_offset / 2),
                         width=5)
        pygame.draw.line(surface=self.screen,
                         color=self.lines_color,
                         start_pos=(2 * self.screen_width / 3, self.screen_height_offset / 2),
                         end_pos=(2 * self.screen_width / 3, self.screen_height + self.screen_height_offset / 2),
                         width=5)
        pygame.draw.line(surface=self.screen,
                         color=self.lines_color,
                         start_pos=(0, self.screen_height / 3 + self.screen_height_offset / 2),
                         end_pos=(self.screen_width, self.screen_height / 3 + self.screen_height_offset / 2),
                         width=5)
        pygame.draw.line(surface=self.screen,
                         color=self.lines_color,
                         start_pos=(0, 2 * self.screen_height / 3 + self.screen_height_offset / 2),
                         end_pos=(self.screen_width, 2 * self.screen_height / 3 + self.screen_height_offset / 2),
                         width=5)

    def main_menu(self):
        main_menu_text_sizes = self.get_text_button_sizes()
        quit_button = self.create_button(button_y_coordinate=(self.screen_height + self.screen_height_offset) * 0.05,
                                         button_text=self.main_menu_buttons_texts[0],
                                         button_width=main_menu_text_sizes)
        start_button = self.create_button(button_y_coordinate=(self.screen_height + self.screen_height_offset) * 0.8,
                                          button_text=self.main_menu_buttons_texts[1],
                                          button_width=main_menu_text_sizes)
        game_is_not_started = True
        while game_is_not_started:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and pygame.K_ESCAPE):
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_button.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                    elif start_button.collidepoint(pygame.mouse.get_pos()):
                        self.screen.fill(self.black_color)
                        game_is_not_started = False
                        del quit_button
                        del start_button
            pygame.display.update()

    def create_board_buttons(self):
        for index in range(9):
            self.board_buttons.append(self.create_invisible_button(
                button_x_coordinate=(self.screen_width / 3) * (index % 3),
                button_y_coordinate=(self.screen_width / 3) * math.floor(index / 3) + self.screen_height_offset / 2,
                button_size=int(self.screen_width / 3)))

    def draw_cross_shape(self, x_center, y_center, cross_size, color):
        pygame.draw.line(surface=self.screen,
                         color=color,
                         start_pos=(x_center - cross_size, y_center + cross_size),
                         end_pos=(x_center + cross_size, y_center - cross_size),
                         width=5)
        pygame.draw.line(surface=self.screen,
                         color=color,
                         start_pos=(x_center + cross_size, y_center + cross_size),
                         end_pos=(x_center - cross_size, y_center - cross_size),
                         width=5)

    def draw_shape_in_the_board(self, cross_form, turn_indicator=False, index=None):
        if not turn_indicator:
            x_center = int((self.screen_width / 3) / 2 + (self.screen_width / 3) * (index % 3))
            y_center = int((self.screen_width / 3) / 2 + (self.screen_width / 3) * math.floor(index / 3))
            y_center += int(self.screen_height_offset / 2)
            if cross_form:
                self.draw_cross_shape(x_center, y_center, self.screen_width / 10, self.cross_color)
            else:
                pygame.draw.circle(self.screen, self.circle_color, (x_center, y_center), self.screen_width / 10, 5)
        else:
            x_center = int(self.screen_width / 3)
            y_center = int(self.screen_height_offset / 4)
            if cross_form:
                pygame.draw.circle(self.screen, self.black_color, (x_center, y_center), self.screen_width / 10, 5)
                self.draw_cross_shape(x_center, y_center, self.screen_width / 10, self.cross_color)
            else:
                self.draw_cross_shape(x_center, y_center, self.screen_width / 10, self.black_color)
                pygame.draw.circle(self.screen, self.circle_color, (x_center, y_center), self.screen_width / 10, 5)
            text_render = self.font.render("turns", True, (255, 255, 0))
            self.screen.blit(text_render, (1.5 * x_center, y_center / 2))

    def create_the_board(self):
        self.create_board_buttons()
        self.draw_board_lines()

    def play_the_game(self):
        self.draw_shape_in_the_board(cross_form=self.cross_turn, turn_indicator=True)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for index, specific_button in enumerate(self.board_buttons):
                        if specific_button.collidepoint(pygame.mouse.get_pos()):
                            if self.list_of_cell_states_of_the_board[index] == "Free":
                                if self.cross_turn:
                                    self.list_of_cell_states_of_the_board[index] = "Cross"
                                else:
                                    self.list_of_cell_states_of_the_board[index] = "Circle"
                                self.draw_shape_in_the_board(cross_form=self.cross_turn, index=index)
                                self.cross_turn = not self.cross_turn
                                self.draw_shape_in_the_board(cross_form=self.cross_turn, turn_indicator=True)
            pygame.display.update()
        pygame.quit()

    def run_the_game(self):
        self.main_menu()
        self.create_the_board()
        self.play_the_game()


class_object = ChuckChackChoe()
class_object.run_the_game()
