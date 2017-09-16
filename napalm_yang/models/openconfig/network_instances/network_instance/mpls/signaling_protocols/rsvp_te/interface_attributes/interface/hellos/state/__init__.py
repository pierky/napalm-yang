
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/interface-attributes/interface/hellos/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information associated with RSVP hellos
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__hello_interval','__refresh_reduction',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__refresh_reduction = None
    self.__hello_interval = None

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
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'rsvp-te', u'interface-attributes', u'interface', u'hellos', u'state']

  def _initialized_hello_interval(self):
    return self.__hello_interval is not None

  def _get_hello_interval(self):
    """
    Getter method for hello_interval, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/hellos/state/hello_interval (uint16)

    YANG Description: set the interval in ms between RSVP hello
messages
    """
    if self.__hello_interval is None:
        self.__hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1000..60000']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(9000), is_leaf=True, yang_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    return self.__hello_interval
      
  def _set_hello_interval(self, v, load=False):
    """
    Setter method for hello_interval, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/hellos/state/hello_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_interval() directly.

    YANG Description: set the interval in ms between RSVP hello
messages
    """
    if self.__hello_interval is None:
        self.__hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1000..60000']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(9000), is_leaf=True, yang_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1000..60000']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(9000), is_leaf=True, yang_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello_interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1000..60000']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(9000), is_leaf=True, yang_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)""",
        })

    self.__hello_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello_interval(self):
    self.__hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1000..60000']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(9000), is_leaf=True, yang_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)


  def _initialized_refresh_reduction(self):
    return self.__refresh_reduction is not None

  def _get_refresh_reduction(self):
    """
    Getter method for refresh_reduction, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/hellos/state/refresh_reduction (boolean)

    YANG Description: enables all RSVP refresh reduction message
bundling, RSVP message ID, reliable message delivery
and summary refresh
    """
    if self.__refresh_reduction is None:
        self.__refresh_reduction = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="refresh-reduction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    return self.__refresh_reduction
      
  def _set_refresh_reduction(self, v, load=False):
    """
    Setter method for refresh_reduction, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/hellos/state/refresh_reduction (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_refresh_reduction is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_refresh_reduction() directly.

    YANG Description: enables all RSVP refresh reduction message
bundling, RSVP message ID, reliable message delivery
and summary refresh
    """
    if self.__refresh_reduction is None:
        self.__refresh_reduction = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="refresh-reduction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="refresh-reduction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """refresh_reduction must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="refresh-reduction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__refresh_reduction = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_refresh_reduction(self):
    self.__refresh_reduction = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="refresh-reduction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  hello_interval = __builtin__.property(_get_hello_interval)
  refresh_reduction = __builtin__.property(_get_refresh_reduction)


  _pyangbind_elements = {'hello_interval': hello_interval, 'refresh_reduction': refresh_reduction, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/interface-attributes/interface/hellos/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information associated with RSVP hellos
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__hello_interval','__refresh_reduction',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__refresh_reduction = None
    self.__hello_interval = None

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
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'rsvp-te', u'interface-attributes', u'interface', u'hellos', u'state']

  def _initialized_hello_interval(self):
    return self.__hello_interval is not None

  def _get_hello_interval(self):
    """
    Getter method for hello_interval, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/hellos/state/hello_interval (uint16)

    YANG Description: set the interval in ms between RSVP hello
messages
    """
    if self.__hello_interval is None:
        self.__hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1000..60000']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(9000), is_leaf=True, yang_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    return self.__hello_interval
      
  def _set_hello_interval(self, v, load=False):
    """
    Setter method for hello_interval, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/hellos/state/hello_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_interval() directly.

    YANG Description: set the interval in ms between RSVP hello
messages
    """
    if self.__hello_interval is None:
        self.__hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1000..60000']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(9000), is_leaf=True, yang_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1000..60000']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(9000), is_leaf=True, yang_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello_interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1000..60000']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(9000), is_leaf=True, yang_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)""",
        })

    self.__hello_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello_interval(self):
    self.__hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1000..60000']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(9000), is_leaf=True, yang_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)


  def _initialized_refresh_reduction(self):
    return self.__refresh_reduction is not None

  def _get_refresh_reduction(self):
    """
    Getter method for refresh_reduction, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/hellos/state/refresh_reduction (boolean)

    YANG Description: enables all RSVP refresh reduction message
bundling, RSVP message ID, reliable message delivery
and summary refresh
    """
    if self.__refresh_reduction is None:
        self.__refresh_reduction = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="refresh-reduction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    return self.__refresh_reduction
      
  def _set_refresh_reduction(self, v, load=False):
    """
    Setter method for refresh_reduction, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/hellos/state/refresh_reduction (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_refresh_reduction is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_refresh_reduction() directly.

    YANG Description: enables all RSVP refresh reduction message
bundling, RSVP message ID, reliable message delivery
and summary refresh
    """
    if self.__refresh_reduction is None:
        self.__refresh_reduction = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="refresh-reduction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="refresh-reduction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """refresh_reduction must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="refresh-reduction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__refresh_reduction = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_refresh_reduction(self):
    self.__refresh_reduction = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="refresh-reduction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  hello_interval = __builtin__.property(_get_hello_interval)
  refresh_reduction = __builtin__.property(_get_refresh_reduction)


  _pyangbind_elements = {'hello_interval': hello_interval, 'refresh_reduction': refresh_reduction, }


