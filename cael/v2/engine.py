#!/usr/bin/env python3
"""Cael v2 deterministic character projection engine. Standard library only."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEGACY = ROOT.parent / "rules" / "2024"

def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def modifier(score):
    return (score - 10) // 2

def derive(character, level, scenario="confirmed"):
    if not 1 <= level <= 20:
        raise ValueError("level must be between 1 and 20")
    if scenario not in ("confirmed", "planned"):
        raise ValueError("scenario must be confirmed or planned")
    scores = dict(character["initialAbilityScores"])
    selected = []
    unresolved = []
    for choice in character["decisions"]:
        if choice["level"] > level:
            continue
        if choice["status"] == "unselected":
            unresolved.append(choice["type"])
            continue
        if choice["status"] == "proposed" and scenario == "confirmed":
            unresolved.append(choice["type"] + " (proposed, not applied)")
            continue
        selected.append(choice)
        for key, delta in choice.get("changes", {}).items():
            scores[key] += delta
            if scores[key] > 20:
                raise ValueError("Ability score exceeds 20: " + key)
    mods = {key: modifier(value) for key, value in scores.items()}
    pb = 2 + (level - 1) // 4
    # 2024 fixed HP: first level 8+CON, subsequent levels 5+CON.
    # Current CON modifier applies to every character level, including earlier levels.
    hp = 8 + mods["CON"] + (level - 1) * (5 + mods["CON"])
    features = read(LEGACY / "character" / "cael-progression.json")["levels"][level - 1]
    skills = {}
    for name in character["skillProficiencies"]:
        ability = {"Perception":"WIS","Nature":"INT","Stealth":"DEX","Survival":"WIS","Investigation":"INT"}[name]
        bonus = mods[ability] + pb
        if name == "Nature" and any(x.get("choice") == "Magician" for x in selected):
            bonus += mods["WIS"]
        skills[name] = bonus
    if any(x.get("choice") == "Magician" for x in selected):
        skills["Arcana"] = mods["INT"] + mods["WIS"]
    alert = any(x.get("choice") == "Alert" for x in selected)
    return {
        "schemaVersion":"2.0.0",
        "characterId":character["id"],
        "level":level,
        "scenario":scenario,
        "isCurrentLevel":level == character["currentLevel"],
        "abilityScores":scores,
        "modifiers":mods,
        "proficiencyBonus":pb,
        "hpMax":hp,
        "spellAttackBonus":pb + mods["WIS"],
        "spellSaveDC":8 + pb + mods["WIS"],
        "initiative":mods["DEX"] + (pb if alert else 0),
        "skills":skills,
        "passivePerception":10 + skills["Perception"],
        "savingThrows":{k:mods[k] + (pb if k in character["savingThrowProficiencies"] else 0) for k in scores},
        "spellSlots":features["spell_slots"],
        "druidPreparedSpells":features["druid_prepared_spells"],
        "druidCantrips":features["druid_cantrips"],
        "classFeatures":features["class_features"],
        "subclassFeatures":features["subclass_features"],
        "selectedDecisions":selected,
        "unresolvedDecisions":unresolved,
        "provenance":{"character":"characters/cael/character.json","progressionTable":"../rules/2024/character/cael-progression.json","hpRule":"Druid d8, fixed advancement, XPHB 2024"},
        "warnings":(["Future spell preparations and equipment are not projected"] if level != character["currentLevel"] else []) + (["Future proposed ASI changes applied"] if scenario == "planned" and level >= 8 else [])
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", type=int, default=4)
    parser.add_argument("--scenario", choices=("confirmed", "planned"), default="confirmed")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--output")
    args = parser.parse_args()
    character = read(ROOT / "characters" / "cael" / "character.json")
    levels = range(1, 21) if args.all else [args.level]
    result = [derive(character, level, args.scenario) for level in levels]
    content = json.dumps(result if args.all else result[0], ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(content + "\n", encoding="utf-8")
    else:
        print(content)

if __name__ == "__main__":
    main()
