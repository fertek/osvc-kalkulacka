# Changelog
Všechny významné změny v tomto projektu budou zaznamenány v tomto souboru.

## [Unreleased]
- (zatim nic)

## [0.7.0] - 2025-12-28
### Přidáno
- Příkaz `osvc presets import-epo` pro generování ročních presetů z EPO XML.
- Příkaz `osvc presets template` pro vypsání/zápis šablony presetů (`--output`, `--output-default`, `--force`).
- `verify` umí vzít rok automaticky z EPO XML, pokud není zadán `--year`.

### Změněno
- `osvc defaults` je nyní přímý příkaz (bez `dump`).
- `osvc init` je nyní `osvc presets template`.
- README zjednodušeno a přesun detailů o defaults do `ADVANCED_USAGE.md`.

## [0.6.0] - 2025-12-28
### Přidáno
- Volba typu činnosti `--activity primary|secondary` (včetně presetů).
- Výpočet pojistného pro vedlejší činnost (bez minima u ZP, rozhodná částka u SP).
- Rozšířeny roční defaulty o parametry pro vedlejší činnost (`sp_min_base_share_secondary`, `sp_threshold_secondary_czk`).
- Soubor `SOURCES.md` pro evidenci zdrojů hodnot v `year_defaults.toml`.
- Sekce „Omezení kalkulačky“ v README.

## [0.5.0] - 2025-12-28
### Přidáno
- Příkaz `osvc verify` pro porovnání výsledků kalkulačky s EPO XML (DPFDP6/DPFDP7).

## [0.4.0] - 2025-12-27
### Změněno
- Zjednodušení §15 na jediný vstup `section_15_allowances_czk`.
- Přidány testy pro zaokrouhlování minimálních záloh a ověření oficiálních hodnot 2022-2026.

## [0.1.0] - 2025-12-26
### Přidáno
- První vydání: CLI kalkulačka pro DPFO + ZP/SP s ročními defaulty a presetem.
