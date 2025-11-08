import pytest
from gilded_rose import Item, GildedRose

def test_normal_item_before_sell_date():
    item = Item("foo", 10, 20)
    gr = GildedRose([item])
    gr.update_quality()
    assert item.sell_in == 9
    assert item.quality == 19

def test_normal_item_after_sell_date():
    item = Item("foo", 0, 20)
    gr = GildedRose([item])
    gr.update_quality()
    assert item.sell_in == -1
    assert item.quality == 18

def test_normal_item_quality_never_negative():
    item = Item("foo", 5, 0)
    gr = GildedRose([item])
    gr.update_quality()
    assert item.quality == 0

def test_aged_brie_increases_quality():
    item = Item("Aged Brie", 2, 0)
    gr = GildedRose([item])
    gr.update_quality()
    assert item.sell_in == 1
    assert item.quality == 1

def test_aged_brie_quality_max_50():
    item = Item("Aged Brie", 2, 50)
    gr = GildedRose([item])
    gr.update_quality()
    assert item.quality == 50

def test_sulfuras_never_changes():
    item = Item("Sulfuras, Hand of Ragnaros", 0, 80)
    gr = GildedRose([item])
    gr.update_quality()
    assert item.sell_in == 0
    assert item.quality == 80

def test_backstage_pass_long_before_concert():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    gr = GildedRose([item])
    gr.update_quality()
    assert item.sell_in == 14
    assert item.quality == 21

def test_backstage_pass_medium_close_to_concert():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)
    gr = GildedRose([item])
    gr.update_quality()
    assert item.sell_in == 9
    assert item.quality == 22  # +2 because 10 days or less

def test_backstage_pass_very_close_to_concert():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)
    gr = GildedRose([item])
    gr.update_quality()
    assert item.sell_in == 4
    assert item.quality == 23  # +3 because 5 days or less

def test_backstage_pass_after_concert():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
    gr = GildedRose([item])
    gr.update_quality()
    assert item.sell_in == -1
    assert item.quality == 0

def test_quality_never_exceeds_50():
    item = Item("Aged Brie", 2, 50)
    gr = GildedRose([item])
    gr.update_quality()
    assert item.quality <= 50

def test_multiple_items_update():
    items = [
        Item("Aged Brie", 2, 0),
        Item("foo", 5, 7),
        Item("Backstage passes to a TAFKAL80ETC concert", 10, 20),
        Item("Sulfuras, Hand of Ragnaros", 0, 80)
    ]
    gr = GildedRose(items)
    gr.update_quality()
    # Aged Brie
    assert items[0].quality == 1
    assert items[0].sell_in == 1
    # Normal
    assert items[1].quality == 6
    assert items[1].sell_in == 4
    # Backstage passes
    assert items[2].quality == 22
    assert items[2].sell_in == 9
    # Sulfuras
    assert items[3].quality == 80
    assert items[3].sell_in == 0
