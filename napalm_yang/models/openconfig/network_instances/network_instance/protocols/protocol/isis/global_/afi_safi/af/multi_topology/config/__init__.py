
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/global/afi-safi/af/multi-topology/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines AFI-SAFI multi-topology configuration
parameters
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__afi_name','__safi_name',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__safi_name = None
    self.__afi_name = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'afi-safi', u'af', u'multi-topology', u'config']

  def _initialized_afi_name(self):
    return self.__afi_name is not None

  def _get_afi_name(self):
    """
    Getter method for afi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/multi_topology/config/afi_name (identityref)

    YANG Description: Address-family type.
    """
    if self.__afi_name is None:
        self.__afi_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-isis-types:IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    return self.__afi_name
      
  def _set_afi_name(self, v, load=False):
    """
    Setter method for afi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/multi_topology/config/afi_name (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_afi_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_afi_name() directly.

    YANG Description: Address-family type.
    """
    if self.__afi_name is None:
        self.__afi_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-isis-types:IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-isis-types:IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """afi_name must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-isis-types:IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)""",
        })

    self.__afi_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_afi_name(self):
    self.__afi_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-isis-types:IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)


  def _initialized_safi_name(self):
    return self.__safi_name is not None

  def _get_safi_name(self):
    """
    Getter method for safi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/multi_topology/config/safi_name (identityref)

    YANG Description: Subsequent address-family type.
    """
    if self.__safi_name is None:
        self.__safi_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    return self.__safi_name
      
  def _set_safi_name(self, v, load=False):
    """
    Setter method for safi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/multi_topology/config/safi_name (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_safi_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_safi_name() directly.

    YANG Description: Subsequent address-family type.
    """
    if self.__safi_name is None:
        self.__safi_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """safi_name must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)""",
        })

    self.__safi_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_safi_name(self):
    self.__safi_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)

  afi_name = __builtin__.property(_get_afi_name, _set_afi_name)
  safi_name = __builtin__.property(_get_safi_name, _set_safi_name)


  _pyangbind_elements = {'afi_name': afi_name, 'safi_name': safi_name, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/global/afi-safi/af/multi-topology/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines AFI-SAFI multi-topology configuration
parameters
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__afi_name','__safi_name',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__safi_name = None
    self.__afi_name = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'afi-safi', u'af', u'multi-topology', u'config']

  def _initialized_afi_name(self):
    return self.__afi_name is not None

  def _get_afi_name(self):
    """
    Getter method for afi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/multi_topology/config/afi_name (identityref)

    YANG Description: Address-family type.
    """
    if self.__afi_name is None:
        self.__afi_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-isis-types:IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    return self.__afi_name
      
  def _set_afi_name(self, v, load=False):
    """
    Setter method for afi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/multi_topology/config/afi_name (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_afi_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_afi_name() directly.

    YANG Description: Address-family type.
    """
    if self.__afi_name is None:
        self.__afi_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-isis-types:IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-isis-types:IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """afi_name must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-isis-types:IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)""",
        })

    self.__afi_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_afi_name(self):
    self.__afi_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-isis-types:IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)


  def _initialized_safi_name(self):
    return self.__safi_name is not None

  def _get_safi_name(self):
    """
    Getter method for safi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/multi_topology/config/safi_name (identityref)

    YANG Description: Subsequent address-family type.
    """
    if self.__safi_name is None:
        self.__safi_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    return self.__safi_name
      
  def _set_safi_name(self, v, load=False):
    """
    Setter method for safi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/multi_topology/config/safi_name (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_safi_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_safi_name() directly.

    YANG Description: Subsequent address-family type.
    """
    if self.__safi_name is None:
        self.__safi_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """safi_name must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)""",
        })

    self.__safi_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_safi_name(self):
    self.__safi_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'MULTICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}, u'oc-isis-types:UNICAST': {'@namespace': u'http://openconfig.net/yang/isis-types', '@module': u'openconfig-isis-types'}},), is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)

  afi_name = __builtin__.property(_get_afi_name, _set_afi_name)
  safi_name = __builtin__.property(_get_safi_name, _set_safi_name)


  _pyangbind_elements = {'afi_name': afi_name, 'safi_name': safi_name, }


