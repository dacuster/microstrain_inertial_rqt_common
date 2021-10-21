import os

# Bit of a hack here, but this is the easiest way to find out the ROS version that I am aware of
_MICROSTRAIN_ROS_VERISON = 0
try:
  import rospy
  _MICROSTRAIN_ROS_VERISON = 1
except ModuleNotFoundError:
  pass
try:
  import rclpy
  _MICROSTRAIN_ROS_VERISON = 2
except ModuleNotFoundError:
  pass
if _MICROSTRAIN_ROS_VERISON == 0:
  raise Exception("Unable to find ROS1 or ROS2 library")

# ROS version specific imports
if _MICROSTRAIN_ROS_VERISON == 1:
  import rospkg
elif _MICROSTRAIN_ROS_VERISON == 2:
  from ament_index_python.packages import get_package_share_directory

_PACKAGE_NAME = "microstrain_inertial_quickview"
_RESOURCE_DIR_NAME = "microstrain_inertial_quickview_common/resource"
if _MICROSTRAIN_ROS_VERISON == 1:
  _PACKAGE_RESOURCE_DIR = os.path.join(rospkg.RosPack().get_path(_PACKAGE_NAME), _RESOURCE_DIR_NAME)
elif _MICROSTRAIN_ROS_VERISON == 2:
  _PACKAGE_RESOURCE_DIR = os.path.join(get_package_share_directory(_PACKAGE_NAME), _RESOURCE_DIR_NAME)

_DEFAULT_MESSAGE_TIMEOUT = 5
_DEFAULT_POLL_INTERVAL = 1.0
_DEFAULT_VAL = None
_DEFAULT_STR = "Unavailable"

_UNIT_DEGREES = u"\N{DEGREE SIGN}"
_UNIT_METERS = "m"
_UNIT_RADIANS = "rad"
_UNIT_GS = "g"
_UNIT_METERS_PER_SEC = "m/s"
_UNIT_RADIANS_PER_SEC = "rad/s"
_UNIT_GUASSIAN = "guass"

_ICON_TEMPLATE = '<html><img height="%%d" width="%%d" src="%s" /></html>'
_ICON_FILE_TEMPLATE = 'icon-%s-%s'
_ICON_COLOR_GREY = "grey"
_ICON_COLOR_RED = "red"
_ICON_COLOR_YELLOW = "yellow"
_ICON_COLOR_GREEN = "green"
_ICON_COLOR_BLUE = "blue"
_ICON_COLOR_TEAL = "teal"
_ICON_CHECKED = "checked"
_ICON_UNCHECKED = "unchecked"
_ICON_SIZE_SMALL = (25, 25)
_ICON_SIZE_MEDIUM = (75, 75)

def _FORM_ICON_STRING(color, size, checked):
  icon_file = os.path.join(_PACKAGE_RESOURCE_DIR, _ICON_FILE_TEMPLATE % (color, checked))
  icon_tag_no_size = _ICON_TEMPLATE % icon_file
  return icon_tag_no_size % size

_ICON_GREY_CHECKED_SMALL = _FORM_ICON_STRING(_ICON_COLOR_GREY, _ICON_SIZE_SMALL, _ICON_CHECKED)
_ICON_RED_CHECKED_SMALL = _FORM_ICON_STRING(_ICON_COLOR_RED, _ICON_SIZE_SMALL, _ICON_CHECKED)
_ICON_YELLOW_CHECKED_SMALL = _FORM_ICON_STRING(_ICON_COLOR_YELLOW, _ICON_SIZE_SMALL, _ICON_CHECKED)
_ICON_GREEN_CHECKED_SMALL = _FORM_ICON_STRING(_ICON_COLOR_GREEN, _ICON_SIZE_SMALL, _ICON_CHECKED)
_ICON_BLUE_CHECKED_SMALL = _FORM_ICON_STRING(_ICON_COLOR_BLUE, _ICON_SIZE_SMALL, _ICON_CHECKED)
_ICON_TEAL_CHECKED_SMALL = _FORM_ICON_STRING(_ICON_COLOR_TEAL, _ICON_SIZE_SMALL, _ICON_CHECKED)

_ICON_GREY_UNCHECKED_SMALL = _FORM_ICON_STRING(_ICON_COLOR_GREY, _ICON_SIZE_SMALL, _ICON_UNCHECKED)
_ICON_RED_UNCHECKED_SMALL = _FORM_ICON_STRING(_ICON_COLOR_RED, _ICON_SIZE_SMALL, _ICON_UNCHECKED)
_ICON_YELLOW_UNCHECKED_SMALL = _FORM_ICON_STRING(_ICON_COLOR_YELLOW, _ICON_SIZE_SMALL, _ICON_UNCHECKED)
_ICON_GREEN_UNCHECKED_SMALL = _FORM_ICON_STRING(_ICON_COLOR_GREEN, _ICON_SIZE_SMALL, _ICON_UNCHECKED)
_ICON_BLUE_UNCHECKED_SMALL = _FORM_ICON_STRING(_ICON_COLOR_BLUE, _ICON_SIZE_SMALL, _ICON_UNCHECKED)
_ICON_TEAL_UNCHECKED_SMALL = _FORM_ICON_STRING(_ICON_COLOR_TEAL, _ICON_SIZE_SMALL, _ICON_UNCHECKED)

_ICON_GREY_CHECKED_MEDIUM = _FORM_ICON_STRING(_ICON_COLOR_GREY, _ICON_SIZE_MEDIUM, _ICON_CHECKED)
_ICON_RED_CHECKED_MEDIUM = _FORM_ICON_STRING(_ICON_COLOR_RED, _ICON_SIZE_MEDIUM, _ICON_CHECKED)
_ICON_YELLOW_CHECKED_MEDIUM = _FORM_ICON_STRING(_ICON_COLOR_YELLOW, _ICON_SIZE_MEDIUM, _ICON_CHECKED)
_ICON_GREEN_CHECKED_MEDIUM = _FORM_ICON_STRING(_ICON_COLOR_GREEN, _ICON_SIZE_MEDIUM, _ICON_CHECKED)
_ICON_BLUE_CHECKED_MEDIUM = _FORM_ICON_STRING(_ICON_COLOR_BLUE, _ICON_SIZE_MEDIUM, _ICON_CHECKED)
_ICON_TEAL_CHECKED_MEDIUM = _FORM_ICON_STRING(_ICON_COLOR_TEAL, _ICON_SIZE_MEDIUM, _ICON_CHECKED)

_ICON_GREY_UNCHECKED_MEDIUM = _FORM_ICON_STRING(_ICON_COLOR_GREY, _ICON_SIZE_MEDIUM, _ICON_UNCHECKED)
_ICON_RED_UNCHECKED_MEDIUM = _FORM_ICON_STRING(_ICON_COLOR_RED, _ICON_SIZE_MEDIUM, _ICON_UNCHECKED)
_ICON_YELLOW_UNCHECKED_MEDIUM = _FORM_ICON_STRING(_ICON_COLOR_YELLOW, _ICON_SIZE_MEDIUM, _ICON_UNCHECKED)
_ICON_GREEN_UNCHECKED_MEDIUM = _FORM_ICON_STRING(_ICON_COLOR_GREEN, _ICON_SIZE_MEDIUM, _ICON_UNCHECKED)
_ICON_BLUE_UNCHECKED_MEDIUM = _FORM_ICON_STRING(_ICON_COLOR_BLUE, _ICON_SIZE_MEDIUM, _ICON_UNCHECKED)
_ICON_TEAL_UNCHECKED_MEDIUM = _FORM_ICON_STRING(_ICON_COLOR_TEAL, _ICON_SIZE_MEDIUM, _ICON_UNCHECKED)
