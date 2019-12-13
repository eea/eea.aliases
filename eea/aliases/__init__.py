""" EEA Aliases
"""
import logging
from zope.interface import Interface
from plone.app.upgrade.utils import alias_module
logger = logging.getLogger("eea.aliases")

try:
    from App.interfaces import IPersistentExtra
except ImportError:
    class IPersistentExtra(Interface):
        pass
    alias_module('App.interfaces.IPersistentExtra', IPersistentExtra)
    logger.warn("Alias registered for missing: App.interfaces.IPersistentExtra")


try:
    from App.interfaces import IUndoSupport
except ImportError:
    class IUndoSupport(Interface):
        pass
    alias_module('App.interfaces.IUndoSupport', IUndoSupport)
    logger.warn("Alias registered for missing: App.interfaces.IUndoSupport")


try:
    from webdav.interfaces import IFTPAccess  # noqa
except ImportError:
    class IFTPAccess(Interface):
        pass
    alias_module('webdav.interfaces.IFTPAccess', IFTPAccess)
    logger.warn("Alias registered for missing: webdav.interfaces.IFTPAccess")


try:
    from webdav.EtagSupport import EtagBaseInterface  # noqa
except ImportError:
    class EtagBaseInterface(Interface):
        pass
    alias_module('webdav.EtagSupport.EtagBaseInterface', EtagBaseInterface)
    logger.warn("Alias registered for missing: webdav.EtagSupport.EtagBaseInterface")


try:
    from Products.ResourceRegistries.interfaces.settings import IResourceRegistriesSettings  # noqa
except ImportError:
    class IResourceRegistriesSettings(Interface):
        pass
    alias_module('Products.ResourceRegistries.interfaces.settings.IResourceRegistriesSettings', IResourceRegistriesSettings)
    logger.warn("Alias registered for missing: Products.ResourceRegistries.interfaces.settings.IResourceRegistriesSettings")


try:
    from Products.RedirectionTool.RedirectionTool import RedirectionTool
except ImportError:
    class RedirectionTool(object):
        pass
    alias_module('Products.RedirectionTool.RedirectionTool.RedirectionTool', RedirectionTool)
    logger.warn("Alias registered for missing: Products.RedirectionTool.RedirectionTool.RedirectionTool")


try:
    from plone.dexterity.schema import SchemaModuleFactory
    from zope.component.hooks import getSiteManager
    sm = getSiteManager()
    sm.registerUtility(factory=SchemaModuleFactory, name="plone.dexterity.schema.generated")
except Exception as err:
    logger.exception(err)
else:
    logger.warn("Manually register plone.dexterity.schema.generated utility")

#
# Custom renames for zodbupdate
#
rename_dict = {

#    'mypackage.mymodule ClassName':'otherpackage.othermodule OtherClass'

}
