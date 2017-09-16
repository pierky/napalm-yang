
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/lsa-filter/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state parameters relating to filtering
LSAs on the specified interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__all',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__all = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'interfaces', u'interface', u'lsa-filter', u'state']

  def _initialized_all(self):
    return self.__all is not None

  def _get_all(self):
    """
    Getter method for all, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/lsa_filter/state/all (boolean)

    YANG Description: When this leaf is set to true, all LSAs should be
filtered to the neighbours with whom adjacencies are
formed on the interface.
    """
    if self.__all is None:
        self.__all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    return self.__all
      
  def _set_all(self, v, load=False):
    """
    Setter method for all, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/lsa_filter/state/all (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_all is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_all() directly.

    YANG Description: When this leaf is set to true, all LSAs should be
filtered to the neighbours with whom adjacencies are
formed on the interface.
    """
    if self.__all is None:
        self.__all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """all must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__all = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_all(self):
    self.__all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  all = __builtin__.property(_get_all)


  _pyangbind_elements = {'all': all, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/lsa-filter/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state parameters relating to filtering
LSAs on the specified interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__all',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__all = None

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'interfaces', u'interface', u'lsa-filter', u'state']

  def _initialized_all(self):
    return self.__all is not None

  def _get_all(self):
    """
    Getter method for all, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/lsa_filter/state/all (boolean)

    YANG Description: When this leaf is set to true, all LSAs should be
filtered to the neighbours with whom adjacencies are
formed on the interface.
    """
    if self.__all is None:
        self.__all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    return self.__all
      
  def _set_all(self, v, load=False):
    """
    Setter method for all, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/lsa_filter/state/all (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_all is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_all() directly.

    YANG Description: When this leaf is set to true, all LSAs should be
filtered to the neighbours with whom adjacencies are
formed on the interface.
    """
    if self.__all is None:
        self.__all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """all must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__all = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_all(self):
    self.__all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  all = __builtin__.property(_get_all)


  _pyangbind_elements = {'all': all, }


