
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

from . import config
from . import state
class candidate_secondary_path(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/p2p-tunnel-attributes/p2p-primary-path/p2p-primary-path/candidate-secondary-paths/candidate-secondary-path. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of secondary paths which may be utilised when the
current primary path is in use
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__secondary_path','__config','__state',)

  _yang_name = 'candidate-secondary-path'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__state = None
    self.__config = None
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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'tunnels', u'tunnel', u'p2p-tunnel-attributes', u'p2p-primary-path', u'p2p-primary-path', u'candidate-secondary-paths', u'candidate-secondary-path']

  def _initialized_secondary_path(self):
    return self.__secondary_path is not None

  def _get_secondary_path(self):
    """
    Getter method for secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/secondary_path (leafref)

    YANG Description: A reference to the secondary path option reference
which acts as the key of the candidate-secondary-path
list
    """
    if self.__secondary_path is None:
        self.__secondary_path = YANGDynClass(base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    return self.__secondary_path
      
  def _set_secondary_path(self, v, load=False):
    """
    Setter method for secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/secondary_path (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_secondary_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_secondary_path() directly.

    YANG Description: A reference to the secondary path option reference
which acts as the key of the candidate-secondary-path
list
    """
    if self.__secondary_path is None:
        self.__secondary_path = YANGDynClass(base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """secondary_path must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__secondary_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_secondary_path(self):
    self.__secondary_path = YANGDynClass(base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _initialized_config(self):
    return self.__config is not None

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/config (container)

    YANG Description: Configuration parameters relating to the candidate
secondary path
    """
    if self.__config is None:
        self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters relating to the candidate
secondary path
    """
    if self.__config is None:
        self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _initialized_state(self):
    return self.__state is not None

  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/state (container)

    YANG Description: Operational state parameters relating to the candidate
secondary path
    """
    if self.__state is None:
        self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters relating to the candidate
secondary path
    """
    if self.__state is None:
        self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  secondary_path = __builtin__.property(_get_secondary_path, _set_secondary_path)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)


  _pyangbind_elements = {'secondary_path': secondary_path, 'config': config, 'state': state, }


from . import config
from . import state
class candidate_secondary_path(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/p2p-tunnel-attributes/p2p-primary-path/p2p-primary-path/candidate-secondary-paths/candidate-secondary-path. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of secondary paths which may be utilised when the
current primary path is in use
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__secondary_path','__config','__state',)

  _yang_name = 'candidate-secondary-path'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__state = None
    self.__config = None
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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'tunnels', u'tunnel', u'p2p-tunnel-attributes', u'p2p-primary-path', u'p2p-primary-path', u'candidate-secondary-paths', u'candidate-secondary-path']

  def _initialized_secondary_path(self):
    return self.__secondary_path is not None

  def _get_secondary_path(self):
    """
    Getter method for secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/secondary_path (leafref)

    YANG Description: A reference to the secondary path option reference
which acts as the key of the candidate-secondary-path
list
    """
    if self.__secondary_path is None:
        self.__secondary_path = YANGDynClass(base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    return self.__secondary_path
      
  def _set_secondary_path(self, v, load=False):
    """
    Setter method for secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/secondary_path (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_secondary_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_secondary_path() directly.

    YANG Description: A reference to the secondary path option reference
which acts as the key of the candidate-secondary-path
list
    """
    if self.__secondary_path is None:
        self.__secondary_path = YANGDynClass(base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """secondary_path must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__secondary_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_secondary_path(self):
    self.__secondary_path = YANGDynClass(base=unicode, is_leaf=True, yang_name="secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _initialized_config(self):
    return self.__config is not None

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/config (container)

    YANG Description: Configuration parameters relating to the candidate
secondary path
    """
    if self.__config is None:
        self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters relating to the candidate
secondary path
    """
    if self.__config is None:
        self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _initialized_state(self):
    return self.__state is not None

  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/state (container)

    YANG Description: Operational state parameters relating to the candidate
secondary path
    """
    if self.__state is None:
        self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters relating to the candidate
secondary path
    """
    if self.__state is None:
        self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  secondary_path = __builtin__.property(_get_secondary_path, _set_secondary_path)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)


  _pyangbind_elements = {'secondary_path': secondary_path, 'config': config, 'state': state, }


