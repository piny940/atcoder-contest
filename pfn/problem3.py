import sys
from enum import Enum
from typing import Literal
from itertools import combinations
import abc


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


class HandKind(Enum):
  HIGH_CARD = 0
  ONE_PAIR = 1
  TWO_PAIR = 2
  THREE_CARD = 3
  STRAIGHT = 4
  FLUSH = 5
  FULL_HOUSE = 6
  FOUR_CARD = 7
  STRAIGHT_FLUSH = 8


class PokerHand(metaclass=abc.ABCMeta):
  def kind(self) -> HandKind:
    pass

  def stronger_than(self, other: 'PokerHand') -> bool:
    pass


class HighCard(PokerHand):
  def __init__(self, ranks: list[Rank]):
    self.ranks: list[Rank] = sorted(ranks, reverse=True)

  def kind(self) -> HandKind:
    return HandKind.HIGH_CARD

  def stronger_than(self, other: 'PokerHand') -> bool:
    if other.kind() != HandKind.HIGH_CARD:
      return False
    for i in range(len(self.ranks)):
      if self.ranks[i] != other.ranks[i]:
        return self.ranks[i] > other.ranks[i]
    return False


class OnePair(PokerHand):
  def __init__(self, pair: Rank, remains: list[Rank]):
    self.pair: Rank = pair
    self.remains: list[Rank] = sorted(remains, reverse=True)

  def kind(self) -> HandKind:
    return HandKind.ONE_PAIR

  def stronger_than(self, other: 'PokerHand') -> bool:
    if other.kind() != HandKind.ONE_PAIR:
      return self.kind().value > other.kind().value
    if self.pair != other.pair:
      return self.pair > other.pair
    for i in range(len(self.remains)):
      if self.remains[i] != other.remains[i]:
        return self.remains[i] > other.remains[i]
    return False


class TwoPair(PokerHand):
  def __init__(self, pairs: list[Rank], remain: Rank):
    self.pairs: list[Rank] = sorted(pairs, reverse=True)
    self.remain: Rank = remain

  def kind(self) -> HandKind:
    return HandKind.TWO_PAIR

  def stronger_than(self, other: 'PokerHand') -> bool:
    if other.kind() != HandKind.TWO_PAIR:
      return self.kind().value > other.kind().value
    for i in range(len(self.pairs)):
      if self.pairs[i] != other.pairs[i]:
        return self.pairs[i] > other.pairs[i]
    if self.remain != other.remain:
      return self.remain > other.remain
    return False


class ThreeCard(PokerHand):
  def __init__(self, three_card: Rank, remains: list[Rank]):
    self.three_card: Rank = three_card
    self.remains: list[Rank] = sorted(remains, reverse=True)

  def kind(self) -> HandKind:
    return HandKind.THREE_CARD

  def stronger_than(self, other: 'PokerHand') -> bool:
    if other.kind() != HandKind.THREE_CARD:
      return self.kind().value > other.kind().value
    if self.three_card != other.three_card:
      return self.three_card > other.three_card
    for i in range(len(self.remains)):
      if self.remains[i] != other.remains[i]:
        return self.remains[i] > other.remains[i]
    return False


class Straight(PokerHand):
  def __init__(self, top: Rank):
    self.top: Rank = top

  def kind(self) -> HandKind:
    return HandKind.STRAIGHT

  def stronger_than(self, other: 'PokerHand') -> bool:
    if other.kind() != HandKind.STRAIGHT:
      return self.kind().value > other.kind().value
    return self.top > other.top


class Flush(PokerHand):
  def __init__(self, ranks: list[Rank]):
    self.ranks: list[Rank] = sorted(ranks, reverse=True)

  def kind(self) -> HandKind:
    return HandKind.FLUSH

  def stronger_than(self, other: 'PokerHand') -> bool:
    if other.kind() != HandKind.FLUSH:
      return self.kind().value > other.kind().value
    for i in range(len(self.ranks)):
      if self.ranks[i] != other.ranks[i]:
        return self.ranks[i] > other.ranks[i]
    return False


class FullHouse(PokerHand):
  def __init__(self, three_card: Rank, pair: Rank):
    self.three_card: Rank = three_card
    self.pair: Rank = pair

  def kind(self) -> HandKind:
    return HandKind.FULL_HOUSE

  def stronger_than(self, other: 'PokerHand') -> bool:
    if other.kind() != HandKind.FULL_HOUSE:
      return self.kind().value > other.kind().value
    if self.three_card != other.three_card:
      return self.three_card > other.three_card
    if self.pair != other.pair:
      return self.pair > other.pair
    return False


class FourCard(PokerHand):
  def __init__(self, four_card: Rank, remain: Rank):
    self.four_card: Rank = four_card
    self.remain: Rank = remain

  def kind(self) -> HandKind:
    return HandKind.FOUR_CARD

  def stronger_than(self, other: 'PokerHand') -> bool:
    if other.kind() != HandKind.FOUR_CARD:
      return self.kind().value > other.kind().value
    if self.four_card != other.four_card:
      return self.four_card > other.four_card
    if self.remain != other.remain:
      return self.remain > other.remain
    return False


class StraightFlush(PokerHand):
  def __init__(self, top: Rank):
    self.top: Rank = top

  def kind(self) -> HandKind:
    return HandKind.STRAIGHT_FLUSH

  def stronger_than(self, other: 'PokerHand') -> bool:
    if other.kind() != HandKind.STRAIGHT_FLUSH:
      return self.kind().value > other.kind().value
    return self.top > other.top


class Cards:
  def __init__(self, cards: list[Card]):
    # Sort by rank to make it easier to determine the type of hand
    self.sorted: list[Card] = sorted(cards, key=lambda card: card.rank)
    self.cards: list[Card] = [*cards]

  def size(self) -> int:
    return len(self.cards)

  def ranks(self) -> list[Rank]:
    return list(map(lambda card: card.rank, self.sorted))

  @classmethod
  def from_str(cls, txt: str) -> 'Cards':
    return Cards(list(map(Card.from_str, txt.split(' '))))

  def hand(self) -> PokerHand:
    one_pair = self.__one_pair()
    straight = self.__straight()
    flush = self.__flush()
    if not one_pair and not flush and not straight:
      return HighCard(self.ranks())
    if straight and flush:
      return StraightFlush(straight.top)
    three_card = self.__three_card()
    if three_card:
      return self.__four_card() or self.__full_house() or three_card
    return flush or straight or self.__two_pair() or one_pair

  # Determine the number of cards of a same rank. ex: {'2': 3, 'A': 2}
  def __counts(self) -> dict[str, int]:
    counts = {}
    for rank in self.ranks():
      counts[rank.name] = counts.get(rank.name, 0) + 1
    return counts

  # Determine the ranks of the pairs. ex: ['2', 'A']
  def __pairs(self) -> list[Rank]:
    counts = self.__counts()
    pairs = [Rank[rank_name] for rank_name, count in counts.items() if count >= 2]
    return pairs

  # Determine the number of cards of a same rank. ex: ('2', 3)
  def __a_kind_count(self) -> tuple[None, Literal[0]] | tuple[Rank, int]:
    max_count = (None, 0)
    counts = self.__counts()
    for rank_name, count in counts.items():
      if count > max_count[1]:
        max_count = (Rank[rank_name], count)
    return max_count

  def __one_pair(self) -> OnePair | None:
    pairs = self.__pairs()[:1]
    if len(pairs) < 1:
      return None
    remains = [card.rank for card in self.sorted if card.rank != pairs[0]]
    return OnePair(pairs[0], remains)

  def __two_pair(self) -> TwoPair | None:
    pairs = self.__pairs()[:2]
    if len(pairs) < 2:
      return None
    remains = [card.rank for card in self.sorted if card.rank not in pairs]
    return TwoPair(pairs, remains[0])

  def __three_card(self) -> ThreeCard | None:
    three_card, count = self.__a_kind_count()
    if count < 3:
      return None
    remains = [card.rank for card in self.sorted if card.rank != three_card]
    return ThreeCard(three_card, remains)

  def __straight(self) -> Straight | None:
    if list(map(lambda card: card.rank.value, self.sorted)) == ['2', '3', '4', '5', 'A']:
      return Straight(Rank.FIVE)
    top = list(Rank).index(self.sorted[-1].rank)
    if top < self.size() - 1:
      return None
    if all(self.sorted[self.size() - 1 - i].rank == list(Rank)[top - i] for i in range(self.size())):
      return Straight(self.sorted[-1].rank)
    return None

  def __flush(self) -> Flush | None:
    if all(self.sorted[i].suit == self.sorted[0].suit for i in range(self.size())):
      return Flush(self.ranks())
    return None

  def __full_house(self) -> FullHouse | None:
    three_card = self.__three_card()
    if not three_card:
      return None
    if len(three_card.remains) == 2 and three_card.remains[0] == three_card.remains[1]:
      return FullHouse(three_card.three_card, three_card.remains[0])
    return None

  def __four_card(self) -> FourCard | None:
    four_card, count = self.__a_kind_count()
    if count < 4:
      return None
    remains = [card.rank for card in self.sorted if card.rank != four_card]
    return FourCard(four_card, remains[0])


class Player:
  def __init__(self, cards: Cards):
    self.original = cards
    self.__hand = cards.hand()

  def hand(self):
    return self.__hand

  def is_winner(self, others: list['Player']) -> bool:
    for other in others:
      if not self.hand().stronger_than(other.hand()):
        return False
    return True

  def win_rate(self, others: list['Player'], to_change_idxs: list[int]) -> float:
    remains = [card for i, card in enumerate(self.original.cards) if i not in to_change_idxs]
    used_cards = [*self.original.cards]
    for player in others:
      used_cards += player.original.cards
    deck_cards = [card for card in ALL_CARDS if card not in used_cards]
    all_combinations = list(combinations(deck_cards, len(to_change_idxs)))
    if len(all_combinations) == 0:
      return 1 if self.is_winner(others) else 0
    win_count = 0
    for picked in all_combinations:
      current = Cards(remains + list(picked))
      if self.__is_winner(current, others):
        win_count += 1
    return win_count / len(all_combinations)

  def max_win_rate(self, others: list['Player'], changeable: int) -> tuple[float, list[list[int]]]:
    max_win_rate = 0
    best_ways = []
    for to_change_len in range(0, changeable + 1):
      for to_change_idxs in combinations(range(self.original.size()), to_change_len):
        change_list = list(to_change_idxs)
        rate = self.win_rate(others, change_list)
        if rate > max_win_rate:
          max_win_rate = rate
          best_ways = [change_list]
        elif rate == max_win_rate:
          best_ways.append(change_list)
    return max_win_rate, best_ways

  def __is_winner(self, current: Cards, others: list['Player']) -> bool:
    hand = current.hand()
    for other in others:
      if not hand.stronger_than(other.hand()):
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
  ways_str = []
  for way in best_ways:
    str_cards = lines[0].split(' ')
    for to_change in way:
      str_cards[to_change] = '**'
    ways_str.append(' '.join(str_cards))
  print('\n'.join(sorted(ways_str)))


if __name__ == '__main__':
  lines = []
  for l in sys.stdin:
    lines.append(l.rstrip('\r\n'))
  main(lines)
