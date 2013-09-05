import sublime_plugin

class HooksListener(sublime_plugin.EventListener):
    def get_hooks(self, view, hook):
        # Retrieve the current settings
        view_settings = view.settings()

        # Collect all levels of hooks into a list
        hooks = []
        hooks += view_settings.get(hook + '_user', [])
        hooks += view_settings.get(hook + '_project', [])
        hooks += view_settings.get(hook + '_language', [])

        # Return the collection of hooks
        return hooks

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
        print self.get_hooks(view, 'on_post_save')
        pass

    def on_activated(self, view):
        pass

    def on_deactivated(self, view):
        pass
