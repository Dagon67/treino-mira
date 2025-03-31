
import pygame
import random
import time

# Inicialização do Pygame
pygame.init()

# Inicialização do mixer de som
pygame.mixer.init()

# Configurações da tela
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Treino de Mira")

# Cores
white = (255, 255, 255)
black = (0, 0, 0)

# Variáveis do jogo
target_radius = 50
target_x = random.randint(target_radius, screen_width - target_radius)
target_y = random.randint(target_radius, screen_height - target_radius)
score = 0
font = pygame.font.Font(None, 36)

# Tempo de jogo
game_duration = 30  # segundos
start_time = time.time()

# Caminho das imagens (substitua pelos caminhos corretos)
background_path = r'Downloads\imagem.png'
target_image_path = r'Downloads\alvo_imagem.png'
shot_sound_path = r'Downloads\som_do_tiro.mp3'

# Carregar imagens
background = pygame.image.load(background_path).convert()  # Carregar e converter para otimizar exibição
background = pygame.transform.scale(background, (screen_width, screen_height))

target_image = pygame.image.load(target_image_path)
target_image = pygame.transform.scale(target_image, (2 * target_radius, 2 * target_radius))

# Carregar som
shot_sound = pygame.mixer.Sound(shot_sound_path)

# Função para desenhar o alvo
def draw_target(x, y):
    screen.blit(target_image, (x - target_radius, y - target_radius))

# Função para desenhar o cursor personalizado (cruz)
def draw_custom_cursor(x, y):
    pygame.draw.line(screen, white, (x - 8, y), (x + 8, y), 3)
    pygame.draw.line(screen, white, (x, y - 8), (x, y + 8), 3)

# Esconder cursor padrão do sistema
pygame.mouse.set_visible(False)

# Loop principal do jogo
running = True
while running:
    # Verificar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = ((mouse_x - target_x) ** 2 + (mouse_y - target_y) ** 2) ** 0.5
            shot_sound.play()  # Tocar som de tiro ao clicar
            if distance <= target_radius:
                score += 1
                target_x = random.randint(target_radius, screen_width - target_radius)
                target_y = random.randint(target_radius, screen_height - target_radius)

    # Preencher a tela com branco antes de desenhar novamente
    screen.fill(black)

    # Desenhar a imagem de fundo
    screen.blit(background, (0, 0))

    # Desenhar o alvo
    draw_target(target_x, target_y)

    # Exibir pontuação e tempo restante
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

    elapsed_time = time.time() - start_time
    remaining_time = max(0, game_duration - elapsed_time)
    time_text = font.render(f"Time: {int(remaining_time)}s", True, white)
    screen.blit(time_text, (screen_width - 150, 10))

    # Obter posição do mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Desenhar cursor personalizado
    draw_custom_cursor(mouse_x, mouse_y)

    # Atualizar a tela
    pygame.display.flip()

    # Limitar a taxa de quadros
    pygame.time.Clock().tick(240)  # Limita a 240 FPS

    # Verificar se o tempo acabou
    if remaining_time <= 0:
        running = False

# Exibir pontuação final
screen.fill(black)
final_score_text = font.render(f"Final Score: {score}", True, white)
screen.blit(final_score_text, (screen_width // 2 - 100, screen_height // 2 - 20))
pygame.display.flip()

# Mostrar cursor padrão novamente ao sair do jogo
pygame.mouse.set_visible(True)

# Esperar alguns segundos antes de fechar
time.sleep(5)

pygame.quit()
