# Pokročilé použití

## Výchozí tabulky (year_defaults)

Výchozí tabulky obsahují roční parametry pro výpočet (průměrná/minimální mzda, slevy, sazby). Bez nich výpočet neběží.

### Pořadí zdrojů (priorita)

První nalezená cesta vyhrává:

```text
osvc --defaults ./my_year_defaults.toml --year 2025
OSVC_DEFAULTS_PATH=./my_year_defaults.toml osvc --year 2025
~/.config/osvc-kalkulacka/year_defaults.override.toml (pokud existuje)
vestavěné year_defaults.toml
```

### Export vestavěných tabulek

```bash
osvc defaults --output year_defaults.toml
```

### Ruční override tabulek

Pokud potřebuješ upravit tabulky ručně, vytvoř nebo uprav:

```text
~/.config/osvc-kalkulacka/year_defaults.override.toml
```

## Předvolby (year_presets) a OSVC_PRESETS_PATH

Předvolby jsou roční vstupy (příjmy, děti, nezdanitelné části). Slouží jako výchozí hodnoty pro výpočet.

### Pořadí zdrojů (priorita)

```text
osvc --presets ./my_year_presets.toml --year 2025
OSVC_PRESETS_PATH=./my_year_presets.toml osvc --year 2025
~/.config/osvc-kalkulacka/year_presets.toml
```
