# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue  # Sulfuras never changes

            # Decrease sell_in
            item.sell_in -= 1

            if item.name == "Aged Brie":
                self._increase_quality(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_pass(item)
            else:  # Normal items
                self._decrease_quality(item)

            # Extra rules for items past their sell date
            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    self._increase_quality(item)
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0
                else:
                    self._decrease_quality(item)

    # Helper functions to keep code clean
    def _increase_quality(self, item, amount=1):
        item.quality = min(50, item.quality + amount)

    def _decrease_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)

    def _update_backstage_pass(self, item):
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            self._increase_quality(item, 3)
        elif item.sell_in < 10:
            self._increase_quality(item, 2)
        else:
            self._increase_quality(item, 1)
