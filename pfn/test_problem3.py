import time
from problem3 import *


def test_rank_strength():
  assert Rank.ACE > Rank.KING


def test_high_card():
  h1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.QUEEN),
      Card(Suit.DIAMOND, Rank.JACK),
      Card(Suit.HEART, Rank.NINE),
  ]).hand()
  assert h1.kind() == HandKind.HIGH_CARD


def test_strong_high_card():
  h1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.QUEEN),
      Card(Suit.DIAMOND, Rank.JACK),
      Card(Suit.HEART, Rank.NINE),
  ]).hand()
  h2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.QUEEN),
      Card(Suit.DIAMOND, Rank.JACK),
      Card(Suit.HEART, Rank.EIGHT),
  ]).hand()
  assert h1.stronger_than(h2)
  assert not h2.stronger_than(h1)
  assert h1.kind() == HandKind.HIGH_CARD
  assert h2.kind() == HandKind.HIGH_CARD


def test_one_pair1():
  h1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.TWO),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  assert h1.kind() == HandKind.ONE_PAIR


def test_strong_one_pair():
  h1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.TWO),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  h2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.KING),
      Card(Suit.DIAMOND, Rank.TWO),
      Card(Suit.HEART, Rank.NINE),
  ]).hand()
  assert h1.stronger_than(h2)
  assert not h2.stronger_than(h1)
  assert h1.kind() == HandKind.ONE_PAIR
  assert h2.kind() == HandKind.ONE_PAIR


def test_strong_one_pair_same():
  h1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.TWO),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  h2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.DIAMOND, Rank.TWO),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  assert not h1.stronger_than(h2)
  assert not h2.stronger_than(h1)
  assert h1.kind() == HandKind.ONE_PAIR
  assert h2.kind() == HandKind.ONE_PAIR


def test_strong_one_pair_remaining():
  h1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.TWO),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  h2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.TWO),
      Card(Suit.HEART, Rank.NINE),
  ]).hand()
  assert h1.stronger_than(h2)
  assert not h2.stronger_than(h1)
  assert h1.kind() == HandKind.ONE_PAIR
  assert h2.kind() == HandKind.ONE_PAIR


def test_two_pair():
  h1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  assert h1.kind() == HandKind.TWO_PAIR


def test_strong_two_pair_second():
  h1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.NINE),
  ]).hand()
  h2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.QUEEN),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.QUEEN),
      Card(Suit.HEART, Rank.NINE),
  ]).hand()
  assert h1.stronger_than(h2)
  assert not h2.stronger_than(h1)
  assert h1.kind() == HandKind.TWO_PAIR
  assert h2.kind() == HandKind.TWO_PAIR


def test_strong_two_pair_remaining():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.NINE),
  ]).hand()
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)
  assert c1.kind() == HandKind.TWO_PAIR
  assert c2.kind() == HandKind.TWO_PAIR


def test_strong_two_pair_same():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  assert not c1.stronger_than(c2)
  assert not c2.stronger_than(c1)
  assert c1.kind() == HandKind.TWO_PAIR
  assert c2.kind() == HandKind.TWO_PAIR


def test_three_card():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.HEART, Rank.QUEEN),
      Card(Suit.SPADE, Rank.ACE),
  ]).hand()
  assert c1.kind() == HandKind.THREE_CARD


def test_strong_three_card():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  c2 = Cards([
      Card(Suit.HEART, Rank.TWO),
      Card(Suit.CLUB, Rank.TWO),
      Card(Suit.SPADE, Rank.TWO),
      Card(Suit.DIAMOND, Rank.QUEEN),
      Card(Suit.HEART, Rank.NINE),
  ]).hand()
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)
  assert c1.kind() == HandKind.THREE_CARD
  assert c2.kind() == HandKind.THREE_CARD


def test_strong_three_card_remaining():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.NINE),
  ]).hand()
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  assert not c1.stronger_than(c2)
  assert c2.stronger_than(c1)
  assert c1.kind() == HandKind.THREE_CARD
  assert c2.kind() == HandKind.THREE_CARD


def test_strong_three_card_same():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  assert c1.kind() == HandKind.THREE_CARD
  assert c2.kind() == HandKind.THREE_CARD
  assert not c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_four_card():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.HEART, Rank.TEN),
      Card(Suit.DIAMOND, Rank.ACE),
  ]).hand()
  assert c1.kind() == HandKind.FOUR_CARD


def test_strong_four_card():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.ACE),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  c2 = Cards([
      Card(Suit.HEART, Rank.TWO),
      Card(Suit.CLUB, Rank.TWO),
      Card(Suit.SPADE, Rank.TWO),
      Card(Suit.DIAMOND, Rank.TWO),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  assert c1.kind() == HandKind.FOUR_CARD
  assert c2.kind() == HandKind.FOUR_CARD
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_strong_four_card_remaining():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.ACE),
      Card(Suit.HEART, Rank.NINE),
  ]).hand()
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.ACE),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  assert c1.kind() == HandKind.FOUR_CARD
  assert c2.kind() == HandKind.FOUR_CARD
  assert c2.stronger_than(c1)
  assert not c1.stronger_than(c2)


def test_strong_four_card_same():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.ACE),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.ACE),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  assert c1.kind() == HandKind.FOUR_CARD
  assert c2.kind() == HandKind.FOUR_CARD
  assert not c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_straight():
  c1 = Cards([
      Card(Suit.CLUB, Rank.FIVE),
      Card(Suit.SPADE, Rank.EIGHT),
      Card(Suit.HEART, Rank.SIX),
      Card(Suit.HEART, Rank.NINE),
      Card(Suit.DIAMOND, Rank.SEVEN),
  ]).hand()
  assert c1.kind() == HandKind.STRAIGHT


def test_straight_ace14():
  c1 = Cards([
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.DIAMOND, Rank.JACK),
      Card(Suit.SPADE, Rank.QUEEN),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  assert c1.kind() == HandKind.STRAIGHT


def test_straight_ace1():
  c1 = Cards([
      Card(Suit.CLUB, Rank.TWO),
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.DIAMOND, Rank.THREE),
      Card(Suit.SPADE, Rank.FOUR),
      Card(Suit.HEART, Rank.FIVE),
  ]).hand()
  assert c1.kind() == HandKind.STRAIGHT


def test_strong_straight():
  c1 = Cards([
      Card(Suit.CLUB, Rank.TEN),
      Card(Suit.SPADE, Rank.EIGHT),
      Card(Suit.HEART, Rank.SIX),
      Card(Suit.HEART, Rank.NINE),
      Card(Suit.DIAMOND, Rank.SEVEN),
  ]).hand()
  c2 = Cards([
      Card(Suit.CLUB, Rank.FIVE),
      Card(Suit.SPADE, Rank.EIGHT),
      Card(Suit.HEART, Rank.SIX),
      Card(Suit.HEART, Rank.NINE),
      Card(Suit.DIAMOND, Rank.SEVEN),
  ]).hand()
  assert c1.kind() == HandKind.STRAIGHT
  assert c2.kind() == HandKind.STRAIGHT
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_straight_ace1_weak():
  c1 = Cards([
      Card(Suit.CLUB, Rank.TWO),
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.DIAMOND, Rank.THREE),
      Card(Suit.SPADE, Rank.FOUR),
      Card(Suit.HEART, Rank.FIVE),
  ]).hand()
  c2 = Cards([
      Card(Suit.CLUB, Rank.TWO),
      Card(Suit.HEART, Rank.FIVE),
      Card(Suit.DIAMOND, Rank.THREE),
      Card(Suit.SPADE, Rank.FOUR),
      Card(Suit.HEART, Rank.SIX),
  ]).hand()
  assert c1.kind() == HandKind.STRAIGHT
  assert c2.kind() == HandKind.STRAIGHT
  assert c2.stronger_than(c1)
  assert not c1.stronger_than(c2)


def test_straight_ace14_strong():
  c1 = Cards([
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.DIAMOND, Rank.JACK),
      Card(Suit.SPADE, Rank.QUEEN),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  c2 = Cards([
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.HEART, Rank.TEN),
      Card(Suit.DIAMOND, Rank.JACK),
      Card(Suit.SPADE, Rank.QUEEN),
      Card(Suit.HEART, Rank.NINE),
  ]).hand()
  assert c1.kind() == HandKind.STRAIGHT
  assert c2.kind() == HandKind.STRAIGHT
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_full_house():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.TEN),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  assert c1.kind() == HandKind.FULL_HOUSE


def test_strong_full_house_pair():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.TEN),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.NINE),
      Card(Suit.HEART, Rank.NINE),
  ]).hand()
  assert c1.kind() == HandKind.FULL_HOUSE
  assert c2.kind() == HandKind.FULL_HOUSE
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_strong_full_house_three_card():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.CLUB, Rank.ACE),
      Card(Suit.SPADE, Rank.ACE),
      Card(Suit.DIAMOND, Rank.TEN),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  c2 = Cards([
      Card(Suit.HEART, Rank.KING),
      Card(Suit.CLUB, Rank.KING),
      Card(Suit.SPADE, Rank.KING),
      Card(Suit.DIAMOND, Rank.JACK),
      Card(Suit.HEART, Rank.JACK),
  ]).hand()
  assert c1.kind() == HandKind.FULL_HOUSE
  assert c2.kind() == HandKind.FULL_HOUSE
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_flush():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.HEART, Rank.KING),
      Card(Suit.HEART, Rank.QUEEN),
      Card(Suit.HEART, Rank.JACK),
      Card(Suit.HEART, Rank.NINE),
  ]).hand()
  assert c1.kind() == HandKind.FLUSH


def test_strong_flush():
  c1 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.HEART, Rank.KING),
      Card(Suit.HEART, Rank.QUEEN),
      Card(Suit.HEART, Rank.JACK),
      Card(Suit.HEART, Rank.NINE),
  ]).hand()
  c2 = Cards([
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.HEART, Rank.KING),
      Card(Suit.HEART, Rank.QUEEN),
      Card(Suit.HEART, Rank.JACK),
      Card(Suit.HEART, Rank.EIGHT),
  ]).hand()
  assert c1.kind() == HandKind.FLUSH
  assert c2.kind() == HandKind.FLUSH
  assert c1.stronger_than(c2)
  assert not c2.stronger_than(c1)


def test_straight_flush():
  c1 = Cards([
      Card(Suit.HEART, Rank.FIVE),
      Card(Suit.HEART, Rank.EIGHT),
      Card(Suit.HEART, Rank.SIX),
      Card(Suit.HEART, Rank.NINE),
      Card(Suit.HEART, Rank.SEVEN),
  ]).hand()
  assert c1.kind() == HandKind.STRAIGHT_FLUSH


def test_straight_flush_ace14():
  c1 = Cards([
      Card(Suit.HEART, Rank.KING),
      Card(Suit.HEART, Rank.ACE),
      Card(Suit.HEART, Rank.JACK),
      Card(Suit.HEART, Rank.QUEEN),
      Card(Suit.HEART, Rank.TEN),
  ]).hand()
  assert c1.kind() == HandKind.STRAIGHT_FLUSH


def test_strong_straight_flush():
  c1 = Cards([
      Card(Suit.HEART, Rank.FIVE),
      Card(Suit.HEART, Rank.EIGHT),
      Card(Suit.HEART, Rank.SIX),
      Card(Suit.HEART, Rank.NINE),
      Card(Suit.HEART, Rank.SEVEN),
  ]).hand()
  c2 = Cards([
      Card(Suit.HEART, Rank.TEN),
      Card(Suit.HEART, Rank.EIGHT),
      Card(Suit.HEART, Rank.SIX),
      Card(Suit.HEART, Rank.NINE),
      Card(Suit.HEART, Rank.SEVEN),
  ]).hand()
  assert c1.kind() == HandKind.STRAIGHT_FLUSH
  assert c2.kind() == HandKind.STRAIGHT_FLUSH
  assert not c1.stronger_than(c2)
  assert c2.stronger_than(c1)
