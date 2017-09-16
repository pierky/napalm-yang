
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

from . import vlan
class vlans(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-vlan - based on the path /vlans. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for VLAN configuration and state
variables
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__vlan',)

  _yang_name = 'vlans'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vlan = None

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
      return [u'vlans']

  def _initialized_vlan(self):
    return self.__vlan is not None

  def _get_vlan(self):
    """
    Getter method for vlan, mapped from YANG variable /vlans/vlan (list)

    YANG Description: Configured VLANs keyed by id
    """
    if self.__vlan is None:
        self.__vlan = YANGDynClass(base=YANGListType("vlan_id",vlan.vlan, yang_name="vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions=None), is_container='list', yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='list', is_config=True)
    return self.__vlan
      
  def _set_vlan(self, v, load=False):
    """
    Setter method for vlan, mapped from YANG variable /vlans/vlan (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan() directly.

    YANG Description: Configured VLANs keyed by id
    """
    if self.__vlan is None:
        self.__vlan = YANGDynClass(base=YANGListType("vlan_id",vlan.vlan, yang_name="vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions=None), is_container='list', yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='list', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("vlan_id",vlan.vlan, yang_name="vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions=None), is_container='list', yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vlan_id",vlan.vlan, yang_name="vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions=None), is_container='list', yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='list', is_config=True)""",
        })

    self.__vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan(self):
    self.__vlan = YANGDynClass(base=YANGListType("vlan_id",vlan.vlan, yang_name="vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions=None), is_container='list', yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='list', is_config=True)

  vlan = __builtin__.property(_get_vlan, _set_vlan)


  _pyangbind_elements = {'vlan': vlan, }


