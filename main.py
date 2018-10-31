import sys
import pygame
import random

# Função que retorna o sinal de um número
sign = lambda x: -1 if x < 0 else 1

rocket_velocity = 0
rocket_acceleration = 0
drag_constant = 0.00005

gravity_acceleration = 9.8  # m/s²
rocket_weight = 100  # kg
gravity_force = -1 * gravity_acceleration * rocket_weight  # N

rocket_output = 0

plc_in = 0


def update():
    global plc_in, rocket_velocity, rocket_acceleration, rocket_output

    if pygame.key.get_pressed()[pygame.K_UP]:
        plc_in += 5
    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        plc_in -= 5

    plc_in = 0 if plc_in < 0 else plc_in
    plc_in = 1023 if plc_in > 1023 else plc_in

    # Pra tornar sobressinal possível, fazemos com que haja um "delay"
    # na entrada do CLP; quer dizer, o sistema não assume imediatamente
    # a saída desejada
    rocket_output += (plc_in - rocket_output) / 30

    # A força é dada pela entrada (0-1024) multiplicada por uma constante arbitrária
    rocket_force = rocket_output * 2

    # Força de arrasto é proporcional ao quadrado da velocidade
    drag_force = -1 * sign(rocket_velocity) * (rocket_velocity ** 2) * drag_constant

    # F = m*a
    # a = F/m
    rocket_acceleration = (gravity_force + rocket_force + drag_force) / rocket_weight
    rocket_velocity += rocket_acceleration

    # Limitamos a velocidade de queda
    if rocket_velocity < -100:
        rocket_velocity = -100


pygame.init()
size = width, height = 656, 1216
screen = pygame.display.set_mode(size)
pygame.font.init()
font_comic_sans = pygame.font.SysFont('Comic Sans MS', 24)
clock = pygame.time.Clock()

rocket_image = pygame.image.load("images/rocket.png")
rocket_rect = rocket_image.get_rect()
rocket_rect.left = width / 2 - rocket_rect.width / 2
rocket_rect.top = height / 3 - rocket_rect.height / 2

fire_image = pygame.image.load("images/fire.png")
fire_rect = fire_image.get_rect()
fire_image_width, fire_image_height = fire_rect.width, fire_rect.height
fire_rect.left = width / 2 - fire_rect.width / 2
fire_rect.top = height / 3 + rocket_rect.height / 2 + fire_rect.height / 2 - 100


def display_text(text, screen, position, color=(0, 0, 0)):
    text_surface = font_comic_sans.render(text, True, color)
    screen.blit(text_surface, position)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    clock.tick(30)
    update()
    screen.fill((135, 206, 235))

    # Entradas
    text_input = '{}/{:.0f} (Saida CLP)'.format(plc_in, rocket_output)
    # Velocidade
    text_velocity = '{:.1f} m/s'.format(rocket_velocity)
    # Aceleração
    text_acceleration = '{:.3f} m/s²'.format(rocket_acceleration)

    display_text(text_input, screen, (0, 0))
    display_text(text_velocity, screen, (0, 30))
    display_text(text_acceleration, screen, (0, 60))

    shake_x = random.uniform(-rocket_velocity / 300, rocket_velocity / 300)
    shake_y = random.uniform(-rocket_velocity / 300, rocket_velocity / 300)

    rocket_rect.left = width / 2 - rocket_rect.width / 2 + shake_x
    rocket_rect.top = height / 3 - rocket_rect.height / 2 + shake_y

    #rocket_rect.move_ip(shake_x, shake_y)

    rocket_output_percentage = rocket_output / 1024

    resized_fire_image = pygame.transform.scale(fire_image,
                                                (int(rocket_output_percentage * fire_image_width),
                                                 int(rocket_output_percentage * fire_image_height)))
    fire_rect.left = width / 2 - rocket_output_percentage * fire_image_width / 2 + shake_x
    fire_rect.top = height / 3 + rocket_rect.height / 2 + fire_rect.height / 2 - 100 + shake_y

    screen.blit(rocket_image, rocket_rect)
    screen.blit(resized_fire_image, fire_rect)
    pygame.display.flip()
