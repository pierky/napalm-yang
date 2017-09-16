
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

from . import state
from . import forwarding_classes
class sid_counter(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/segment-routing/interfaces/interface/sid-counters/sid-counter. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per segment identifier counters for the MPLS dataplane.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__mpls_label','__state','__forwarding_classes',)

  _yang_name = 'sid-counter'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__state = None
    self.__forwarding_classes = None
    self.__mpls_label = None

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
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'segment-routing', u'interfaces', u'interface', u'sid-counters', u'sid-counter']

  def _initialized_mpls_label(self):
    return self.__mpls_label is not None

  def _get_mpls_label(self):
    """
    Getter method for mpls_label, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/mpls_label (leafref)

    YANG Description: The MPLS label representing the segment identifier
    """
    if self.__mpls_label is None:
        self.__mpls_label = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    return self.__mpls_label
      
  def _set_mpls_label(self, v, load=False):
    """
    Setter method for mpls_label, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/mpls_label (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_label() directly.

    YANG Description: The MPLS label representing the segment identifier
    """
    if self.__mpls_label is None:
        self.__mpls_label = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mpls-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_label must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__mpls_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_label(self):
    self.__mpls_label = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _initialized_state(self):
    return self.__state is not None

  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/state (container)

    YANG Description: State parameters for per-SID statistics
    """
    if self.__state is None:
        self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters for per-SID statistics
    """
    if self.__state is None:
        self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _initialized_forwarding_classes(self):
    return self.__forwarding_classes is not None

  def _get_forwarding_classes(self):
    """
    Getter method for forwarding_classes, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/forwarding_classes (container)

    YANG Description: Per-SID per-forwarding class counters for Segment Routing.
    """
    if self.__forwarding_classes is None:
        self.__forwarding_classes = YANGDynClass(base=forwarding_classes.forwarding_classes, is_container='container', yang_name="forwarding-classes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    return self.__forwarding_classes
      
  def _set_forwarding_classes(self, v, load=False):
    """
    Setter method for forwarding_classes, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/forwarding_classes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forwarding_classes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forwarding_classes() directly.

    YANG Description: Per-SID per-forwarding class counters for Segment Routing.
    """
    if self.__forwarding_classes is None:
        self.__forwarding_classes = YANGDynClass(base=forwarding_classes.forwarding_classes, is_container='container', yang_name="forwarding-classes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=forwarding_classes.forwarding_classes, is_container='container', yang_name="forwarding-classes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forwarding_classes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=forwarding_classes.forwarding_classes, is_container='container', yang_name="forwarding-classes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__forwarding_classes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forwarding_classes(self):
    self.__forwarding_classes = YANGDynClass(base=forwarding_classes.forwarding_classes, is_container='container', yang_name="forwarding-classes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  mpls_label = __builtin__.property(_get_mpls_label)
  state = __builtin__.property(_get_state)
  forwarding_classes = __builtin__.property(_get_forwarding_classes)


  _pyangbind_elements = {'mpls_label': mpls_label, 'state': state, 'forwarding_classes': forwarding_classes, }


from . import state
from . import forwarding_classes
class sid_counter(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/segment-routing/interfaces/interface/sid-counters/sid-counter. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per segment identifier counters for the MPLS dataplane.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__mpls_label','__state','__forwarding_classes',)

  _yang_name = 'sid-counter'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__state = None
    self.__forwarding_classes = None
    self.__mpls_label = None

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
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'segment-routing', u'interfaces', u'interface', u'sid-counters', u'sid-counter']

  def _initialized_mpls_label(self):
    return self.__mpls_label is not None

  def _get_mpls_label(self):
    """
    Getter method for mpls_label, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/mpls_label (leafref)

    YANG Description: The MPLS label representing the segment identifier
    """
    if self.__mpls_label is None:
        self.__mpls_label = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    return self.__mpls_label
      
  def _set_mpls_label(self, v, load=False):
    """
    Setter method for mpls_label, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/mpls_label (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_label() directly.

    YANG Description: The MPLS label representing the segment identifier
    """
    if self.__mpls_label is None:
        self.__mpls_label = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mpls-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_label must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__mpls_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_label(self):
    self.__mpls_label = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _initialized_state(self):
    return self.__state is not None

  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/state (container)

    YANG Description: State parameters for per-SID statistics
    """
    if self.__state is None:
        self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters for per-SID statistics
    """
    if self.__state is None:
        self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _initialized_forwarding_classes(self):
    return self.__forwarding_classes is not None

  def _get_forwarding_classes(self):
    """
    Getter method for forwarding_classes, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/forwarding_classes (container)

    YANG Description: Per-SID per-forwarding class counters for Segment Routing.
    """
    if self.__forwarding_classes is None:
        self.__forwarding_classes = YANGDynClass(base=forwarding_classes.forwarding_classes, is_container='container', yang_name="forwarding-classes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    return self.__forwarding_classes
      
  def _set_forwarding_classes(self, v, load=False):
    """
    Setter method for forwarding_classes, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/forwarding_classes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forwarding_classes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forwarding_classes() directly.

    YANG Description: Per-SID per-forwarding class counters for Segment Routing.
    """
    if self.__forwarding_classes is None:
        self.__forwarding_classes = YANGDynClass(base=forwarding_classes.forwarding_classes, is_container='container', yang_name="forwarding-classes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=forwarding_classes.forwarding_classes, is_container='container', yang_name="forwarding-classes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forwarding_classes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=forwarding_classes.forwarding_classes, is_container='container', yang_name="forwarding-classes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__forwarding_classes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forwarding_classes(self):
    self.__forwarding_classes = YANGDynClass(base=forwarding_classes.forwarding_classes, is_container='container', yang_name="forwarding-classes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  mpls_label = __builtin__.property(_get_mpls_label)
  state = __builtin__.property(_get_state)
  forwarding_classes = __builtin__.property(_get_forwarding_classes)


  _pyangbind_elements = {'mpls_label': mpls_label, 'state': state, 'forwarding_classes': forwarding_classes, }


