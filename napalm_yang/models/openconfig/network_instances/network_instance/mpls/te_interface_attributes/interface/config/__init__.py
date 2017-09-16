
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/te-interface-attributes/interface/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters related to TE interfaces:
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interface_id','__te_metric','__srlg_membership','__admin_group',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__te_metric = None
    self.__admin_group = None
    self.__srlg_membership = None
    self.__interface_id = None

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
      return [u'network-instances', u'network-instance', u'mpls', u'te-interface-attributes', u'interface', u'config']

  def _initialized_interface_id(self):
    return self.__interface_id is not None

  def _get_interface_id(self):
    """
    Getter method for interface_id, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface/config/interface_id (oc-if:interface-id)

    YANG Description: Id of the interface
    """
    if self.__interface_id is None:
        self.__interface_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)
    return self.__interface_id
      
  def _set_interface_id(self, v, load=False):
    """
    Setter method for interface_id, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface/config/interface_id (oc-if:interface-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_id() directly.

    YANG Description: Id of the interface
    """
    if self.__interface_id is None:
        self.__interface_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_id must be of a type compatible with oc-if:interface-id""",
          'defined-type': "oc-if:interface-id",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)""",
        })

    self.__interface_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_id(self):
    self.__interface_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)


  def _initialized_te_metric(self):
    return self.__te_metric is not None

  def _get_te_metric(self):
    """
    Getter method for te_metric, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface/config/te_metric (uint32)

    YANG Description: TE specific metric for the link
    """
    if self.__te_metric is None:
        self.__te_metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="te-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    return self.__te_metric
      
  def _set_te_metric(self, v, load=False):
    """
    Setter method for te_metric, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface/config/te_metric (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_te_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_te_metric() directly.

    YANG Description: TE specific metric for the link
    """
    if self.__te_metric is None:
        self.__te_metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="te-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="te-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """te_metric must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="te-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)""",
        })

    self.__te_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_te_metric(self):
    self.__te_metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="te-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)


  def _initialized_srlg_membership(self):
    return self.__srlg_membership is not None

  def _get_srlg_membership(self):
    """
    Getter method for srlg_membership, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface/config/srlg_membership (leafref)

    YANG Description: list of references to named shared risk link groups that the
interface belongs to.
    """
    if self.__srlg_membership is None:
        self.__srlg_membership = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="srlg-membership", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    return self.__srlg_membership
      
  def _set_srlg_membership(self, v, load=False):
    """
    Setter method for srlg_membership, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface/config/srlg_membership (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_srlg_membership is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_srlg_membership() directly.

    YANG Description: list of references to named shared risk link groups that the
interface belongs to.
    """
    if self.__srlg_membership is None:
        self.__srlg_membership = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="srlg-membership", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="srlg-membership", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """srlg_membership must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="srlg-membership", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__srlg_membership = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_srlg_membership(self):
    self.__srlg_membership = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="srlg-membership", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _initialized_admin_group(self):
    return self.__admin_group is not None

  def _get_admin_group(self):
    """
    Getter method for admin_group, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface/config/admin_group (string)

    YANG Description: list of admin groups (by name) on the interface
    """
    if self.__admin_group is None:
        self.__admin_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="admin-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    return self.__admin_group
      
  def _set_admin_group(self, v, load=False):
    """
    Setter method for admin_group, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface/config/admin_group (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_admin_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_admin_group() directly.

    YANG Description: list of admin groups (by name) on the interface
    """
    if self.__admin_group is None:
        self.__admin_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="admin-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="admin-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """admin_group must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="admin-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)""",
        })

    self.__admin_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_admin_group(self):
    self.__admin_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="admin-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)

  interface_id = __builtin__.property(_get_interface_id, _set_interface_id)
  te_metric = __builtin__.property(_get_te_metric, _set_te_metric)
  srlg_membership = __builtin__.property(_get_srlg_membership, _set_srlg_membership)
  admin_group = __builtin__.property(_get_admin_group, _set_admin_group)


  _pyangbind_elements = {'interface_id': interface_id, 'te_metric': te_metric, 'srlg_membership': srlg_membership, 'admin_group': admin_group, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/te-interface-attributes/interface/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters related to TE interfaces:
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interface_id','__te_metric','__srlg_membership','__admin_group',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__te_metric = None
    self.__admin_group = None
    self.__srlg_membership = None
    self.__interface_id = None

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
      return [u'network-instances', u'network-instance', u'mpls', u'te-interface-attributes', u'interface', u'config']

  def _initialized_interface_id(self):
    return self.__interface_id is not None

  def _get_interface_id(self):
    """
    Getter method for interface_id, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface/config/interface_id (oc-if:interface-id)

    YANG Description: Id of the interface
    """
    if self.__interface_id is None:
        self.__interface_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)
    return self.__interface_id
      
  def _set_interface_id(self, v, load=False):
    """
    Setter method for interface_id, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface/config/interface_id (oc-if:interface-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_id() directly.

    YANG Description: Id of the interface
    """
    if self.__interface_id is None:
        self.__interface_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_id must be of a type compatible with oc-if:interface-id""",
          'defined-type': "oc-if:interface-id",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)""",
        })

    self.__interface_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_id(self):
    self.__interface_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)


  def _initialized_te_metric(self):
    return self.__te_metric is not None

  def _get_te_metric(self):
    """
    Getter method for te_metric, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface/config/te_metric (uint32)

    YANG Description: TE specific metric for the link
    """
    if self.__te_metric is None:
        self.__te_metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="te-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    return self.__te_metric
      
  def _set_te_metric(self, v, load=False):
    """
    Setter method for te_metric, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface/config/te_metric (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_te_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_te_metric() directly.

    YANG Description: TE specific metric for the link
    """
    if self.__te_metric is None:
        self.__te_metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="te-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="te-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """te_metric must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="te-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)""",
        })

    self.__te_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_te_metric(self):
    self.__te_metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="te-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)


  def _initialized_srlg_membership(self):
    return self.__srlg_membership is not None

  def _get_srlg_membership(self):
    """
    Getter method for srlg_membership, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface/config/srlg_membership (leafref)

    YANG Description: list of references to named shared risk link groups that the
interface belongs to.
    """
    if self.__srlg_membership is None:
        self.__srlg_membership = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="srlg-membership", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    return self.__srlg_membership
      
  def _set_srlg_membership(self, v, load=False):
    """
    Setter method for srlg_membership, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface/config/srlg_membership (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_srlg_membership is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_srlg_membership() directly.

    YANG Description: list of references to named shared risk link groups that the
interface belongs to.
    """
    if self.__srlg_membership is None:
        self.__srlg_membership = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="srlg-membership", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="srlg-membership", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """srlg_membership must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="srlg-membership", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__srlg_membership = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_srlg_membership(self):
    self.__srlg_membership = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="srlg-membership", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _initialized_admin_group(self):
    return self.__admin_group is not None

  def _get_admin_group(self):
    """
    Getter method for admin_group, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface/config/admin_group (string)

    YANG Description: list of admin groups (by name) on the interface
    """
    if self.__admin_group is None:
        self.__admin_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="admin-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    return self.__admin_group
      
  def _set_admin_group(self, v, load=False):
    """
    Setter method for admin_group, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes/interface/config/admin_group (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_admin_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_admin_group() directly.

    YANG Description: list of admin groups (by name) on the interface
    """
    if self.__admin_group is None:
        self.__admin_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="admin-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="admin-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """admin_group must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="admin-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)""",
        })

    self.__admin_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_admin_group(self):
    self.__admin_group = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="admin-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)

  interface_id = __builtin__.property(_get_interface_id, _set_interface_id)
  te_metric = __builtin__.property(_get_te_metric, _set_te_metric)
  srlg_membership = __builtin__.property(_get_srlg_membership, _set_srlg_membership)
  admin_group = __builtin__.property(_get_admin_group, _set_admin_group)


  _pyangbind_elements = {'interface_id': interface_id, 'te_metric': te_metric, 'srlg_membership': srlg_membership, 'admin_group': admin_group, }


