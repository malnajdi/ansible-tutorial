# Make coding more python3-ish, this is required for contributions to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

# not only visible to ansible-doc, it also 'declares' the options the plugin requires and how to configure them.
DOCUMENTATION = '''
  callback: timer
  callback_type: aggregate
  requirements:
    - whitelist in configuration
  short_description: Adds time to play stats
  version_added: "2.0"
  description:
      - This callback just adds total play duration to the play stats.
  options:
    format_string:
      description: format of the string shown to user at play end
      ini:
        - section: callback_timer
          key: format_string
      env:
        - name: ANSIBLE_CALLBACK_TIMER_FORMAT
      default: "Playbook run took %s days, %s hours, %s minutes, %s seconds"
'''
from datetime import datetime

from ansible.plugins.callback import CallbackBase


class CallbackModule(CallbackBase):
    """
    This callback module tells you how long your plays ran for.
    """
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'namespace.collection_name.timer'

    # only needed if you ship it and don't want to enable by default
    CALLBACK_NEEDS_WHITELIST = False

    def __init__(self):

        # make sure the expected objects are present, calling the base's __init__
        super(CallbackModule, self).__init__()

        # start the timer when the plugin is loaded, the first play should start a few milliseconds after.
        self.start_time = datetime.now()

    def _days_hours_minutes_seconds(self, runtime):
        ''' internal helper method for this callback '''
        minutes = (runtime.seconds // 60) % 60
        r_seconds = runtime.seconds - (minutes * 60)
        return runtime.days, runtime.seconds // 3600, minutes, r_seconds

    # this is only event we care about for display, when the play shows its summary stats; the rest are ignored by the base class
    def v2_playbook_on_stats(self, stats):
        end_time = datetime.now()
        runtime = end_time - self.start_time

        # Shows the usage of a config option declared in the DOCUMENTATION variable. Ansible will have set it when it loads the plugin.
        # Also note the use of the display object to print to screen. This is available to all callbacks, and you should use this over printing yourself
        self._display.display(self._plugin_options['format_string'] % (self._days_hours_minutes_seconds(runtime)))