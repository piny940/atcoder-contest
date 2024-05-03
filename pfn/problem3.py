import sys
from enum import Enum
from typing import Literal
from itertools import combinations


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

  def __eq__(self, other: 'Card'):
    return self.suit == other.suit and self.rank == other.rank

  @classmethod
  def from_str(cls, txt: str) -> 'Card':
    for s in Suit:
      if s.value == txt[0]:
        suit = s
    for r in Rank:
      if r.value == txt[1]:
        rank = r
    if suit is None or rank is None:
      raise ValueError('Invalid card')
    return Card(suit, rank)


ALL_CARDS = [Card(suit, rank) for suit in Suit for rank in Rank]


class Cards:
  def __init__(self, cards: list[Card]):
    # Sort by rank to make it easier to determine the type of hand
    self.cards: list[Card] = sorted(cards, key=lambda card: card.rank)

  def size(self) -> int:
    return len(self.cards)

  def ranks(self) -> list[Rank]:
    return list(map(lambda card: card.rank, self.cards))

  @classmethod
  def from_str(cls, txt: str) -> 'Cards':
    return Cards(list(map(Card.from_str, txt.split(' '))))

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

  # Determine the ranks of the pairs. ex: ['2', 'A']
  def __pairs(self) -> list[Rank]:
    pairs: list[Rank] = []
    for rank in self.ranks():
      if self.ranks().count(rank) == 2 and rank not in pairs:
        pairs.append(rank)
    return pairs

  # Determine the number of cards of a same rank. ex: ('2', 3)
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
    if start + self.size() > len(Rank):
      return False
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
    for i in reversed(range(self.size())):
      if self.cards[i].rank != other.cards[i].rank:
        return self.cards[i].rank > other.cards[i].rank
    return False

  def __strong_pair(self, other: 'Cards') -> bool:
    self_pair = self.__pairs()
    other_pair = other.__pairs()
    if len(self_pair) != len(other_pair):
      return len(self_pair) > len(other_pair)
    for i in reversed(range(len(self_pair))):
      if self_pair[i] != other_pair[i]:
        return self_pair[i] > other_pair[i]

    # Compare the remaining cards
    self_remaining = list(filter(lambda card: card.rank not in self_pair, self.cards))
    other_remaining = list(filter(lambda card: card.rank not in other_pair, other.cards))
    for i in reversed(range(len(self_remaining))):
      if self_remaining[i].rank != other_remaining[i].rank:
        return self_remaining[i].rank > other_remaining[i].rank
    return False

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
    for i in reversed(range(len(self_remaining))):
      if self_remaining[i].rank != other_remaining[i].rank:
        return self_remaining[i].rank > other_remaining[i].rank

  def __strong_straight(self, other: 'Cards') -> bool:
    if list(map(lambda card: card.rank.value, self.cards)) == ['2', '3', '4', '5', 'A']:
      return False
    if list(map(lambda card: card.rank.value, other.cards)) == ['2', '3', '4', '5', 'A']:
      return True
    return self.cards[-1].rank > other.cards[-1].rank

  def __strong_flush(self, other: 'Cards') -> bool:
    for i in reversed(range(self.size())):
      if self.cards[i].rank != other.cards[i].rank:
        return self.cards[i].rank > other.cards[i].rank
    return False

  def __strong_full_house(self, other: 'Cards') -> bool:
    self_three_card = self.__a_kind_count()
    other_three_card = other.__a_kind_count()
    if self_three_card[0] != other_three_card[0]:
      return self_three_card[0] > other_three_card[0]
    self_pair = self.__pairs()[0]
    other_pair = other.__pairs()[0]
    return self_pair > other_pair

  def __strong_straight_flush(self, other: 'Cards') -> bool:
    return self.__strong_straight(other)


class Player:
  def __init__(self, cards: Cards):
    self.original = cards

  def is_best(self, others: list['Player']) -> bool:
    for other in others:
      if not self.original.stronger_than(other.original):
        return False
    return True

  def win_rate(self, others: list['Player'], to_change_idxs: list[int]) -> float:
    remains = [card for i, card in enumerate(self.original.cards) if i not in to_change_idxs]
    used_cards = [*self.original.cards]
    for player in others:
      used_cards += player.original.cards
    deck_cards = [card for card in ALL_CARDS if card not in used_cards]
    all_combinations = list(combinations(deck_cards, len(to_change_idxs)))
    print(len(all_combinations))
    if len(all_combinations) == 0:
      return 1 if self.is_best(others) else 0
    win_count = 0
    for picked in all_combinations:
      current = Cards(remains + list(picked))
      if self.__is_best(current, others):
        win_count += 1
    return win_count / len(all_combinations)

  def max_win_rate(self, others: list['Player'], changeable: int) -> tuple[float, list[list[int]]]:
    max_win_rate = 0
    best_ways = []
    for to_change_len in range(0, changeable + 1):
      for to_change_idxs in combinations(range(self.original.size()), to_change_len):
        rate = self.win_rate(others, list(to_change_idxs))
        if rate > max_win_rate:
          max_win_rate = rate
          best_ways = [list(to_change_idxs)]
        elif rate == max_win_rate:
          best_ways.append(list(to_change_idxs))
    return max_win_rate, best_ways

  def __is_best(self, current: Cards, others: list['Player']) -> bool:
    for other in others:
      if not current.stronger_than(other.original):
        return False
    return True


def main(lines: list[str]):
  PLAYER_COUNT = 6
  me = Player(Cards.from_str(lines[0]))
  others = []
  for i in range(1, PLAYER_COUNT):
    cards = Cards.from_str(lines[i])
    others.append(Player(cards))
  k = int(lines[PLAYER_COUNT])
  max_win_rate, best_ways = me.max_win_rate(others, k)
  print(max_win_rate)
  for way in best_ways:
    str_cards = lines[0].split(' ')
    for to_change in way:
      str_cards[to_change] = '**'
    print(' '.join(str_cards))


if __name__ == '__main__':
  lines = []
  for l in sys.stdin:
    lines.append(l.rstrip('\r\n'))
  main(lines)
