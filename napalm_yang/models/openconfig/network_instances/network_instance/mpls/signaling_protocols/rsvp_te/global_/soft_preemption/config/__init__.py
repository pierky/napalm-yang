
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/global/soft-preemption/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to RSVP
soft preemption support
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__enable','__soft_preemption_timeout',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enable = None
    self.__soft_preemption_timeout = None

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
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'rsvp-te', u'global', u'soft-preemption', u'config']

  def _initialized_enable(self):
    return self.__enable is not None

  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/soft_preemption/config/enable (boolean)

    YANG Description: Enables soft preemption on a node.
    """
    if self.__enable is None:
        self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/soft_preemption/config/enable (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.

    YANG Description: Enables soft preemption on a node.
    """
    if self.__enable is None:
        self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _initialized_soft_preemption_timeout(self):
    return self.__soft_preemption_timeout is not None

  def _get_soft_preemption_timeout(self):
    """
    Getter method for soft_preemption_timeout, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/soft_preemption/config/soft_preemption_timeout (uint16)

    YANG Description: Timeout value for soft preemption to revert
to hard preemption. The default timeout for
soft-preemption is 30 seconds - after which
the local system reverts to hard pre-emption.
    """
    if self.__soft_preemption_timeout is None:
        self.__soft_preemption_timeout = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..max']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(30), is_leaf=True, yang_name="soft-preemption-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)
    return self.__soft_preemption_timeout
      
  def _set_soft_preemption_timeout(self, v, load=False):
    """
    Setter method for soft_preemption_timeout, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/soft_preemption/config/soft_preemption_timeout (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_soft_preemption_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_soft_preemption_timeout() directly.

    YANG Description: Timeout value for soft preemption to revert
to hard preemption. The default timeout for
soft-preemption is 30 seconds - after which
the local system reverts to hard pre-emption.
    """
    if self.__soft_preemption_timeout is None:
        self.__soft_preemption_timeout = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..max']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(30), is_leaf=True, yang_name="soft-preemption-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..max']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(30), is_leaf=True, yang_name="soft-preemption-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """soft_preemption_timeout must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..max']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(30), is_leaf=True, yang_name="soft-preemption-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)""",
        })

    self.__soft_preemption_timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_soft_preemption_timeout(self):
    self.__soft_preemption_timeout = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..max']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(30), is_leaf=True, yang_name="soft-preemption-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)

  enable = __builtin__.property(_get_enable, _set_enable)
  soft_preemption_timeout = __builtin__.property(_get_soft_preemption_timeout, _set_soft_preemption_timeout)


  _pyangbind_elements = {'enable': enable, 'soft_preemption_timeout': soft_preemption_timeout, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/global/soft-preemption/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to RSVP
soft preemption support
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__enable','__soft_preemption_timeout',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enable = None
    self.__soft_preemption_timeout = None

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
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'rsvp-te', u'global', u'soft-preemption', u'config']

  def _initialized_enable(self):
    return self.__enable is not None

  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/soft_preemption/config/enable (boolean)

    YANG Description: Enables soft preemption on a node.
    """
    if self.__enable is None:
        self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/soft_preemption/config/enable (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.

    YANG Description: Enables soft preemption on a node.
    """
    if self.__enable is None:
        self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _initialized_soft_preemption_timeout(self):
    return self.__soft_preemption_timeout is not None

  def _get_soft_preemption_timeout(self):
    """
    Getter method for soft_preemption_timeout, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/soft_preemption/config/soft_preemption_timeout (uint16)

    YANG Description: Timeout value for soft preemption to revert
to hard preemption. The default timeout for
soft-preemption is 30 seconds - after which
the local system reverts to hard pre-emption.
    """
    if self.__soft_preemption_timeout is None:
        self.__soft_preemption_timeout = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..max']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(30), is_leaf=True, yang_name="soft-preemption-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)
    return self.__soft_preemption_timeout
      
  def _set_soft_preemption_timeout(self, v, load=False):
    """
    Setter method for soft_preemption_timeout, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/soft_preemption/config/soft_preemption_timeout (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_soft_preemption_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_soft_preemption_timeout() directly.

    YANG Description: Timeout value for soft preemption to revert
to hard preemption. The default timeout for
soft-preemption is 30 seconds - after which
the local system reverts to hard pre-emption.
    """
    if self.__soft_preemption_timeout is None:
        self.__soft_preemption_timeout = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..max']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(30), is_leaf=True, yang_name="soft-preemption-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..max']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(30), is_leaf=True, yang_name="soft-preemption-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """soft_preemption_timeout must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..max']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(30), is_leaf=True, yang_name="soft-preemption-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)""",
        })

    self.__soft_preemption_timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_soft_preemption_timeout(self):
    self.__soft_preemption_timeout = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..max']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(30), is_leaf=True, yang_name="soft-preemption-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=True)

  enable = __builtin__.property(_get_enable, _set_enable)
  soft_preemption_timeout = __builtin__.property(_get_soft_preemption_timeout, _set_soft_preemption_timeout)


  _pyangbind_elements = {'enable': enable, 'soft_preemption_timeout': soft_preemption_timeout, }


