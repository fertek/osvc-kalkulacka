# Changelog
Všechny významné změny v tomto projektu budou zaznamenány v tomto souboru.

## [Unreleased]
- (zatim nic)

## [0.8.5] - 2026-01-05
### Přidáno
- Volitelné vstupy `--paid-tax`, `--paid-zp`, `--paid-sp` (a `paid_*_czk` v presetech) pro výpočet doplatků z reálně zaplacených záloh.
- Zobrazení minimálních záloh pro následující rok (`year+1`) ve výstupu.

### Změněno
- Výstup rozlišuje předepsané vs. zaplacené zálohy.

## [0.8.0] - 2025-12-29
### Přidáno
- Podpora více §7 položek přes `section_7_items` v CLI i presetech.
- Vstupy `par_6_base_czk`, `par_8_base_czk`, `par_9_base_czk`, `par_10_base_czk` pro dílčí základy (§6/8/9/10).

### Změněno
- Odstraněn `income_czk`/`expense_rate`; vstupy §7 jsou jen přes `section_7_items`.
- Odstraněn implicitní 60% paušál; sazba je povinná u každé položky §7 a omezená na 40/60/80 %.
- Test minimálních příjmů pro daňové zvýhodnění na děti vychází z příjmů §6+§7.
- Přesnější popis záloh ZP/SP ve výstupu (pro následující období).

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
