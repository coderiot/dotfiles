#!/usr/bin/env python
# encoding: utf-8

import os.path

from libqtile.config import Key, Screen, Group, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget

mod = "mod1"


def app_or_group(group, app):
    """ Go to specified group if it exists. Otherwise, run the specified app.
        When used in conjunction with dgroups to auto-assign apps to specific
        groups, this can be used as a way to go to an app if it is already
        running. """
    def f(qtile):
        try:
            qtile.groupMap[group].cmd_toscreen()
        except KeyError:
            qtile.cmd_spawn(app)
    return f

keys = [
    # Switch between windows in current stack pane
    Key(
        [mod], "k",
        lazy.layout.down()
    ),
    Key(
        [mod], "j",
        lazy.layout.up()
    ),
    Key(
        [mod], "h",
        lazy.layout.previous()
    ),
    Key(
        [mod], "l",
        lazy.layout.next()
    ),
    Key(
        [mod], "f",
        lazy.window.toggle_floating()
    ),

    # Move windows up or down in current stack
    Key(
        [mod, "control"], "k",
        lazy.layout.shuffle_down()
    ),
    Key(
        [mod, "control"], "j",
        lazy.layout.shuffle_up()
    ),

    # Switch window focus to other pane(s) of stack
    Key(
        [mod], "space",
        lazy.layout.next()
    ),

    # Swap panes of split stack
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate()
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    Key([mod], "Return", lazy.spawn("xfce4-terminal \
                                    --hide-menubar \
                                    --hide-borders \
                                    --hide-toolbars")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab",    lazy.nextlayout()),
    Key([mod], "w",      lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod], "r", lazy.spawn("dmenu_run -fn 'DejaVu Sans Mono Book-14' -nb '#000000' -nf '#87FF03' -sb '#87FF03' -sf '#000000'")),

    # start specific apps
    Key(["mod4"], "o", lazy.spawn("opera")),
    Key(["mod4"], "f", lazy.spawn("firefox")),
    Key(["mod4"], "l", lazy.spawn("liferea")),
    Key([mod], "n", lazy.function(app_or_group("web", "firefox"))),
    Key([mod], "g", lazy.function(app_or_group("music", "gmusicbrowser"))),
    Key([mod], "c", lazy.function(app_or_group("chat", "pidgin"))),
    Key([mod], "m", lazy.function(app_or_group("mail", "thunderbird"))),
]

groups = [
    Group("a"),
    Group("s"),
    Group("d"),
    Group("i"),
    Group("o"),
    Group("p"),
]
for i in groups:
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], i.name, lazy.group[i.name].toscreen())
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
    )


groups.extend([
    Group('music', layout='max', persist=False,
          matches=[Match(wm_class=['Parole'], title=['gmusicbrowser'])]),
    Group('web', layout='max',
          matches=[Match(wm_class=['Firefox',
                                   'google-chrome',
                                   'Google-chrome',
                                   "Opera"],
                         title=["Liferea"])]),
    Group('chat', layout='pidgin', persist=False,
          matches=[Match(wm_class=['Pidgin'], role=['Buddy List'])]),
    Group('mail', layout='max', persist=False,
          matches=[Match(wm_class=['Thunderbird'])]),
])

dgroups_key_binder = None
dgroups_app_rules = []

border = {'border_normal': '#404040',
          'border_focus': "#9459FF",
          'border_width': 2,
         }

layouts = [
    layout.Max(**border),
    layout.Stack(stacks=2, **border),
    layout.Tile(**border),
    layout.RatioTile(**border),
    layout.MonadTall(**border),
    layout.Slice('right', 256,
                 name='pidgin',
                role='buddy_list',
                 fallback=layout.Stack(stacks=1)),
]

volume_icons = os.path.expanduser("~/.config/qtile/volume-icons")

screens = [
    Screen(
        bottom=bar.Bar(
                       [
                        widget.GroupBox(
                                        borderwidth=2,
                                        fontsize=12,
                                        font="DejaVu Sans",
                                        this_current_screen_border="#87FF03",
                                        active="#F7208B",
                                        ),
                        widget.Spacer(),
                        widget.CurrentLayout(foreground="#404040"),
                       ],
                       30,
                       ),
        top=bar.Bar(
                    [
                        widget.Prompt(foreground="#87FF03"),
                        widget.WindowName(font="Droid Sans",
                                          foreground="#CCCCC6"),
                        widget.Systray(),
                        widget.Volume(fontsize=20,
                                      theme_path=volume_icons
                                      ),
                        widget.Clock('%a, %d %b %Y %H:%M:%S',
                                     font="Droid Sans",
                                     fontsize=15,
                                     foreground="#606060"
                                     ),
                    ],
                    25,
                ),
    ),
]

main = None

follow_mouse_focus = True
cursor_warp = False

floating_layout = layout.Floating(float_rules=[dict(wmclass='gnome-keyring-prompt-3')], **border)
mouse = ()

auto_fullscreen = True
widget_defaults = {}
