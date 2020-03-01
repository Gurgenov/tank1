import pygame, os


def load_image(image, color=None):
    name = os.path.join('../../Desktop/data', image)
    pic = pygame.image.load(name)
    if color is not None:
        if color == -1:
            color = pic.get_at((0, 0))
        pic.set_colorkey(color)
    return pic.convert_alpha()


pygame.init()

sur = pygame.Surface([200, 300])
sur.fill((255, 0, 0))
running = True

geolocation = 'left'
geolocation2 = 'right'

size = width, height = [1024, 720]
screen = pygame.display.set_mode(size)

all_sprites = pygame.sprite.Group()
sprites_tank = pygame.sprite.Group()

tank = pygame.sprite.Sprite()

im_tank = load_image("tank1.png")

tank2 = pygame.sprite.Sprite()

im_tank2 = load_image('tank2.png')
tank2.rect = im_tank2.get_rect()
tank2.rect.x = 100
tank2.rect.y = 100

shell = pygame.sprite.Sprite()
im_shell = load_image('shell_left.png')

shell.rect = im_shell.get_rect()
shell.rect.x = 910
shell.rect.y = 450

shell_2 = pygame.sprite.Sprite()
im_shell_2 = load_image('shell_right.png')

shell_2.rect = im_shell_2.get_rect()
shell_2.rect.x = 110
shell_2.rect.y = 125

tank.rect = im_tank.get_rect()

all_sprites.add(tank2)
sprites_tank.add(tank)

tank.rect.x = 900
tank.rect.y = 400

screen.blit(im_shell, (shell.rect.x, shell.rect.y))
screen.blit(im_tank, (tank.rect.x, tank.rect.y))
screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))


def draw():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Крассный Победил!", 1, (100, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)


def draw1():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Крассный Победил!", 1, (100, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if tank.rect.x > 0:
            tank.rect.x -= 1
            shell.rect.x -= 1
            im_shell = load_image('shell_left.png')
            im_tank = load_image('tank1.png')
            screen.fill(0)
            screen.blit(im_shell, (shell.rect.x, shell.rect.y))
            screen.blit(im_tank, (tank.rect.x, tank.rect.y))
            screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
            screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))
            geolocation = 'left'
        else:
            tank.rect.x += 0
    if keys[pygame.K_RIGHT]:
        if tank.rect.x < 930:
            tank.rect.x += 1
            shell.rect.x += 1
            im_tank = load_image('tank1_right.png')
            im_shell = load_image('shell_right.png')
            screen.fill(0)
            screen.blit(im_shell, (shell.rect.x, shell.rect.y))
            screen.blit(im_tank, (tank.rect.x, tank.rect.y))
            screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
            screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))
            geolocation = 'right'
        else:
            tank.rect.x += 0
    if keys[pygame.K_UP]:
        if tank.rect.y > 0:
            tank.rect.y -= 1
            shell.rect.y -= 1
            im_shell = load_image('shell_up.png')
            im_tank = load_image('tank1_up.png')
            screen.fill(0)
            screen.blit(im_shell, (shell.rect.x, shell.rect.y))
            screen.blit(im_tank, (tank.rect.x, tank.rect.y))
            screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
            screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))
            geolocation = 'up'
        else:
            tank.rect.y += 0
    if keys[pygame.K_DOWN]:
        if tank.rect.y < 620:
            tank.rect.y += 1
            shell.rect.y += 1
            im_shell = load_image('shell_down.png')
            im_tank = load_image('tank1_down.png')
            screen.fill(0)
            screen.blit(im_shell, (shell.rect.x, shell.rect.y))
            screen.blit(im_tank, (tank.rect.x, tank.rect.y))
            screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
            screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))
            geolocation = 'down'
        else:
            tank.rect.y += 0
    if keys[pygame.K_w]:
        if tank2.rect.y > 0:
            tank2.rect.y -= 1
            shell_2.rect.y -= 1
            im_shell_2 = load_image('shell_up.png')
            im_tank2 = load_image('tank2_up.png')
            screen.fill(0)
            screen.blit(im_shell, (shell.rect.x, shell.rect.y))
            screen.blit(im_tank, (tank.rect.x, tank.rect.y))
            screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
            screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))
            geolocation2 = 'up'
        else:
            tank2.rect.y += 0
            shell_2.rect.y += 0
    if keys[pygame.K_s]:
        if tank2.rect.y < 620:
            tank2.rect.y += 1
            shell_2.rect.y += 1
            im_shell_2 = load_image('shell_down.png')
            im_tank2 = load_image('tank2_down.png')
            screen.fill(0)
            screen.blit(im_shell, (shell.rect.x, shell.rect.y))
            screen.blit(im_tank, (tank.rect.x, tank.rect.y))
            screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
            screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))
            geolocation2 = 'down'
        else:
            tank2.rect.y += 0
            shell_2.rect.y += 0
    if keys[pygame.K_a]:
        if tank2.rect.x > 0:
            tank2.rect.x -= 1
            shell_2.rect.x -= 1
            im_shell_2 = load_image('shell_left.png')
            im_tank2 = load_image('tank2_left.png')
            screen.fill(0)
            screen.blit(im_shell, (shell.rect.x, shell.rect.y))
            screen.blit(im_tank, (tank.rect.x, tank.rect.y))
            screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
            screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))
            geolocation2 = 'left'
        else:
            tank2.rect.x += 0
            shell_2.rect.x += 0
    if keys[pygame.K_d]:
        if tank2.rect.x < 930:
            tank2.rect.x += 1
            shell_2.rect.x += 1
            im_tank2 = load_image('tank2.png')
            im_shell_2 = load_image('shell_right.png')
            screen.fill(0)
            screen.blit(im_shell, (shell.rect.x, shell.rect.y))
            screen.blit(im_tank, (tank.rect.x, tank.rect.y))
            screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
            screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))
            geolocation2 = 'right'
        else:
            tank2.rect.x += 0
            shell_2.rect.x += 0
    if keys[pygame.K_SPACE]:
        if geolocation == 'down':
            if shell.rect.y < 720:
                hits = pygame.sprite.spritecollide(shell, all_sprites, False)
                if hits:
                    draw()
                else:
                    shell.rect.y += 1
                    im_shell = load_image('shell_down.png')
                    screen.fill(0)
                    screen.blit(im_shell, (shell.rect.x, shell.rect.y))
                    screen.blit(im_tank, (tank.rect.x, tank.rect.y))
                    screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
                    screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))
            else:
                shell.rect.x = tank.rect.x + 20
                shell.rect.y = tank.rect.y
                im_shell = load_image('shell_down.png')
                screen.blit(im_shell, (shell.rect.x, shell.rect.y))
                screen.blit(im_tank, (tank.rect.x, tank.rect.y))
        if geolocation == 'up':
            if shell.rect.y > 0:
                hits = pygame.sprite.spritecollide(shell, all_sprites, False)
                if hits:
                    draw()
                else:
                    shell.rect.y -= 0.8
                    im_shell = load_image('shell_up.png')
                    screen.fill(0)
                    screen.blit(im_shell, (shell.rect.x, shell.rect.y))
                    screen.blit(im_tank, (tank.rect.x, tank.rect.y))
                    screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
                    screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))
            else:
                shell.rect.x = tank.rect.x
                shell.rect.y = tank.rect.y
                im_shell = load_image('shell.png')
                screen.blit(im_shell, (shell.rect.x, shell.rect.y))
                screen.blit(im_tank, (tank.rect.x, tank.rect.y))
                screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
                screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))
        if geolocation == 'left':
            if shell.rect.x > 0:
                hits = pygame.sprite.spritecollide(shell, all_sprites, False)
                if hits:
                    draw()
                else:
                    shell.rect.x -= 0.8
                    im_shell = load_image('shell_left.png')
                    screen.fill(0)
                    screen.blit(im_shell, (shell.rect.x, shell.rect.y))
                    screen.blit(im_tank, (tank.rect.x, tank.rect.y))
                    screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
                    screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))
            else:
                shell.rect.x = tank.rect.x
                shell.rect.y = tank.rect.y + 20
                im_shell = load_image('shell_left.png')
                screen.blit(im_shell, (shell.rect.x, shell.rect.y))
                screen.blit(im_tank, (tank.rect.x, tank.rect.y))
                screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
                screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))
        if geolocation == 'right':
            if shell.rect.x < 1024:
                hits = pygame.sprite.spritecollide(shell, all_sprites, False)
                if hits:
                    draw()
                else:
                    shell.rect.x += 1
                    im_shell = load_image('shell_right.png')
                    screen.fill(0)
                    screen.blit(im_shell, (shell.rect.x, shell.rect.y))
                    screen.blit(im_tank, (tank.rect.x, tank.rect.y))
                    screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
                    screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))
            else:
                shell.rect.x = tank.rect.x
                shell.rect.y = tank.rect.y + 20
                im_shell = load_image('shell_right.png')
                screen.blit(im_shell, (shell.rect.x, shell.rect.y))
                screen.blit(im_tank, (tank.rect.x, tank.rect.y))
                screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
                screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))
    if keys[pygame.K_z]:
        if geolocation2 == 'right':
            if shell_2.rect.x < 1024:
                hits = pygame.sprite.spritecollide(shell_2, sprites_tank, False)
                if hits:
                    draw()
                else:
                    shell_2.rect.x += 1
                    im_shell = load_image('shell_right.png')
                    screen.fill(0)
                    screen.blit(im_shell, (shell.rect.x, shell.rect.y))
                    screen.blit(im_tank, (tank.rect.x, tank.rect.y))
                    screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
                    screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))
            else:
                shell_2.rect.x = tank2.rect.x
                shell_2.rect.y = tank2.rect.y + 20
                im_shell_2 = load_image('shell_right.png')
                screen.blit(im_shell, (shell.rect.x, shell.rect.y))
                screen.blit(im_tank, (tank.rect.x, tank.rect.y))
                screen.blit(im_shell_2, (shell_2.rect.x, shell_2.rect.y))
                screen.blit(im_tank2, (tank2.rect.x, tank2.rect.y))



    pygame.display.flip()

pygame.quit()
