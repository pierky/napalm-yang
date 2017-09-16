
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/peer-groups/peer-group/transport/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to the transport session(s)
used for the BGP neighbor or group
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__tcp_mss','__mtu_discovery','__passive_mode','__local_address',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tcp_mss = None
    self.__local_address = None
    self.__passive_mode = None
    self.__mtu_discovery = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'peer-groups', u'peer-group', u'transport', u'state']

  def _initialized_tcp_mss(self):
    return self.__tcp_mss is not None

  def _get_tcp_mss(self):
    """
    Getter method for tcp_mss, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/transport/state/tcp_mss (uint16)

    YANG Description: Sets the max segment size for BGP TCP sessions.
    """
    if self.__tcp_mss is None:
        self.__tcp_mss = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tcp-mss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    return self.__tcp_mss
      
  def _set_tcp_mss(self, v, load=False):
    """
    Setter method for tcp_mss, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/transport/state/tcp_mss (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tcp_mss is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tcp_mss() directly.

    YANG Description: Sets the max segment size for BGP TCP sessions.
    """
    if self.__tcp_mss is None:
        self.__tcp_mss = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tcp-mss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tcp-mss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tcp_mss must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tcp-mss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)""",
        })

    self.__tcp_mss = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tcp_mss(self):
    self.__tcp_mss = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tcp-mss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)


  def _initialized_mtu_discovery(self):
    return self.__mtu_discovery is not None

  def _get_mtu_discovery(self):
    """
    Getter method for mtu_discovery, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/transport/state/mtu_discovery (boolean)

    YANG Description: Turns path mtu discovery for BGP TCP sessions on (true)
or off (false)
    """
    if self.__mtu_discovery is None:
        self.__mtu_discovery = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mtu-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    return self.__mtu_discovery
      
  def _set_mtu_discovery(self, v, load=False):
    """
    Setter method for mtu_discovery, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/transport/state/mtu_discovery (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mtu_discovery is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mtu_discovery() directly.

    YANG Description: Turns path mtu discovery for BGP TCP sessions on (true)
or off (false)
    """
    if self.__mtu_discovery is None:
        self.__mtu_discovery = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mtu-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mtu-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mtu_discovery must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mtu-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__mtu_discovery = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mtu_discovery(self):
    self.__mtu_discovery = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mtu-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _initialized_passive_mode(self):
    return self.__passive_mode is not None

  def _get_passive_mode(self):
    """
    Getter method for passive_mode, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/transport/state/passive_mode (boolean)

    YANG Description: Wait for peers to issue requests to open a BGP session,
rather than initiating sessions from the local router.
    """
    if self.__passive_mode is None:
        self.__passive_mode = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    return self.__passive_mode
      
  def _set_passive_mode(self, v, load=False):
    """
    Setter method for passive_mode, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/transport/state/passive_mode (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_passive_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_passive_mode() directly.

    YANG Description: Wait for peers to issue requests to open a BGP session,
rather than initiating sessions from the local router.
    """
    if self.__passive_mode is None:
        self.__passive_mode = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """passive_mode must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__passive_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_passive_mode(self):
    self.__passive_mode = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _initialized_local_address(self):
    return self.__local_address is not None

  def _get_local_address(self):
    """
    Getter method for local_address, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/transport/state/local_address (union)

    YANG Description: Set the local IP (either IPv4 or IPv6) address to use
for the session when sending BGP update messages.  This
may be expressed as either an IP address or reference
to the name of an interface.
    """
    if self.__local_address is None:
        self.__local_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))$'}),unicode,], is_leaf=True, yang_name="local-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)
    return self.__local_address
      
  def _set_local_address(self, v, load=False):
    """
    Setter method for local_address, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/transport/state/local_address (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_address() directly.

    YANG Description: Set the local IP (either IPv4 or IPv6) address to use
for the session when sending BGP update messages.  This
may be expressed as either an IP address or reference
to the name of an interface.
    """
    if self.__local_address is None:
        self.__local_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))$'}),unicode,], is_leaf=True, yang_name="local-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))$'}),unicode,], is_leaf=True, yang_name="local-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_address must be of a type compatible with union""",
          'defined-type': "openconfig-network-instance:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))$'}),unicode,], is_leaf=True, yang_name="local-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)""",
        })

    self.__local_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_address(self):
    self.__local_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))$'}),unicode,], is_leaf=True, yang_name="local-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

  tcp_mss = __builtin__.property(_get_tcp_mss)
  mtu_discovery = __builtin__.property(_get_mtu_discovery)
  passive_mode = __builtin__.property(_get_passive_mode)
  local_address = __builtin__.property(_get_local_address)


  _pyangbind_elements = {'tcp_mss': tcp_mss, 'mtu_discovery': mtu_discovery, 'passive_mode': passive_mode, 'local_address': local_address, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/peer-groups/peer-group/transport/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to the transport session(s)
used for the BGP neighbor or group
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__tcp_mss','__mtu_discovery','__passive_mode','__local_address',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tcp_mss = None
    self.__local_address = None
    self.__passive_mode = None
    self.__mtu_discovery = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'peer-groups', u'peer-group', u'transport', u'state']

  def _initialized_tcp_mss(self):
    return self.__tcp_mss is not None

  def _get_tcp_mss(self):
    """
    Getter method for tcp_mss, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/transport/state/tcp_mss (uint16)

    YANG Description: Sets the max segment size for BGP TCP sessions.
    """
    if self.__tcp_mss is None:
        self.__tcp_mss = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tcp-mss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    return self.__tcp_mss
      
  def _set_tcp_mss(self, v, load=False):
    """
    Setter method for tcp_mss, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/transport/state/tcp_mss (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tcp_mss is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tcp_mss() directly.

    YANG Description: Sets the max segment size for BGP TCP sessions.
    """
    if self.__tcp_mss is None:
        self.__tcp_mss = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tcp-mss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tcp-mss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tcp_mss must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tcp-mss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)""",
        })

    self.__tcp_mss = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tcp_mss(self):
    self.__tcp_mss = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tcp-mss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)


  def _initialized_mtu_discovery(self):
    return self.__mtu_discovery is not None

  def _get_mtu_discovery(self):
    """
    Getter method for mtu_discovery, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/transport/state/mtu_discovery (boolean)

    YANG Description: Turns path mtu discovery for BGP TCP sessions on (true)
or off (false)
    """
    if self.__mtu_discovery is None:
        self.__mtu_discovery = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mtu-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    return self.__mtu_discovery
      
  def _set_mtu_discovery(self, v, load=False):
    """
    Setter method for mtu_discovery, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/transport/state/mtu_discovery (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mtu_discovery is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mtu_discovery() directly.

    YANG Description: Turns path mtu discovery for BGP TCP sessions on (true)
or off (false)
    """
    if self.__mtu_discovery is None:
        self.__mtu_discovery = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mtu-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mtu-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mtu_discovery must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mtu-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__mtu_discovery = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mtu_discovery(self):
    self.__mtu_discovery = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mtu-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _initialized_passive_mode(self):
    return self.__passive_mode is not None

  def _get_passive_mode(self):
    """
    Getter method for passive_mode, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/transport/state/passive_mode (boolean)

    YANG Description: Wait for peers to issue requests to open a BGP session,
rather than initiating sessions from the local router.
    """
    if self.__passive_mode is None:
        self.__passive_mode = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    return self.__passive_mode
      
  def _set_passive_mode(self, v, load=False):
    """
    Setter method for passive_mode, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/transport/state/passive_mode (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_passive_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_passive_mode() directly.

    YANG Description: Wait for peers to issue requests to open a BGP session,
rather than initiating sessions from the local router.
    """
    if self.__passive_mode is None:
        self.__passive_mode = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """passive_mode must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__passive_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_passive_mode(self):
    self.__passive_mode = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _initialized_local_address(self):
    return self.__local_address is not None

  def _get_local_address(self):
    """
    Getter method for local_address, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/transport/state/local_address (union)

    YANG Description: Set the local IP (either IPv4 or IPv6) address to use
for the session when sending BGP update messages.  This
may be expressed as either an IP address or reference
to the name of an interface.
    """
    if self.__local_address is None:
        self.__local_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))$'}),unicode,], is_leaf=True, yang_name="local-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)
    return self.__local_address
      
  def _set_local_address(self, v, load=False):
    """
    Setter method for local_address, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/transport/state/local_address (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_address() directly.

    YANG Description: Set the local IP (either IPv4 or IPv6) address to use
for the session when sending BGP update messages.  This
may be expressed as either an IP address or reference
to the name of an interface.
    """
    if self.__local_address is None:
        self.__local_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))$'}),unicode,], is_leaf=True, yang_name="local-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))$'}),unicode,], is_leaf=True, yang_name="local-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_address must be of a type compatible with union""",
          'defined-type': "openconfig-network-instance:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))$'}),unicode,], is_leaf=True, yang_name="local-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)""",
        })

    self.__local_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_address(self):
    self.__local_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))$'}),unicode,], is_leaf=True, yang_name="local-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

  tcp_mss = __builtin__.property(_get_tcp_mss)
  mtu_discovery = __builtin__.property(_get_mtu_discovery)
  passive_mode = __builtin__.property(_get_passive_mode)
  local_address = __builtin__.property(_get_local_address)


  _pyangbind_elements = {'tcp_mss': tcp_mss, 'mtu_discovery': mtu_discovery, 'passive_mode': passive_mode, 'local_address': local_address, }


