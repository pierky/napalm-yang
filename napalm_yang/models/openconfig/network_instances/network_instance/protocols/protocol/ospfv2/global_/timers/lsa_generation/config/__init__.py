
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/global/timers/lsa-generation/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the generation of
LSAs by the local system
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__initial_delay','__maximum_delay',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__initial_delay = None
    self.__maximum_delay = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'global', u'timers', u'lsa-generation', u'config']

  def _initialized_initial_delay(self):
    return self.__initial_delay is not None

  def _get_initial_delay(self):
    """
    Getter method for initial_delay, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/timers/lsa_generation/config/initial_delay (uint32)

    YANG Description: The value of this leaf specifies the time between the first
time an LSA is generated and advertised and the subsequent
generation of that LSA.
    """
    if self.__initial_delay is None:
        self.__initial_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="initial-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    return self.__initial_delay
      
  def _set_initial_delay(self, v, load=False):
    """
    Setter method for initial_delay, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/timers/lsa_generation/config/initial_delay (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_initial_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_initial_delay() directly.

    YANG Description: The value of this leaf specifies the time between the first
time an LSA is generated and advertised and the subsequent
generation of that LSA.
    """
    if self.__initial_delay is None:
        self.__initial_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="initial-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="initial-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """initial_delay must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="initial-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)""",
        })

    self.__initial_delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_initial_delay(self):
    self.__initial_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="initial-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)


  def _initialized_maximum_delay(self):
    return self.__maximum_delay is not None

  def _get_maximum_delay(self):
    """
    Getter method for maximum_delay, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/timers/lsa_generation/config/maximum_delay (uint32)

    YANG Description: The value of this leaf specifies the maximum time between the
generation of an LSA and the subsequent re-generation of that
LSA. This value is used in implementations that support
increasing delay between generation of an LSA
    """
    if self.__maximum_delay is None:
        self.__maximum_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="maximum-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    return self.__maximum_delay
      
  def _set_maximum_delay(self, v, load=False):
    """
    Setter method for maximum_delay, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/timers/lsa_generation/config/maximum_delay (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_maximum_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_maximum_delay() directly.

    YANG Description: The value of this leaf specifies the maximum time between the
generation of an LSA and the subsequent re-generation of that
LSA. This value is used in implementations that support
increasing delay between generation of an LSA
    """
    if self.__maximum_delay is None:
        self.__maximum_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="maximum-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="maximum-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """maximum_delay must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="maximum-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)""",
        })

    self.__maximum_delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_maximum_delay(self):
    self.__maximum_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="maximum-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)

  initial_delay = __builtin__.property(_get_initial_delay, _set_initial_delay)
  maximum_delay = __builtin__.property(_get_maximum_delay, _set_maximum_delay)


  _pyangbind_elements = {'initial_delay': initial_delay, 'maximum_delay': maximum_delay, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/global/timers/lsa-generation/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the generation of
LSAs by the local system
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__initial_delay','__maximum_delay',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__initial_delay = None
    self.__maximum_delay = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'global', u'timers', u'lsa-generation', u'config']

  def _initialized_initial_delay(self):
    return self.__initial_delay is not None

  def _get_initial_delay(self):
    """
    Getter method for initial_delay, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/timers/lsa_generation/config/initial_delay (uint32)

    YANG Description: The value of this leaf specifies the time between the first
time an LSA is generated and advertised and the subsequent
generation of that LSA.
    """
    if self.__initial_delay is None:
        self.__initial_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="initial-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    return self.__initial_delay
      
  def _set_initial_delay(self, v, load=False):
    """
    Setter method for initial_delay, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/timers/lsa_generation/config/initial_delay (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_initial_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_initial_delay() directly.

    YANG Description: The value of this leaf specifies the time between the first
time an LSA is generated and advertised and the subsequent
generation of that LSA.
    """
    if self.__initial_delay is None:
        self.__initial_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="initial-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="initial-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """initial_delay must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="initial-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)""",
        })

    self.__initial_delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_initial_delay(self):
    self.__initial_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="initial-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)


  def _initialized_maximum_delay(self):
    return self.__maximum_delay is not None

  def _get_maximum_delay(self):
    """
    Getter method for maximum_delay, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/timers/lsa_generation/config/maximum_delay (uint32)

    YANG Description: The value of this leaf specifies the maximum time between the
generation of an LSA and the subsequent re-generation of that
LSA. This value is used in implementations that support
increasing delay between generation of an LSA
    """
    if self.__maximum_delay is None:
        self.__maximum_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="maximum-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    return self.__maximum_delay
      
  def _set_maximum_delay(self, v, load=False):
    """
    Setter method for maximum_delay, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/timers/lsa_generation/config/maximum_delay (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_maximum_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_maximum_delay() directly.

    YANG Description: The value of this leaf specifies the maximum time between the
generation of an LSA and the subsequent re-generation of that
LSA. This value is used in implementations that support
increasing delay between generation of an LSA
    """
    if self.__maximum_delay is None:
        self.__maximum_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="maximum-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="maximum-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """maximum_delay must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="maximum-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)""",
        })

    self.__maximum_delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_maximum_delay(self):
    self.__maximum_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="maximum-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)

  initial_delay = __builtin__.property(_get_initial_delay, _set_initial_delay)
  maximum_delay = __builtin__.property(_get_maximum_delay, _set_maximum_delay)


  _pyangbind_elements = {'initial_delay': initial_delay, 'maximum_delay': maximum_delay, }


