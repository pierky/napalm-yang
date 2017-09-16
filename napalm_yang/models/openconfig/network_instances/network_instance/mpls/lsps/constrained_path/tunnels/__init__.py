
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

from . import tunnel
class tunnels(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for tunnels
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__tunnel',)

  _yang_name = 'tunnels'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tunnel = None

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'tunnels']

  def _initialized_tunnel(self):
    return self.__tunnel is not None

  def _get_tunnel(self):
    """
    Getter method for tunnel, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel (list)

    YANG Description: List of TE tunnels. This list contains only the LSPs that the
current device originates (i.e., for which it is the head-end).
Where the signaling protocol utilised for an LSP allows a mid-point
or tail device to be aware of the LSP (e.g., RSVP-TE), then the
associated sessions are maintained per protocol
    """
    if self.__tunnel is None:
        self.__tunnel = YANGDynClass(base=YANGListType("name",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    return self.__tunnel
      
  def _set_tunnel(self, v, load=False):
    """
    Setter method for tunnel, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnel() directly.

    YANG Description: List of TE tunnels. This list contains only the LSPs that the
current device originates (i.e., for which it is the head-end).
Where the signaling protocol utilised for an LSP allows a mid-point
or tail device to be aware of the LSP (e.g., RSVP-TE), then the
associated sessions are maintained per protocol
    """
    if self.__tunnel is None:
        self.__tunnel = YANGDynClass(base=YANGListType("name",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnel must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__tunnel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnel(self):
    self.__tunnel = YANGDynClass(base=YANGListType("name",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  tunnel = __builtin__.property(_get_tunnel, _set_tunnel)


  _pyangbind_elements = {'tunnel': tunnel, }


from . import tunnel
class tunnels(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for tunnels
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__tunnel',)

  _yang_name = 'tunnels'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tunnel = None

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'tunnels']

  def _initialized_tunnel(self):
    return self.__tunnel is not None

  def _get_tunnel(self):
    """
    Getter method for tunnel, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel (list)

    YANG Description: List of TE tunnels. This list contains only the LSPs that the
current device originates (i.e., for which it is the head-end).
Where the signaling protocol utilised for an LSP allows a mid-point
or tail device to be aware of the LSP (e.g., RSVP-TE), then the
associated sessions are maintained per protocol
    """
    if self.__tunnel is None:
        self.__tunnel = YANGDynClass(base=YANGListType("name",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    return self.__tunnel
      
  def _set_tunnel(self, v, load=False):
    """
    Setter method for tunnel, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnel() directly.

    YANG Description: List of TE tunnels. This list contains only the LSPs that the
current device originates (i.e., for which it is the head-end).
Where the signaling protocol utilised for an LSP allows a mid-point
or tail device to be aware of the LSP (e.g., RSVP-TE), then the
associated sessions are maintained per protocol
    """
    if self.__tunnel is None:
        self.__tunnel = YANGDynClass(base=YANGListType("name",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnel must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__tunnel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnel(self):
    self.__tunnel = YANGDynClass(base=YANGListType("name",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  tunnel = __builtin__.property(_get_tunnel, _set_tunnel)


  _pyangbind_elements = {'tunnel': tunnel, }


