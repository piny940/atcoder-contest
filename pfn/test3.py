import sys
from enum import Enum
from typing import Literal


class PokerHand(Enum):
  HIGH_CARD = 0
  ONE_PAIR = 1
  TWO_PAIR = 2
  THREE_CARD = 3
  STRAIGHT = 4
  FLUSH = 5
  FULL_HOUSE = 6
  FOUR_CARD = 7
  STRAIGHT_FLUSH = 8


class Suit(Enum):
  SPADE = 'S'
  HEART = 'H'
  DIAMOND = 'D'
  CLUB = 'C'


RANK_STRENGTH = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}


class Rank(Enum):
  TWO = '2'
  THREE = '3'
  FOUR = '4'
  FIVE = '5'
  SIX = '6'
  SEVEN = '7'
  EIGHT = '8'
  NINE = '9'
  TEN = 'T'
  JACK = 'J'
  QUEEN = 'Q'
  KING = 'K'
  ACE = 'A'

  def __lt__(self, other: 'Rank'):
    return RANK_STRENGTH[self.value] < RANK_STRENGTH[other.value]

  def __le__(self, other: 'Rank'):
    return RANK_STRENGTH[self.value] <= RANK_STRENGTH[other.value]

  def __eq__(self, other: 'Rank'):
    return RANK_STRENGTH[self.value] == RANK_STRENGTH[other.value]

  def __ne__(self, other: 'Rank'):
    return RANK_STRENGTH[self.value] != RANK_STRENGTH[other.value]

  def __gt__(self, other: 'Rank'):
    return RANK_STRENGTH[self.value] > RANK_STRENGTH[other.value]

  def __ge__(self, other: 'Rank'):
    return RANK_STRENGTH[self.value] >= RANK_STRENGTH[other.value]


class Card:
  def __init__(self, suit: Suit, rank: Rank):
    self.suit = suit
    self.rank = rank


class Cards:
  def __init__(self, cards: list[Card]):
    # Sort by rank to make it easier to determine the type of hand
    self.cards: list[Card] = sorted(cards, key=lambda card: card.rank)

  def size(self) -> int:
    return len(self.cards)

  def ranks(self) -> list[Rank]:
    return list(map(lambda card: card.rank, self.cards))

  def hand(self) -> PokerHand:
    if self.__is_straight_flush():
      return PokerHand.STRAIGHT_FLUSH
    if self.__is_four_card():
      return PokerHand.FOUR_CARD
    if self.__is_full_house():
      return PokerHand.FULL_HOUSE
    if self.__is_flush():
      return PokerHand.FLUSH
    if self.__is_straight():
      return PokerHand.STRAIGHT
    if self.__is_three_card():
      return PokerHand.THREE_CARD
    if self.__is_two_pair():
      return PokerHand.TWO_PAIR
    if self.__is_one_pair():
      return PokerHand.ONE_PAIR
    return PokerHand.HIGH_CARD

  def stronger_than(self, other: 'Cards') -> bool:
    if self.hand().value != other.hand().value:
      return self.hand().value > other.hand().value
    if self.hand() == PokerHand.HIGH_CARD:
      return self.__strong_high_card(other)
    if self.hand() == PokerHand.ONE_PAIR or self.hand() == PokerHand.TWO_PAIR:
      return self.__strong_pair(other)
    if self.hand() == PokerHand.THREE_CARD or self.hand() == PokerHand.FOUR_CARD:
      return self.__strong_a_kind(other)
    if self.hand() == PokerHand.STRAIGHT:
      return self.__strong_straight(other)
    if self.hand() == PokerHand.FLUSH:
      return self.__strong_flush(other)
    if self.hand() == PokerHand.FULL_HOUSE:
      return self.__strong_full_house(other)
    if self.hand() == PokerHand.STRAIGHT_FLUSH:
      return self.__strong_straight_flush(other)

  # Determine the ranks of the pairs. ex) ['2', 'A']
  def __pairs(self) -> list[Rank]:
    pairs: list[Rank] = []
    for rank in self.ranks():
      if self.ranks().count(rank) == 2 and rank not in pairs:
        pairs.append(rank)
    return pairs

  # Determine the number of cards of a same rank. ex) ('2', 3)
  def __a_kind_count(self) -> tuple[None, Literal[0]] | tuple[Rank, int]:
    max_count = (None, 0)
    for rank in map(lambda card: card.rank, self.cards):
      count = self.ranks().count(rank)
      if count > max_count[1]:
        max_count = (rank, count)
    return max_count

  def __is_one_pair(self) -> bool:
    return len(self.__pairs()) == 1

  def __is_two_pair(self) -> bool:
    return len(self.__pairs()) == 2

  def __is_three_card(self) -> bool:
    return self.__a_kind_count()[1] == 3

  def __is_straight(self) -> bool:
    if list(map(lambda card: card.rank.value, self.cards)) == ['2', '3', '4', '5', 'A']:
      return True
    start = list(Rank).index(self.cards[0].rank)
    return all(self.cards[i].rank == list(Rank)[start + i] for i in range(self.size()))

  def __is_flush(self) -> bool:
    return all(self.cards[i].suit == self.cards[0].suit for i in range(self.size()))

  def __is_full_house(self) -> bool:
    return self.__is_one_pair() and self.__is_three_card()

  def __is_four_card(self) -> bool:
    return self.__a_kind_count()[1] == 4

  def __is_straight_flush(self) -> bool:
    return self.__is_straight() and self.__is_flush()

  def __strong_high_card(self, other: 'Cards') -> bool:
    for i in range(0, self.size(), -1):
      if self.cards[i].rank != other.cards[i].rank:
        return self.cards[i].rank > other.cards[i].rank
    return False

  def __strong_pair(self, other: 'Cards') -> bool:
    self_pair = self.__pairs()
    other_pair = other.__pairs()
    if len(self_pair) != len(other_pair):
      return len(self_pair) > len(other_pair)
    for i in range(0, len(self_pair), -1):
      if self_pair[i] != other_pair[i]:
        return self_pair[i] > other_pair[i]

    # Compare the remaining cards
    self_remaining = list(filter(lambda card: card.rank not in self_pair, self.cards))
    other_remaining = list(filter(lambda card: card.rank not in other_pair, other.cards))
    for i in range(0, len(self_remaining), -1):
      if self_remaining[i].rank != other_remaining[i].rank:
        return self_remaining[i].rank > other_remaining[i].rank

  def __strong_a_kind(self, other: 'Cards') -> bool:
    self_card = self.__a_kind_count()
    other_card = other.__a_kind_count()
    if self_card[1] != other_card[1]:
      return self_card[1] > other_card[1]
    if self_card[0] != other_card[0]:
      return self_card[0] > other_card[0]

    # Compare the remaining cards
    self_remaining = list(filter(lambda card: card.rank != self_card[0], self.cards))
    other_remaining = list(filter(lambda card: card.rank != other_card[0], other.cards))
    for i in range(0, len(self_remaining), -1):
      if self_remaining[i].rank != other_remaining[i].rank:
        return self_remaining[i].rank > other_remaining[i].rank

  def __strong_straight(self, other: 'Cards') -> bool:
    if list(map(lambda card: card.rank.value, self.cards)) == ['2', '3', '4', '5', 'A']:
      return False
    if list(map(lambda card: card.rank.value, other.cards)) == ['2', '3', '4', '5', 'A']:
      return True
    return self.cards[-1].rank > other.cards[-1].rank

  def __strong_flush(self, other: 'Cards') -> bool:
    for i in range(0, self.size(), -1):
      if self.cards[i].rank != other.cards[i].rank:
        return self.cards[i].rank > other.cards[i].rank
    return False

  def __strong_full_house(self, other: 'Cards') -> bool:
    self_three_card = self.__a_kind_count()
    other_three_card = other.__a_kind_count()
    if self_three_card[0] != other_three_card[0]:
      return self_three_card[0] > other_three_card[0]
    self_pair = self.__pairs()[0]
    other_pair = self.__pairs()[0]
    return self_pair > other_pair

  def __strong_straight_flush(self, other: 'Cards') -> bool:
    return self.__strong_straight(other)


class Player:
  def __init__(self, cards: Cards):
    self.cards = cards

  def is_winner(self, others: list['Player']) -> bool:
    for other in others:
      if not self.cards.stronger_than(other.cards):
        return False
    return True


def main(lines: list[str]):
  PLAYER_COUNT = 6
  me = Player(line_to_cards(lines[0]))
  others = []
  for i in range(1, PLAYER_COUNT):
    cards = line_to_cards(lines[i])
    others.append(Player(cards))
  k = int(lines[PLAYER_COUNT])
  if k != 0:
    print(1)
    return
  if me.is_winner(others):
    print(1)
  else:
    print(0)
  print(lines[0])


def str_to_card(txt: str) -> Card:
  for s in Suit:
    if s.value == txt[0]:
      suit = s
  for r in Rank:
    if r.value == txt[1]:
      rank = r
  if suit is None or rank is None:
    raise ValueError('Invalid card')
  return Card(suit, rank)


def line_to_cards(line: str) -> Cards:
  return Cards(list(map(str_to_card, line.split(' '))))


if __name__ == '__main__':
  lines = []
  for l in sys.stdin:
    lines.append(l.rstrip('\r\n'))
  main(lines)
