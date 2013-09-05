import sublime_plugin

class HooksListener(sublime_plugin.EventListener):
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
        pass

    def on_activated(self, view):
        pass

    def on_deactivated(self, view):
        pass
