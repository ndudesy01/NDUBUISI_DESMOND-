# # # # #ask the student to enter marksand print the grade using if
# # # # #>90:A,
# # # # #>75:B,
# # # # #>50:C,
# # # # #else fail
# # # # name=int(input("please enter mark"))
# # # # if num1>90:
# # # #     # print the grade is A
# # # #
# # # #
# # #
# # #
# # # def is_palindrome(s: str) -> bool:
# # #     true = ''.join(c.lower() for c in s if c.isalnum())
# # #
# # #     return true == true[::-1]
# #
# #
# # import random
# #
# # # Pick a random number between 1 and 10
# # random_number = random.randint(1, 10)
# #
# # print("Random number between 1 and 10:", random_number)
#
# import random
# import time
#
# import pygame
#
# # Card values (2 to 14 where 11=Jack, 12=Queen, 13=King, 14=Ace)
# card_values = list(range(2, 15))
# card_names = {
#     11: "Jack",
#     12: "Queen",
#     13: "King",
#     14: "Ace"
# }
# pygame
# def get_card_name(card):
#     return card_names.get(card, str(card))
#
# def play_war_round():
#     player1_card = random.choice(card_values)
#     player2_card = random.choice(card_values)
#
#     print("Player 1 draws:", get_card_name(player1_card))
#     time.sleep(1)
#     print("Player 2 draws:", get_card_name(player2_card))
#     time.sleep(1)
#
#     if player1_card > player2_card:
#         print("Player 1 wins the round!\n")
#     elif player2_card > player1_card:
#         print("Player 2 wins the round!\n")
#     else:
#         print("It's a tie! WAR!\n")
#
# # Main loop
# rounds = 5
# print("Welcome to the War Card Game!")
# for i in range(1, rounds + 1):
#     print(f"--- Round {i} ---")
#     play_war_round()
#     time.sleep(1)
#
# print("Game over!")
import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("War Card Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load card images
card_images = {
    '2': pygame.image.load('cards/2.png'),
    '3': pygame.image.load('cards/3.png'),
    '4': pygame.image.load('cards/4.png'),
    '5': pygame.image.load('cards/5.png'),
    '6': pygame.image.load('cards/6.png'),
    '7': pygame.image.load('cards/7.png'),
    '8': pygame.image.load('cards/8.png'),
    '9': pygame.image.load('cards/9.png'),
    '10': pygame.image.load('cards/10.png'),
    'J': pygame.image.load('cards/J.png'),
    'Q': pygame.image.load('cards/Q.png'),
    'K': pygame.image.load('cards/K.png'),
    'A': pygame.image.load('cards/A.png')
}

# Define card values
card_values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

# Create a deck of cards
# suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
# deck = [f'{rank} of {suit}' for suit in suits for rank in card_values.keys()]
#
# # Shuffle the deck
# random.shuffle(deck)
#
# # Split the deck into two hands
# player1_hand = deck[:len(deck)//2]
# player2_hand = deck[len(deck)//2:]
#
# # Function to draw a card
# def draw_card(hand):
#     card = hand.pop()
#     rank = card.split(' ')[0]
#     return rank
#
# # Game loop
# running = True
# while running:
#     screen.fill(WHITE)
#
#     # Check for events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # Draw cards for both players
#     if player1_hand and player2_hand:
#         player1_card = draw_card(player1_hand)
#         player2_card = draw_card(player2_hand)
#
#         # Display the cards
#         screen.blit(card_images[player1_card], (150, 200))
#         screen.blit(card_images[player2_card], (450, 200))
#
#         # Determine the winner
#         if card_values[player1_card] > card_values[player2_card]:
#             winner = "Player 1"
#         elif card_values[player1_card] < card_values[player2_card]:
#             winner = "Player 2"
#         else:
#             winner = "It's a tie"
#
#         # Display the winner
#         font = pygame.font.Font(None, 36)
#         text = font.render(f'{winner} wins this round!', True, BLACK)
#         screen.blit(text, (250, 100))
#
#         pygame.display.flip()
#         time.sleep(1)
#     else:
#         # End the game
#         font = pygame.font.Font(None, 48)
#         text = font.render("Game Over!", True, BLACK)
#         screen.blit(text, (330, 250))
#         pygame.display.flip()
#         time.sleep(2)
#         running = False
#
# # Quit Pygame
# pygame.qui

# if 5:
# print("china is working haerd")
#
# whilex<25:
#  print("ebele")

x = 0
while x < 5:
    print("ebele")
    x+= 1