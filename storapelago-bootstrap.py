#!/usr/bin/env python
## Not forcing python 3.4 right now

from yapsy.PluginManager import PluginManager

# Build the manager
simplePluginManager = PluginManager()
# Tell it the default place(s) where to find plugins
simplePluginManager.setPluginPlaces(["plugins"])
# Load all plugins
#print (simplePluginManager.locatePlugins ())
simplePluginManager.collectPlugins()

# Activate all loaded plugins

simplePluginManager.getAllPlugins()

for pluginInfo in simplePluginManager.getAllPlugins():
   simplePluginManager.activatePluginByName(pluginInfo.name)
   pluginInfo.plugin_object.print_name()
   print pluginInfo
   