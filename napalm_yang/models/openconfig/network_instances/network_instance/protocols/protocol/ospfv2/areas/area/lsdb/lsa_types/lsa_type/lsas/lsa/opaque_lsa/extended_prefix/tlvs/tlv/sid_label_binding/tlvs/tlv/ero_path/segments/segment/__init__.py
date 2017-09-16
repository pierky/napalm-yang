
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
from . import ipv4_segment
from . import unnumbered_hop
class segment(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/extended-prefix/tlvs/tlv/sid-label-binding/tlvs/tlv/ero-path/segments/segment. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A segment of the path described within the sub-TLV
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__state','__ipv4_segment','__unnumbered_hop',)

  _yang_name = 'segment'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__state = None
    self.__ipv4_segment = None
    self.__unnumbered_hop = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'extended-prefix', u'tlvs', u'tlv', u'sid-label-binding', u'tlvs', u'tlv', u'ero-path', u'segments', u'segment']

  def _initialized_state(self):
    return self.__state is not None

  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments/segment/state (container)

    YANG Description: State parameters relating to the path segment
contained within the sub-TLV
    """
    if self.__state is None:
        self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments/segment/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters relating to the path segment
contained within the sub-TLV
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


  def _initialized_ipv4_segment(self):
    return self.__ipv4_segment is not None

  def _get_ipv4_segment(self):
    """
    Getter method for ipv4_segment, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments/segment/ipv4_segment (container)

    YANG Description: Details of the IPv4 segment interface of the ERO
    """
    if self.__ipv4_segment is None:
        self.__ipv4_segment = YANGDynClass(base=ipv4_segment.ipv4_segment, is_container='container', yang_name="ipv4-segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    return self.__ipv4_segment
      
  def _set_ipv4_segment(self, v, load=False):
    """
    Setter method for ipv4_segment, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments/segment/ipv4_segment (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4_segment is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4_segment() directly.

    YANG Description: Details of the IPv4 segment interface of the ERO
    """
    if self.__ipv4_segment is None:
        self.__ipv4_segment = YANGDynClass(base=ipv4_segment.ipv4_segment, is_container='container', yang_name="ipv4-segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ipv4_segment.ipv4_segment, is_container='container', yang_name="ipv4-segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4_segment must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv4_segment.ipv4_segment, is_container='container', yang_name="ipv4-segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__ipv4_segment = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4_segment(self):
    self.__ipv4_segment = YANGDynClass(base=ipv4_segment.ipv4_segment, is_container='container', yang_name="ipv4-segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _initialized_unnumbered_hop(self):
    return self.__unnumbered_hop is not None

  def _get_unnumbered_hop(self):
    """
    Getter method for unnumbered_hop, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments/segment/unnumbered_hop (container)

    YANG Description: Details of the unnumbered interface segment of the
ERO
    """
    if self.__unnumbered_hop is None:
        self.__unnumbered_hop = YANGDynClass(base=unnumbered_hop.unnumbered_hop, is_container='container', yang_name="unnumbered-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    return self.__unnumbered_hop
      
  def _set_unnumbered_hop(self, v, load=False):
    """
    Setter method for unnumbered_hop, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments/segment/unnumbered_hop (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unnumbered_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unnumbered_hop() directly.

    YANG Description: Details of the unnumbered interface segment of the
ERO
    """
    if self.__unnumbered_hop is None:
        self.__unnumbered_hop = YANGDynClass(base=unnumbered_hop.unnumbered_hop, is_container='container', yang_name="unnumbered-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unnumbered_hop.unnumbered_hop, is_container='container', yang_name="unnumbered-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unnumbered_hop must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=unnumbered_hop.unnumbered_hop, is_container='container', yang_name="unnumbered-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__unnumbered_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unnumbered_hop(self):
    self.__unnumbered_hop = YANGDynClass(base=unnumbered_hop.unnumbered_hop, is_container='container', yang_name="unnumbered-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  state = __builtin__.property(_get_state)
  ipv4_segment = __builtin__.property(_get_ipv4_segment)
  unnumbered_hop = __builtin__.property(_get_unnumbered_hop)


  _pyangbind_elements = {'state': state, 'ipv4_segment': ipv4_segment, 'unnumbered_hop': unnumbered_hop, }


from . import state
from . import ipv4_segment
from . import unnumbered_hop
class segment(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/extended-prefix/tlvs/tlv/sid-label-binding/tlvs/tlv/ero-path/segments/segment. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A segment of the path described within the sub-TLV
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__state','__ipv4_segment','__unnumbered_hop',)

  _yang_name = 'segment'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__state = None
    self.__ipv4_segment = None
    self.__unnumbered_hop = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'extended-prefix', u'tlvs', u'tlv', u'sid-label-binding', u'tlvs', u'tlv', u'ero-path', u'segments', u'segment']

  def _initialized_state(self):
    return self.__state is not None

  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments/segment/state (container)

    YANG Description: State parameters relating to the path segment
contained within the sub-TLV
    """
    if self.__state is None:
        self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments/segment/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters relating to the path segment
contained within the sub-TLV
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


  def _initialized_ipv4_segment(self):
    return self.__ipv4_segment is not None

  def _get_ipv4_segment(self):
    """
    Getter method for ipv4_segment, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments/segment/ipv4_segment (container)

    YANG Description: Details of the IPv4 segment interface of the ERO
    """
    if self.__ipv4_segment is None:
        self.__ipv4_segment = YANGDynClass(base=ipv4_segment.ipv4_segment, is_container='container', yang_name="ipv4-segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    return self.__ipv4_segment
      
  def _set_ipv4_segment(self, v, load=False):
    """
    Setter method for ipv4_segment, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments/segment/ipv4_segment (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4_segment is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4_segment() directly.

    YANG Description: Details of the IPv4 segment interface of the ERO
    """
    if self.__ipv4_segment is None:
        self.__ipv4_segment = YANGDynClass(base=ipv4_segment.ipv4_segment, is_container='container', yang_name="ipv4-segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ipv4_segment.ipv4_segment, is_container='container', yang_name="ipv4-segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4_segment must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv4_segment.ipv4_segment, is_container='container', yang_name="ipv4-segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__ipv4_segment = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4_segment(self):
    self.__ipv4_segment = YANGDynClass(base=ipv4_segment.ipv4_segment, is_container='container', yang_name="ipv4-segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _initialized_unnumbered_hop(self):
    return self.__unnumbered_hop is not None

  def _get_unnumbered_hop(self):
    """
    Getter method for unnumbered_hop, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments/segment/unnumbered_hop (container)

    YANG Description: Details of the unnumbered interface segment of the
ERO
    """
    if self.__unnumbered_hop is None:
        self.__unnumbered_hop = YANGDynClass(base=unnumbered_hop.unnumbered_hop, is_container='container', yang_name="unnumbered-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    return self.__unnumbered_hop
      
  def _set_unnumbered_hop(self, v, load=False):
    """
    Setter method for unnumbered_hop, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments/segment/unnumbered_hop (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unnumbered_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unnumbered_hop() directly.

    YANG Description: Details of the unnumbered interface segment of the
ERO
    """
    if self.__unnumbered_hop is None:
        self.__unnumbered_hop = YANGDynClass(base=unnumbered_hop.unnumbered_hop, is_container='container', yang_name="unnumbered-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unnumbered_hop.unnumbered_hop, is_container='container', yang_name="unnumbered-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unnumbered_hop must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=unnumbered_hop.unnumbered_hop, is_container='container', yang_name="unnumbered-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__unnumbered_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unnumbered_hop(self):
    self.__unnumbered_hop = YANGDynClass(base=unnumbered_hop.unnumbered_hop, is_container='container', yang_name="unnumbered-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  state = __builtin__.property(_get_state)
  ipv4_segment = __builtin__.property(_get_ipv4_segment)
  unnumbered_hop = __builtin__.property(_get_unnumbered_hop)


  _pyangbind_elements = {'state': state, 'ipv4_segment': ipv4_segment, 'unnumbered_hop': unnumbered_hop, }


