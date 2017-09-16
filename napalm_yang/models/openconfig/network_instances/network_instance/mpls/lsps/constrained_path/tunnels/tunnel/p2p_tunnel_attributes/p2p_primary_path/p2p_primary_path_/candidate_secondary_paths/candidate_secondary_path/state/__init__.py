
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/p2p-tunnel-attributes/p2p-primary-path/p2p-primary-path/candidate-secondary-paths/candidate-secondary-path/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state parameters relating to the candidate
secondary path
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__secondary_path','__priority','__active',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__priority = None
    self.__active = None
    self.__secondary_path = None

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'tunnels', u'tunnel', u'p2p-tunnel-attributes', u'p2p-primary-path', u'p2p-primary-path', u'candidate-secondary-paths', u'candidate-secondary-path', u'state']

  def _initialized_secondary_path(self):
    return self.__secondary_path is not None

  def _get_secondary_path(self):
    """
    Getter method for secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/state/secondary_path (leafref)

    YANG Description: A reference to the secondary path that should be utilised
when the containing primary path option is in use
    """
    if self.__secondary_path is None:
        self.__secondary_path = YANGDynClass(base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    return self.__secondary_path
      
  def _set_secondary_path(self, v, load=False):
    """
    Setter method for secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/state/secondary_path (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_secondary_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_secondary_path() directly.

    YANG Description: A reference to the secondary path that should be utilised
when the containing primary path option is in use
    """
    if self.__secondary_path is None:
        self.__secondary_path = YANGDynClass(base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """secondary_path must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__secondary_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_secondary_path(self):
    self.__secondary_path = YANGDynClass(base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _initialized_priority(self):
    return self.__priority is not None

  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/state/priority (uint16)

    YANG Description: The priority of the specified secondary path option. Higher
priority options are less preferable - such that a secondary
path reference with a priority of 0 is the most preferred
    """
    if self.__priority is None:
        self.__priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/state/priority (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: The priority of the specified secondary path option. Higher
priority options are less preferable - such that a secondary
path reference with a priority of 0 is the most preferred
    """
    if self.__priority is None:
        self.__priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)


  def _initialized_active(self):
    return self.__active is not None

  def _get_active(self):
    """
    Getter method for active, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/state/active (boolean)

    YANG Description: Indicates the current active path option that has
been selected of the candidate secondary paths
    """
    if self.__active is None:
        self.__active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    return self.__active
      
  def _set_active(self, v, load=False):
    """
    Setter method for active, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/state/active (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_active is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_active() directly.

    YANG Description: Indicates the current active path option that has
been selected of the candidate secondary paths
    """
    if self.__active is None:
        self.__active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """active must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__active = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_active(self):
    self.__active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  secondary_path = __builtin__.property(_get_secondary_path)
  priority = __builtin__.property(_get_priority)
  active = __builtin__.property(_get_active)


  _pyangbind_elements = {'secondary_path': secondary_path, 'priority': priority, 'active': active, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/p2p-tunnel-attributes/p2p-primary-path/p2p-primary-path/candidate-secondary-paths/candidate-secondary-path/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state parameters relating to the candidate
secondary path
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__secondary_path','__priority','__active',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__priority = None
    self.__active = None
    self.__secondary_path = None

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'tunnels', u'tunnel', u'p2p-tunnel-attributes', u'p2p-primary-path', u'p2p-primary-path', u'candidate-secondary-paths', u'candidate-secondary-path', u'state']

  def _initialized_secondary_path(self):
    return self.__secondary_path is not None

  def _get_secondary_path(self):
    """
    Getter method for secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/state/secondary_path (leafref)

    YANG Description: A reference to the secondary path that should be utilised
when the containing primary path option is in use
    """
    if self.__secondary_path is None:
        self.__secondary_path = YANGDynClass(base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    return self.__secondary_path
      
  def _set_secondary_path(self, v, load=False):
    """
    Setter method for secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/state/secondary_path (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_secondary_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_secondary_path() directly.

    YANG Description: A reference to the secondary path that should be utilised
when the containing primary path option is in use
    """
    if self.__secondary_path is None:
        self.__secondary_path = YANGDynClass(base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """secondary_path must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__secondary_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_secondary_path(self):
    self.__secondary_path = YANGDynClass(base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _initialized_priority(self):
    return self.__priority is not None

  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/state/priority (uint16)

    YANG Description: The priority of the specified secondary path option. Higher
priority options are less preferable - such that a secondary
path reference with a priority of 0 is the most preferred
    """
    if self.__priority is None:
        self.__priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/state/priority (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: The priority of the specified secondary path option. Higher
priority options are less preferable - such that a secondary
path reference with a priority of 0 is the most preferred
    """
    if self.__priority is None:
        self.__priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)


  def _initialized_active(self):
    return self.__active is not None

  def _get_active(self):
    """
    Getter method for active, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/state/active (boolean)

    YANG Description: Indicates the current active path option that has
been selected of the candidate secondary paths
    """
    if self.__active is None:
        self.__active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    return self.__active
      
  def _set_active(self, v, load=False):
    """
    Setter method for active, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/state/active (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_active is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_active() directly.

    YANG Description: Indicates the current active path option that has
been selected of the candidate secondary paths
    """
    if self.__active is None:
        self.__active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """active must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__active = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_active(self):
    self.__active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  secondary_path = __builtin__.property(_get_secondary_path)
  priority = __builtin__.property(_get_priority)
  active = __builtin__.property(_get_active)


  _pyangbind_elements = {'secondary_path': secondary_path, 'priority': priority, 'active': active, }


