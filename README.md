xplr-yml2lua
============

This tool tries to convert yaml files to lua, aimed at easing the [xplr](https://github.com/sayanarijit/xplr) YAML -> Lua migration.

**Important:** This tool will not generate 100% correct lua code. You will need to mix and match the flat nd nested outputs and fix syntax issues manually.

Install
-------

#### You will need Python ~ 3.8 and [poetry](https://python-poetry.org/docs/#installation)

```bash
git clone https://github.com/sayanarijit/xplr-yml2lua

cd xplr-yml2lua

poetry install --no-dev

poetry run xplr-yml2lua --help
```

**Note:** It may run on other versions of Python, but I haven't tested it.

Examples
--------

#### Nested

```bash
cat ~/.config/xplr/config.yml | poetry run xplr-yml2lua
```


#### Flat

```bash
cat ~/.config/xplr/config.yml | poetry run xplr-yml2lua --flat
```
