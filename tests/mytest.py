#!/usr/bin/env python3.4

from yapsy.PluginManager import PluginManager

# Build the manager
simplePluginManager = PluginManager()
# Tell it the default place(s) where to find plugins
simplePluginManager.setPluginPlaces(["../plugins"])
# Load all plugins
simplePluginManager.collectPlugins()

# Activate all loaded plugins
for pluginInfo in simplePluginManager.getAllPlugins():
   print ("1")
   simplePluginManager.activatePluginByName(pluginInfo.name)
   