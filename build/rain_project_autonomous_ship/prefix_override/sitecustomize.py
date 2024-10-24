import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rain/pointpillars_ws/install/rain_project_autonomous_ship'
