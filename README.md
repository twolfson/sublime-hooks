# sublime-hooks

Run [Sublime][subl] commands on common event hooks (e.g. `on_new`, `on_post_save`).

[subl]: http://www.sublimetext.com/

This was designed to give event level bindings to other [Sublime][subl] plugins.

My common use case is making a [request][] (via [sublime-request][request] to a server when a save occurs. My User settings contain the following:

```json
"on_post_save_user": [
  {
    "command": "request",
    "args": {
      "open_args": ["http://localhost:7060/"]
    },
    "scope": "window"
  }
]
```

[request]: http://github.com/twolfson/sublime-request

### Installation
This package is available under `hooks` inside of [Package Control][pkg-control], a [Sublime Text][subl] plugin that allows for easy management of other plugins.

[pkg-control]: http://wbond.net/sublime_packages/package_control

If you prefer the manual route, you can install the script via the following command in the Sublime Text terminal (``ctrl+` ``) which utilizes `git clone`.

```python
import os; path=sublime.packages_path(); (os.makedirs(path) if not os.path.exists(path) else None); window.run_command('exec', {'cmd': ['git', 'clone', 'https://github.com/twolfson/sublime-hooks', 'hooks'], 'working_dir': path})
```

Packages can be uninstalled via "Package Control: Remove Package" via the command pallete, `ctrl+shift+p` on Windows/Linux, `command+shift+p` on Mac.

### Creating a new hook
_(Coming soon)_

## Documentation
_(Coming soon)_

## Examples
_(Coming soon)_

## Donating
Support this project and [others by twolfson][gittip] via [gittip][].

[![Support via Gittip][gittip-badge]][gittip]

[gittip-badge]: https://rawgithub.com/twolfson/gittip-badge/master/dist/gittip.png
[gittip]: https://www.gittip.com/twolfson/

## Contributing
In lieu of a formal styleguide, take care to maintain the existing coding style. Add unit tests for any new or changed functionality. Lint via [grunt](https://github.com/gruntjs/grunt) and test via `npm test`.

## Unlicense
As of Sep 04 2013, Todd Wolfson has released this repository and its contents to the public domain.

It has been released under the [UNLICENSE][].

[UNLICENSE]: UNLICENSE

