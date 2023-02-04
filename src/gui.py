import sys, pygame
from model import CardType, Card, Game, Color

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (200,0,0)
GREEN = (0,150,0)
BLUE = (0,0,255)

BACKGROUND_COLOR = (50, 100, 50)
SCREEN_SIZE = (int(600*1.2), int(400*1.2))

# Card
CARD_EDGE_COLOR = WHITE
SLOT_EDGE_COLOR = BLACK
CARD_FILL_COLOR = (210,210,210)
CARD_SIZE = (60,90)
CARD_FONT_SIZE = 32

# Board
CARD_VERT_OFFSET = CARD_SIZE[1]//4
COLUMNS_VERT_POS = SCREEN_SIZE[0]//4
Y_MARGIN = SCREEN_SIZE[0]//15
X_MARGIN = SCREEN_SIZE[0]//15

def init():
    global card_font 
    card_font = pygame.font.SysFont(None, CARD_FONT_SIZE)

def draw_slot(screen, card_pos, flower=False):
    # draw card shape
    pygame.draw.rect(screen, SLOT_EDGE_COLOR, pygame.Rect(card_pos[0], card_pos[1], CARD_SIZE[0], CARD_SIZE[1]), width=1, border_radius=4)
    if flower:
        img = card_font.render('Ý', True, BLACK)
        screen.blit(img, card_pos)

def draw_card(card : Card, screen, card_pos):
    # draw card shape
    pygame.draw.rect(screen, CARD_FILL_COLOR, pygame.Rect(card_pos[0], card_pos[1], CARD_SIZE[0], CARD_SIZE[1]), border_radius=4)
    pygame.draw.rect(screen, CARD_EDGE_COLOR, pygame.Rect(card_pos[0], card_pos[1], CARD_SIZE[0], CARD_SIZE[1]), width=2, border_radius=4)

    # draw symbol
    if card.getType() == CardType.FLOWER:
        color = BLACK
    elif card.getColor() == Color.RED:
        color = RED
    elif card.getColor() == Color.GREEN:
        color = GREEN
    elif card.getColor() == Color.BLUE:
        color = BLUE
    else:
        raise ValueError("Unknown color of card")
    
    if card.getType() == CardType.FLOWER:
        symbol = 'Ý'
    elif card.getType() == CardType.DRAGON:
        symbol = '§'
    elif card.getType() == CardType.NUMERAL:
        symbol = str(card.getValue())
    else:
        raise ValueError("Unknown type of card")

    img = card_font.render(symbol, True, color)
    screen.blit(img, card_pos)

    
def draw_game(game : Game, screen):
    screen.fill(BACKGROUND_COLOR)
    #draw_card(Card(CardType.FLOWER), screen, (30,30))
    #draw_card(Card(CardType.DRAGON, color=Color.RED), screen, (130,30))
    #draw_card(Card(CardType.NUMERAL,color=Color.BLUE, value=7), screen, (230,30))
    #draw_card(Card(CardType.NUMERAL,color=Color.GREEN, value=1), screen, (330,30))

    column_width = SCREEN_SIZE[0] // (game.NB_COLUMNS+1)
    # draw reserve
    for iR in range(game.NB_RESERVES):
        card = game.get_reserve(iR)
        x = iR * column_width + X_MARGIN
        draw_slot(screen, (x,Y_MARGIN))
        if len(card)!=0:
            draw_card(card[0], screen, (x,Y_MARGIN))

    # draw flower
    pos_flower = ((game.NB_RESERVES+0.5)*column_width + X_MARGIN,Y_MARGIN)
    draw_slot(screen, pos_flower, flower=True)
    if game.get_flower():
        draw_card(Card(CardType.FLOWER), screen, pos_flower)

    # draw end slots
    for iE, card in enumerate(game.get_end_stacks()):
        pos = ((game.NB_RESERVES+2+iE)*column_width + X_MARGIN,Y_MARGIN)
        draw_slot(screen, pos)
        if card!=None:
            draw_card(card, screen, pos)

    # draw columns
    
    for iCol in range(game.NB_COLUMNS):
        x = column_width*iCol + X_MARGIN
        #pygame.draw.line(screen, BLACK, (x,0), (x,SCREEN_SIZE[1]))
        draw_slot(screen, (x,COLUMNS_VERT_POS))

        cards = game.get_column(iCol)
        for j,card in enumerate(cards):
            y = COLUMNS_VERT_POS + CARD_VERT_OFFSET * j
            draw_card(card, screen, (x,y))


