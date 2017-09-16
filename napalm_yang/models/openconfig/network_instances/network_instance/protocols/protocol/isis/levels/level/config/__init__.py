
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS level based configuration.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__enabled','__level_number','__metric_style','__authentication_check',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__level_number = None
    self.__enabled = None
    self.__metric_style = None
    self.__authentication_check = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'config']

  def _initialized_enabled(self):
    return self.__enabled is not None

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/config/enabled (boolean)

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
    if self.__enabled is None:
        self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
    if self.__enabled is None:
        self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _initialized_level_number(self):
    return self.__level_number is not None

  def _get_level_number(self):
    """
    Getter method for level_number, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/config/level_number (oc-isis-types:level-number)

    YANG Description: ISIS level number (level-1, level-2).
    """
    if self.__level_number is None:
        self.__level_number = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..2']}), is_leaf=True, yang_name="level-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:level-number', is_config=True)
    return self.__level_number
      
  def _set_level_number(self, v, load=False):
    """
    Setter method for level_number, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/config/level_number (oc-isis-types:level-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_level_number is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_level_number() directly.

    YANG Description: ISIS level number (level-1, level-2).
    """
    if self.__level_number is None:
        self.__level_number = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..2']}), is_leaf=True, yang_name="level-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:level-number', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..2']}), is_leaf=True, yang_name="level-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:level-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """level_number must be of a type compatible with oc-isis-types:level-number""",
          'defined-type': "oc-isis-types:level-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..2']}), is_leaf=True, yang_name="level-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:level-number', is_config=True)""",
        })

    self.__level_number = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_level_number(self):
    self.__level_number = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..2']}), is_leaf=True, yang_name="level-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:level-number', is_config=True)


  def _initialized_metric_style(self):
    return self.__metric_style is not None

  def _get_metric_style(self):
    """
    Getter method for metric_style, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/config/metric_style (oc-isis-types:metric-style)

    YANG Description: ISIS metric style types(narrow, wide).
    """
    if self.__metric_style is None:
        self.__metric_style = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NARROW_METRIC': {}, u'WIDE_METRIC': {}},), is_leaf=True, yang_name="metric-style", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:metric-style', is_config=True)
    return self.__metric_style
      
  def _set_metric_style(self, v, load=False):
    """
    Setter method for metric_style, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/config/metric_style (oc-isis-types:metric-style)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric_style is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric_style() directly.

    YANG Description: ISIS metric style types(narrow, wide).
    """
    if self.__metric_style is None:
        self.__metric_style = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NARROW_METRIC': {}, u'WIDE_METRIC': {}},), is_leaf=True, yang_name="metric-style", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:metric-style', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NARROW_METRIC': {}, u'WIDE_METRIC': {}},), is_leaf=True, yang_name="metric-style", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:metric-style', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric_style must be of a type compatible with oc-isis-types:metric-style""",
          'defined-type': "oc-isis-types:metric-style",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NARROW_METRIC': {}, u'WIDE_METRIC': {}},), is_leaf=True, yang_name="metric-style", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:metric-style', is_config=True)""",
        })

    self.__metric_style = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric_style(self):
    self.__metric_style = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NARROW_METRIC': {}, u'WIDE_METRIC': {}},), is_leaf=True, yang_name="metric-style", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:metric-style', is_config=True)


  def _initialized_authentication_check(self):
    return self.__authentication_check is not None

  def _get_authentication_check(self):
    """
    Getter method for authentication_check, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/config/authentication_check (boolean)

    YANG Description: When set to true, reject all ISIS protocol PDUs that either have a mismatch
in authentication-type or authentication-key.
    """
    if self.__authentication_check is None:
        self.__authentication_check = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="authentication-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    return self.__authentication_check
      
  def _set_authentication_check(self, v, load=False):
    """
    Setter method for authentication_check, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/config/authentication_check (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authentication_check is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authentication_check() directly.

    YANG Description: When set to true, reject all ISIS protocol PDUs that either have a mismatch
in authentication-type or authentication-key.
    """
    if self.__authentication_check is None:
        self.__authentication_check = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="authentication-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="authentication-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authentication_check must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="authentication-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__authentication_check = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authentication_check(self):
    self.__authentication_check = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="authentication-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  enabled = __builtin__.property(_get_enabled, _set_enabled)
  level_number = __builtin__.property(_get_level_number, _set_level_number)
  metric_style = __builtin__.property(_get_metric_style, _set_metric_style)
  authentication_check = __builtin__.property(_get_authentication_check, _set_authentication_check)


  _pyangbind_elements = {'enabled': enabled, 'level_number': level_number, 'metric_style': metric_style, 'authentication_check': authentication_check, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS level based configuration.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__enabled','__level_number','__metric_style','__authentication_check',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__level_number = None
    self.__enabled = None
    self.__metric_style = None
    self.__authentication_check = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'config']

  def _initialized_enabled(self):
    return self.__enabled is not None

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/config/enabled (boolean)

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
    if self.__enabled is None:
        self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
    if self.__enabled is None:
        self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _initialized_level_number(self):
    return self.__level_number is not None

  def _get_level_number(self):
    """
    Getter method for level_number, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/config/level_number (oc-isis-types:level-number)

    YANG Description: ISIS level number (level-1, level-2).
    """
    if self.__level_number is None:
        self.__level_number = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..2']}), is_leaf=True, yang_name="level-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:level-number', is_config=True)
    return self.__level_number
      
  def _set_level_number(self, v, load=False):
    """
    Setter method for level_number, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/config/level_number (oc-isis-types:level-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_level_number is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_level_number() directly.

    YANG Description: ISIS level number (level-1, level-2).
    """
    if self.__level_number is None:
        self.__level_number = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..2']}), is_leaf=True, yang_name="level-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:level-number', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..2']}), is_leaf=True, yang_name="level-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:level-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """level_number must be of a type compatible with oc-isis-types:level-number""",
          'defined-type': "oc-isis-types:level-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..2']}), is_leaf=True, yang_name="level-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:level-number', is_config=True)""",
        })

    self.__level_number = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_level_number(self):
    self.__level_number = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..2']}), is_leaf=True, yang_name="level-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:level-number', is_config=True)


  def _initialized_metric_style(self):
    return self.__metric_style is not None

  def _get_metric_style(self):
    """
    Getter method for metric_style, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/config/metric_style (oc-isis-types:metric-style)

    YANG Description: ISIS metric style types(narrow, wide).
    """
    if self.__metric_style is None:
        self.__metric_style = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NARROW_METRIC': {}, u'WIDE_METRIC': {}},), is_leaf=True, yang_name="metric-style", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:metric-style', is_config=True)
    return self.__metric_style
      
  def _set_metric_style(self, v, load=False):
    """
    Setter method for metric_style, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/config/metric_style (oc-isis-types:metric-style)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric_style is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric_style() directly.

    YANG Description: ISIS metric style types(narrow, wide).
    """
    if self.__metric_style is None:
        self.__metric_style = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NARROW_METRIC': {}, u'WIDE_METRIC': {}},), is_leaf=True, yang_name="metric-style", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:metric-style', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NARROW_METRIC': {}, u'WIDE_METRIC': {}},), is_leaf=True, yang_name="metric-style", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:metric-style', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric_style must be of a type compatible with oc-isis-types:metric-style""",
          'defined-type': "oc-isis-types:metric-style",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NARROW_METRIC': {}, u'WIDE_METRIC': {}},), is_leaf=True, yang_name="metric-style", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:metric-style', is_config=True)""",
        })

    self.__metric_style = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric_style(self):
    self.__metric_style = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NARROW_METRIC': {}, u'WIDE_METRIC': {}},), is_leaf=True, yang_name="metric-style", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:metric-style', is_config=True)


  def _initialized_authentication_check(self):
    return self.__authentication_check is not None

  def _get_authentication_check(self):
    """
    Getter method for authentication_check, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/config/authentication_check (boolean)

    YANG Description: When set to true, reject all ISIS protocol PDUs that either have a mismatch
in authentication-type or authentication-key.
    """
    if self.__authentication_check is None:
        self.__authentication_check = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="authentication-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    return self.__authentication_check
      
  def _set_authentication_check(self, v, load=False):
    """
    Setter method for authentication_check, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/config/authentication_check (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authentication_check is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authentication_check() directly.

    YANG Description: When set to true, reject all ISIS protocol PDUs that either have a mismatch
in authentication-type or authentication-key.
    """
    if self.__authentication_check is None:
        self.__authentication_check = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="authentication-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="authentication-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authentication_check must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="authentication-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__authentication_check = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authentication_check(self):
    self.__authentication_check = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="authentication-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  enabled = __builtin__.property(_get_enabled, _set_enabled)
  level_number = __builtin__.property(_get_level_number, _set_level_number)
  metric_style = __builtin__.property(_get_metric_style, _set_metric_style)
  authentication_check = __builtin__.property(_get_authentication_check, _set_authentication_check)


  _pyangbind_elements = {'enabled': enabled, 'level_number': level_number, 'metric_style': metric_style, 'authentication_check': authentication_check, }


