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

    def on_new(self, view):
        pass

    def on_clone(self, view):
        pass

    def on_load(self, view):
        pass

    def on_close(self, view):
        pass

    def on_pre_save(self, view):
        pass

    def on_post_save(self, view):
        self.run_hooks(view, 'on_post_save')
        pass

    def on_activated(self, view):
        pass

    def on_deactivated(self, view):
        pass
