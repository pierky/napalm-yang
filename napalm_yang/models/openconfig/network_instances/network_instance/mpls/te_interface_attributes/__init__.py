
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
  unicode = str
elif six.PY2:
  import __builtin__

from . import interface
class te_interface_attributes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/te-interface-attributes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: traffic engineering attributes specific
for interfaces
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interface',)

  _yang_name = 'te-interface-attributes'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interface = None

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'mpls', u'te-interface-attributes']

  def _initialized_interface(self):
    return self.__interface is not None

  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface (list)

    YANG Description: List of TE interfaces
    """
    if self.__interface is None:
        self.__interface = YANGDynClass(base=YANGListType("interface_id",interface.interface, yang_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-id', extensions=None), is_container='list', yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description: List of TE interfaces
    """
    if self.__interface is None:
        self.__interface = YANGDynClass(base=YANGListType("interface_id",interface.interface, yang_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-id', extensions=None), is_container='list', yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("interface_id",interface.interface, yang_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-id', extensions=None), is_container='list', yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("interface_id",interface.interface, yang_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-id', extensions=None), is_container='list', yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=YANGListType("interface_id",interface.interface, yang_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-id', extensions=None), is_container='list', yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  interface = __builtin__.property(_get_interface, _set_interface)


  _pyangbind_elements = {'interface': interface, }


from . import interface
class te_interface_attributes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/te-interface-attributes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: traffic engineering attributes specific
for interfaces
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interface',)

  _yang_name = 'te-interface-attributes'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interface = None

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'mpls', u'te-interface-attributes']

  def _initialized_interface(self):
    return self.__interface is not None

  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface (list)

    YANG Description: List of TE interfaces
    """
    if self.__interface is None:
        self.__interface = YANGDynClass(base=YANGListType("interface_id",interface.interface, yang_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-id', extensions=None), is_container='list', yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description: List of TE interfaces
    """
    if self.__interface is None:
        self.__interface = YANGDynClass(base=YANGListType("interface_id",interface.interface, yang_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-id', extensions=None), is_container='list', yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("interface_id",interface.interface, yang_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-id', extensions=None), is_container='list', yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("interface_id",interface.interface, yang_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-id', extensions=None), is_container='list', yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=YANGListType("interface_id",interface.interface, yang_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-id', extensions=None), is_container='list', yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  interface = __builtin__.property(_get_interface, _set_interface)


  _pyangbind_elements = {'interface': interface, }


