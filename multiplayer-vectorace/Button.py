import pygame

def play(algo):
    pygame.display.set_caption("VECTOR RACE")

class Button:
    def __init__(self, x, y, image, hover_image=None, hover_scale_factor=1.0):
        self.original_image = image
        self.image = image
        self.hover_image_provided = hover_image
        self.hover_scale_factor = hover_scale_factor
        

        if self.hover_image_provided:
            self.hover_image = self.hover_image_provided
        else:
            original_width, original_height = self.original_image.get_size()
            scaled_width = int(original_width * self.hover_scale_factor)
            scaled_height = int(original_height * self.hover_scale_factor)
            self.hover_image = pygame.transform.scale(self.original_image, (scaled_width, scaled_height))
        

        self.current_image = self.image
        self.rect = self.current_image.get_rect(center=(x, y))
        self.original_rect = self.rect.copy()

    def update(self, screen):
        screen.blit(self.current_image, self.rect)

    def check_hover(self, mouse_pos):
        if self.original_rect.collidepoint(mouse_pos):
            self.current_image = self.hover_image
            self.rect = self.current_image.get_rect(center=self.original_rect.center)
            return True
        else:
            self.current_image = self.original_image
            self.rect = self.original_rect.copy()
            return False

    def check_click(self, mouse_pos):
        return self.original_rect.collidepoint(mouse_pos)