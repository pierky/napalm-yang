
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

class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/default-route-distance/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to the default route distance
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__external_route_distance','__internal_route_distance',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__external_route_distance = None
    self.__internal_route_distance = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'global', u'default-route-distance', u'state']

  def _initialized_external_route_distance(self):
    return self.__external_route_distance is not None

  def _get_external_route_distance(self):
    """
    Getter method for external_route_distance, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/default_route_distance/state/external_route_distance (uint8)

    YANG Description: Administrative distance for routes learned from external
BGP (eBGP).
    """
    if self.__external_route_distance is None:
        self.__external_route_distance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="external-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    return self.__external_route_distance
      
  def _set_external_route_distance(self, v, load=False):
    """
    Setter method for external_route_distance, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/default_route_distance/state/external_route_distance (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_external_route_distance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_external_route_distance() directly.

    YANG Description: Administrative distance for routes learned from external
BGP (eBGP).
    """
    if self.__external_route_distance is None:
        self.__external_route_distance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="external-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="external-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """external_route_distance must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="external-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__external_route_distance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_external_route_distance(self):
    self.__external_route_distance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="external-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _initialized_internal_route_distance(self):
    return self.__internal_route_distance is not None

  def _get_internal_route_distance(self):
    """
    Getter method for internal_route_distance, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/default_route_distance/state/internal_route_distance (uint8)

    YANG Description: Administrative distance for routes learned from internal
BGP (iBGP).
    """
    if self.__internal_route_distance is None:
        self.__internal_route_distance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="internal-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    return self.__internal_route_distance
      
  def _set_internal_route_distance(self, v, load=False):
    """
    Setter method for internal_route_distance, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/default_route_distance/state/internal_route_distance (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_internal_route_distance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_internal_route_distance() directly.

    YANG Description: Administrative distance for routes learned from internal
BGP (iBGP).
    """
    if self.__internal_route_distance is None:
        self.__internal_route_distance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="internal-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="internal-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """internal_route_distance must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="internal-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__internal_route_distance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_internal_route_distance(self):
    self.__internal_route_distance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="internal-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)

  external_route_distance = __builtin__.property(_get_external_route_distance)
  internal_route_distance = __builtin__.property(_get_internal_route_distance)


  _pyangbind_elements = {'external_route_distance': external_route_distance, 'internal_route_distance': internal_route_distance, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/default-route-distance/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to the default route distance
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__external_route_distance','__internal_route_distance',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__external_route_distance = None
    self.__internal_route_distance = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'global', u'default-route-distance', u'state']

  def _initialized_external_route_distance(self):
    return self.__external_route_distance is not None

  def _get_external_route_distance(self):
    """
    Getter method for external_route_distance, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/default_route_distance/state/external_route_distance (uint8)

    YANG Description: Administrative distance for routes learned from external
BGP (eBGP).
    """
    if self.__external_route_distance is None:
        self.__external_route_distance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="external-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    return self.__external_route_distance
      
  def _set_external_route_distance(self, v, load=False):
    """
    Setter method for external_route_distance, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/default_route_distance/state/external_route_distance (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_external_route_distance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_external_route_distance() directly.

    YANG Description: Administrative distance for routes learned from external
BGP (eBGP).
    """
    if self.__external_route_distance is None:
        self.__external_route_distance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="external-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="external-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """external_route_distance must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="external-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__external_route_distance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_external_route_distance(self):
    self.__external_route_distance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="external-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _initialized_internal_route_distance(self):
    return self.__internal_route_distance is not None

  def _get_internal_route_distance(self):
    """
    Getter method for internal_route_distance, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/default_route_distance/state/internal_route_distance (uint8)

    YANG Description: Administrative distance for routes learned from internal
BGP (iBGP).
    """
    if self.__internal_route_distance is None:
        self.__internal_route_distance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="internal-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    return self.__internal_route_distance
      
  def _set_internal_route_distance(self, v, load=False):
    """
    Setter method for internal_route_distance, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/default_route_distance/state/internal_route_distance (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_internal_route_distance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_internal_route_distance() directly.

    YANG Description: Administrative distance for routes learned from internal
BGP (iBGP).
    """
    if self.__internal_route_distance is None:
        self.__internal_route_distance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="internal-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="internal-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """internal_route_distance must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="internal-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__internal_route_distance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_internal_route_distance(self):
    self.__internal_route_distance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="internal-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)

  external_route_distance = __builtin__.property(_get_external_route_distance)
  internal_route_distance = __builtin__.property(_get_internal_route_distance)


  _pyangbind_elements = {'external_route_distance': external_route_distance, 'internal_route_distance': internal_route_distance, }


