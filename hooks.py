import sublime
import sublime_plugin

class HooksListener(sublime_plugin.EventListener):
    def get_hooks(self, view, namespace):
        # Retrieve the current settings
        view_settings = view.settings()

        # Collect all levels of cmds into a list
        cmds = []
        cmds += view_settings.get(namespace + '_user', [])
        cmds += view_settings.get(namespace + '_project', [])
        cmds += view_settings.get(namespace + '_language', [])

        # Return the collection of cmds
        return cmds

    def run_hooks(self, view, namespace):
        # Resolve the commands
        cmds = self.get_hooks(view, namespace)

        # For each command, run it
        for cmd in cmds:
            self.run_cmd(view, cmd)

    def run_cmd(self, view, cmd):
        # By default, run the command on the view
        scope = view

        # If there is a scope key
        scope_key = cmd.get('scope', None)
        if scope_key:
            # If it is app, move to app
            if scope_key == 'app':
                scope = sublime
            elif scope_key == 'window':
            # Otherwise if it is window, move to window
                scope = view.window()
            else:
            # Otherwise, complain
                raise Exception('Scope key "%s" for `hooks` plugin was not recognized.')

        # Run the command in its scope
        scope.run_command(cmd['command'], cmd['args'])

# Set up all hooks
ST_HOOKS = [
    # ST2 / ST3 hooks
    'on_new',
    'on_clone',
    'on_load',
    'on_close',
    'on_pre_save',
    'on_post_save',
    # 'on_modified',  # Disabled for potential overrun
    # 'on_selection_modified',  # Disabled for potential overrun
    'on_activated',
    'on_deactivated',
    # 'on_query_context',  # Disabled for potential overrun

    # ST3 hooks
    'on_new_async',
    'on_clone_async',
    'on_load_async',
    'on_pre_close',
    'on_pre_save_async',
    'on_post_save_async',
    # 'on_modified_async',  # Disabled for potential overrun
    # 'on_selection_modified_async',  # Disabled for potential overrun
    'on_activated_async',
    'on_deactivated_async',
    # 'on_text_command',  # Disabled for potential overrun
    # 'on_window_command',  # Disabled for potential overrun
    # 'post_text_command',  # Disabled for potential overrun
    # 'post_window_command',  # Disabled for potential overrun
]

# For each hook, set it up
for namespace in ST_HOOKS:
    ns = namespace
    def run_hook_namespace(self, view):
        print 'hii', ns
        self.run_hooks(view, ns)
    setattr(HooksListener, ns, run_hook_namespace)

# print HooksListener.__dict__
