#!/usr/bin/env python3
"""Standard-library tests for the canonical character projection."""
import json
import unittest
from pathlib import Path
from engine import derive, read, ROOT

class CaelEngineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.character = read(ROOT / "characters/cael/character.json")

    def test_level_three_historical_wisdom(self):
        r = derive(self.character, 3)
        self.assertEqual((r["abilityScores"]["WIS"], r["hpMax"]), (18, 27))
        self.assertEqual((r["spellAttackBonus"], r["spellSaveDC"]), (6, 14))

    def test_current_level_four(self):
        r = derive(self.character, 4)
        for key, expected in {"hpMax":35,"spellAttackBonus":7,"spellSaveDC":15,"initiative":5,"passivePerception":17}.items():
            self.assertEqual(r[key], expected, key)
        self.assertEqual(r["skills"]["Nature"], 7)
        self.assertEqual(r["skills"]["Arcana"], 5)

    def test_level_seven_selected_spellcasting(self):
        r = derive(self.character, 7)
        self.assertTrue(any(x.get("choice") == "Potent Spellcasting" for x in r["selectedDecisions"]))
        self.assertEqual(r["hpMax"], 59)

    def test_level_eight_scenario_retroactive_hp(self):
        baseline = derive(self.character, 8, "confirmed")
        planned = derive(self.character, 8, "planned")
        self.assertEqual(baseline["hpMax"], 67)
        self.assertEqual(planned["hpMax"], 75)
        self.assertEqual(planned["abilityScores"]["CON"], 18)
        self.assertEqual(planned["abilityScores"]["DEX"], 17)

    def test_level_twelve_planned_dex(self):
        r = derive(self.character, 12, "planned")
        self.assertEqual(r["abilityScores"]["DEX"], 18)
        self.assertEqual(r["abilityScores"]["INT"], 11)
        self.assertEqual(r["hpMax"], 115)

    def test_no_level_outside_range(self):
        for n in (0, 21):
            with self.assertRaises(ValueError):
                derive(self.character, n)

    def test_refs_and_source(self):
        rules = read(ROOT / "rules/homebrew/cael-blessed-quarterstaff.json")
        self.assertEqual(rules["modifiers"][0]["damageType"], "radiant")
        self.assertEqual(rules["modifiers"][0]["when"]["targetCreatureType"], "undead")
        self.assertEqual(self.character["backgroundRef"], "background:guide:XPHB")

if __name__ == "__main__":
    unittest.main()
