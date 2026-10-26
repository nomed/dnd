#!/usr/bin/env python3
"""Validazione senza dipendenze del catalogo Cael 2024."""
import json
from pathlib import Path

R = Path(__file__).resolve().parent
read = lambda p: json.loads((R / p).read_text(encoding="utf-8"))
en = read("spells/source-extract.en.json")["records"]
it = read("spells/italiano.it.json")["records"]
progress = read("character/cael-progression.json")
features = read("source/5etools/features.index.json")["features"]
errors = []
warnings = []
names = [s["name"] for s in en]
if len(names) != len(set(names)): errors.append("Duplicate spells")
if set(names) != {s["name"] for s in it}: errors.append("EN/IT spell set differs")
for s in en:
    if not s.get("source") or s.get("page") is None: errors.append("Missing spell source: " + s["name"])
if len(progress["levels"]) != 20: errors.append("Expected 20 levels")
for l in progress["levels"]:
    n = l["level"]
    if l["hp_max"] != 11 + (n - 1) * 8: errors.append(f"HP formula wrong at level {n}")
    if l["proficiency_bonus"] != 2 + (n - 1) // 4: errors.append(f"Proficiency wrong at level {n}")
    if n >= 4 and l["derived_if_wisdom_remains_20"]["spell_save_dc"] != 8 + 5 + l["proficiency_bonus"]: errors.append(f"Spell DC wrong at level {n}")
if len({f["id"] for f in features}) != len(features): errors.append("Duplicate feature ID")
for name, level in [("Star Map", 3), ("Starry Form", 3), ("Cosmic Omen", 6), ("Twinkling Constellations", 10), ("Full of Stars", 14)]:
    if not any(f["name"] == name and f["level"] == level and f["source"] == "XPHB" for f in features): errors.append(f"Missing XPHB feature {name} level {level}")
legacy = read("../../edizioni/level3/cael-level3.json")
if legacy.get("spell_scaling", {}).get("Healing Word", {}).get("ability_modifier") != 5:
    warnings.append("Legacy level3 JSON contains stale healing modifier; do not render from it")
if legacy.get("special_spells", {}).get("Guiding Bolt", {}).get("free_casts_per_long_rest") != 5:
    warnings.append("Legacy level3 JSON contains stale Guiding Bolt free uses")
for field in ("background", "skills", "speed", "passive_perception"):
    if progress["base"].get(field) == "unverified": warnings.append("Unverified character field: " + field)
if progress["advancement"].get("magician_cantrip") == "unconfirmed": warnings.append("Unconfirmed Magician cantrip")
print(json.dumps({"valid": not errors, "errors": errors, "warnings": warnings, "spells": len(en), "features": len(features), "levels": len(progress["levels"])}, ensure_ascii=False, indent=2))
raise SystemExit(1 if errors else 0)
