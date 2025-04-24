import pandas as pd

# Plages HSV simulées pour les couleurs courantes du Mushaf (à ajuster selon ta version)
color_rule_map = pd.DataFrame([
    { 'rule_name': 'Ikhfa', 'hsv_lower': [20, 100, 100], 'hsv_upper': [30, 255, 255], 'pixel_threshold': 500 },
    { 'rule_name': 'Idgham', 'hsv_lower': [35, 100, 100], 'hsv_upper': [45, 255, 255], 'pixel_threshold': 500 },
    { 'rule_name': 'Iqlab', 'hsv_lower': [0, 100, 100],  'hsv_upper': [10, 255, 255], 'pixel_threshold': 500 },
    { 'rule_name': 'Izhar', 'hsv_lower': [50, 100, 100], 'hsv_upper': [70, 255, 255], 'pixel_threshold': 500 },
    { 'rule_name': 'Ghunnah', 'hsv_lower': [90, 100, 100], 'hsv_upper': [110, 255, 255], 'pixel_threshold': 500 },
    { 'rule_name': 'Madd', 'hsv_lower': [120, 100, 100], 'hsv_upper': [140, 255, 255], 'pixel_threshold': 500 },
    { 'rule_name': 'Qalqalah', 'hsv_lower': [160, 100, 100], 'hsv_upper': [180, 255, 255], 'pixel_threshold': 500 },
])
