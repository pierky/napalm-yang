
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

from . import sent
from . import received
class messages(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/messages. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Counters for BGP messages sent and received from the
neighbor
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__sent','__received',)

  _yang_name = 'messages'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__received = None
    self.__sent = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'neighbors', u'neighbor', u'state', u'messages']

  def _initialized_sent(self):
    return self.__sent is not None

  def _get_sent(self):
    """
    Getter method for sent, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/sent (container)

    YANG Description: Counters relating to BGP messages sent to the neighbor
    """
    if self.__sent is None:
        self.__sent = YANGDynClass(base=sent.sent, is_container='container', yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    return self.__sent
      
  def _set_sent(self, v, load=False):
    """
    Setter method for sent, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/sent (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sent() directly.

    YANG Description: Counters relating to BGP messages sent to the neighbor
    """
    if self.__sent is None:
        self.__sent = YANGDynClass(base=sent.sent, is_container='container', yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=sent.sent, is_container='container', yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sent must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=sent.sent, is_container='container', yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__sent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sent(self):
    self.__sent = YANGDynClass(base=sent.sent, is_container='container', yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _initialized_received(self):
    return self.__received is not None

  def _get_received(self):
    """
    Getter method for received, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received (container)

    YANG Description: Counters for BGP messages received from the neighbor
    """
    if self.__received is None:
        self.__received = YANGDynClass(base=received.received, is_container='container', yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    return self.__received
      
  def _set_received(self, v, load=False):
    """
    Setter method for received, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_received is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_received() directly.

    YANG Description: Counters for BGP messages received from the neighbor
    """
    if self.__received is None:
        self.__received = YANGDynClass(base=received.received, is_container='container', yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=received.received, is_container='container', yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """received must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=received.received, is_container='container', yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__received = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_received(self):
    self.__received = YANGDynClass(base=received.received, is_container='container', yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  sent = __builtin__.property(_get_sent)
  received = __builtin__.property(_get_received)


  _pyangbind_elements = {'sent': sent, 'received': received, }


from . import sent
from . import received
class messages(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/messages. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Counters for BGP messages sent and received from the
neighbor
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__sent','__received',)

  _yang_name = 'messages'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__received = None
    self.__sent = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'neighbors', u'neighbor', u'state', u'messages']

  def _initialized_sent(self):
    return self.__sent is not None

  def _get_sent(self):
    """
    Getter method for sent, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/sent (container)

    YANG Description: Counters relating to BGP messages sent to the neighbor
    """
    if self.__sent is None:
        self.__sent = YANGDynClass(base=sent.sent, is_container='container', yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    return self.__sent
      
  def _set_sent(self, v, load=False):
    """
    Setter method for sent, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/sent (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sent() directly.

    YANG Description: Counters relating to BGP messages sent to the neighbor
    """
    if self.__sent is None:
        self.__sent = YANGDynClass(base=sent.sent, is_container='container', yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=sent.sent, is_container='container', yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sent must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=sent.sent, is_container='container', yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__sent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sent(self):
    self.__sent = YANGDynClass(base=sent.sent, is_container='container', yang_name="sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _initialized_received(self):
    return self.__received is not None

  def _get_received(self):
    """
    Getter method for received, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received (container)

    YANG Description: Counters for BGP messages received from the neighbor
    """
    if self.__received is None:
        self.__received = YANGDynClass(base=received.received, is_container='container', yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    return self.__received
      
  def _set_received(self, v, load=False):
    """
    Setter method for received, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_received is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_received() directly.

    YANG Description: Counters for BGP messages received from the neighbor
    """
    if self.__received is None:
        self.__received = YANGDynClass(base=received.received, is_container='container', yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=received.received, is_container='container', yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """received must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=received.received, is_container='container', yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__received = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_received(self):
    self.__received = YANGDynClass(base=received.received, is_container='container', yang_name="received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  sent = __builtin__.property(_get_sent)
  received = __builtin__.property(_get_received)


  _pyangbind_elements = {'sent': sent, 'received': received, }


