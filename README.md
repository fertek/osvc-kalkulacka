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
~/.config/cz.janfertek.osvc-kalkulacka/year_presets.toml
```

2) Doplň `year_presets.toml` (příjmy, děti, dary…). Minimálně potřebuješ `income_czk` pro daný rok. Výchozí cesta je `~/.config/cz.janfertek.osvc-kalkulacka/year_presets.toml` a ověříš ji přes `osvc config path`.

Příklad obsahu:

```toml
["2025"]
income_czk = 650000
mortgage_interest_paid_czk = 150000
donations_paid_czk = 0
child_months_by_order = [6, 12]
spouse_allowance = true
```

Hodnota `child_months_by_order` je seznam měsíců nároku podle pořadí dítěte (1., 2., 3+). Zápis `child_months_by_order = [6, 12]` znamená 1. dítě 6 měsíců, 2. dítě 12 měsíců.

3) Volitelně přepiš výchozí tabulky, pokud potřebuješ vlastní parametry:

```text
nano ~/.config/cz.janfertek.osvc-kalkulacka/year_defaults.override.toml
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

Poznámka: výchozí adresář lze změnit přes `OSVC_USER_PATH`. Cesty k presetům/defaultům můžeš přepsat přes `OSVC_PRESETS_PATH` a `OSVC_DEFAULTS_PATH`.

Očekávané soubory:

```text
~/.config/cz.janfertek.osvc-kalkulacka/year_presets.toml
~/.config/cz.janfertek.osvc-kalkulacka/year_defaults.override.toml
```

## Pořadí zdrojů

Předvolby (roční vstupy):
Vlastní čísla, která zadáváš každý rok (příjmy, dary, děti). Slouží jako výchozí hodnoty pro výpočet.

Priorita je shora dolů (první nalezená cesta vyhrává).

Příklad: pokud nastavíš `OSVC_PRESETS_PATH`, přebije soubor v `~/.config/cz.janfertek.osvc-kalkulacka/year_presets.toml`.

```text
osvc --presets ./my_year_presets.toml --year 2025
OSVC_PRESETS_PATH=./my_year_presets.toml osvc --year 2025
~/.config/cz.janfertek.osvc-kalkulacka/year_presets.toml
```

Výchozí tabulky (parametry pro výpočet):
Oficiální roční parametry (průměrná/minimální mzda, slevy, sazby). Bez nich výpočet neběží.

Priorita je shora dolů (první nalezená cesta vyhrává).

Příklad: pokud nastavíš `OSVC_DEFAULTS_PATH`, přebije `~/.config/cz.janfertek.osvc-kalkulacka/year_defaults.override.toml` i vestavěný soubor.

```text
osvc --defaults ./my_year_defaults.toml --year 2025
OSVC_DEFAULTS_PATH=./my_year_defaults.toml osvc --year 2025
~/.config/cz.janfertek.osvc-kalkulacka/year_defaults.override.toml (pokud existuje)
vestavěné year_defaults.toml
```

Export vestavěných tabulek do souboru:

```bash
osvc defaults dump --output year_defaults.toml
```
