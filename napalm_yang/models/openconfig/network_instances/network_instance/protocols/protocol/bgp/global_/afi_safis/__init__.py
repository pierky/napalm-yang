
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

from . import afi_safi
class afi_safis(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/afi-safis. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Address family specific configuration
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__afi_safi',)

  _yang_name = 'afi-safis'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__afi_safi = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'global', u'afi-safis']

  def _initialized_afi_safi(self):
    return self.__afi_safi is not None

  def _get_afi_safi(self):
    """
    Getter method for afi_safi, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi (list)

    YANG Description: AFI,SAFI configuration available for the
neighbour or group
    """
    if self.__afi_safi is None:
        self.__afi_safi = YANGDynClass(base=YANGListType("afi_safi_name",afi_safi.afi_safi, yang_name="afi-safi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-safi-name', extensions=None), is_container='list', yang_name="afi-safi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    return self.__afi_safi
      
  def _set_afi_safi(self, v, load=False):
    """
    Setter method for afi_safi, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_afi_safi is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_afi_safi() directly.

    YANG Description: AFI,SAFI configuration available for the
neighbour or group
    """
    if self.__afi_safi is None:
        self.__afi_safi = YANGDynClass(base=YANGListType("afi_safi_name",afi_safi.afi_safi, yang_name="afi-safi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-safi-name', extensions=None), is_container='list', yang_name="afi-safi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("afi_safi_name",afi_safi.afi_safi, yang_name="afi-safi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-safi-name', extensions=None), is_container='list', yang_name="afi-safi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """afi_safi must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("afi_safi_name",afi_safi.afi_safi, yang_name="afi-safi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-safi-name', extensions=None), is_container='list', yang_name="afi-safi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__afi_safi = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_afi_safi(self):
    self.__afi_safi = YANGDynClass(base=YANGListType("afi_safi_name",afi_safi.afi_safi, yang_name="afi-safi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-safi-name', extensions=None), is_container='list', yang_name="afi-safi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  afi_safi = __builtin__.property(_get_afi_safi, _set_afi_safi)


  _pyangbind_elements = {'afi_safi': afi_safi, }


from . import afi_safi
class afi_safis(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/afi-safis. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Address family specific configuration
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__afi_safi',)

  _yang_name = 'afi-safis'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__afi_safi = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'global', u'afi-safis']

  def _initialized_afi_safi(self):
    return self.__afi_safi is not None

  def _get_afi_safi(self):
    """
    Getter method for afi_safi, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi (list)

    YANG Description: AFI,SAFI configuration available for the
neighbour or group
    """
    if self.__afi_safi is None:
        self.__afi_safi = YANGDynClass(base=YANGListType("afi_safi_name",afi_safi.afi_safi, yang_name="afi-safi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-safi-name', extensions=None), is_container='list', yang_name="afi-safi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    return self.__afi_safi
      
  def _set_afi_safi(self, v, load=False):
    """
    Setter method for afi_safi, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_afi_safi is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_afi_safi() directly.

    YANG Description: AFI,SAFI configuration available for the
neighbour or group
    """
    if self.__afi_safi is None:
        self.__afi_safi = YANGDynClass(base=YANGListType("afi_safi_name",afi_safi.afi_safi, yang_name="afi-safi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-safi-name', extensions=None), is_container='list', yang_name="afi-safi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("afi_safi_name",afi_safi.afi_safi, yang_name="afi-safi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-safi-name', extensions=None), is_container='list', yang_name="afi-safi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """afi_safi must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("afi_safi_name",afi_safi.afi_safi, yang_name="afi-safi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-safi-name', extensions=None), is_container='list', yang_name="afi-safi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__afi_safi = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_afi_safi(self):
    self.__afi_safi = YANGDynClass(base=YANGListType("afi_safi_name",afi_safi.afi_safi, yang_name="afi-safi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-safi-name', extensions=None), is_container='list', yang_name="afi-safi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  afi_safi = __builtin__.property(_get_afi_safi, _set_afi_safi)


  _pyangbind_elements = {'afi_safi': afi_safi, }


