# OSVČ kalkulačka (DPFO + ZP/SP)

## Instalace

```bash
pip install osvc-kalkulacka
```

```bash
uv tool install osvc-kalkulacka
```

```bash
pipx install osvc-kalkulacka
```

Aktualizace:

```bash
pip install --upgrade osvc-kalkulacka
```

```bash
uv tool upgrade osvc-kalkulacka
```

```bash
pipx upgrade osvc-kalkulacka
```

## Postup použití

1) Vytvoř předvolby pro roky, se kterými počítáš:

```bash
osvc init
```

```bash
${USER_DIR}/year_presets.toml
```

2) Doplň `year_presets.toml` (příjmy, děti, dary…). Minimálně potřebuješ `income_czk` pro daný rok.

3) Volitelně přepiš výchozí tabulky, pokud potřebuješ vlastní parametry:

```text
${USER_DIR}/year_defaults.override.toml
```

4) Spusť výpočet jen s `--year`, pokud máš v předvolbách vše potřebné:

```bash
osvc --year 2025
```

5) Když chceš přepsat hodnoty z předvoleb, zadej je přímo:

```bash
osvc --year 2025 --income 800000 --child-months-by-order 12
```

Alternativně explicitně:

```bash
osvc calc --year 2025 --income 800000 --child-months-by-order 12
```

## Přehled příkazů

Zobrazení cest:

```bash
osvc config path
```

Očekávané soubory:

```text
${USER_DIR}/year_presets.toml
${USER_DIR}/year_defaults.override.toml
```

## Pořadí zdrojů

Předvolby (roční vstupy):
Vlastní čísla, která zadáváš každý rok (příjmy, dary, děti). Slouží jako výchozí hodnoty pro výpočet.

```text
--presets
OSVC_PRESETS_PATH
${USER_DIR}/year_presets.toml
```

Výchozí tabulky (parametry pro výpočet):
Oficiální roční parametry (průměrná/minimální mzda, slevy, sazby). Bez nich výpočet neběží.

```text
--defaults
OSVC_DEFAULTS_PATH
${USER_DIR}/year_defaults.override.toml (pokud existuje)
vestavěné year_defaults.toml
```

## Export vestavěných tabulek

```bash
osvc defaults dump --output year_defaults.toml
```
