# sublime-hooks

Run [Sublime][subl] commands on common event hooks (e.g. `on_new`, `on_post_save`).

[subl]: http://www.sublimetext.com/

This was designed to give event level bindings to other [Sublime][subl] plugins.

My use case was to make a [request][] (via [sublime-request][request] to a server when a save occurs. The result was:

```js
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

## Getting started
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

A hook can be added at the `User`, `Project`, or `Language` level. We will add a `User` level hook.

To edit `User` settings, open the command pallete, and select "Preferences: Settings - User".

In the opened preferences, create a new key/value pair for `on_post_save_user` with the following:

```js
"on_post_save_user": [
  {
    "command": "select_all"
  }
]
```

Then, save twice (once to save settings, another to trigger the plugin).

At this step, all text will be selected, demonstrating the hook and command were run.

Examples of user, project, and language hooks can be [found below][examples].

[examples]: #examples

## Documentation
Hooks are stored in the `User`, `Project`, or `Language` settings. Each of these expects a list of dictionaries. Each of those dictionaries satisfies the following:

- `command` (required), Command for Sublime to run via `run_command` at the listed `scope`.
- `args` (optional), Dictionary of arguments to be passed to . Comparable to `args` in "Key Bindings".
- `scope` (optional), String indicating where to run `command`. By default, commands are run in the `view`. Other options are `window` and `app` which run at the `window` and `sublime` levels respectively.

```js
"on_post_save_user": [
  {
    // Runs `request` command
    "command": "request",

    // Invokes `request` with `open_args=["http://...:7060/"]`
    "args": {
      "open_args": ["http://localhost:7060/"]
    },

    // Runs `request` via `window.run_command`
    "scope": "window"
  }
]
```

### Accessing settings
`User` settings are accessed via "Preferences: Settings - User" in the command pallete.

`Project` settings are accessed via "Project -> Edit Project" from the menu bar. **You must be in a saved project for this option to be accessible.**

`Language` settings are accessed via "Preferences -> Settings - More -> Syntax Specific - User". This will open settings specifically for the language in the open file.

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
### User
User settings should be defined at the top level in your user's `.sublime-settings`. This can be accessed either via the `Preferences: Settings - User` command palette or `Preferences -> Settings - User` in the menu.

```js
// Inside Packages/User/Preferences.sublime-settings
{
  "ignored_packages": [
  // ...
  ],
  "on_post_save_user": [
    {
      "command": "select_all"
    }
  ]
}
```

### Project
Project settings should be defined under a `settings` in your current `.sublime-project`. This can be accessed either via the `Project: Edit` command palette or `Project -> Edit` in the menu.

```js
// Inside my-project.sublime-project
{
  "folders": [
  // ...
  ],
  "settings": {
    "on_post_save_project": [
      {
        "command": "select_all"
      }
    ]
  }
}
```

### Language
Language settings should be defined at the top level in your language's `.sublime-settings`. This can be accessed via `Preferences -> Settings - More -> Syntax Specific - User` in the menu.

```js
// Inside my-language.sublime-settings
{
  "extensions": [
  // ...
  ],
  "on_post_save_language": [
    {
      "command": "select_all"
    }
  ]
}
```

## Donating
Support this project and [others by twolfson][gittip] via [gittip][].

[![Support via Gittip][gittip-badge]][gittip]

[gittip-badge]: https://rawgithub.com/twolfson/gittip-badge/master/dist/gittip.png
[gittip]: https://www.gittip.com/twolfson/

## Unlicense
As of Sep 04 2013, Todd Wolfson has released this repository and its contents to the public domain.

It has been released under the [UNLICENSE][].

[UNLICENSE]: UNLICENSE
