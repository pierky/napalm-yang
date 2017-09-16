
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/named-explicit-paths/named-explicit-path/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state parameters relating to the named
explicit paths
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__name','__sid_selection_mode','__sid_protection_required',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sid_selection_mode = None
    self.__name = None
    self.__sid_protection_required = None

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'named-explicit-paths', u'named-explicit-path', u'state']

  def _initialized_name(self):
    return self.__name is not None

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/named_explicit_paths/named_explicit_path/state/name (string)

    YANG Description: A string name that uniquely identifies an explicit
path
    """
    if self.__name is None:
        self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/named_explicit_paths/named_explicit_path/state/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: A string name that uniquely identifies an explicit
path
    """
    if self.__name is None:
        self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)


  def _initialized_sid_selection_mode(self):
    return self.__sid_selection_mode is not None

  def _get_sid_selection_mode(self):
    """
    Getter method for sid_selection_mode, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/named_explicit_paths/named_explicit_path/state/sid_selection_mode (enumeration)

    YANG Description: The restrictions placed on the SIDs to be selected by the
calculation method for the explicit path when it is
instantiated for a SR-TE LSP
    """
    if self.__sid_selection_mode is None:
        self.__sid_selection_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MIXED_MODE': {}, u'ADJ_SID_ONLY': {}},), default=unicode("MIXED_MODE"), is_leaf=True, yang_name="sid-selection-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    return self.__sid_selection_mode
      
  def _set_sid_selection_mode(self, v, load=False):
    """
    Setter method for sid_selection_mode, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/named_explicit_paths/named_explicit_path/state/sid_selection_mode (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid_selection_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid_selection_mode() directly.

    YANG Description: The restrictions placed on the SIDs to be selected by the
calculation method for the explicit path when it is
instantiated for a SR-TE LSP
    """
    if self.__sid_selection_mode is None:
        self.__sid_selection_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MIXED_MODE': {}, u'ADJ_SID_ONLY': {}},), default=unicode("MIXED_MODE"), is_leaf=True, yang_name="sid-selection-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MIXED_MODE': {}, u'ADJ_SID_ONLY': {}},), default=unicode("MIXED_MODE"), is_leaf=True, yang_name="sid-selection-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sid_selection_mode must be of a type compatible with enumeration""",
          'defined-type': "openconfig-network-instance:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MIXED_MODE': {}, u'ADJ_SID_ONLY': {}},), default=unicode("MIXED_MODE"), is_leaf=True, yang_name="sid-selection-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)""",
        })

    self.__sid_selection_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sid_selection_mode(self):
    self.__sid_selection_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MIXED_MODE': {}, u'ADJ_SID_ONLY': {}},), default=unicode("MIXED_MODE"), is_leaf=True, yang_name="sid-selection-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)


  def _initialized_sid_protection_required(self):
    return self.__sid_protection_required is not None

  def _get_sid_protection_required(self):
    """
    Getter method for sid_protection_required, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/named_explicit_paths/named_explicit_path/state/sid_protection_required (boolean)

    YANG Description: When this value is set to true, only SIDs that are
protected are to be selected by the calculating method
when the explicit path is instantiated by a SR-TE LSP.
    """
    if self.__sid_protection_required is None:
        self.__sid_protection_required = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="sid-protection-required", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    return self.__sid_protection_required
      
  def _set_sid_protection_required(self, v, load=False):
    """
    Setter method for sid_protection_required, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/named_explicit_paths/named_explicit_path/state/sid_protection_required (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid_protection_required is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid_protection_required() directly.

    YANG Description: When this value is set to true, only SIDs that are
protected are to be selected by the calculating method
when the explicit path is instantiated by a SR-TE LSP.
    """
    if self.__sid_protection_required is None:
        self.__sid_protection_required = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="sid-protection-required", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="sid-protection-required", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sid_protection_required must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="sid-protection-required", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__sid_protection_required = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sid_protection_required(self):
    self.__sid_protection_required = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="sid-protection-required", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  name = __builtin__.property(_get_name)
  sid_selection_mode = __builtin__.property(_get_sid_selection_mode)
  sid_protection_required = __builtin__.property(_get_sid_protection_required)


  _pyangbind_elements = {'name': name, 'sid_selection_mode': sid_selection_mode, 'sid_protection_required': sid_protection_required, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/named-explicit-paths/named-explicit-path/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state parameters relating to the named
explicit paths
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__name','__sid_selection_mode','__sid_protection_required',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sid_selection_mode = None
    self.__name = None
    self.__sid_protection_required = None

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'named-explicit-paths', u'named-explicit-path', u'state']

  def _initialized_name(self):
    return self.__name is not None

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/named_explicit_paths/named_explicit_path/state/name (string)

    YANG Description: A string name that uniquely identifies an explicit
path
    """
    if self.__name is None:
        self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/named_explicit_paths/named_explicit_path/state/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: A string name that uniquely identifies an explicit
path
    """
    if self.__name is None:
        self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)


  def _initialized_sid_selection_mode(self):
    return self.__sid_selection_mode is not None

  def _get_sid_selection_mode(self):
    """
    Getter method for sid_selection_mode, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/named_explicit_paths/named_explicit_path/state/sid_selection_mode (enumeration)

    YANG Description: The restrictions placed on the SIDs to be selected by the
calculation method for the explicit path when it is
instantiated for a SR-TE LSP
    """
    if self.__sid_selection_mode is None:
        self.__sid_selection_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MIXED_MODE': {}, u'ADJ_SID_ONLY': {}},), default=unicode("MIXED_MODE"), is_leaf=True, yang_name="sid-selection-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    return self.__sid_selection_mode
      
  def _set_sid_selection_mode(self, v, load=False):
    """
    Setter method for sid_selection_mode, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/named_explicit_paths/named_explicit_path/state/sid_selection_mode (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid_selection_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid_selection_mode() directly.

    YANG Description: The restrictions placed on the SIDs to be selected by the
calculation method for the explicit path when it is
instantiated for a SR-TE LSP
    """
    if self.__sid_selection_mode is None:
        self.__sid_selection_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MIXED_MODE': {}, u'ADJ_SID_ONLY': {}},), default=unicode("MIXED_MODE"), is_leaf=True, yang_name="sid-selection-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MIXED_MODE': {}, u'ADJ_SID_ONLY': {}},), default=unicode("MIXED_MODE"), is_leaf=True, yang_name="sid-selection-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sid_selection_mode must be of a type compatible with enumeration""",
          'defined-type': "openconfig-network-instance:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MIXED_MODE': {}, u'ADJ_SID_ONLY': {}},), default=unicode("MIXED_MODE"), is_leaf=True, yang_name="sid-selection-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)""",
        })

    self.__sid_selection_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sid_selection_mode(self):
    self.__sid_selection_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MIXED_MODE': {}, u'ADJ_SID_ONLY': {}},), default=unicode("MIXED_MODE"), is_leaf=True, yang_name="sid-selection-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)


  def _initialized_sid_protection_required(self):
    return self.__sid_protection_required is not None

  def _get_sid_protection_required(self):
    """
    Getter method for sid_protection_required, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/named_explicit_paths/named_explicit_path/state/sid_protection_required (boolean)

    YANG Description: When this value is set to true, only SIDs that are
protected are to be selected by the calculating method
when the explicit path is instantiated by a SR-TE LSP.
    """
    if self.__sid_protection_required is None:
        self.__sid_protection_required = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="sid-protection-required", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    return self.__sid_protection_required
      
  def _set_sid_protection_required(self, v, load=False):
    """
    Setter method for sid_protection_required, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/named_explicit_paths/named_explicit_path/state/sid_protection_required (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid_protection_required is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid_protection_required() directly.

    YANG Description: When this value is set to true, only SIDs that are
protected are to be selected by the calculating method
when the explicit path is instantiated by a SR-TE LSP.
    """
    if self.__sid_protection_required is None:
        self.__sid_protection_required = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="sid-protection-required", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="sid-protection-required", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sid_protection_required must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="sid-protection-required", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__sid_protection_required = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sid_protection_required(self):
    self.__sid_protection_required = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="sid-protection-required", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  name = __builtin__.property(_get_name)
  sid_selection_mode = __builtin__.property(_get_sid_selection_mode)
  sid_protection_required = __builtin__.property(_get_sid_protection_required)


  _pyangbind_elements = {'name': name, 'sid_selection_mode': sid_selection_mode, 'sid_protection_required': sid_protection_required, }


