
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

from . import dynamic_neighbor_prefix
class dynamic_neighbor_prefixes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/dynamic-neighbor-prefixes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A list of IP prefixes from which the system should:
 - Accept connections to the BGP daemon
 - Dynamically configure a BGP neighbor corresponding to the
   source address of the remote system, using the parameters
   of the specified peer-group.
For such neighbors, an entry within the neighbor list should
be created, indicating that the peer was dynamically
configured, and referencing the peer-group from which the
configuration was derived.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__dynamic_neighbor_prefix',)

  _yang_name = 'dynamic-neighbor-prefixes'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__dynamic_neighbor_prefix = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'global', u'dynamic-neighbor-prefixes']

  def _initialized_dynamic_neighbor_prefix(self):
    return self.__dynamic_neighbor_prefix is not None

  def _get_dynamic_neighbor_prefix(self):
    """
    Getter method for dynamic_neighbor_prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/dynamic_neighbor_prefixes/dynamic_neighbor_prefix (list)

    YANG Description: An individual prefix from which dynamic neighbor
connections are allowed.
    """
    if self.__dynamic_neighbor_prefix is None:
        self.__dynamic_neighbor_prefix = YANGDynClass(base=YANGListType("prefix",dynamic_neighbor_prefix.dynamic_neighbor_prefix, yang_name="dynamic-neighbor-prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="dynamic-neighbor-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    return self.__dynamic_neighbor_prefix
      
  def _set_dynamic_neighbor_prefix(self, v, load=False):
    """
    Setter method for dynamic_neighbor_prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/dynamic_neighbor_prefixes/dynamic_neighbor_prefix (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dynamic_neighbor_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dynamic_neighbor_prefix() directly.

    YANG Description: An individual prefix from which dynamic neighbor
connections are allowed.
    """
    if self.__dynamic_neighbor_prefix is None:
        self.__dynamic_neighbor_prefix = YANGDynClass(base=YANGListType("prefix",dynamic_neighbor_prefix.dynamic_neighbor_prefix, yang_name="dynamic-neighbor-prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="dynamic-neighbor-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("prefix",dynamic_neighbor_prefix.dynamic_neighbor_prefix, yang_name="dynamic-neighbor-prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="dynamic-neighbor-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dynamic_neighbor_prefix must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("prefix",dynamic_neighbor_prefix.dynamic_neighbor_prefix, yang_name="dynamic-neighbor-prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="dynamic-neighbor-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__dynamic_neighbor_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dynamic_neighbor_prefix(self):
    self.__dynamic_neighbor_prefix = YANGDynClass(base=YANGListType("prefix",dynamic_neighbor_prefix.dynamic_neighbor_prefix, yang_name="dynamic-neighbor-prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="dynamic-neighbor-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  dynamic_neighbor_prefix = __builtin__.property(_get_dynamic_neighbor_prefix, _set_dynamic_neighbor_prefix)


  _pyangbind_elements = {'dynamic_neighbor_prefix': dynamic_neighbor_prefix, }


from . import dynamic_neighbor_prefix
class dynamic_neighbor_prefixes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/dynamic-neighbor-prefixes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A list of IP prefixes from which the system should:
 - Accept connections to the BGP daemon
 - Dynamically configure a BGP neighbor corresponding to the
   source address of the remote system, using the parameters
   of the specified peer-group.
For such neighbors, an entry within the neighbor list should
be created, indicating that the peer was dynamically
configured, and referencing the peer-group from which the
configuration was derived.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__dynamic_neighbor_prefix',)

  _yang_name = 'dynamic-neighbor-prefixes'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__dynamic_neighbor_prefix = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'global', u'dynamic-neighbor-prefixes']

  def _initialized_dynamic_neighbor_prefix(self):
    return self.__dynamic_neighbor_prefix is not None

  def _get_dynamic_neighbor_prefix(self):
    """
    Getter method for dynamic_neighbor_prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/dynamic_neighbor_prefixes/dynamic_neighbor_prefix (list)

    YANG Description: An individual prefix from which dynamic neighbor
connections are allowed.
    """
    if self.__dynamic_neighbor_prefix is None:
        self.__dynamic_neighbor_prefix = YANGDynClass(base=YANGListType("prefix",dynamic_neighbor_prefix.dynamic_neighbor_prefix, yang_name="dynamic-neighbor-prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="dynamic-neighbor-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    return self.__dynamic_neighbor_prefix
      
  def _set_dynamic_neighbor_prefix(self, v, load=False):
    """
    Setter method for dynamic_neighbor_prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/dynamic_neighbor_prefixes/dynamic_neighbor_prefix (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dynamic_neighbor_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dynamic_neighbor_prefix() directly.

    YANG Description: An individual prefix from which dynamic neighbor
connections are allowed.
    """
    if self.__dynamic_neighbor_prefix is None:
        self.__dynamic_neighbor_prefix = YANGDynClass(base=YANGListType("prefix",dynamic_neighbor_prefix.dynamic_neighbor_prefix, yang_name="dynamic-neighbor-prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="dynamic-neighbor-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("prefix",dynamic_neighbor_prefix.dynamic_neighbor_prefix, yang_name="dynamic-neighbor-prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="dynamic-neighbor-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dynamic_neighbor_prefix must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("prefix",dynamic_neighbor_prefix.dynamic_neighbor_prefix, yang_name="dynamic-neighbor-prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="dynamic-neighbor-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__dynamic_neighbor_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dynamic_neighbor_prefix(self):
    self.__dynamic_neighbor_prefix = YANGDynClass(base=YANGListType("prefix",dynamic_neighbor_prefix.dynamic_neighbor_prefix, yang_name="dynamic-neighbor-prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="dynamic-neighbor-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  dynamic_neighbor_prefix = __builtin__.property(_get_dynamic_neighbor_prefix, _set_dynamic_neighbor_prefix)


  _pyangbind_elements = {'dynamic_neighbor_prefix': dynamic_neighbor_prefix, }


