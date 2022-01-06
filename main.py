import pygame
import math
pygame.init()
screen_width = 600
screen_height = 600
screen_height_offset = 300
screen = pygame.display.set_mode((screen_width, screen_height + screen_height_offset))


def get_button_sizes(list_of_text, screen_width_size):
    sizes = []
    for text in list_of_text:
        font = pygame.font.SysFont("Arial", int(screen_width_size / 12))
        text_render = font.render(text, 1, (255, 0, 0))
        x, y, w, h = text_render.get_rect()
        sizes.append(w)
    return max(sizes)


def button(screen_object, y_coordinate, text, width, screen_width_size):
    font = pygame.font.SysFont("Arial", int(screen_width_size / 12))
    text_render = font.render(text, 1, (255, 0, 0))
    _, _, _, height = text_render.get_rect()
    x_coordinate = screen_width_size - width - screen_width_size * 0.05
    pygame.draw.line(screen_object,
                     (150, 150, 150),
                     (x_coordinate, y_coordinate),
                     (x_coordinate + width, y_coordinate),
                     5)
    pygame.draw.line(screen_object,
                     (150, 150, 150),
                     (x_coordinate, y_coordinate - 2),
                     (x_coordinate, y_coordinate + height),
                     5)
    pygame.draw.line(screen_object,
                     (50, 50, 50),
                     (x_coordinate, y_coordinate + height),
                     (x_coordinate + width, y_coordinate + height),
                     5)
    pygame.draw.line(screen_object,
                     (50, 50, 50),
                     (x_coordinate + width, y_coordinate + height),
                     [x_coordinate + width, y_coordinate],
                     5)
    pygame.draw.rect(screen_object,
                     (100, 100, 100),
                     (x_coordinate, y_coordinate, width, height))
    return screen_object.blit(text_render, (x_coordinate, y_coordinate))


def invisible_button(screen_object, x, y, size):
    surface = pygame.Surface((size, size))
    return screen_object.blit(surface, (x, y))


def draw_board(screen_object, screen_width_size, screen_height_size, screen_height_offset_size):
    pygame.draw.line(screen_object,
                     (150, 150, 150),
                     (screen_width_size / 3, screen_height_offset_size / 2),
                     (screen_width_size / 3 , screen_height_size + screen_height_offset_size / 2),
                     5)
    pygame.draw.line(screen_object,
                     (150, 150, 150),
                     (2 * screen_width_size / 3, screen_height_offset_size / 2),
                     (2 * screen_width_size / 3 , screen_height_size + screen_height_offset_size / 2),
                     5)
    pygame.draw.line(screen_object,
                     (150, 150, 150),
                     (0, screen_height_size / 3 + screen_height_offset_size / 2),
                     (screen_width_size, screen_height_size / 3 + screen_height_offset_size / 2),
                     5)
    pygame.draw.line(screen_object,
                     (150, 150, 150),
                     (0, 2 * screen_height_size / 3 + screen_height_offset_size / 2),
                     (screen_width_size, 2 * screen_height_size / 3 + screen_height_offset_size / 2),
                     5)


def main_menu():
    text = ["Quit", "Start"]
    size = get_button_sizes(text, screen_width)
    quit_button = button(screen, (screen_height + screen_height_offset) * 0.05, text[0], size, screen_width)
    start_button = button(screen, (screen_height + screen_height_offset) * 0.8, text[1], size, screen_width)
    not_started = True
    while not_started:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and pygame.K_ESCAPE):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif start_button.collidepoint(pygame.mouse.get_pos()):
                    screen.fill((0, 0, 0))
                    not_started = False
                    del quit_button
                    del start_button
        pygame.display.update()


def create_board_buttons(screen_width_size):
    buttons = [invisible_button(screen_object=screen,
                                x=0,
                                y=screen_height_offset / 2,
                                size=int(screen_width_size / 3)),
               invisible_button(screen_object=screen,
                                x=screen_width_size / 3,
                                y=screen_height_offset / 2,
                                size=int(screen_width_size / 3)),
               invisible_button(screen_object=screen,
                                x=2 * screen_width_size / 3,
                                y=screen_height_offset / 2,
                                size=int(screen_width_size / 3)),
               invisible_button(screen_object=screen,
                                x=0,
                                y=int(screen_width_size / 3) + screen_height_offset / 2,
                                size=int(screen_width_size / 3)),
               invisible_button(screen_object=screen,
                                x=screen_width_size / 3,
                                y=int(screen_width_size / 3) + screen_height_offset / 2,
                                size=int(screen_width_size / 3)),
               invisible_button(screen_object=screen,
                                x=2 * screen_width_size / 3,
                                y=int(screen_width_size / 3) + screen_height_offset / 2,
                                size=int(screen_width_size / 3)),
               invisible_button(screen_object=screen,
                                x=0,
                                y=2 * int(screen_width_size / 3) + screen_height_offset / 2,
                                size=int(screen_width_size / 3)),
               invisible_button(screen_object=screen,
                                x=screen_width_size / 3,
                                y=2 * int(screen_width_size / 3) + screen_height_offset / 2,
                                size=int(screen_width_size / 3)),
               invisible_button(screen_object=screen,
                                x=2 * screen_width_size / 3,
                                y=2 * int(screen_width_size / 3) + screen_height_offset / 2,
                                size=int(screen_width_size / 3))]

    return buttons


def draw_shape(index, cross_form):
    cross_color = (0, 0, 255)
    circle_color = (255, 127, 0)
    if index < 9:
        x_center = int((screen_width / 3) / 2 + (screen_width / 3) * (index % 3))
        y_center = int((screen_width / 3) / 2 + (screen_width / 3) * math.floor(index / 3))
        y_center += int(screen_height_offset / 2)

        if cross_form:
            pygame.draw.line(screen,
                             cross_color,
                             (x_center - screen_width / 10, y_center + screen_width / 10),
                             (x_center + screen_width / 10, y_center - screen_width / 10),
                             5)
            pygame.draw.line(screen,
                             cross_color,
                             (x_center + screen_width / 10, y_center + screen_width / 10),
                             (x_center - screen_width / 10, y_center - screen_width / 10),
                             5)

        else:
            pygame.draw.circle(screen, circle_color, (x_center, y_center), screen_width / 10, 5)
    else:
        x_center = int(screen_width / 3)
        y_center = int(screen_height_offset / 4)
        if cross_form:
            pygame.draw.circle(screen, (0, 0, 0), (x_center, y_center), screen_width / 10, 5)
            pygame.draw.line(screen,
                             cross_color,
                             (x_center - screen_width / 10, y_center + screen_width / 10),
                             (x_center + screen_width / 10, y_center - screen_width / 10),
                             5)
            pygame.draw.line(screen,
                             cross_color,
                             (x_center + screen_width / 10, y_center + screen_width / 10),
                             (x_center - screen_width / 10, y_center - screen_width / 10),
                             5)
        else:
            pygame.draw.line(screen,
                             (0, 0, 0),
                             (x_center - screen_width / 10, y_center + screen_width / 10),
                             (x_center + screen_width / 10, y_center - screen_width / 10),
                             5)
            pygame.draw.line(screen,
                             (0, 0, 0),
                             (x_center + screen_width / 10, y_center + screen_width / 10),
                             (x_center - screen_width / 10, y_center - screen_width / 10),
                             5)
            pygame.draw.circle(screen, circle_color, (x_center, y_center), screen_width / 10, 5)
        font = pygame.font.SysFont("Arial", int(screen_width / 12))
        text_render = font.render("turns", 1, (255, 255, 0))
        screen.blit(text_render, ( 1.5 * x_center,  y_center / 2))


def play_the_game(buttons):
    cross_turn = True
    board = ["Free"] * len(buttons)
    draw_shape(10, cross_turn)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for index, specific_button in enumerate(buttons):
                    if specific_button.collidepoint(pygame.mouse.get_pos()):
                        if board[index] == "Free":
                            if cross_turn:
                                board[index] = "Cross"
                            else:
                                board[index] = "Circle"
                            draw_shape(index, cross_turn)
                            cross_turn = not cross_turn
                            draw_shape(10, cross_turn)
        pygame.display.update()
    pygame.quit()


def run():
    main_menu()
    buttons = create_board_buttons(screen_width)
    draw_board(screen, screen_width, screen_height, screen_height_offset)
    play_the_game(buttons)


run()
