"""Skeleton defining the dtool plugin entry points."""

import os
from pkg_resources import iter_entry_points

import click
from click_plugins import with_plugins

import dtoolcore

from . import __version__


def pretty_version_text():
    """Return pretty version text listing all plugins."""
    modules = [ep.module_name for ep in iter_entry_points("dtool.cli")]
    packages = set([m.split(".")[0] for m in modules])
    version_lines = ["dtool, version {}".format(__version__)]
    version_lines.append("\nCore:")
    version_lines.append("dtoolcore, version {}".format(dtoolcore.__version__))
    version_lines.append("\nPlugins:")
    for p in packages:
        dyn_load_p = __import__(p)
        version_lines.append("{}, version {}".format(p,  dyn_load_p.__version__))
    return "\n".join(version_lines)

@with_plugins(iter_entry_points("dtool.cli"))
@click.group()
@click.version_option(message=pretty_version_text())
def dtool():
    """Tool to work with datasets."""
