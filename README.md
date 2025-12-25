# OSVČ kalkulačka (DPFO + ZP/SP)

## Instalace

```bash
pipx install osvc-kalkulacka
```

```bash
uv tool install osvc-kalkulacka
```

## Rychlý start

```bash
osvc init
osvc --year 2025 --income 800000 --child-months-by-order 12
```

Alternativně explicitně:

```bash
osvc calc --year 2025 --income 800000 --child-months-by-order 12
```

## Konfigurace

Zobrazení cest:

```bash
osvc config path
```

Očekávané soubory:

```text
${USER_DIR}/year_presets.toml
${USER_DIR}/year_defaults.override.toml
```

## Precedence

Presets:

```text
--presets
OSVC_PRESETS_PATH
${USER_DIR}/year_presets.toml
```

Defaults:

```text
--defaults
OSVC_DEFAULTS_PATH
${USER_DIR}/year_defaults.override.toml (pokud existuje)
vestavěné year_defaults.toml
```

## Export vestavěných defaults

```bash
osvc defaults dump --output year_defaults.toml
```
