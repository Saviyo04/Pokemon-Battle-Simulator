import pygame
from pokemon_elem import PokemonElectric, PokemonFire, PokemonGrass, PokemonWater

# Inizializzazione di PyGame
pygame.init()

# Impostazioni base della finestra
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokemon Battle Game")

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font per il testo
font = pygame.font.Font(None, 36)

# Funzione per disegnare il testo
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# Schermata principale
def main_menu():
    running = True
    while running:
        screen.fill(WHITE)
        draw_text("Pokemon Battle Game", font, BLACK, screen, 20, 20)
        draw_text("Press SPACE to start", font, BLACK, screen, 20, 60)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    battle_screen()

# Schermata di battaglia
def battle_screen():
    running = True
    while running:
        screen.fill(WHITE)
        draw_text("Battle Starts!", font, BLACK, screen, 20, 20)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

# Avvia il gioco
main_menu()
pygame.quit()
