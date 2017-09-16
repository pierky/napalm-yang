
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
  from YANG module openconfig-system - based on the path /system/aaa/authorization/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for authorization based on AAA
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__authorization_method',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__authorization_method = None

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
      return [u'system', u'aaa', u'authorization', u'state']

  def _initialized_authorization_method(self):
    return self.__authorization_method is not None

  def _get_authorization_method(self):
    """
    Getter method for authorization_method, mapped from YANG variable /system/aaa/authorization/state/authorization_method (union)

    YANG Description: Ordered list of methods for authorizing commands.  The first
method that provides a response (positive or negative) should
be used.  The list may contain a well-defined method such
as the set of all TACACS or RADIUS servers, or the name of
a defined AAA server group.  The system must validate
that the named server group exists.
    """
    if self.__authorization_method is None:
        self.__authorization_method = YANGDynClass(base=TypedListType(allowed_type=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'RADIUS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:LOCAL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:TACACS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:RADIUS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'LOCAL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'TACACS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}},),unicode,]), is_leaf=False, yang_name="authorization-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='union', is_config=False)
    return self.__authorization_method
      
  def _set_authorization_method(self, v, load=False):
    """
    Setter method for authorization_method, mapped from YANG variable /system/aaa/authorization/state/authorization_method (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authorization_method is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authorization_method() directly.

    YANG Description: Ordered list of methods for authorizing commands.  The first
method that provides a response (positive or negative) should
be used.  The list may contain a well-defined method such
as the set of all TACACS or RADIUS servers, or the name of
a defined AAA server group.  The system must validate
that the named server group exists.
    """
    if self.__authorization_method is None:
        self.__authorization_method = YANGDynClass(base=TypedListType(allowed_type=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'RADIUS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:LOCAL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:TACACS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:RADIUS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'LOCAL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'TACACS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}},),unicode,]), is_leaf=False, yang_name="authorization-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='union', is_config=False)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'RADIUS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:LOCAL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:TACACS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:RADIUS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'LOCAL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'TACACS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}},),unicode,]), is_leaf=False, yang_name="authorization-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authorization_method must be of a type compatible with union""",
          'defined-type': "openconfig-system:union",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'RADIUS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:LOCAL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:TACACS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:RADIUS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'LOCAL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'TACACS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}},),unicode,]), is_leaf=False, yang_name="authorization-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='union', is_config=False)""",
        })

    self.__authorization_method = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authorization_method(self):
    self.__authorization_method = YANGDynClass(base=TypedListType(allowed_type=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'RADIUS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:LOCAL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:TACACS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'oc-aaa-types:RADIUS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'LOCAL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}, u'TACACS_ALL': {'@namespace': u'http://openconfig.net/yang/aaa/types', '@module': u'openconfig-aaa-types'}},),unicode,]), is_leaf=False, yang_name="authorization-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='union', is_config=False)

  authorization_method = __builtin__.property(_get_authorization_method)


  _pyangbind_elements = {'authorization_method': authorization_method, }


