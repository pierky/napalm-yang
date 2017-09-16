
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

class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/global/graceful-restart/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to OSPFv2 graceful
restart
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__enabled','__helper_only',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled = None
    self.__helper_only = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'global', u'graceful-restart', u'config']

  def _initialized_enabled(self):
    return self.__enabled is not None

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/graceful_restart/config/enabled (boolean)

    YANG Description: When the value of this leaf is set to true, graceful restart
is enabled on the local system. In this case, the system will
use Grace-LSAs to signal that it is restarting to its
neighbors.
    """
    if self.__enabled is None:
        self.__enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/graceful_restart/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: When the value of this leaf is set to true, graceful restart
is enabled on the local system. In this case, the system will
use Grace-LSAs to signal that it is restarting to its
neighbors.
    """
    if self.__enabled is None:
        self.__enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _initialized_helper_only(self):
    return self.__helper_only is not None

  def _get_helper_only(self):
    """
    Getter method for helper_only, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/graceful_restart/config/helper_only (boolean)

    YANG Description: Operate graceful-restart only in helper mode. When this leaf
is set to true, the local system does not use Grace-LSAs to
indicate that it is restarting, but will accept Grace-LSAs
from remote systems, and suppress withdrawl of adjacencies
of the system for the grace period specified
    """
    if self.__helper_only is None:
        self.__helper_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    return self.__helper_only
      
  def _set_helper_only(self, v, load=False):
    """
    Setter method for helper_only, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/graceful_restart/config/helper_only (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_helper_only is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_helper_only() directly.

    YANG Description: Operate graceful-restart only in helper mode. When this leaf
is set to true, the local system does not use Grace-LSAs to
indicate that it is restarting, but will accept Grace-LSAs
from remote systems, and suppress withdrawl of adjacencies
of the system for the grace period specified
    """
    if self.__helper_only is None:
        self.__helper_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """helper_only must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__helper_only = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_helper_only(self):
    self.__helper_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  enabled = __builtin__.property(_get_enabled, _set_enabled)
  helper_only = __builtin__.property(_get_helper_only, _set_helper_only)


  _pyangbind_elements = {'enabled': enabled, 'helper_only': helper_only, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/global/graceful-restart/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to OSPFv2 graceful
restart
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__enabled','__helper_only',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled = None
    self.__helper_only = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'global', u'graceful-restart', u'config']

  def _initialized_enabled(self):
    return self.__enabled is not None

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/graceful_restart/config/enabled (boolean)

    YANG Description: When the value of this leaf is set to true, graceful restart
is enabled on the local system. In this case, the system will
use Grace-LSAs to signal that it is restarting to its
neighbors.
    """
    if self.__enabled is None:
        self.__enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/graceful_restart/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: When the value of this leaf is set to true, graceful restart
is enabled on the local system. In this case, the system will
use Grace-LSAs to signal that it is restarting to its
neighbors.
    """
    if self.__enabled is None:
        self.__enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _initialized_helper_only(self):
    return self.__helper_only is not None

  def _get_helper_only(self):
    """
    Getter method for helper_only, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/graceful_restart/config/helper_only (boolean)

    YANG Description: Operate graceful-restart only in helper mode. When this leaf
is set to true, the local system does not use Grace-LSAs to
indicate that it is restarting, but will accept Grace-LSAs
from remote systems, and suppress withdrawl of adjacencies
of the system for the grace period specified
    """
    if self.__helper_only is None:
        self.__helper_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    return self.__helper_only
      
  def _set_helper_only(self, v, load=False):
    """
    Setter method for helper_only, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/graceful_restart/config/helper_only (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_helper_only is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_helper_only() directly.

    YANG Description: Operate graceful-restart only in helper mode. When this leaf
is set to true, the local system does not use Grace-LSAs to
indicate that it is restarting, but will accept Grace-LSAs
from remote systems, and suppress withdrawl of adjacencies
of the system for the grace period specified
    """
    if self.__helper_only is None:
        self.__helper_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """helper_only must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__helper_only = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_helper_only(self):
    self.__helper_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  enabled = __builtin__.property(_get_enabled, _set_enabled)
  helper_only = __builtin__.property(_get_helper_only, _set_helper_only)


  _pyangbind_elements = {'enabled': enabled, 'helper_only': helper_only, }


