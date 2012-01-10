import sublime_plugin

class OtherGroupCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.focus_group(
      (self.window.active_group() + 1) % self.window.num_groups())
