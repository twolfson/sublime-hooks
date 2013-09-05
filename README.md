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
For this exercise, we will be creating a binding that selects all text after a save occurs.

A hook can be added at the `User`, `Project`, or `Language` level. For this example, we will add a `User` level hook.

To edit `User` settings, open the command pallete, and select "Preferences: Settings - User".

In the opened preferences, create a new key/value pair for `on_post_save_user` with the following:

```json
"on_post_save_user": [
  {
    "command": "select_all"
  }
],
```

Then, select another file and save it. The plugin will automatically select all text.

## Documentation
### Namespacing
Hooks are required to be namespaced at the `User`, `Project`, or `Language` level. The key will be the `event_name` followed by its `_level`.

The namespaces are `_user`, `_project`, and `_language`.

For demonstration:

- An `on_new` hook at the `Project` level will be `on_new_project`
- An `on_load` at the `Language` level will be `on_load_language`

### Events
For both Sublime Text 2 and 3, you will have access to the following events:

- `on_new`
- `on_clone`
- `on_load`
- `on_close`
- `on_pre_save`
- `on_post_save`
- `on_activated`
- `on_deactivated`

For Sublime Text 3, you gain access to:

- `on_new_async`
- `on_clone_async`
- `on_load_async`
- `on_pre_close`
- `on_pre_save_async`
- `on_post_save_async`
- `on_activated_async`
- `on_deactivated_async`

Documentation on each hook can be found in the Sublime Text documentation:

Sublime Text 2 - http://www.sublimetext.com/docs/2/api_reference.html#sublime_plugin.EventListener

Sublime Text 3 - http://www.sublimetext.com/docs/3/api_reference.html#sublime_plugin.EventListener

The events not on these lists were excluded due to potential performance issues (e.g. `on_modified`, `on_text_command`).

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

