from problem3 import *


def test_rank_strength():
  assert Rank.ACE > Rank.KING


def test_high_card():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.QUEEN),
      Card(Suit.DIAMOND, Rank.JACK),
      Card(Suit.HEART, Rank.NINE),
  ])
  assert c1.hand() == PokerHand.HIGH_CARD


def test_strong_high_card():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.QUEEN),
      Card(Suit.DIAMOND, Rank.JACK),
      Card(Suit.HEART, Rank.NINE),
  ])
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.QUEEN),
      Card(Suit.DIAMOND, Rank.JACK),
      Card(Suit.HEART, Rank.EIGHT),
  ])
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)
  assert c1.hand() == PokerHand.HIGH_CARD
  assert c2.hand() == PokerHand.HIGH_CARD


def test_one_pair():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.TWO),
      Card(Suit.HEART, Rank.TEN),
  ])
  assert c1.hand() == PokerHand.ONE_PAIR


def test_strong_one_pair():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.TWO),
      Card(Suit.HEART, Rank.TEN),
  ])
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.KING),
      Card(Suit.DIAMOND, Rank.TWO),
      Card(Suit.HEART, Rank.NINE),
  ])
  assert c1.hand() == PokerHand.ONE_PAIR
  assert c2.hand() == PokerHand.ONE_PAIR
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_strong_one_pair_same():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.TWO),
      Card(Suit.HEART, Rank.TEN),
  ])
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.DIAMOND, Rank.TWO),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.HEART, Rank.TEN),
  ])
  assert c1.hand() == PokerHand.ONE_PAIR
  assert c2.hand() == PokerHand.ONE_PAIR
  assert not c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_strong_one_pair_remaining():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.TWO),
      Card(Suit.HEART, Rank.TEN),
  ])
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.TWO),
      Card(Suit.HEART, Rank.NINE),
  ])
  assert c1.hand() == PokerHand.ONE_PAIR
  assert c2.hand() == PokerHand.ONE_PAIR
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_two_pair():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
  ])
  assert c1.hand() == PokerHand.TWO_PAIR


def test_strong_two_pair_second():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.NINE),
  ])
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.QUEEN),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.QUEEN),
      Card(Suit.HEART, Rank.NINE),
  ])
  assert c1.hand() == PokerHand.TWO_PAIR
  assert c2.hand() == PokerHand.TWO_PAIR
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_strong_two_pair_remaining():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
  ])
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.NINE),
  ])
  assert c1.hand() == PokerHand.TWO_PAIR
  assert c2.hand() == PokerHand.TWO_PAIR
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_strong_two_pair_same():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
  ])
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
  ])
  assert c1.hand() == PokerHand.TWO_PAIR
  assert c2.hand() == PokerHand.TWO_PAIR
  assert not c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_three_card():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.HEART, Rank.TEN),
      Card(Suit.SPADE, Rank.ACE),
  ])
  assert c1.hand() == PokerHand.THREE_CARD


def test_strong_three_card():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
  ])
  c2 = Cards([
      Card(Suit.HEART, Rank.TWO),
      Card(Suit.CLUB, Rank.TWO),
      Card(Suit.SPADE, Rank.TWO),
      Card(Suit.DIAMOND, Rank.QUEEN),
      Card(Suit.HEART, Rank.NINE),
  ])
  assert c1.hand() == PokerHand.THREE_CARD
  assert c2.hand() == PokerHand.THREE_CARD
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_strong_three_card_remaining():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.NINE),
  ])
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
  ])
  assert c1.hand() == PokerHand.THREE_CARD
  assert c2.hand() == PokerHand.THREE_CARD
  assert c2.stronger_than(c1)
  assert not c1.stronger_than(c2)


def test_strong_three_card_same():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
  ])
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
  ])
  assert c1.hand() == PokerHand.THREE_CARD
  assert c2.hand() == PokerHand.THREE_CARD
  assert not c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_four_card():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.HEART, Rank.TEN),
      Card(Suit.DIAMOND, Rank.ACE),
  ])
  assert c1.hand() == PokerHand.FOUR_CARD


def test_strong_four_card():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.ACE),
      Card(Suit.HEART, Rank.TEN),
  ])
  c2 = Cards([
      Card(Suit.HEART, Rank.TWO),
      Card(Suit.CLUB, Rank.TWO),
      Card(Suit.SPADE, Rank.TWO),
      Card(Suit.DIAMOND, Rank.TWO),
      Card(Suit.HEART, Rank.TEN),
  ])
  assert c1.hand() == PokerHand.FOUR_CARD
  assert c2.hand() == PokerHand.FOUR_CARD
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_strong_four_card_remaining():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.ACE),
      Card(Suit.HEART, Rank.NINE),
  ])
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.ACE),
      Card(Suit.HEART, Rank.TEN),
  ])
  assert c1.hand() == PokerHand.FOUR_CARD
  assert c2.hand() == PokerHand.FOUR_CARD
  assert c2.stronger_than(c1)
  assert not c1.stronger_than(c2)


def test_strong_four_card_same():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.ACE),
      Card(Suit.HEART, Rank.TEN),
  ])
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.ACE),
      Card(Suit.HEART, Rank.TEN),
  ])
  assert c1.hand() == PokerHand.FOUR_CARD
  assert c2.hand() == PokerHand.FOUR_CARD
  assert not c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_straight():
  c1 = Cards([
      Card(Suit.CLUB, Rank.FIVE),
      Card(Suit.SPADE, Rank.EIGHT),
      Card(Suit.HEART, Rank.SIX),
      Card(Suit.HEART, Rank.NINE),
      Card(Suit.DIAMOND, Rank.SEVEN),
  ])
  assert c1.hand() == PokerHand.STRAIGHT


def test_straight_ace14():
  c1 = Cards([
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.DIAMOND, Rank.JACK),
      Card(Suit.SPADE, Rank.QUEEN),
      Card(Suit.HEART, Rank.TEN),
  ])
  assert c1.hand() == PokerHand.STRAIGHT


def test_straight_ace1():
  c1 = Cards([
      Card(Suit.CLUB, Rank.TWO),
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.DIAMOND, Rank.THREE),
      Card(Suit.SPADE, Rank.FOUR),
      Card(Suit.HEART, Rank.FIVE),
  ])
  assert c1.hand() == PokerHand.STRAIGHT


def test_strong_straight():
  c1 = Cards([
      Card(Suit.CLUB, Rank.TEN),
      Card(Suit.SPADE, Rank.EIGHT),
      Card(Suit.HEART, Rank.SIX),
      Card(Suit.HEART, Rank.NINE),
      Card(Suit.DIAMOND, Rank.SEVEN),
  ])
  c2 = Cards([
      Card(Suit.CLUB, Rank.FIVE),
      Card(Suit.SPADE, Rank.EIGHT),
      Card(Suit.HEART, Rank.SIX),
      Card(Suit.HEART, Rank.NINE),
      Card(Suit.DIAMOND, Rank.SEVEN),
  ])
  assert c1.hand() == PokerHand.STRAIGHT
  assert c2.hand() == PokerHand.STRAIGHT
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_straight_ace1_weak():
  c1 = Cards([
      Card(Suit.CLUB, Rank.TWO),
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.DIAMOND, Rank.THREE),
      Card(Suit.SPADE, Rank.FOUR),
      Card(Suit.HEART, Rank.FIVE),
  ])
  c2 = Cards([
      Card(Suit.CLUB, Rank.TWO),
      Card(Suit.HEART, Rank.FIVE),
      Card(Suit.DIAMOND, Rank.THREE),
      Card(Suit.SPADE, Rank.FOUR),
      Card(Suit.HEART, Rank.SIX),
  ])
  assert c1.hand() == PokerHand.STRAIGHT
  assert c2.hand() == PokerHand.STRAIGHT
  assert c2.stronger_than(c1)
  assert not c1.stronger_than(c2)


def test_straight_ace14_strong():
  c1 = Cards([
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.DIAMOND, Rank.JACK),
      Card(Suit.SPADE, Rank.QUEEN),
      Card(Suit.HEART, Rank.TEN),
  ])
  c2 = Cards([
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
      Card(Suit.DIAMOND, Rank.JACK),
      Card(Suit.SPADE, Rank.QUEEN),
      Card(Suit.HEART, Rank.NINE),
  ])
  assert c1.hand() == PokerHand.STRAIGHT
  assert c2.hand() == PokerHand.STRAIGHT
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_full_house():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.TEN),
      Card(Suit.HEART, Rank.TEN),
  ])
  assert c1.hand() == PokerHand.FULL_HOUSE


def test_strong_full_house_pair():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.TEN),
      Card(Suit.HEART, Rank.TEN),
  ])
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.NINE),
      Card(Suit.HEART, Rank.NINE),
  ])
  assert c1.hand() == PokerHand.FULL_HOUSE
  assert c2.hand() == PokerHand.FULL_HOUSE
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_strong_full_house_three_card():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.TEN),
      Card(Suit.HEART, Rank.TEN),
  ])
  c2 = Cards([
      Card(Suit.HEART, Rank.KING),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.KING),
      Card(Suit.DIAMOND, Rank.JACK),
      Card(Suit.HEART, Rank.JACK),
  ])
  assert c1.hand() == PokerHand.FULL_HOUSE
  assert c2.hand() == PokerHand.FULL_HOUSE
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_flush():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.HEART, Rank.KING),
      Card(Suit.HEART, Rank.QUEEN),
      Card(Suit.HEART, Rank.JACK),
      Card(Suit.HEART, Rank.NINE),
  ])
  assert c1.hand() == PokerHand.FLUSH


def test_strong_flush():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.HEART, Rank.KING),
      Card(Suit.HEART, Rank.QUEEN),
      Card(Suit.HEART, Rank.JACK),
      Card(Suit.HEART, Rank.NINE),
  ])
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.HEART, Rank.KING),
      Card(Suit.HEART, Rank.QUEEN),
      Card(Suit.HEART, Rank.JACK),
      Card(Suit.HEART, Rank.EIGHT),
  ])
  assert c1.hand() == PokerHand.FLUSH
  assert c2.hand() == PokerHand.FLUSH
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_straight_flush():
  c1 = Cards([
      Card(Suit.HEART, Rank.FIVE),
      Card(Suit.HEART, Rank.EIGHT),
      Card(Suit.HEART, Rank.SIX),
      Card(Suit.HEART, Rank.NINE),
      Card(Suit.HEART, Rank.SEVEN),
  ])
  assert c1.hand() == PokerHand.STRAIGHT_FLUSH


def test_straight_flush_ace14():
  c1 = Cards([
      Card(Suit.HEART, Rank.KING),
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.HEART, Rank.JACK),
      Card(Suit.HEART, Rank.QUEEN),
      Card(Suit.HEART, Rank.TEN),
  ])
  assert c1.hand() == PokerHand.STRAIGHT_FLUSH


def test_strong_straight_flush():
  c1 = Cards([
      Card(Suit.HEART, Rank.FIVE),
      Card(Suit.HEART, Rank.EIGHT),
      Card(Suit.HEART, Rank.SIX),
      Card(Suit.HEART, Rank.NINE),
      Card(Suit.HEART, Rank.SEVEN),
  ])
  c2 = Cards([
      Card(Suit.HEART, Rank.TEN),
      Card(Suit.HEART, Rank.EIGHT),
      Card(Suit.HEART, Rank.SIX),
      Card(Suit.HEART, Rank.NINE),
      Card(Suit.HEART, Rank.SEVEN),
  ])
  assert c1.hand() == PokerHand.STRAIGHT_FLUSH
  assert c2.hand() == PokerHand.STRAIGHT_FLUSH
  assert not c1.stronger_than(c2)
  assert c2.stronger_than(c1)
