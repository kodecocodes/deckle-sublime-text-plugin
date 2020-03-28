import os
import sys
import subprocess
import sublime_plugin

# A Sublime Text Plugin that opens the currently open file in
# the RayWenderlich.com Deckle Markdown Preview App.
# Created by 01-02-2018 eric@issfl.com

class DeckleCommand(sublime_plugin.WindowCommand):
    def run(self):
        filename = self.window.active_view().file_name()
        if filename is None:
            return

        proc_env = os.environ.copy()
        encoding = sys.getfilesystemencoding()
        for k, v in proc_env.items():
            proc_env[k] = os.path.expandvars(v).encode(encoding)

        print("Opening Deckle with " + filename)
        try:
            subprocess.check_call(
                ['open', '-a', "Deckle", filename],
                env=proc_env
            )
        except:
            sublime.error_message('Error running: ' + app + ', check the console')
            pass

    def is_enabled(self):
        return True
