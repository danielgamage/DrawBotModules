# DrawBotModules
[DrawBot](http://www.drawbot.com/) modules I make / use
```python
from DrawBotModules import Color

fg = Color.hex('#face')
bg = Color.hex('223344')
```

## Color
### Color.hex(_string_)
The `Color.hex` interface parses hex strings into DrawBot-compatible RGBA floats. It supports several formats:

- `#rgb`
- `#rgba`
- `#rrggbb`
- `#rrggbbaa`

In all cases, the leading hashbang (`#`) is optional

The class then exposes the following properties:

#### `Color.r` _int_
#### `Color.g` _int_
#### `Color.b` _int_
#### `Color.a` _int_
Default: `1`
#### `Color.tuple` _tuple_
Default: `(Color.r, Color.g, Color.b, Color.a)`

With this, you can either manually insert `rgba` values or splat / spread the tuple into a DrawBot `fill`/`stroke` function:

```python
fg = Color.Hex('#002B36')
t = FormattedString()
t.fill(*fg.tuple)
```

